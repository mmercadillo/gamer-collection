# Fase 15.1 — Normalización de redes sociales de procedencia

## Objetivo
Evitar que identificadores como `@frodrig` se interpreten como rutas relativas dentro de la ficha del juego.

## Comportamiento
- Instagram: acepta `@usuario`, `usuario`, dominio sin esquema o URL completa y genera un enlace HTTPS a Instagram.
- X: acepta `@usuario`, `usuario`, dominio sin esquema o URL completa (`x.com`/`twitter.com`) y genera un enlace HTTPS.
- Facebook: se recomienda URL completa; también se admite alias simple.
- Ningún identificador social se emite como URL relativa.
- El texto visible conserva una etiqueta compacta, por ejemplo `Instagram @frodrig`.

## Ejemplo
`"instagram": "@frodrig"` se renderiza con `href="https://www.instagram.com/frodrig/"`.
