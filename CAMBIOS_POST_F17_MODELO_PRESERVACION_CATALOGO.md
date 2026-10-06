# Cambio posterior a F17 — Modelo mínimo de preservación en el catálogo

**Fecha:** 06/10/2026

## Objetivo

Eliminar del catálogo estructurado afirmaciones históricas o recomendaciones de preservación no verificadas y dejar en cada pieza únicamente un resumen público respaldado por trabajo de laboratorio real.

## Nuevo contrato de datos

El antiguo bloque `proteccion` se sustituye por:

```json
"preservacion": {
  "resumen": ""
}
```

`resumen` es obligatorio como campo, pero admite cadena vacía. Debe permanecer vacío hasta que la pieza haya sido tratada conforme al protocolo de preservación/compatibilidad.

## Migración

Se incorpora `migrar_preservacion_resumen.py`, seguro por defecto (simulación) y aplicable mediante `--apply`. La migración elimina `proteccion`, crea `preservacion.resumen` en las 1.571 piezas y solo conserva automáticamente un resumen anterior si existe documentación pública de preservación asociada a la pieza. En la migración actual únicamente **Red Baron 3-D (#000215)** cumple ese criterio.

Resultado:

- 1.571 piezas migradas;
- 1 resumen verificado conservado;
- 1.570 resúmenes vacíos.

## Schema y herramientas

- `json_schema.json` exige ahora `preservacion.resumen` y elimina el contrato legado `proteccion`.
- `validar_catalogo.py` valida exclusivamente el nuevo bloque.
- `corregir_catalogo.py` crea/repara únicamente la estructura mínima de preservación.
- `generar_web.py` ya no muestra Protección, Formato recomendado ni Jugable en virtualización.
- Las fichas sin resumen verificado no muestran una sección de preservación vacía.
- El buscador indexa `preservacion` en lugar de `proteccion`.

## Principio

`juegos.json` resume resultados verificados; no prescribe cómo preservar ni cómo ejecutar una pieza. La evidencia detallada y las decisiones técnicas viven en la documentación y registros F17.
