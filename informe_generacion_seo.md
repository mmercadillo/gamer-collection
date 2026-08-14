# Informe de generación SEO

- Fecha: 2026-08-14T10:04:45
- Juegos en catálogo: 1552
- URLs duplicadas detectadas: 1
- URLs inválidas omitidas: 0

## Observaciones

- Las páginas de juego se generan físicamente como `juegos/<slug>/index.html`, pero todos los enlaces y canonical usan `/juegos/<slug>/`.
- El sitemap contiene exclusivamente URLs canónicas y no publica fechas `lastmod` artificiales.
- `bigbox.html` se conserva únicamente como redirección a `juegos-pc-big-box.html`.
- `detalle.html?juego=<slug>` se conserva únicamente como compatibilidad con URLs antiguas.
- Google Analytics normaliza `page_location` a la canonical y registra búsquedas, filtros, selección de juegos y clics de contacto.
- Los duplicados no se sobrescriben: se conserva la primera aparición en el catálogo.
- Se generan landing pages SEO en español para búsquedas genéricas.
- Se generan favicon PNG/ICO y manifest desde logo.png para favorecer el icono en resultados de Google.

## URLs duplicadas

- `juegos/the-rise-and-rule-of-ancient-empires-bigbox/`
