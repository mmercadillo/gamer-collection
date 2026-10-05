# F17.3 — Estándar y plantilla de guías de ejecución y compatibilidad

## Objetivo

Definir el estándar que utilizará PC Game Archive para documentar de forma reproducible cómo instalar y ejecutar en sistemas actuales una edición física concreta conservada por el archivo.

F17.3 no publica todavía una guía de un juego real. Cierra el método, la estructura, la checklist y los criterios de validación que deberán aplicarse en F17.5 sobre la pieza piloto.

## Cambios implementados

- Publicación de **Estándar de guías de ejecución y compatibilidad** en:

```text
/documentacion/guias/estandar-guias-ejecucion-compatibilidad/
```

- Creación de `PLANTILLA_GUIA_EJECUCION.md` como hoja de trabajo obligatoria por guía.
- Inclusión del estándar en `documentacion.json` bajo la categoría `guias`.
- Actualización de README, diseño rector de F17, backlog y Novedades.
- Reutilización íntegra de la maquetación documental consolidada en la corrección de F17.2; no se añaden estilos específicos de artículos.

## Decisiones normativas

### 1. Una guía pertenece a una edición concreta

La guía debe identificar la edición física probada. No se extrapolará automáticamente el resultado a otras ediciones, idiomas, reediciones o mercados.

### 2. El máster de preservación no se usa como espacio de trabajo

Instalaciones, parches, wrappers, configuraciones y transformaciones se realizan sobre una copia o derivado de trabajo.

### 3. El entorno forma parte de la evidencia

Se registrarán sistema operativo, versión/build, arquitectura y hardware relevante, además de las herramientas auxiliares y sus versiones.

### 4. Solo se publican soluciones probadas

Las referencias externas pueden orientar una investigación, pero no se incorporan al procedimiento final hasta haber sido validadas por PC Game Archive sobre la edición y entorno documentados.

### 5. No basta con que el juego arranque

Cada guía debe completar una matriz funcional que permita distinguir entre `Correcto`, `Correcto con limitaciones`, `No funcional`, `No probado` y `No aplicable` para los subsistemas relevantes.

### 6. El procedimiento debe repetirse

Antes de declararse verificada, la guía debe repetirse desde un estado suficientemente limpio para comprobar que no depende de pasos omitidos, residuos de pruebas anteriores o conocimiento implícito.

### 7. La compatibilidad caduca

Toda guía mantiene una fecha de última prueba. Un cambio relevante del sistema operativo, wrapper, parche o procedimiento puede obligar a repetir la validación.

## Estados conceptuales de compatibilidad

- `No probada`.
- `Funcional`.
- `Funcional con ajustes`.
- `Parcial`.
- `No funcional`.

El estado nunca sustituye a la matriz funcional ni a la fecha de la prueba.

## Plantilla operativa

`PLANTILLA_GUIA_EJECUCION.md` incluye:

- identificación exacta de la pieza;
- punto de partida y relación con preservación;
- entorno anfitrión;
- herramientas, actualizaciones y componentes adicionales;
- instalación base;
- ajustes de compatibilidad;
- procedimiento final reproducible;
- matriz funcional;
- limitaciones y elementos no probados;
- intentos fallidos para trazabilidad interna;
- fuentes externas;
- evidencias internas;
- repetición final;
- Definition of Done.

## Criterio de publicación

La plantilla interna puede conservar información de investigación e intentos fallidos. La guía pública debe presentar el procedimiento final validado, las limitaciones, los elementos no probados y las fuentes necesarias para entender y repetir el resultado.

## Criterio de cierre de F17.3

F17.3 se considera completada cuando:

- existe un estándar público de guías de ejecución;
- existe una plantilla operativa obligatoria;
- están definidos los estados y la matriz funcional;
- la repetición forma parte del Definition of Done;
- preservación y compatibilidad permanecen separadas;
- la documentación utiliza el sistema visual existente sin estilos específicos nuevos.

## Siguiente entrega

**F17.4 — Integración bidireccional entre documentación y fichas de las piezas.**
