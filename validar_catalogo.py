#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador de catálogo para PC Game Archive.

Uso básico:
  python validar_catalogo.py

Uso indicando rutas:
  python validar_catalogo.py --catalogo juegos.json --schema json_schema.json

Criterio especial del proyecto:
  - num == "000000" significa juego pendiente de publicar en Instagram.
  - en ese caso ig == "" es válido y no se considera error.
  - los num == "000000" pueden repetirse sin marcarse como duplicado.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:  # pragma: no cover
    Draft202012Validator = None
    FormatChecker = None


PENDING_NUM = "000000"
HTTPS_RE = re.compile(r"^https://")
EAN_RE = re.compile(r"^(\d{8}|\d{13})$")
URL_RE = re.compile(r"^juegos/[a-z0-9\-]+/$")
IMG_NAME_RE = re.compile(r"^\d{3}\.jpg$", re.IGNORECASE)

# Normalizaciones recomendadas. No corrige automáticamente; solo avisa.
GENERO_EQUIVALENTES = {
    "Point & Click": "Point and click",
    "Point-and-click": "Point and click",
    "Point-&-click": "Point and click",
    "Survival Horror": "Survival horror",
}

DISTRIBUIDOR_EQUIVALENTES = {
    "Sierra OnLine": "Sierra On-Line",
    "Sierra Online": "Sierra On-Line",
    "Sierra Studios": "Sierra Studios",
    "Sierra Entertainment": "Sierra Entertainment",
    "Electronic Arts Software": "Electronic Arts",
}

DESARROLLADOR_EQUIVALENTES = {
    "Lucasfilm Games": "Lucasfilm Games",
    "LucasArts": "LucasArts",
}


@dataclass(frozen=True)
class Issue:
    level: str  # ERROR | WARN | INFO
    index: int | None
    num: str | None
    titulo: str | None
    field: str
    message: str

    def line(self) -> str:
        prefix = self.level
        if self.index is None:
            item = "catálogo"
        else:
            n = "?" if self.num is None else self.num
            t = "?" if self.titulo is None else self.titulo
            item = f"#{self.index + 1} num={n} · {t}"
        return f"[{prefix}] {item} · {self.field}: {self.message}"


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"ERROR: no existe el fichero: {path}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"ERROR: JSON inválido en {path}: línea {e.lineno}, columna {e.colno}: {e.msg}")


def as_games(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("juegos"), list):
        return data["juegos"]
    raise SystemExit("ERROR: el catálogo debe ser una lista JSON o un objeto con la propiedad 'juegos'.")


def get_item_id(game: dict[str, Any]) -> tuple[str | None, str | None]:
    return game.get("num"), game.get("titulo")


def add(issues: list[Issue], level: str, idx: int | None, game: dict[str, Any] | None, field: str, message: str) -> None:
    num, titulo = (None, None) if game is None else get_item_id(game)
    issues.append(Issue(level, idx, num, titulo, field, message))


def path_to_str(path: Iterable[Any]) -> str:
    parts = []
    for p in path:
        if isinstance(p, int):
            parts.append(f"[{p}]")
        else:
            if parts:
                parts.append(f".{p}")
            else:
                parts.append(str(p))
    return "".join(parts) if parts else "$"


def validate_schema(games: list[dict[str, Any]], schema: dict[str, Any], issues: list[Issue]) -> None:
    if Draft202012Validator is None:
        add(
            issues,
            "WARN",
            None,
            None,
            "jsonschema",
            "No está instalada la librería 'jsonschema'. Se omite validación formal de schema. Instala con: pip install jsonschema",
        )
        return

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for idx, game in enumerate(games):
        for err in sorted(validator.iter_errors(game), key=lambda e: list(e.path)):
            field = path_to_str(err.path)
            add(issues, "ERROR", idx, game, field, err.message)


