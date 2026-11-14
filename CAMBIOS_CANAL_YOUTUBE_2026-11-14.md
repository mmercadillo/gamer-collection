# Canal oficial de YouTube — 14/11/2026

- Enlace al canal oficial en pie de página, contacto y sección de vídeos.
- `Organization.sameAs` ampliado con YouTube para todos los documentos con dicho dato estructurado.
- Medición GA4 `outbound_social_click` con `platform=youtube`.
- Nueva noticia editorial en `novedades.json` con artículo Markdown autocontenido.
- Fecha global de actualización ajustada a 2026-11-14.
- La reproducción propia y las fichas permanecen intactas; sin migración de MP4 ni inserción de reproductores externos.

## Verificación

Ejecutar `python generar_web.py --out .` y comprobar `/`, `/videos/`, `/contacto.html`, `/novedades/` y `/novedades/canal-youtube-pc-game-archive-20261114/`.
