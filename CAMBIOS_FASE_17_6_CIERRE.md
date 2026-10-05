# F17.6 — Validación y cierre de F17

**Fecha de cierre:** 05/10/2026  
**Base:** F17.5 — piloto completo Red Baron 3-D

## Objetivo

Validar el recorrido completo de F17 con evidencia obtenida sobre una pieza real, consolidar las lecciones del piloto y cerrar formalmente la fase sin dejar decisiones críticas únicamente en la conversación de trabajo.

## Validación realizada

El piloto de **Red Baron 3-D — edición española Big Box, ficha #000215** demuestra el recorrido completo:

1. identificación y caracterización de la pieza;
2. caracterización lógica del CD-ROM;
3. escaneo de protección;
4. adquisición con MPF 3.10.0 + Redumper b749;
5. dos adquisiciones independientes coincidentes;
6. verificación SHA-256 de BIN y CUE;
7. separación del máster y copia de trabajo;
8. comprobación de hashes de la copia de trabajo;
9. montaje con WinCDEmu 4.1;
10. instalación y ejecución en Windows 10 Pro 22H2 build 19045;
11. validación funcional por subsistemas;
12. publicación del registro de preservación y de la guía de ejecución;
13. navegación bidireccional desde la ficha de la pieza.

## Ajustes consolidados

- El estándar de preservación pasa a considerarse **v1.0 estable**.
- Cada pieza debe registrar la versión del estándar aplicada.
- La caracterización se realiza antes de decidir método o formato de adquisición.
- Se registra el mecanismo lector real, firmware, software, versiones y parámetros.
- “No se detectó protección” se mantiene diferenciado de “no existe protección”.
- La verificación del máster requiere evidencia reproducible conforme al procedimiento aplicable.
- La copia de trabajo se verifica contra el máster antes de utilizarse.
- Compatibilidad y preservación son estados independientes.
- Una guía declara expresamente qué subsistemas se probaron y cuáles no.
- `Novedades` utiliza lenguaje de visitante y no nomenclatura interna de fases.
- La documentación pública reutiliza la interfaz visual existente del proyecto.

## Resultado

F17 queda cerrada. El proceso deja de ser un diseño teórico y pasa a ser un procedimiento operativo reutilizable para nuevas piezas. Los casos futuros que no encajen en v1.0 deberán evolucionar el estándar o el procedimiento con trazabilidad antes de generalizarse.

## Definition of Done de F17

- [x] Área documental pública.
- [x] Estándar de preservación versionado.
- [x] Plantilla de registro por pieza.
- [x] Estándar de compatibilidad.
- [x] Plantilla de guía de ejecución.
- [x] Integración bidireccional documentación ↔ ficha.
- [x] Pieza real preservada y verificada.
- [x] Copia de trabajo derivada y comprobada.
- [x] Ejecución real en sistema actual.
- [x] Guía pública reproducible.
- [x] Registros internos de evidencia.
- [x] Seguimiento y documentación de proyecto actualizados.