def check_required_order(games: list[dict[str, Any]], issues: list[Issue]) -> None:
    expected_first = ["num", "ig"]
    for idx, game in enumerate(games):
        keys = list(game.keys())
        if keys[:2] != expected_first:
            add(issues, "ERROR", idx, game, "orden_campos", "Los dos primeros campos deben ser 'num' e 'ig', en ese orden.")


def check_num_and_ig(games: list[dict[str, Any]], issues: list[Issue]) -> None:
    nums = [g.get("num") for g in games]
    counts = Counter(nums)

    for idx, game in enumerate(games):
        num = game.get("num")
        ig = game.get("ig")

        if num == PENDING_NUM:
            if ig != "":
                add(issues, "WARN", idx, game, "ig", "El juego está pendiente (num=000000), pero 'ig' no está vacío.")
        else:
            if not isinstance(num, str) or not re.fullmatch(r"\d{6}", num):
                add(issues, "ERROR", idx, game, "num", "Debe ser un string de 6 dígitos.")
            if ig == "":
                add(issues, "WARN", idx, game, "ig", "El juego tiene num definitivo pero no tiene URL de Instagram.")
            elif not isinstance(ig, str) or not HTTPS_RE.match(ig):
                add(issues, "ERROR", idx, game, "ig", "Debe estar vacío o ser una URL https.")

    for num, count in counts.items():
        if num == PENDING_NUM:
            continue
        if count > 1:
            positions = [str(i + 1) for i, g in enumerate(games) if g.get("num") == num]
            add(issues, "ERROR", None, None, "num", f"Duplicado num={num} en registros: {', '.join(positions)}")

    pending = counts.get(PENDING_NUM, 0)
    if pending:
        add(issues, "INFO", None, None, "num", f"{pending} juego(s) pendientes con num=000000. No se consideran duplicados.")


def check_urls(games: list[dict[str, Any]], issues: list[Issue]) -> None:
    urls = [g.get("url") for g in games]
    counts = Counter(urls)

    for idx, game in enumerate(games):
        url = game.get("url")
        formato = game.get("formato")
        serie = game.get("serie", [])

        if not isinstance(url, str) or not URL_RE.match(url):
            add(issues, "ERROR", idx, game, "url", "Debe cumplir el patrón juegos/<slug>/ con minúsculas, números y guiones.")
            continue

        if formato == "Big Box" and not url.endswith("-bigbox/"):
            add(issues, "ERROR", idx, game, "url", "Los juegos Big Box deben terminar en '-bigbox/'.")
        elif formato == "DVD Case" and not url.endswith("-cddvd/"):
            add(issues, "WARN", idx, game, "url", "Según la convención actual, los DVD Case deberían terminar en '-cddvd/'.")
        elif formato == "Jewel Case" and not url.endswith("-jewelcase/"):
            add(issues, "WARN", idx, game, "url", "Los Jewel Case deberían terminar en '-jewelcase/'.")

        if isinstance(serie, list):
            if formato == "Big Box" and "Big Box" not in serie:
                add(issues, "ERROR", idx, game, "serie", "Formato Big Box pero la serie no contiene 'Big Box'.")
            if formato == "DVD Case" and "DVD Case" not in serie:
                add(issues, "WARN", idx, game, "serie", "Formato DVD Case pero la serie no contiene 'DVD Case'.")
            if formato == "Jewel Case" and "Jewel Case" not in serie:
                add(issues, "WARN", idx, game, "serie", "Formato Jewel Case pero la serie no contiene 'Jewel Case'.")

    for url, count in counts.items():
        if url and count > 1:
            positions = [str(i + 1) for i, g in enumerate(games) if g.get("url") == url]
            add(issues, "ERROR", None, None, "url", f"Duplicada url={url} en registros: {', '.join(positions)}")


