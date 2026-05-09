#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrige reglas estructurales del catálogo de PC Game Archive según json_schema.json.

Reglas aplicadas:
  - Si formato = "Big Box": añade "Big Box" a serie y fuerza URL terminada en -bigbox/
  - Si formato = "DVD Case": añade "DVD Case" a serie y fuerza URL terminada en -cddvd/
  - Si formato = "Jewel Case": añade "Jewel Case" a serie y fuerza URL terminada en -jewelcase/
  - Si cambia la URL y existe la carpeta antigua, intenta renombrarla a la nueva.

Por seguridad, por defecto NO modifica nada: usa modo simulación (--dry-run implícito).
Para aplicar cambios reales: python corregir_catalogo.py --apply
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

FORMAT_RULES: Dict[str, Dict[str, str]] = {
    "Big Box": {"serie": "Big Box", "suffix": "-bigbox"},
    "DVD Case": {"serie": "DVD Case", "suffix": "-cddvd"},
    "Jewel Case": {"serie": "Jewel Case", "suffix": "-jewelcase"},
}

KNOWN_SUFFIXES = ("-bigbox", "-cddvd", "-jewelcase")
URL_RE = re.compile(r"^juegos/[a-z0-9\-]+/$")


def now_stamp() -> str:
    return dt.datetime.now().strftime("%Y%m%d_%H%M%S")


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def normalize_url_for_format(url: str, formato: str) -> Tuple[str, bool, str]:
    """
    Devuelve (nueva_url, changed, motivo).
    Mantiene el slug base y sustituye/añade el sufijo esperado por formato.
    """
    rule = FORMAT_RULES.get(formato)
    if not rule:
        return url, False, f"Formato no gestionado: {formato!r}"

    if not isinstance(url, str) or not url.strip():
        return url, False, "URL vacía o no textual; no se puede corregir automáticamente"

    raw = url.strip()
    if not raw.startswith("juegos/") or not raw.endswith("/"):
        return raw, False, "URL fuera del patrón juegos/<slug>/; no se corrige automáticamente"

    slug = raw[len("juegos/"):-1]
    if not slug:
        return raw, False, "Slug vacío; no se corrige automáticamente"

    base_slug = slug
    for suffix in KNOWN_SUFFIXES:
        if base_slug.endswith(suffix):
            base_slug = base_slug[: -len(suffix)]
            break

    expected_slug = f"{base_slug}{rule['suffix']}"
    expected_url = f"juegos/{expected_slug}/"
    return expected_url, expected_url != raw, "URL ajustada al sufijo requerido por formato"


def ensure_series(juego: Dict[str, Any], required_serie: str) -> bool:
    serie = juego.get("serie")
    if not isinstance(serie, list):
        juego["serie"] = ["Todos", required_serie]
        return True

    changed = False
    if "Todos" not in serie:
        serie.insert(0, "Todos")
        changed = True
    if required_serie not in serie:
        # La serie editorial se conserva; el formato se añade al final para no pisar semántica existente.
        serie.append(required_serie)
        changed = True

    # Elimina duplicados conservando orden.
    seen = set()
    deduped = []
    for item in serie:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    if deduped != serie:
        juego["serie"] = deduped
        changed = True

    return changed


def safe_game_label(index: int, juego: Dict[str, Any]) -> str:
    return f"#{index + 1} num={juego.get('num', '—')} · {juego.get('titulo', 'Sin título')}"


def rename_folder_if_possible(
    base_dir: Path,
    old_url: str,
    new_url: str,
    apply: bool,
) -> Tuple[str, str]:
    """
    Devuelve (estado, detalle).
    Estados: renamed, would_rename, old_missing, target_exists, skipped_invalid, same.
    """
    if old_url == new_url:
        return "same", "La URL no cambia; no hay carpeta que renombrar"

    if not (isinstance(old_url, str) and isinstance(new_url, str)):
        return "skipped_invalid", "URL antigua o nueva no textual"

    if not (old_url.startswith("juegos/") and new_url.startswith("juegos/")):
        return "skipped_invalid", "URL fuera de juegos/"

    old_rel = old_url.strip("/")
    new_rel = new_url.strip("/")
    old_path = base_dir / old_rel
    new_path = base_dir / new_rel

    if not old_path.exists():
        return "old_missing", f"No existe carpeta antigua: {old_path}"

    if new_path.exists():
        return "target_exists", f"Ya existe carpeta destino: {new_path}"

    if not old_path.is_dir():
        return "skipped_invalid", f"La ruta antigua existe pero no es directorio: {old_path}"

    if not apply:
        return "would_rename", f"Se renombraría {old_path} -> {new_path}"

    new_path.parent.mkdir(parents=True, exist_ok=True)
    old_path.rename(new_path)
    return "renamed", f"Renombrada {old_path} -> {new_path}"


def detect_url_duplicates(catalogo: List[Dict[str, Any]]) -> List[str]:
    seen: Dict[str, int] = {}
    duplicates: List[str] = []
    for i, juego in enumerate(catalogo):
        url = juego.get("url")
        if not isinstance(url, str):
            continue
        if url in seen:
            duplicates.append(f"URL duplicada: {url} en #{seen[url] + 1} y #{i + 1}")
        else:
            seen[url] = i
    return duplicates


