# Registro de compatibilidad — Red Baron 3-D / Windows 10

**Estado:** Funcional en el entorno probado  
**Ficha PCGA:** #000215  
**URL:** `juegos/red-baron-3d-bigbox/`  
**Fecha de prueba:** 05/10/2026  
**Responsable:** PC Game Archive

## 1. Identificación

- Título: Red Baron 3-D
- Edición: española Big Box
- Mercado: España
- Idioma: Español
- Soporte: 1 CD-ROM
- Registro de preservación: `registros_preservacion/red-baron-3d-bigbox.md`

## 2. Punto de partida

- Origen: copia de trabajo derivada del máster BIN/CUE verificado.
- BIN SHA-256: `1E354950083B85F76623CD5BED2F061C90833EB1431ED2BBBD288BEB125BA66B`
- CUE SHA-256: `CB27C9E074A1BC07DFBF5A967C5641F216CBB2E166D460DF9418EC78BED501F6`
- Hashes de la copia de trabajo: coincidentes con el máster antes de la prueba.

## 3. Entorno anfitrión

- Sistema operativo: Windows 10 Pro 22H2
- Build: 19045
- CPU: Intel Core i5-3470
- RAM: 16 GB
- GPU: Intel HD Graphics
- Driver: 10.18.10.4358
- Resolución: 1360 × 768

## 4. Herramientas

- WinCDEmu 4.1: montaje de BIN/CUE.
- PowerShell: verificación SHA-256 de la copia de trabajo.
- Parches/wrappers adicionales: ninguno.
- Modo compatibilidad: no utilizado.
- Ejecución como administrador: no utilizada.

## 5. Instalación

1. Copia de trabajo creada en `C:\PCGA\trabajo\red-baron-3d`.
2. SHA-256 de BIN y CUE comprobados y coincidentes con el máster.
3. `REDBARON_3D.cue` montado con WinCDEmu 4.1.
4. Volumen virtual comprobado: `REDBARON_3D`, CDFS, 718.379.008 bytes.
5. `SETUP.EXE` ejecutado de forma nativa.
6. Instalación completada correctamente.

## 6. Ejecución

- Primer arranque: correcto.
- Menú principal: correcto.
- Vídeo/gráficos: correctos durante la prueba.
- Sonido: correcto.
- Música: correcta.
- Teclado/ratón: correctos.
- Inicio de partida: correcto.
- Guardado: correcto.
- Carga: correcta.
- Cierre y segundo arranque: correctos.

## 7. Matriz funcional

- Instalación: Correcto
- Arranque: Correcto
- Menús: Correcto
- Vídeo/cinemáticas: Correcto durante la prueba realizada
- Gráficos 2D/3D: Correcto durante la prueba realizada
- Sonido: Correcto
- Música: Correcto
- Teclado/ratón: Correcto
- Gamepad/joystick: No probado
- Inicio de partida: Correcto
- Juego representativo: Correcto durante la prueba realizada
- Guardado: Correcto
- Carga: Correcto
- Cambio de nivel/escena: No probado expresamente
- Multijugador: No probado
- Cierre: Correcto
- Segundo arranque: Correcto

## 8. Ajustes aplicados

Ninguno. El juego funcionó de forma nativa en el entorno probado.

## 9. Limitaciones

- No se probó multijugador.
- No se probó joystick/gamepad.
- No se realizó una validación específica de cambio de nivel/escena.
- No se extrapola el resultado a otras ediciones, Windows 11, otros controladores o hardware.

## 10. Estado final

**Funcional** en Windows 10 Pro 22H2 build 19045 en el equipo probado, sin parches, wrappers, modo compatibilidad ni elevación administrativa.
