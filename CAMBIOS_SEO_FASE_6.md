# Cambios SEO · Fase 6

Fecha: 2026-08-14

## Objetivo

Crear una landing específica de captación para personas que quieran vender, donar u ofrecer videojuegos físicos de PC a PC Game Archive, preparada para SEO orgánico, medición en Google Analytics y futuras campañas SEM.

## Cambios realizados

- Nueva URL canónica: `/vender-videojuegos-pc-antiguos/`.
- Landing generada automáticamente por `generar_web.py`.
- Contenido específico para:
  - compra de colecciones, lotes y juegos individuales;
  - donaciones;
  - Big Box, CD-ROM, DVD, Jewel Case y disquetes;
  - manuales, documentación y material promocional;
  - ediciones españolas y europeas;
  - material incompleto con interés documental.
- Proceso de contacto explicado en cuatro pasos.
- Preguntas frecuentes visibles para reducir fricción antes del contacto.
- Reutilización de `anuncio_with_bgc.png` como imagen principal y Open Graph.
- Nuevo acceso `Ofrecer juegos` en la navegación principal.
- Nueva llamada a la acción desde la portada.
- `contacto.html` deriva las ofertas de juegos a la landing específica.
- Inclusión de la landing en `sitemap.xml`.
- Canonical propio y breadcrumbs HTML + JSON-LD.
- JSON-LD `WebPage` y `Organization`.

## Analítica

Los CTA de la landing registran el evento:

`offer_games_click`

con parámetros:

- `intent`: `sell`, `donate` o `general`.
- `channel`: `email` o `instagram`.
- `link_url`.

Los eventos existentes `contact_click` y `outbound_social_click` se mantienen.

## Automatización

Al ejecutar:

```bash
python generar_web.py
```

la landing, navegación, sitemap y medición se regeneran junto con el resto de la web.

## Validaciones

- 1.552 juegos procesados.
- 2.041 URLs únicas en sitemap.
- Nueva landing presente una sola vez en sitemap.
- 59.491 enlaces internos comprobados: 0 rotos.
- Canonical correcto.
- JSON-LD válido.
- JavaScript válido con `node --check`.
- Imagen principal servida desde `/anuncio_with_bgc.png`.
- Sin cambios en `/juegos/<slug>/img/` ni en el contenido documental de los juegos.
