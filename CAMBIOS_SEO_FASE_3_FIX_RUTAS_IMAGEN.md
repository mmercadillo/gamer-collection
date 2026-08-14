# Fase 3 — Corrección de rutas de imágenes

Corrección aplicada sobre `pcgamearchive_fase3.zip`.

## Problema

Las tarjetas recreadas dinámicamente por `assets/js/catalogo.js` utilizaban la URL de la ficha como ruta relativa (`juegos/<slug>/`). En páginas anidadas como `/plataformas/winnt/` el navegador resolvía las imágenes como `/plataformas/winnt/juegos/<slug>/img/001.jpg`.

## Corrección

- Todas las URLs de fichas incluidas en `search-index.js` son absolutas desde la raíz: `/juegos/<slug>/`.
- `catalogo.js` normaliza defensivamente las URLs a raíz antes de crear enlaces e imágenes.
- Las tarjetas HTML generadas usan `/juegos/<slug>/img/001.jpg`.
- Las galerías de fichas usan también rutas absolutas `/juegos/<slug>/img/<archivo>`.
- El fallback visual usa `/no_disponible.png`.

## Validación

- 1.552 entradas del índice de búsqueda con URL `/juegos/.../`.
- 0 rutas relativas de imágenes de juegos en el HTML generado.
- JavaScript validado con `node --check`.
- Generación completa correcta con 1.552 registros.
