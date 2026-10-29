# F18 — Novedades destacadas y acontecimientos del archivo

## Implementación

- Se mantiene **un único `novedades.json`**. Los registros antiguos no necesitan modificarse.
- `destacado` es un booleano opcional (ausente = `false`). `imagen` es una lista opcional de rutas de fotografías. `contenido` es una ruta opcional a Markdown.
- Se selecciona **una sola noticia**: la marcada como destacada de fecha más reciente. Si ha caducado, no se recupera otra noticia destacada anterior.
- Durante **14 días naturales**, contando la fecha de publicación como día 1 (huso horario Europe/Madrid), aparece un bloque a todo el ancho del contenedor encima de las cuatro tarjetas habituales.
- El script `assets/js/destacados.js` evalúa las fechas en el navegador, de modo que la portada se actualiza sin regeneración. Si JavaScript no funciona, el bloque permanece oculto y las novedades normales se muestran.
- La novedad destacada no se duplica en las cuatro tarjetas mientras está activa; al caducar regresa a la selección ordinaria si corresponde por fecha.
- Para noticias con `contenido` se genera una página propia de artículo, con renderizado Markdown, galería fotográfica, OG image (primera foto), datos estructurados Article y entrada en sitemap.
- Las imágenes se abren individualmente a tamaño completo; las galerías no se generan si el array está vacío.

## Ejemplo editorial pendiente

`EJEMPLO_F18_DONACION_NO_PUBLICAR.json` contiene un registro preparado para añadir a `novedades.json` después de revisar el texto, fotografías y permisos de atribución. **No se ha añadido automáticamente a `novedades.json`**. Las fotos reales están en `img/novedades/donacion-coleccion/` y el borrador del artículo en `contenidos/novedades/donacion-coleccion.md`.

## Validaciones

El generador comprueba que `destacado` sea booleano, que `imagen` sea una lista de rutas locales de imágenes, que los archivos existan y que `contenido` sea un Markdown existente. No se aceptan rutas relativas con `..` ni URLs externas para estos campos.

## Uso

Para publicar una novedad ampliada: agregar el objeto de ejemplo a `novedades.json`, adaptar su contenido e imágenes y ejecutar `python generar_web.py`. La página del acontecimiento seguirá publicada al finalizar sus 14 días en portada.

## Alcance de las pruebas

Generación normal y de ejemplo en directorio separado; comprobaciones de selección y HTML. La caducidad en navegadores reales debe verificarse al desplegar (reloj local del dispositivo, con referencia Europe/Madrid).
