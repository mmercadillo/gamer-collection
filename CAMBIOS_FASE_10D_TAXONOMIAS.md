# Fase 10D · Explotación web de los nuevos campos

Base: `pcgamearchive_fase10C.zip`.

## Objetivo

Cerrar la Fase 10 incorporando los nuevos metadatos (`anio`, `mercado`, `idioma`, `soporte`, `tipo_edicion`) a la arquitectura SEO de forma automática, conservadora y retrocompatible.

## Cambios

- Se añaden cinco taxonomías potenciales al generador:
  - `/anos/`
  - `/mercados/`
  - `/idiomas/`
  - `/soportes/`
  - `/tipos-edicion/`
- Cada taxonomía nueva requiere una masa crítica global mínima de **150 fichas documentadas** antes de publicar su hub.
- Una entidad concreta requiere al menos **3 fichas** para disponer de página indexable.
- Los valores documentados aparecen enlazados desde las fichas solo cuando su entidad es indexable. En caso contrario permanecen como etiquetas normales.
- Los nuevos campos se exponen también de forma estructurada en `search-index.js` cuando tienen valor, permitiendo que las páginas de taxonomía se filtren correctamente en cliente.
- Los hubs y entidades publicables se incorporan automáticamente a `sitemap.xml`.
- La portada muestra únicamente los hubs de taxonomías realmente publicadas.

## Anti-canibalización

`España` reutiliza `ediciones-espanolas-pc.html` como destino, en lugar de generar `/mercados/espana/`. Esto mantiene una única URL principal para esa intención SEO, siguiendo el mismo patrón que Big Box, MS-DOS, Windows 95/98 y aventura gráfica.

## Estado con el catálogo actual

- Año: 13 fichas documentadas → no se publica todavía.
- Mercado: 267 fichas documentadas → hub activo.
  - España: 232 (reutiliza `ediciones-espanolas-pc.html`)
  - Europa: 41
  - Italia: 3
- Idioma: 176 fichas documentadas → hub activo.
  - Español: 164
  - Inglés: 19
  - Multilingüe: 8
  - Italiano: 3
- Soporte: 262 fichas documentadas → hub activo.
  - CD-ROM: 219
  - Disquete 3,5": 32
  - Disquete 5,25": 6
  - DVD-ROM: 5
  - CD de audio: 3
- Tipo de edición: 106 fichas documentadas → no se publica todavía.

El umbral global es absoluto, no porcentual. Así, una taxonomía ya publicada no desaparece simplemente porque el catálogo crezca con nuevas fichas cuyos metadatos aún estén vacíos.

## Retrocompatibilidad

Con los cinco campos nuevos completamente vacíos, la salida del generador 10D es idéntica byte a byte a la de 10C (salvo `informe_generacion_seo.md`, que contiene fecha/hora).

`juegos.json`, `json_schema.json` e `inferir_campos_fase10c.py` no se modifican en esta subfase.

## Validaciones

- 1.552 juegos procesados.
- 2.055 URLs canónicas únicas en el sitemap actual.
- 72.758 enlaces internos comprobados: 0 rotos.
- 2.055 páginas indexables: 2.055 canonical únicas.
- `catalogo.js`: sintaxis JavaScript válida.
- `sitemap.xml`: XML válido.
- Validación del catálogo: 817 errores y 1.592 avisos preexistentes, sin nuevas incidencias por Fase 10D.
