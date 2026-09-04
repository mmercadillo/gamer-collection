# Informe de generación SEO

- Fecha: 2026-09-04T09:05:34
- Juegos en catálogo: 1560
- URLs duplicadas detectadas: 1
- URLs inválidas omitidas: 0
- Desarrolladores con página/landing indexable: 158
- Distribuidores con página/landing indexable: 101
- Géneros con página/landing indexable: 144
- Plataformas con página/landing indexable: 13
- Formatos con página/landing indexable: 3
- Años documentados: 21 fichas (1.3%); entidades indexables: 0
- Mercados documentados: 276 fichas (17.7%); entidades indexables: 3
- Idiomas documentados: 184 fichas (11.8%); entidades indexables: 4
- Soportes documentados: 271 fichas (17.4%); entidades indexables: 5
- Tipos de edición documentados: 115 fichas (7.4%); entidades indexables: 0
- Páginas estáticas del catálogo: 65
- Fichas con imágenes documentales detectadas: 1558
- Imágenes documentales incluidas en el sitemap: 2569

## Observaciones

- Las páginas de juego se generan físicamente como `juegos/<slug>/index.html`, pero todos los enlaces y canonical usan `/juegos/<slug>/`.
- El sitemap contiene exclusivamente URLs canónicas y no publica fechas `lastmod` artificiales.
- El sitemap usa la extensión oficial de imágenes y asocia a cada ficha únicamente las imágenes que existen físicamente en `/juegos/<slug>/img/`.
- Las fichas añaden `primaryImageOfPage`/`ImageObject` solo cuando existe fotografía real; `no_disponible.png` se mantiene como fallback visual/social pero no se presenta como imagen documental en datos estructurados ni en el sitemap de imágenes.
- Las imágenes documentales tienen alt descriptivo, captions visibles y la imagen principal usa `fetchpriority=high`; el resto mantiene carga diferida nativa.
- Se permite `max-image-preview:large` para que Google pueda usar previsualizaciones grandes cuando corresponda.
- Se conservan los nombres documentales originales (`001.jpg`, etc.); no se renombran ficheros ni se rompen rutas históricas del archivo.
- `bigbox.html` se conserva únicamente como redirección a `juegos-pc-big-box.html`.
- `detalle.html?juego=<slug>` se conserva únicamente como compatibilidad con URLs antiguas.
- Google Analytics normaliza la ruta a la canonical, conserva parámetros de campaña (`utm_*`, `gclid`, `gbraid`, `wbraid`, `dclid`) para no perder atribución SEM y no se inicializa en localhost/127.0.0.1/::1.
- Los duplicados no se sobrescriben: se conserva la primera aparición en el catálogo.
- Se generan landing pages SEO en español para búsquedas genéricas.
- Se generan automáticamente hubs y páginas SEO por desarrollador, distribuidor, género, plataforma y formato cuando una entidad aparece en 3 o más fichas.
- Fase 10D añade año, mercado, idioma, soporte y tipo de edición como taxonomías potenciales; además del mínimo por entidad, cada campo nuevo exige al menos 150 fichas documentadas antes de publicar su hub para evitar páginas prematuras y despublicaciones por crecimiento del catálogo.
- Variantes puramente tipográficas de una entidad (mayúsculas/acentos) se agrupan en una única página.
- Big Box, MS-DOS, Windows 95/98 y aventura gráfica reutilizan sus landings editoriales existentes para evitar canibalización.
- Las landings principales incorporan contenido editorial específico, métricas dinámicas, breadcrumbs y enlaces internos a entidades relevantes.
- Se genera `/vender-videojuegos-pc-antiguos/` como landing de captación para compra/donación, con CTA medidos mediante `offer_games_click`; los mailto esperan brevemente al callback del Google tag antes de abrir el correo.
- Las fichas enlazan directamente a las páginas de entidad cuando existe una landing indexable.
- Las fichas incorporan bloques automáticos de otras ediciones, serie/colección, desarrollador y juegos relacionados, deduplicados entre sí para reforzar la navegación contextual.
- Se generan favicon PNG/ICO y manifest desde logo.png para favorecer el icono en resultados de Google.
- El scroll infinito de la portada se complementa con `/catalogo/` y una serie paginada de enlaces HTML rastreables, con canonical propio por página.

## URLs duplicadas

- `juegos/the-rise-and-rule-of-ancient-empires-bigbox/`
