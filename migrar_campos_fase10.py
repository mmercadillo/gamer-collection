#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Añade los campos obligatorios de la Fase 10 a juegos.json sin inventar datos.

Campos añadidos, siempre al final de cada ficha si todavía no existen:
  - anio: ""
  - mercado: []
  - idioma: []
  - soporte: []
  - tipo_edicion: []

El script NO sobrescribe valores existentes.
Por seguridad crea una copia de respaldo antes de modificar el catálogo y escribe
el JSON mediante un fichero temporal + reemplazo atómico.

Uso:
  python migrar_campos_fase10.py
  python migrar_campos_fase10.py --dry-run
  python migrar_campos_fase10.py --archivo ruta/juegos.json
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

NUEVOS_CAMPOS: tuple[tuple[str, Any], ...] = (
    ("anio", ""),
    ("mercado", []),
    ("idioma", []),
    ("soporte", []),
    ("tipo_edicion", []),
)


def cargar_catalogo(path: Path) -> tuple[Any, list[dict[str, Any]]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"ERROR: no existe el fichero: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(
            f"ERROR: JSON inválido en {path}: línea {exc.lineno}, columna {exc.colno}: {exc.msg}"
        ) from exc

    if isinstance(data, list):
        games = data
    elif isinstance(data, dict) and isinstance(data.get("juegos"), list):
        games = data["juegos"]
    else:
        raise SystemExit(
            "ERROR: el catálogo debe ser una lista JSON o un objeto con la propiedad 'juegos'."
        )

    if any(not isinstance(game, dict) for game in games):
        raise SystemExit("ERROR: todos los elementos del catálogo deben ser objetos JSON.")

    return data, games


def migrar(games: list[dict[str, Any]]) -> tuple[int, dict[str, int]]:
    modificados = 0
    añadidos_por_campo = {campo: 0 for campo, _ in NUEVOS_CAMPOS}

    for game in games:
        cambiado = False
        for campo, valor_vacio in NUEVOS_CAMPOS:
            if campo in game:
                continue

            # Evita compartir la misma lista mutable entre registros.
            valor = list(valor_vacio) if isinstance(valor_vacio, list) else valor_vacio
            game[campo] = valor
            añadidos_por_campo[campo] += 1
            cambiado = True

        if cambiado:
            modificados += 1

    return modificados, añadidos_por_campo


def crear_backup(path: Path) -> Path:
    sello = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = path.with_name(f"{path.name}.bak_fase10_{sello}")
    shutil.copy2(path, backup)
    return backup


def guardar_atomico(path: Path, data: Any) -> None:
    contenido = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    fd, temp_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent), text=True
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(contenido)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Añade los campos vacíos de la Fase 10 a juegos.json sin sobrescribir datos existentes."
    )
    parser.add_argument("--archivo", default="juegos.json", help="Ruta al catálogo (por defecto: juegos.json).")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Calcula qué cambiaría, pero no crea backup ni modifica el fichero.",
    )
    args = parser.parse_args()

    path = Path(args.archivo).resolve()
    data, games = cargar_catalogo(path)
    total = len(games)
    modificados, añadidos = migrar(games)

    print(f"Registros analizados: {total}")
    print(f"Registros que requieren cambios: {modificados}")
    for campo, cantidad in añadidos.items():
        print(f"  {campo}: {cantidad} campo(s) a añadir")

    if args.dry_run:
        print("DRY-RUN: no se ha modificado ningún fichero.")
        return 0

    if modificados == 0:
        print("No hay cambios que aplicar. El catálogo ya contiene todos los campos de la Fase 10.")
        return 0

    backup = crear_backup(path)
    guardar_atomico(path, data)
    print(f"Backup creado: {backup}")
    print(f"Catálogo actualizado: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
