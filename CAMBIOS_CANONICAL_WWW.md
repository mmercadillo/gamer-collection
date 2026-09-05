# Unificación del dominio canónico en www

PC Game Archive adopta `https://www.pcgamearchive.org` como base URL absoluta oficial para alinear todas las señales SEO con el dominio configurado en `CNAME` (`www.pcgamearchive.org`).

Cambios aplicados sobre `pcgamearchive(4).zip`:

- `DEFAULT_BASE_URL` del generador actualizado a `https://www.pcgamearchive.org`.
- Ejemplos y documentación operativa actualizados a la misma base URL.
- `sitemap.xml` conserva exactamente su estructura y sus imágenes, cambiando únicamente el host a `www`.
- `robots.txt` referencia `https://www.pcgamearchive.org/sitemap.xml`.
- Canonical, Open Graph, Twitter images, JSON-LD y demás URLs absolutas generadas quedan alineadas con `www`.
- Los enlaces absolutos de captación en los prompts se actualizan a `www`.
- El identificador absoluto del schema se actualiza al dominio `www`.
- `CNAME` ya era `www.pcgamearchive.org` y no se modifica.

No se han cambiado el catálogo, los contenidos editoriales, el diseño, las taxonomías, las rutas relativas ni la lógica funcional del sitio.
