# Fase 12 — Buscador avanzado

Base: `pcgamearchive_fase10D(1).zip`.

## Objetivo

Mejorar la búsqueda del archivo sin cambiar URLs, sitemap ni arquitectura SEO.

## Cambios

- Autocompletado en los campos de búsqueda con hasta 8 sugerencias.
- Las sugerencias combinan juegos y entidades: desarrolladores, distribuidores, series, géneros, plataformas, formatos y, cuando existen, mercado, idioma y soporte.
- Un juego con título único abre directamente su ficha desde la sugerencia.
- Una entidad seleccionada aplica un filtro exacto global, evitando que una coincidencia textual de la descripción se confunda con la entidad.
- Compatibilidad de teclado en el autocompletado: flechas, Enter y Escape.
- Búsqueda tolerante a erratas de forma conservadora:
  - términos de menos de 4 caracteres no usan fuzzy matching;
  - distancia máxima 1 para términos medios;
  - distancia máxima 2 para términos de 8 o más caracteres.
- Orden de resultados por relevancia cuando existe texto de búsqueda.
- Facetas dinámicas con recuentos para Formato, Plataforma, Género y Desarrollador.
- Las facetas preservan la consulta actual y el resto de filtros.
- Estado de cero resultados con recomendaciones cercanas y acceso para limpiar la búsqueda.
- Eventos de Analytics existentes conservados (`search`, `search_no_results`, `filter_used`) y nuevo evento `search_suggestion_click`.

## Compatibilidad

Se mantiene compatibilidad con:

- `?q=...`
- antiguas URLs `?titulo=...`
- filtros existentes `formato`, `serie`, `genero` y `plataforma`
- taxonomías y filtros por defecto de las páginas SEO.

El motor admite además filtros exactos por:

- `desarrollador`
- `distribuidor`
- `mercado`
- `idioma`
- `soporte`
- `tipo_edicion`
- `anio`

## Pruebas de regresión

Comparación contra Fase 10D:

- mismo número de ficheros generados: 2.074;
- mismo sitemap: 2.055 URLs únicas;
- 0 páginas añadidas o eliminadas;
- únicamente cambian `assets/js/catalogo.js`, `assets/css/styles.css` y el informe de generación;
- 72.758 enlaces HTML internos comprobados, 0 rotos;
- JavaScript validado con `node --check`;
- Python validado con `py_compile`.

Pruebas de tolerancia realizadas sobre el catálogo actual:

- `Activison` recupera las coincidencias de Activision;
- `Westwod` recupera las 15 fichas relacionadas con Westwood;
- `comand conquer` recupera las 13 ediciones de Command & Conquer.

## Funcionamiento al añadir juegos

No requiere mantenimiento manual. `python generar_web.py` vuelve a crear el índice y el buscador usa automáticamente los nuevos títulos y metadatos.
