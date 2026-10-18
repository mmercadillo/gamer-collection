# PC Game Archive — preservación y compatibilidad de Panzer Commander

Fecha de cierre documental: 18/10/2026

## Objetivo

Cerrar para la edición española Big Box de `Panzer Commander: WWII Tank Simulator` (#000214) las dos vertientes documentales públicas utilizadas por PC Game Archive:

1. registro de preservación digital de la pieza física;
2. guía reproducible para instalar y jugar en Windows 10.

La guía de ejecución publica únicamente la solución final validada y no reproduce el historial de ensayo y error del laboratorio.

## Preservación publicada

- soporte: 1 CD-ROM;
- etiqueta de volumen: `Pzc_v1_0`;
- estructura: una pista `MODE1/2352`;
- frontend: MPF 3.10.0;
- adquisición: Redumper build b749;
- unidad realmente utilizada: TSSTcorp DVD-ROM SH-116AB, firmware FT01;
- velocidad: 8x;
- reintentos: 20;
- Error Count: 0;
- C2 Error Count: 0;
- protección: no detectada por el análisis realizado;
- dos adquisiciones independientes coincidentes;
- BIN y CUE verificados por SHA-256;
- máster separado de la copia de trabajo.

La adquisición es anterior a la formalización de PCGA-MASTER-01. El registro conserva el hardware realmente utilizado y no atribuye retrospectivamente la adquisición al entorno de referencia actual.

## Solución de compatibilidad publicada

- instalador Win16 ejecutado con otvdm 0.9.0;
- DirectX 5 incluido en el CD no instalado;
- DDrawCompat 0.7.2 copiado junto a `Panzer.exe`;
- `DDrawCompat.ini` con una única intervención explícita: `FpsLimiter = flipend(30)`;
- sin modo manual de compatibilidad de Windows;
- CD o imagen montada durante la ejecución.

## Validación funcional publicada

Se documenta como comprobado:

- introducción;
- menús;
- entrada al escenario 3D;
- conducción;
- disparo;
- cambios de vista;
- uso de distintas opciones durante una sesión representativa;
- ausencia del bloqueo 3D durante la prueba final.

No se extrapola el resultado a Windows 11, otras ediciones, gamepad/joystick, multijugador ni campaña completa.

## Ficheros añadidos o modificados

- `registros_preservacion/panzer-commander-wwii-tank-simulator-bigbox.md`
- `registros_compatibilidad/panzer-commander-wwii-tank-simulator-bigbox-windows-10.md`
- `documentacion/fuentes/preservacion-panzer-commander-wwii-tank-simulator-bigbox.md`
- `documentacion/fuentes/guia-panzer-commander-windows-10.md`
- `documentacion.json`
- `novedades.json`
- `juegos.json`
- páginas HTML regeneradas mediante `generar_web.py`
- `sitemap.xml` regenerado