def build_report(
    report_path: Path,
    *,
    apply: bool,
    catalogo_path: Path,
    changes: List[str],
    folder_ops: List[str],
    warnings: List[str],
    errors: List[str],
) -> None:
    lines: List[str] = []
    lines.append("# Informe de corrección del catálogo")
    lines.append("")
    lines.append(f"- Fecha: {dt.datetime.now().isoformat(timespec='seconds')}")
    lines.append(f"- Catálogo: `{catalogo_path}`")
    lines.append(f"- Modo: `{'APLICADO' if apply else 'SIMULACIÓN / DRY-RUN'}`")
    lines.append("")
    lines.append("## Resumen")
    lines.append("")
    lines.append(f"- Cambios de catálogo: {len(changes)}")
    lines.append(f"- Operaciones de carpeta: {len(folder_ops)}")
    lines.append(f"- Avisos: {len(warnings)}")
    lines.append(f"- Errores: {len(errors)}")
    lines.append("")

    def section(title: str, items: List[str]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not items:
            lines.append("Sin elementos.")
        else:
            for item in items:
                lines.append(f"- {item}")
        lines.append("")

    section("Cambios de catálogo", changes)
    section("Operaciones de carpeta", folder_ops)
    section("Avisos", warnings)
    section("Errores", errors)

    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Corrige serie, URL y carpetas del catálogo según el formato definido en json_schema.json."
    )
    parser.add_argument("--catalogo", default="juegos.json", help="Ruta del catálogo JSON. Por defecto: juegos.json")
    parser.add_argument("--base-dir", default=".", help="Raíz del site. Por defecto: directorio actual")
    parser.add_argument("--apply", action="store_true", help="Aplica cambios reales. Sin esto solo simula.")
    parser.add_argument("--no-folder-rename", action="store_true", help="No intenta renombrar carpetas aunque cambie la URL.")
    parser.add_argument("--report", default="informe_correccion_catalogo.md", help="Fichero de informe Markdown.")
    args = parser.parse_args()

    base_dir = Path(args.base_dir).resolve()
    catalogo_path = Path(args.catalogo)
    if not catalogo_path.is_absolute():
        catalogo_path = base_dir / catalogo_path
    catalogo_path = catalogo_path.resolve()
    report_path = Path(args.report)
    if not report_path.is_absolute():
        report_path = base_dir / report_path

    if not catalogo_path.exists():
        print(f"ERROR: no existe el catálogo: {catalogo_path}", file=sys.stderr)
        return 2

    try:
        catalogo = load_json(catalogo_path)
    except Exception as exc:
        print(f"ERROR: no se puede leer el catálogo: {exc}", file=sys.stderr)
        return 2

    if not isinstance(catalogo, list):
        print("ERROR: se esperaba que juegos.json fuera una lista de juegos.", file=sys.stderr)
        return 2

    original = copy.deepcopy(catalogo)
    changes: List[str] = []
    folder_ops: List[str] = []
    warnings: List[str] = []
    errors: List[str] = []

    for i, juego in enumerate(catalogo):
        if not isinstance(juego, dict):
            warnings.append(f"#{i + 1}: elemento no objeto; se omite")
            continue

        label = safe_game_label(i, juego)
        formato = juego.get("formato")
        rule = FORMAT_RULES.get(formato)
        if not rule:
            warnings.append(f"{label}: formato no gestionado: {formato!r}")
            continue

        old_url = juego.get("url")

        if ensure_series(juego, rule["serie"]):
            changes.append(f"{label}: serie actualizada -> {juego.get('serie')}")

        new_url, url_changed, reason = normalize_url_for_format(str(old_url) if old_url is not None else "", formato)
        if url_changed:
            if not URL_RE.match(new_url):
                errors.append(f"{label}: la URL propuesta no cumple patrón: {new_url}")
            else:
                juego["url"] = new_url
                changes.append(f"{label}: url `{old_url}` -> `{new_url}` ({reason})")

                if not args.no_folder_rename:
                    status, detail = rename_folder_if_possible(base_dir, str(old_url), new_url, args.apply)
                    folder_ops.append(f"{label}: [{status}] {detail}")
        elif reason.startswith("URL vacía") or reason.startswith("URL fuera") or reason.startswith("Slug vacío"):
            warnings.append(f"{label}: {reason}")

    duplicates = detect_url_duplicates(catalogo)
    errors.extend(duplicates)

    changed = catalogo != original

    if args.apply and changed:
        backup_path = catalogo_path.with_name(f"{catalogo_path.name}.bak_{now_stamp()}")
        shutil.copy2(catalogo_path, backup_path)
        save_json(catalogo_path, catalogo)
        print(f"Catálogo actualizado: {catalogo_path}")
        print(f"Backup creado: {backup_path}")
    elif not args.apply:
        print("Modo simulación: no se ha modificado ningún fichero.")
    else:
        print("No había cambios que aplicar en el catálogo.")

    build_report(
        report_path,
        apply=args.apply,
        catalogo_path=catalogo_path,
        changes=changes,
        folder_ops=folder_ops,
        warnings=warnings,
        errors=errors,
    )

    print(f"Informe generado: {report_path}")
    print(f"Cambios de catálogo: {len(changes)}")
    print(f"Operaciones de carpeta: {len(folder_ops)}")
    print(f"Avisos: {len(warnings)}")
    print(f"Errores: {len(errors)}")

    if errors:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