def check_arrays_and_duplicates(games: list[dict[str, Any]], issues: list[Issue]) -> None:
    array_fields = ["plataforma", "genero", "desarrollador", "distribuidor", "incluye", "serie", "tags"]
    required_non_empty = ["plataforma", "genero", "desarrollador", "distribuidor", "serie"]

    for idx, game in enumerate(games):
        for field in array_fields:
            value = game.get(field)
            if not isinstance(value, list):
                add(issues, "ERROR", idx, game, field, "Debe ser un array.")
                continue
            if field in required_non_empty and not value:
                add(issues, "ERROR", idx, game, field, "No puede estar vacío.")
            repeated = sorted({x for x in value if value.count(x) > 1})
            if repeated:
                add(issues, "ERROR", idx, game, field, f"Contiene valores duplicados: {', '.join(map(str, repeated))}")


def check_ean(games: list[dict[str, Any]], issues: list[Issue]) -> None:
    for idx, game in enumerate(games):
        ean = game.get("ean")
        if ean == "":
            add(issues, "ERROR", idx, game, "ean", "Debe ser array. Usa [] si no hay EAN documentado.")
            continue
        if not isinstance(ean, list):
            add(issues, "ERROR", idx, game, "ean", "Debe ser array de strings EAN. Usa [] si no hay EAN documentado.")
            continue
        for pos, code in enumerate(ean):
            if not isinstance(code, str):
                add(issues, "ERROR", idx, game, f"ean[{pos}]", "Debe ser string.")
                continue
            if "," in code:
                add(issues, "ERROR", idx, game, f"ean[{pos}]", "Hay varios EAN en una sola cadena. Deben separarse en elementos distintos del array.")
            if not EAN_RE.match(code):
                add(issues, "ERROR", idx, game, f"ean[{pos}]", "Debe tener 8 o 13 dígitos numéricos, sin espacios ni comas.")


def check_taxonomy(games: list[dict[str, Any]], issues: list[Issue]) -> None:
    checks = [
        ("genero", GENERO_EQUIVALENTES),
        ("distribuidor", DISTRIBUIDOR_EQUIVALENTES),
        ("desarrollador", DESARROLLADOR_EQUIVALENTES),
    ]
    for idx, game in enumerate(games):
        for field, mapping in checks:
            value = game.get(field)
            if not isinstance(value, list):
                continue
            for item in value:
                if item in mapping and mapping[item] != item:
                    add(issues, "WARN", idx, game, field, f"Valor '{item}' normalizable como '{mapping[item]}'.")


def check_proteccion(games: list[dict[str, Any]], issues: list[Issue]) -> None:
    for idx, game in enumerate(games):
        prot = game.get("proteccion")
        if prot is None:
            add(issues, "WARN", idx, game, "proteccion", "Falta bloque de preservación/protección. Recomendable completarlo.")
            continue
        if not isinstance(prot, dict):
            add(issues, "ERROR", idx, game, "proteccion", "Debe ser un objeto.")
            continue
        for field in ["tipo", "version", "preservacion", "formato", "jugable_virtual"]:
            if field not in prot:
                add(issues, "ERROR", idx, game, f"proteccion.{field}", "Campo obligatorio ausente.")
        if prot.get("tipo") in {"SafeDisc", "SecuROM", "LaserLock", "StarForce", "TAGES"} and not prot.get("version"):
            add(issues, "WARN", idx, game, "proteccion.version", "Conviene indicar versión cuando la protección es conocida.")


