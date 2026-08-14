# Fase 12.1 — Ajuste visual del buscador avanzado

Base: `pcgamearchive_fase12.zip`.

## Objetivo

Mejorar la presentación del buscador avanzado sin alterar su lógica, filtros, URLs ni arquitectura SEO.

## Cambios

- El campo de búsqueda libre ocupa ahora una fila completa.
- Formato, Serie y el botón Buscar se sitúan en una segunda fila.
- En pantallas estrechas, los filtros y el botón se apilan verticalmente.
- El autocompletado ocupa todo el ancho del campo de búsqueda.
- Las sugerencias usan fondo claro y ya no heredan el estilo negro del botón Buscar.
- Se aumenta el tamaño y espaciado del texto de sugerencias.
- Los títulos largos pueden ocupar más de una línea en vez de quedar truncados prematuramente.
- Se mantienen intactos los desplegables de Formato y Serie y toda la lógica de Fase 12.

## Archivos modificados

- `generar_web.py`
- `index.html`
- `assets/css/styles.css`

No se modifica `catalogo.js`, `search-index.js`, `juegos.json`, `json_schema.json` ni `sitemap.xml`.
