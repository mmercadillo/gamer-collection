#!/usr/bin/env python3
"""Migra juegos.json al modelo mínimo de preservación de PC Game Archive.

Modelo destino por pieza:
    "preservacion": {"resumen": ""}

El resumen permanece vacío hasta que exista trabajo de laboratorio real. Para no
perder resultados ya verificados, si una pieza está relacionada desde
``documentacion.json`` con un documento de categoría ``preservacion``, el script
conserva como resumen el texto histórico de ``proteccion.preservacion`` (si
existe). El resto de datos del bloque legado ``proteccion`` se eliminan.

Por seguridad, la ejecución es simulada salvo que se indique ``--apply``.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def preservation_document_urls(documentation: Any) -> set[str]:
    urls: set[str] = set()
    if not isinstance(documentation, list):
        return urls
    for document in documentation:
        if not isinstance(document, dict) or document.get("categoria") != "preservacion":
            continue
        related = document.get("juegos", [])
        if isinstance(related, list):
            urls.update(str(url).strip() for url in related if str(url).strip())
    return urls


def migrate_game(game: dict[str, Any], verified_urls: set[str]) -> tuple[bool, bool, str]:
    """Devuelve (cambio, resumen_conservado, resumen_final)."""
    current = game.get("preservacion")
    current_summary = ""
    if isinstance(current, dict):
        current_summary = str(current.get("resumen", "") or "").strip()

    legacy = game.get("proteccion")
    legacy_summary = ""
    if isinstance(legacy, dict):
        legacy_summary = str(legacy.get("preservacion", "") or "").strip()

    game_url = str(game.get("url", "") or "").strip()
    summary = current_summary
    retained = bool(summary)

    # Solo se rescata contenido legado si la pieza ya tiene documentación de
    # preservación real asociada. Las recomendaciones históricas no verificadas
    # se descartan deliberadamente.
    if not summary and game_url in verified_urls and legacy_summary:
        summary = legacy_summary
        retained = True

    new_value = {"resumen": summary}
    changed = game.get("preservacion") != new_value or "proteccion" in game
    game["preservacion"] = new_value
    game.pop("proteccion", None)
    return changed, retained, summary


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Migra juegos.json desde el bloque legado 'proteccion' al modelo "
            "mínimo 'preservacion.resumen'."
        )
    )
    parser.add_argument("--catalogo", default="juegos.json", help="Catálogo a migrar.")
    parser.add_argument(
        "--documentacion",
        default="documentacion.json",
        help="Índice documental usado para reconocer preservaciones ya verificadas.",
    )
    parser.add_argument("--apply", action="store_true", help="Escribe los cambios. Sin esta opción solo simula.")
    args = parser.parse_args()

    catalog_path = Path(args.catalogo)
    documentation_path = Path(args.documentacion)

    games = load_json(catalog_path)
    if not isinstance(games, list):
        raise ValueError(f"{catalog_path} debe contener una lista JSON.")

    documentation = load_json(documentation_path) if documentation_path.is_file() else []
    verified_urls = preservation_document_urls(documentation)

    changed = 0
    retained = 0
    empty = 0
    retained_games: list[str] = []

    for game in games:
        if not isinstance(game, dict):
            continue
        did_change, did_retain, summary = migrate_game(game, verified_urls)
        changed += int(did_change)
        retained += int(did_retain)
        empty += int(not bool(summary))
        if did_retain:
            retained_games.append(f"{game.get('num', '??????')} · {game.get('titulo', '')}")

    print(f"Piezas procesadas: {len(games)}")
    print(f"Piezas modificadas: {changed}")
    print(f"Resúmenes verificados conservados: {retained}")
    print(f"Resúmenes vacíos: {empty}")
    if retained_games:
        print("Resúmenes conservados:")
        for label in retained_games:
            print(f"  - {label}")

    if args.apply:
        with catalog_path.open("w", encoding="utf-8", newline="\n") as fh:
            json.dump(games, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"Cambios escritos en {catalog_path}.")
    else:
        print("Simulación completada. Use --apply para escribir los cambios.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
