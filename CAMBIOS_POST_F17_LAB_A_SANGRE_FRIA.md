# Laboratorio posterior a F17 — A Sangre Fría

**Fecha:** 07/10/2026  
**Estado:** Cerrado

## Objetivo

Aplicar de extremo a extremo el estándar F17 a una pieza multi-CD real y validar que el modelo funciona correctamente con tres soportes físicos independientes.

## Resultado

- pieza: A Sangre Fría, edición española Big Box, ficha #000216;
- soportes: 3 CD-ROM identificados como CD1 SPAIN, CD2 SPAIN y CD3 SPAIN;
- los tres discos preservados mediante dos adquisiciones independientes coincidentes por soporte;
- estructura observada: una pista MODE2/2352 en cada CD;
- protección: no detectada por el análisis realizado;
- másteres constituidos y separados de las copias de trabajo;
- copia de trabajo completa verificada mediante SHA-256;
- instalación multi-CD validada en Windows 10 Pro build 19045;
- cambios CD1→CD2→CD3 probados correctamente;
- CD1 requerido para la ejecución;
- ejecución nativa validada sin parches, wrappers, compatibilidad ni elevación administrativa;
- guardado, carga, cierre y segundo arranque verificados.

## Corrección de catálogo

La ficha indicaba `2 CD-ROM`. La evidencia física del ejemplar conservado confirma `3 CD-ROM`, por lo que se corrige el dato.

## Documentación creada

- `registros_preservacion/a-sangre-fria-bigbox.md`
- `registros_compatibilidad/a-sangre-fria-bigbox-windows-10.md`
- `documentacion/fuentes/preservacion-a-sangre-fria-bigbox.md`
- `documentacion/fuentes/guia-a-sangre-fria-windows-10.md`
- relaciones añadidas a `documentacion.json`
- novedades públicas añadidas a `novedades.json`

## Conclusión

El segundo laboratorio valida que el estándar F17 escala de un soporte único a una edición multi-CD sin cambiar sus principios: caracterización independiente, doble adquisición, hashes, másteres inmutables, copia de trabajo verificada y compatibilidad documentada con evidencia.
