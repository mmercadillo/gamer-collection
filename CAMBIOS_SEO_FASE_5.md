# PC Game Archive · Fase 5 · Mejora de landings editoriales

Base: `pcgamearchive_fase4.zip`.

## Cambios realizados

- Se elimina el bloque genérico y repetido orientado a SEO de las seis landings principales.
- Cada landing incorpora contenido editorial propio y útil para el visitante:
  - videojuegos clásicos de PC;
  - Big Box;
  - MS-DOS;
  - Windows 95/98;
  - ediciones españolas;
  - aventuras gráficas.
- Se añade un resumen dinámico calculado desde `juegos.json` con:
  - ediciones documentadas;
  - desarrolladores representados;
  - distribuidores representados;
  - géneros y subgéneros representados.
- Se añade el bloque `Explorar esta colección` con enlaces automáticos a las entidades con mayor presencia en cada selección.
- Los enlaces del bloque se deduplican cuando distintas entidades comparten una misma landing canónica.
- Se añaden breadcrumbs visibles y `BreadcrumbList` en JSON-LD a las seis landings.
- `Ver catálogo completo` enlaza a `/catalogo/`.
- El buscador de las landings mantiene el comportamiento global de la Fase 2.
- Se mantienen intactas las URLs y canonical existentes: no se crean nuevas URLs para estas landings.
- La landing de ediciones españolas explica expresamente que la selección actual se deriva de los datos disponibles de idioma/distribución hasta disponer de campos específicos de mercado e idioma.

## Automatización

Todo el contenido cuantitativo y los enlaces de entidades se recalculan al ejecutar:

`python generar_web.py`

Por tanto, al añadir nuevas fichas no es necesario editar manualmente estas landings.

## Validaciones realizadas

- Generación completa con 1.552 registros.
- 2.040 URLs únicas en sitemap, sin cambios de arquitectura respecto a Fase 4.
- XML del sitemap válido.
- Python y JavaScript válidos.
- 2.042 HTML generados en la validación completa.
- 57.439 enlaces internos HTML comprobados: 0 rotos.
- 0 rutas relativas incorrectas en imágenes de tarjetas.
- Breadcrumb visible y `BreadcrumbList` presentes en las seis landings.
- Eliminados los párrafos SEO genéricos repetidos de la versión anterior.
