# PC Game Archive — Cambios SEO Fase 0 + Fase 1

## Fase 0 — Medición

- Google Analytics envía `page_view` usando la URL canónica como `page_location`.
- Se registra `search` con `search_term` y `results_count`.
- Se registra `search_no_results` cuando una búsqueda devuelve cero resultados.
- Se registra `filter_used` con `filter_name` y `filter_value` para filtros elegidos por URL.
- Se registra `select_content` al abrir una ficha desde el catálogo.
- Se registra `contact_click` en enlaces `mailto:`.
- Se registra `outbound_social_click` para Instagram.

Recomendación en Google Analytics tras desplegar:

- marcar `contact_click` como evento clave si se quiere utilizar el clic en email como conversión provisional;
- crear dimensiones personalizadas para `filter_name`, `filter_value` y, si interesa analizarlos directamente, los parámetros de eventos personalizados.

## Fase 1 — SEO técnico y URLs

- La portada canónica es `/` y los enlaces internos dejan de apuntar a `/index.html`.
- Las fichas usan `/juegos/<slug>/` y no `/juegos/<slug>/index.html`.
- Si una URL `/index.html` se visita directamente por HTTP/HTTPS, se redirige a la variante limpia antes de la medición.
- `bigbox.html` pasa a ser una redirección inmediata a `juegos-pc-big-box.html`.
- `detalle.html?juego=<slug>` redirige a `/juegos/<slug>/` para conservar compatibilidad con URLs antiguas.
- Breadcrumbs y enlaces internos Big Box apuntan a `juegos-pc-big-box.html`.
- El sitemap contiene únicamente URLs canónicas.
- Se eliminan `lastmod` artificiales del sitemap.
- Se elimina `/index.html` del sitemap.
- Se elimina `bigbox.html` del sitemap.
- `no_disponible.png` pasa a ser el fallback Open Graph y el fallback visual cuando no existe imagen del juego.

## Validaciones realizadas

- `generar_web.py` compila correctamente con Python.
- El generador procesa los 1.552 registros del catálogo.
- El sitemap XML es válido.
- El sitemap contiene 1.560 URLs únicas, de las cuales 1.551 son fichas únicas de juego.
- No hay `/index.html` ni `bigbox.html` dentro del sitemap.
- El JavaScript generado pasa `node --check`.
- No quedan enlaces HTML internos generados hacia `index.html` o `bigbox.html`.

La diferencia entre 1.552 registros y 1.551 URLs de juego se debe a la URL duplicada ya detectada en el catálogo; esta fase no modifica `juegos.json`.

## Después de desplegar

1. En Google Search Console, enviar `sitemap.xml` en el informe Sitemaps.
2. Comprobar en Google Analytics DebugView o Tiempo real que aparecen `search`, `select_content` y `contact_click` al realizar esas acciones.
3. Marcar `contact_click` como evento clave si se adopta como conversión provisional.
4. Conservar los datos actuales como baseline y comparar el nuevo periodo tras acumular datos suficientes.
