# Fase 8 · Fichas relacionadas y enlazado interno contextual

Fecha: 2026-08-14
Base: `pcgamearchive_fase7(1).zip`

## Objetivo

Convertir cada ficha de juego en un nodo de navegación del archivo, facilitando al usuario y a los rastreadores descubrir otras ediciones y juegos relacionados a partir de los datos ya catalogados.

## Cambios

- Se generan automáticamente, cuando existen resultados, bloques de:
  - **Otras ediciones de este juego**: mismo título, distinta ficha/edición física.
  - **Misma serie o colección**: excluye valores estructurales como `Todos`, `Big Box`, `DVD Case` y `Jewel Case`.
  - **Otros juegos de <desarrollador>**: prioriza títulos que además comparten género.
  - **Juegos relacionados**: ranking determinista por género, plataforma, formato, distribuidor y tags.
- Los resultados se deduplican entre bloques: una ficha ya mostrada no vuelve a aparecer en los siguientes grupos.
- En serie/desarrollador/relacionados se prioriza variedad de títulos para evitar que varias ediciones del mismo juego monopolicen el bloque.
- Cada bloque muestra hasta 4 fichas y reutiliza las tarjetas existentes del catálogo.
- Los enlaces e imágenes se generan con rutas absolutas `/juegos/<slug>/...`, por lo que funcionan desde cualquier profundidad.
- Las tarjetas mantienen `data-game-link`, por lo que sus clics siguen entrando en la medición `select_content` ya existente.
- Se añade diseño responsive específico para los bloques relacionados.

## Rendimiento del generador

Para no penalizar el flujo de alta de juegos, se construyen índices invertidos y firmas normalizadas una sola vez por ejecución:

- título
- serie/colección
- desarrollador
- género
- plataforma
- distribuidor
- formato
- tags

Con el catálogo actual (1.552 registros), el cálculo de relaciones completo se realiza en aproximadamente 5 segundos en el entorno de validación y la generación completa ronda 7–8 segundos.

## Cobertura con el catálogo actual

- 225 fichas con otras ediciones del mismo título.
- 581 fichas con bloque de serie/colección.
- 1.147 fichas con bloque del mismo desarrollador.
- 1.552 fichas con bloque de juegos relacionados.

## Validaciones

- 1.552 registros procesados.
- 2.041 URLs únicas en sitemap (sin cambios respecto a Fase 7).
- 77.959 enlaces internos HTML revisados: 0 rotos.
- 12.179 tarjetas contextuales generadas.
- 0 rutas relativas incorrectas en enlaces o imágenes de los bloques relacionados.
- Python y XML válidos.
- Se mantiene la compatibilidad con las Fases 0–7.

## Flujo de mantenimiento

No hay mantenimiento manual adicional. Al añadir o modificar un juego y ejecutar:

```bash
python generar_web.py
```

se recalculan automáticamente todas las relaciones de las fichas.