def check_images(games: list[dict[str, Any]], base_dir: Path, issues: list[Issue]) -> None:
    for idx, game in enumerate(games):
        url = game.get("url")
        if not isinstance(url, str):
            continue
        img_dir = base_dir / url / "img"
        if not img_dir.exists():
            add(issues, "WARN", idx, game, "imagenes", f"No existe carpeta de imágenes: {img_dir.as_posix()}")
            continue
        jpgs = sorted(p.name for p in img_dir.iterdir() if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg"})
        if not jpgs:
            add(issues, "WARN", idx, game, "imagenes", "La carpeta img existe, pero no contiene JPG/JPEG.")
            continue
        non_standard = [name for name in jpgs if not IMG_NAME_RE.match(name)]
        if non_standard:
            add(issues, "WARN", idx, game, "imagenes", f"Nombres no estándar. Esperado 001.jpg, 002.jpg...: {', '.join(non_standard[:5])}")
        if "001.jpg" not in {name.lower() for name in jpgs}:
            add(issues, "WARN", idx, game, "imagenes", "No se encuentra 001.jpg, que se usa como portada por defecto.")


def write_report(issues: list[Issue], report_path: Path) -> None:
    levels = Counter(i.level for i in issues)
    lines = [
        "# Informe de validación - PC Game Archive",
        "",
        f"Errores: {levels.get('ERROR', 0)}",
        f"Avisos: {levels.get('WARN', 0)}",
        f"Info: {levels.get('INFO', 0)}",
        "",
    ]
    for level in ["ERROR", "WARN", "INFO"]:
        subset = [i for i in issues if i.level == level]
        if not subset:
            continue
        lines.append(f"## {level}")
        lines.append("")
        for issue in subset:
            lines.append(f"- {issue.line()}")
        lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")


def print_summary(issues: list[Issue], max_lines: int) -> None:
    levels = Counter(i.level for i in issues)
    print("\nResultado de validación")
    print("=======================")
    print(f"Errores : {levels.get('ERROR', 0)}")
    print(f"Avisos  : {levels.get('WARN', 0)}")
    print(f"Info    : {levels.get('INFO', 0)}")

    printable = [i for i in issues if i.level in {"ERROR", "WARN"}]
    if printable:
        print("\nPrimeras incidencias:")
        for issue in printable[:max_lines]:
            print(" - " + issue.line())
        if len(printable) > max_lines:
            print(f" ... {len(printable) - max_lines} incidencia(s) más. Usa --report para ver el informe completo.")
    else:
        print("\nNo se han detectado errores ni avisos.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Valida el catálogo juegos.json de PC Game Archive.")
    parser.add_argument("--catalogo", default="juegos.json", help="Ruta al fichero juegos.json")
    parser.add_argument("--schema", default="json_schema.json", help="Ruta al JSON Schema")
    parser.add_argument("--base-dir", default=".", help="Directorio base del site para comprobar imágenes")
    parser.add_argument("--report", default="informe_validacion_catalogo.md", help="Ruta del informe Markdown")
    parser.add_argument("--no-schema", action="store_true", help="No ejecutar validación contra JSON Schema")
    parser.add_argument("--no-images", action="store_true", help="No comprobar carpetas de imágenes")
    parser.add_argument("--max-lines", type=int, default=40, help="Número máximo de incidencias mostradas por consola")
    parser.add_argument("--strict", action="store_true", help="Devuelve código 1 también si hay avisos")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    catalog_path = Path(args.catalogo)
    schema_path = Path(args.schema)
    base_dir = Path(args.base_dir)
    report_path = Path(args.report)

    data = load_json(catalog_path)
    games = as_games(data)
    issues: list[Issue] = []

    add(issues, "INFO", None, None, "catalogo", f"{len(games)} juego(s) cargado(s).")

    if not args.no_schema:
        schema = load_json(schema_path)
        validate_schema(games, schema, issues)

    check_required_order(games, issues)
    check_num_and_ig(games, issues)
    check_urls(games, issues)
    check_arrays_and_duplicates(games, issues)
    check_ean(games, issues)
    check_taxonomy(games, issues)
    check_proteccion(games, issues)

    if not args.no_images:
        check_images(games, base_dir, issues)

    write_report(issues, report_path)
    print_summary(issues, args.max_lines)
    print(f"\nInforme generado: {report_path}")

    levels = Counter(i.level for i in issues)
    if levels.get("ERROR", 0) > 0:
        return 1
    if args.strict and levels.get("WARN", 0) > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
