#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prueba rápida de regresión para la presentación de procedencia Fase 15."""
import generar_web as g

cases = [
    (
        {"procedencia":{"tipo":"Donación","nombre_publico":"Colección Retro","redes":{"instagram":"https://www.instagram.com/coleccionretro/","facebook":"","x":""}}},
        ("Donación", "Colección Retro", "Instagram @coleccionretro"),
    ),
    (
        {"procedencia":{"tipo":"Donación","nombre_publico":"","redes":{"instagram":"https://www.instagram.com/solo_alias/","facebook":"","x":"https://x.com/solo_alias"}}},
        ("Donación", "Instagram @solo_alias", "X @solo_alias"),
    ),
    (
        {"procedencia":{"tipo":"Donación","nombre_publico":"","redes":{"instagram":"@frodrig","facebook":"","x":"@frodrig"}}},
        ("Instagram @frodrig", 'href="https://www.instagram.com/frodrig/"', "X @frodrig", 'href="https://x.com/frodrig"'),
    ),
    (
        {"procedencia":{"tipo":"Compra","nombre_publico":"","redes":{"instagram":"","facebook":"","x":""}}},
        ("Compra",),
    ),
    (
        {"procedencia":{"tipo":"","nombre_publico":"","redes":{"instagram":"","facebook":"","x":""}}},
        (),
    ),
]

for game, expected in cases:
    html = g.provenance_html(game)
    for token in expected:
        assert token in html, (token, html)
    if not expected:
        assert html == "", html
print("OK - Fase 15 procedencia")
