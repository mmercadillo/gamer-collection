# Cambios SEO · Fase 3

Base utilizada: `pcgamearchive_fase2.zip`.

## Arquitectura por entidades

`generar_web.py` genera automáticamente cinco índices:

- `/desarrolladores/`
- `/distribuidores/`
- `/generos/`
- `/plataformas/`
- `/formatos/`

Para cada entidad con al menos 3 fichas se genera una landing estática con:

- URL limpia y descriptiva;
- canonical autorreferente;
- título y descripción propios;
- breadcrumbs HTML y JSON-LD;
- `CollectionPage` + `ItemList` en JSON-LD;
- resumen construido exclusivamente con datos reales del catálogo;
- primeras 24 fichas prerenderizadas;
- scroll infinito compatible con el buscador global;
- filtro de texto dentro de la entidad;
- enlaces internos a otras entidades.

## Evitar canibalización

Se reutilizan las landings editoriales ya existentes como destino canónico para:

- Big Box → `/juegos-pc-big-box.html`
- MS-DOS → `/juegos-msdos.html`
- Windows 95 / Windows 98 → `/juegos-windows-95-98.html`
- Aventura gráfica / Point and click → `/aventuras-graficas-pc.html`

Por tanto no se generan páginas paralelas como `/formatos/big-box/` o `/plataformas/msdos/`.

## Enlaces desde las fichas

Las fichas enlazan ahora directamente a las páginas de:

- formato;
- plataforma;
- género;
- desarrollador;
- distribuidor.

Cuando una entidad no alcanza el mínimo de 3 fichas se muestra como etiqueta sin crear una landing indexable.
Las series mantienen por ahora el comportamiento previo.

## Normalización de entidades

El generador agrupa diferencias puramente tipográficas de mayúsculas y acentos.
Ejemplos existentes en el catálogo como `Sega` / `SEGA`, `Microïds` / `Microids` o `Erbe Software` / `ERBE Software` no generan páginas duplicadas.

## Buscador

Se mantiene íntegra la Fase 2. El índice incorpora además `desarrollador` y `distribuidor` como campos estructurados para aplicar filtros exactos en las nuevas landings.

## Sitemap

El sitemap incorpora automáticamente:

- los cinco hubs de taxonomía;
- todas las entidades indexables;
- las landings editoriales reutilizadas una sola vez;
- las fichas canónicas de juegos.

Resultado con el catálogo actual: **1.975 URLs únicas**.

## Datos actuales del catálogo

Tras agrupar variantes tipográficas y aplicar el umbral de 3 fichas:

- 157 desarrolladores indexables;
- 100 distribuidores indexables;
- 143 géneros indexables;
- 13 plataformas indexables;
- 3 formatos indexables.

Algunas de estas entidades utilizan las landings editoriales existentes y por ello no crean un directorio adicional.

## Compatibilidad y mantenimiento

Al añadir o modificar un juego solo hay que ejecutar:

```bash
python generar_web.py
```

El generador reconstruye automáticamente buscador, sitemap, páginas de entidad y fichas. Los directorios de taxonomías son contenido generado y se regeneran completamente en cada ejecución.

## Validaciones realizadas

- `python -m py_compile generar_web.py`: OK.
- JavaScript de `catalogo.js` validado con Node.js: OK.
- `sitemap.xml` parseado como XML: OK.
- 1.975 páginas HTML indexables con canonical único: 0 duplicados.
- 52.496 enlaces internos comprobados: 0 destinos rotos.
- `Activision`: 35 resultados en búsqueda global, sin regresión.
- `Westwood Studios`: 15 resultados en búsqueda global.
- EAN de prueba `5028587010408`: 1 resultado.
- `Activision` como distribuidor: 34 fichas exactas.
- `Microïds` + `Microids` como desarrollador: 8 fichas agrupadas.
