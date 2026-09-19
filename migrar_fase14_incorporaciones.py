#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Añade fecha_incorporacion vacía a fichas históricas que aún no tengan el campo."""
from __future__ import annotations
import json
from pathlib import Path

path = Path("juegos.json")
data = json.loads(path.read_text(encoding="utf-8"))
changed = 0
for i, game in enumerate(data):
    if "fecha_incorporacion" in game:
        continue
    updated = {}
    for key, value in game.items():
        updated[key] = value
        if key == "ig":
            updated["fecha_incorporacion"] = ""
    data[i] = updated
    changed += 1
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Fichas migradas: {changed}")
