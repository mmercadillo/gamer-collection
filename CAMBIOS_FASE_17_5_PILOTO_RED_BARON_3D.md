# F17.5 — Pieza piloto: Red Baron 3-D

**Fecha:** 05/10/2026  
**Estado:** En curso — preservación verificada, compatibilidad pendiente

## Objetivo

Validar con una pieza física real el ciclo definido en F17.1–F17.4. El piloto utiliza `Red Baron 3-D`, edición española Big Box, ficha `#000215`.

## Preservación realizada

- soporte: 1 CD-ROM;
- estructura: una pista `MODE1/2352`;
- protección: el escaneo realizado con MPF no detectó una protección de copia;
- frontend: MPF 3.10.0;
- adquisición: Redumper build b749;
- lectora: HL-DT-ST DVDRAM GTB0N, firmware FU03;
- velocidad: 1x;
- reintentos configurados: 20;
- Error Count: 0;
- C2 Error Count: 0;
- dos adquisiciones independientes;
- BIN y CUE con SHA-256 coincidente en ambas adquisiciones.

## Integración pública

Se publica `/documentacion/preservacion/red-baron-3d-bigbox/` y se relaciona exclusivamente desde `documentacion.json` con `juegos/red-baron-3d-bigbox/`. El generador de F17.4 crea automáticamente ambos sentidos:

1. ficha → registro de preservación;
2. registro de preservación → ficha #000215.

No se publica ni distribuye la imagen del CD.

## Registro interno

`registros_preservacion/red-baron-3d-bigbox.md` conserva la evidencia operativa, hashes, hardware, parámetros, incidencias y estado del piloto.

## Corrección del catálogo

La ficha deja de afirmar que la ejecución virtual es viable, ya que todavía no se ha probado. El apartado de preservación se actualiza con la evidencia real obtenida y la compatibilidad permanece como no determinada hasta la segunda etapa del piloto.

## Pendiente

- crear copia de trabajo derivada del máster;
- instalar/probar esta edición en un sistema actual;
- completar la matriz funcional;
- publicar la guía de ejecución;
- cerrar F17.5 solo después de validar el recorrido completo.
## Ajuste de reproducibilidad y versionado del estándar

Durante la revisión del primer registro público se detectó que documentar únicamente resultados no era suficiente para que la preservación actuase también como guía reproducible. Se incorporan:

- versión explícita del estándar aplicado: **v1.0**;
- fecha y operador del proceso;
- software y versiones utilizados;
- hardware separado del software;
- parámetros exactos relevantes de adquisición;
- comandos PowerShell empleados para caracterización y SHA-256;
- procedimiento aplicado paso a paso;
- versionado formal del estándar con histórico de cambios;
- campo obligatorio de versión del estándar en `PLANTILLA_REGISTRO_PRESERVACION.md`.

El estándar continúa siendo un único documento vivo. Los registros cerrados mantienen la versión que utilizaron y no se reescriben retrospectivamente al evolucionar el estándar.

