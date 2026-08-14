# Fase 12.3 · Reestructuración de portada y navegación

## Objetivo

Reordenar visualmente la portada después de las mejoras acumuladas en las fases anteriores, sin cambiar la arquitectura SEO ni los datos del catálogo.

## Cambios

- `Ayuda a ampliar el archivo` pasa a ser la primera sección visible de la portada.
- La presentación de PC Game Archive queda separada del buscador y se hace más compacta.
- El buscador pasa a tener una sección propia `Buscar en el archivo`.
- Los resultados, facetas y fichas aparecen inmediatamente debajo del formulario de búsqueda.
- Cuando existe una búsqueda/filtro activo, la portada entra en modo resultados y oculta la captación y la presentación para priorizar la consulta.
- Se eliminan de la portada los bloques redundantes `Explorar el archivo` y `Explorar por datos del catálogo`.
- La navegación principal queda simplificada a:
  - Inicio
  - Catálogo
  - Explorar
  - Ofrecer juegos
  - Contacto
  - Instagram
- `Explorar` agrupa dos bloques:
  - Colecciones: PC clásico, Big Box PC, MS-DOS, Windows 95/98, Aventuras gráficas, Ediciones españolas y Series.
  - Datos del archivo: solo los hubs de taxonomía que realmente están publicados por `generar_web.py`.
- El menú `Explorar` se adapta al menú móvil de la Fase 12.2.
- Las páginas de taxonomía marcan `Explorar` como navegación activa.

## Conservación de funcionalidad

- Se mantienen el buscador avanzado, autocompletado, tolerancia a erratas y facetas.
- Se mantienen los desplegables de Formato y Serie.
- No se añaden ni eliminan URLs SEO.
- `juegos.json` y `json_schema.json` no se modifican.
- El sitemap mantiene las mismas 2.055 URLs canónicas.
