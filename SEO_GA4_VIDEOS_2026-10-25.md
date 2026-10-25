# SEO audiovisual y medición GA4 — PC Game Archive

Fecha de implementación: 25/10/2026.

## Cambios

- `/videos/` se mantiene como catálogo por número de ficha. El título sigue enlazando con la ficha de la edición física. En cada tarjeta se añade un enlace discreto a la página individual del vídeo.
- `/videos/<slug>/` es una página específica donde el vídeo es el contenido principal, con URL canónica y metadatos `VideoObject` si existe `video_intro_fecha` válida.
- `sitemap.xml` incorpora las páginas individuales y `sitemap-videos.xml` declara las introducciones.
- `poster` y `thumbnailUrl` comparten la imagen principal del juego. Asegurar que `/juegos/<slug>/img/001.jpg` (o la imagen realmente detectada) se publica y responde HTTP 200.
- Los MP4 (`/videos/<slug>.mp4`) **no están incluidos** en el ZIP fuente. Deben conservarse en el destino del despliegue sin borrarlos.
- No se inventan fechas ni duración: el generador utiliza los datos declarados en `juegos.json`.

## Eventos GA4

Todos los reproductores MP4 disponen de identificación con atributos `data-*`. El código compartido emite:

| Evento | Condición |
|---|---|
| `video_start` | Primer inicio de reproducción por carga de página |
| `video_progress` | Primer cruce de 25%, 50% y 75% por carga de página |
| `video_pause` | Pausa durante reproducción, sin duplicar el fin |
| `video_complete` | Finalización |
| `video_game_click` | Enlace a ficha desde catálogo o página individual |

Parámetros: `game_num`, `game_slug`, `video_title`, `video_location`, `video_url` y `source_page` según el evento; `video_percent` en eventos de reproducción.

En GA4 registrar **dimensiones personalizadas de ámbito evento** para `game_num`, `game_slug`, `video_location` y, si resulta útil, `video_title`. `video_percent` se puede registrar como **métrica personalizada** de ámbito evento. No se crean automáticamente por el código.

### Validación tras desplegar

1. Verificar que las URLs MP4, las imágenes principales, `/videos/`, páginas individuales y los dos sitemaps responden correctamente.
2. Revisar el código de seguimiento consentido y validar eventos en GA4 DebugView, comprobando que no se duplican por pausas y reanudaciones.
3. Validar las páginas individuales con Google Rich Results Test y Search Console/Inspección de URL.
4. En Search Console, enviar `sitemap-videos.xml` y revisar el informe de indexación de vídeo. La elegibilidad para resultados enriquecidos **no está garantizada**.

## Notas operativas

- No cambiar el menú validado: «Vídeos» debe permanecer después de «Catálogo».
- Las páginas de las fichas siguen incluyendo sus reproductores originales.
- No interpretar la creación local del marcado SEO como validación de acceso real por Googlebot o de contenido MP4; eso debe comprobarse en el despliegue.
