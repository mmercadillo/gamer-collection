# F18 — Organización autocontenida de novedades destacadas (corrección)

El artículo de la donación está en `contenido/novedades/donacion-jose-antonio-20261029/contenido.md` y sus cinco fotos están en la subcarpeta `img/` del mismo acontecimiento.

**La noticia está incluida en `novedades.json`** con `destacado: true`. Al ejecutar el generador se publica como `/novedades/donacion-jose-antonio-20261029/`, y las fotos se copian a la ruta pública `img/novedades/<identificador>/`. La ruta fuente y la pública son diferentes intencionadamente.

Las carpetas vacías heredadas `img/` y `contenidos/` de la raíz del proyecto han sido eliminadas. Otras imágenes generales del sitio, si existen, no deben eliminarse.

La publicación del nombre del donante o de su historia personal debe revisarse antes del despliegue público. El texto del artículo no menciona su nombre, aunque el identificador de URL sí.

Compatibilidad: las noticias antiguas no requieren `destacado`, `contenido` ni `imagen`; se mantiene la duración de 14 días y la selección del destacado con fecha más reciente.
