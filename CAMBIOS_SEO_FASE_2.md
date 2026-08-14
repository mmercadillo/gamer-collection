# PC Game Archive — Fase 2: buscador global

Fecha: 14/08/2026

Base utilizada: `pcgamearchive-seo-fase0-1.zip`.

## Cambios

- La búsqueda principal deja de estar limitada al título y utiliza el parámetro `q`.
- Se mantiene compatibilidad con URLs antiguas que usen `?titulo=...`.
- El buscador consulta estos metadatos:
  - número de catálogo
  - título
  - plataforma
  - formato
  - género
  - desarrollador
  - distribuidor
  - EAN/UPC
  - descripción
  - contenido físico (`incluye`)
  - serie
  - tags
  - protección y datos de preservación
- Las consultas de varias palabras exigen que estén presentes todos los términos, aunque no aparezcan consecutivamente. Ejemplo: `command conquer`.
- Los filtros de formato, serie, género y plataforma siguen funcionando junto con la búsqueda global.
- Los formularios dejan de enviar parámetros vacíos, generando URLs más limpias.
- La caja principal se presenta como `Buscar en todo el archivo…`.
- Se corrige la actualización del contador de resultados para que modifique el contador del catálogo y no el texto de la sección SEO de la portada.
- Se conserva la medición Analytics implementada en Fase 0/1 (`search`, `search_no_results`, filtros y clics).

## Validaciones realizadas

Catálogo: 1.552 registros.

Consultas de prueba:

- `Activision`: 35 resultados.
- `Westwood Studios`: 15 resultados.
- `command conquer`: 13 resultados.
- `Steve Meretzky`: 1 resultado.
- `5028587010408`: 1 resultado (Blade Runner).
- `Sound Blaster`: 13 resultados.
- `FX Interactive`: 182 resultados.
- `Activision` + formato `Big Box`: 13 resultados.

Validación técnica:

- `generar_web.py` compila correctamente.
- `assets/js/catalogo.js` pasa `node --check`.
- Sitemap XML válido.
- Se mantienen fuera del sitemap `/index.html`, `bigbox.html` y los `lastmod` ficticios.
- La carpeta `juegos/` generada durante las pruebas se excluye del ZIP entregado, igual que en la base recibida.
