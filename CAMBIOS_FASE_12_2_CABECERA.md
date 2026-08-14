# Fase 12.2 — Cabecera en dos niveles

Ajuste exclusivamente visual realizado sobre la Fase 12.1.

## Cambios

- La identidad de PC Game Archive (logo, nombre y subtítulo) ocupa una franja propia.
- La navegación principal pasa a una segunda franja y dispone de todo el ancho útil del sitio.
- En escritorio, el menú se centra y se mantiene en una sola línea.
- A 900 px o menos, la navegación se sustituye por un botón «Menú» accesible mediante `aria-expanded` / `aria-controls`.
- El menú móvil se despliega en dos columnas y pasa a una columna en pantallas pequeñas.
- Se mantienen exactamente los mismos enlaces y el mismo estado activo de navegación.

## Sin cambios funcionales

No se modifica:

- `juegos.json`
- `json_schema.json`
- `catalogo.js`
- `search-index.js`
- `sitemap.xml`
- `robots.txt`
- buscador, filtros o facetas
- URLs, canonical o taxonomías

El cambio queda centralizado en `generar_web.py` y en los estilos generados, de modo que futuras regeneraciones mantienen automáticamente la nueva cabecera.
