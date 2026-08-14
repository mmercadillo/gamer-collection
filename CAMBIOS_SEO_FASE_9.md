# PC Game Archive — Fase 9: SEO de imágenes

Base: `pcgamearchive_fase8(1).zip`.

## Objetivo

Mejorar descubrimiento, contexto semántico y rendimiento de las fotografías documentales en Google Search/Google Images sin modificar ni renombrar los originales almacenados en `/juegos/<slug>/img/`.

## Cambios

- `alt` descriptivos para portadas, imagen principal y galería usando los datos reales de título, formato y plataforma.
- Captions visibles en la imagen principal y en cada fotografía de la galería.
- Las fotografías de galería se pueden abrir a tamaño completo mediante un enlace directo a su fichero original.
- La galería usa `object-fit: contain` para priorizar la visualización completa de la fotografía documental frente al recorte visual.
- Imagen principal de cada ficha: `loading="eager"` + `fetchpriority="high"`.
- Imágenes secundarias: `loading="lazy"` + `decoding="async"`.
- `max-image-preview:large` añadido a las páginas indexables.
- `og:image:alt` y `twitter:image:alt` cuando existe un texto alternativo específico.
- Las fichas con fotografía real generan `WebPage.primaryImageOfPage` y `ImageObject`, enlazados con el `VideoGame` mediante `@id`.
- `no_disponible.png` continúa siendo fallback visual/social, pero no se presenta como fotografía documental en `ImageObject` ni en el sitemap de imágenes.
- `sitemap.xml` incorpora el namespace oficial de imágenes y añade `<image:image><image:loc>...` únicamente para ficheros que existen físicamente en la carpeta `img` de cada juego.
- Los nombres `001.jpg`, `002.jpg`, etc. se conservan. No se renombran originales ni se cambian rutas documentales.
- El inventario de imágenes se calcula una vez por ejecución de `generar_web.py` y se reutiliza para fichas, sitemap e informe.

## Funcionamiento al añadir un juego

El flujo no cambia:

```bash
python generar_web.py
```

Si el juego tiene fotografías en:

```text
/juegos/<slug>/img/
```

el generador las detectará automáticamente, actualizará la galería, los datos estructurados y `sitemap.xml`.

## Validaciones realizadas

- Generación completa con 1.552 registros.
- Sitemap XML válido.
- 2.041 URLs canónicas de página, sin modificar la arquitectura de Fase 8.
- Prueba con una ficha de 3 imágenes: 3 entradas `image:image` y 3 URLs correctas.
- `primaryImageOfPage` e `ImageObject` presentes solo cuando existe imagen real.
- `no_disponible.png` excluido de los datos estructurados documentales.
- JSON-LD parseable.
- JavaScript generado válido con `node --check`.
- Rutas de juego e imágenes absolutas desde raíz.
