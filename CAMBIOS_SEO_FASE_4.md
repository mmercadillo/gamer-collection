# Cambios SEO · Fase 4

## Objetivo

Complementar el scroll infinito de la portada con una serie HTML paginada y rastreable, sin cambiar la experiencia principal de navegación.

## Cambios realizados

- Nuevo catálogo estático en `/catalogo/`.
- Páginas sucesivas en `/catalogo/pagina/<n>/`.
- Tamaño de página: 24 fichas.
- Con el catálogo actual de 1.552 registros se generan 65 páginas.
- Cada página tiene:
  - canonical propio;
  - título y descripción propios;
  - breadcrumbs;
  - JSON-LD `CollectionPage` + `BreadcrumbList`;
  - enlaces HTML reales a las fichas;
  - navegación `Anterior` / `Siguiente` y números de página.
- La portada mantiene el scroll infinito y enlaza al catálogo paginado.
- La navegación principal incorpora `Catálogo`.
- `sitemap.xml` incorpora automáticamente todas las páginas del catálogo paginado.
- `generar_web.py` regenera el número necesario de páginas al cambiar el tamaño del catálogo.
- Si disminuye el catálogo, el directorio `/catalogo/` se limpia antes de regenerarse para no dejar páginas obsoletas.

## Automatización

No requiere mantenimiento manual. Al ejecutar:

```bash
python generar_web.py
```

se recalcula automáticamente el número de páginas según `len(juegos) / 24`.

## Validaciones realizadas

- 1.552 tarjetas distribuidas en 65 páginas.
- 1.551 URLs de ficha únicas (existe un duplicado ya conocido en `juegos.json`).
- 65 URLs de catálogo incluidas en sitemap.
- 2.040 URLs totales y únicas en sitemap.
- canonical correcto en las 65 páginas.
- 0 rutas relativas incorrectas de imágenes en el catálogo paginado.
- 69.606 enlaces internos HTML comprobados sobre la generación completa: 0 destinos rotos.
- `catalogo.js` válido con `node --check`.
- `generar_web.py` válido con `python -m py_compile`.
