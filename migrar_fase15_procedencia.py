#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Añade la estructura vacía de procedencia Fase 15 a catálogos anteriores."""
from pathlib import Path
import argparse, json

def blank():
    return {"tipo":"","nombre_publico":"","redes":{"instagram":"","facebook":"","x":""}}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--catalogo", default="juegos.json")
    args=ap.parse_args()
    p=Path(args.catalogo)
    games=json.loads(p.read_text(encoding="utf-8"))
    changed=0
    for game in games:
        if "procedencia" not in game:
            game["procedencia"]=blank(); changed+=1
    p.write_text(json.dumps(games,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Fase 15: {changed} ficha(s) migrada(s).")
if __name__ == "__main__": main()
