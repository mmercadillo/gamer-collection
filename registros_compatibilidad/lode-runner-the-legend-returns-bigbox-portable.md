# Registro de compatibilidad de la instalación portable de Lode Runner

## 1. Identificación

- **Pieza** — Lode Runner: The Legend Returns, edición española Big Box en CD-ROM, variante para Windows 3.x.
- **Ficha** — [PC Game Archive](https://www.pcgamearchive.org/juegos/lode-runner-the-legend-returns-bigbox/).
- **Preservación relacionada** — `registros_preservacion/lode-runner-the-legend-returns-bigbox.md`.
- **Fecha de la sesión y última validación** — 15/11/2026, por el responsable del laboratorio de PC Game Archive.

## 2. Punto de partida

Imagen de trabajo BIN/CUE de la edición preservada, con 33 pistas (1 de datos y 32 CD-DA). La sesión portable reutilizó la imagen de trabajo y la letra `D:` dentro del entorno emulado. Las huellas siguientes identifican la adquisición de referencia. La sesión portable no incluye un cálculo nuevo de huellas.

| Archivo | SHA-256 de referencia |
| --- | --- |
| LODE_RUNNER_CD.BIN | `458d988aad773a130c38b312d2be51278a66c49c484278de71bbf45dd94a0c62` |
| LODE_RUNNER_CD.CUE | `3252e3a21509d8e02c31e7bd4e1b82d4f1f05a02517169cd65604d6557d3fba0` |

## 3. Entorno anfitrión

PCGA-LAB-01, Windows 10 Pro 22H2 x64 (19045.6466), AMD Ryzen 5 PRO 4650U, AMD Radeon Graphics y 16 GB de RAM, según ficha del laboratorio. La captura de escritorio muestra 1920 × 1080. Visualización final a pantalla completa en DOSBox, con resolución emulada S3 de 640 × 480 y 256 colores. La sesión verificó interacción con teclado y ratón y salida audible. Ruta física de salida de audio sin registrar.

## 4. Herramientas y componentes

- DOSBox Staging **0.83.0** Portable ZIP para Windows x64. [Descarga oficial](https://www.dosbox-staging.org/releases/windows/).
- Windows 3.1 en español, siete imágenes de disquete. Instalador DOS `INSTALAR.EXE`. Audio CD [MCI] desde el cuarto disquete.
- S3 Vision 964 **v1.41B5** (`s3-964-141B5.ZIP`) y Creative Sound Blaster 16 para Windows 3.1 (`SB16W3X.ZIP`). [Referencia de la que se obtuvieron los controladores](https://www.dosbox-staging.org/0.83/manual/using-dosbox-staging/windows-31/).

## 5. Instalación base

Se instaló Windows 3.1 en `C:\WINDOWS` desde las imágenes de disquete. La unidad invitada `C:` correspondía a `drives\c`. Se verificó el inicio de Windows y se reutilizó la base en el paquete de Lode Runner. El instalador del juego se ejecutó desde Windows 3.1 como `D:\INSTALL.EXE`; creó el grupo Sierra con el icono Lode Runner CD. El primer intento de ejecución presentó un aviso de CD/MCI.

## 6. Ajustes de compatibilidad

| Intervención | Aplicación y resultado |
| --- | --- |
| Audio CD [MCI] | Se añadió desde Controladores con el CD en `D:` y el disquete 4 en `A:`. Windows detectó el CD-ROM y el juego avanzó al modo gráfico. |
| Vídeo S3 | Se cargó el controlador desde `C:\DRIVERS\S3` con `OEMSETUP.INF`. Se utilizó 640 × 480 a 256 colores. |
| Creative SB16 | El instalador DOS se ejecutó desde `C:\DRIVERS\SB16W3X` con destino de Windows explícito `C:\WINDOWS`. `SET BLASTER` devolvió `A220 I7 D1 H5 T6`. Se configuró IRQ 7. La copia de `SB16SND.DRV` en Windows y la reproducción de `TADA.WAV` confirmaron la instalación y el funcionamiento del audio digital. |
| Arranque portable | `dosbox-staging.conf` junto al ejecutable, montaje relativo del CUE, inicio automático de Windows y acceso del juego copiado al grupo Inicio. El BAT de la raíz establece el directorio de trabajo de DOSBox. |
| Pantalla completa | `fullscreen = on`, `aspect = stretch`, `viewport = fit`, `integer_scaling = off`. El escalado se aplica a la salida del emulador. |

## 7. Procedimiento final reproducible

La guía pública del paquete detalla las rutas y comandos. La secuencia es instalar Windows 3.1, copiar la base, montar el CUE, instalar el juego, incorporar MCI y los controladores S3 y Creative, verificar WAV y audio del juego, configurar el arranque y probar el BAT desde una segunda ubicación.

## 8. Matriz de validación funcional

| Subsistema | Estado | Observaciones |
| --- | --- | --- |
| Instalación y arranque | Correcto | Instalador de Windows y acceso del grupo Sierra. Arranque automático desde BAT confirmado. |
| Menús, teclado, ratón e inicio de partida | Correcto | Interacción observada durante la instalación y la prueba de juego. |
| Gráficos 2D y juego representativo | Correcto | Modo S3 de 256 colores y prueba en partida. |
| Sonido digital y música | Correcto | Prueba de WAV, efectos en juego y música CD-DA confirmados. |
| Guardado, cierre, reapertura y carga | Correcto | Reportado tras la prueba de la copia portable. |
| Vídeos, joystick, cambio de nivel, multijugador y editor | No probado | Fuera del alcance de la prueba. |
| Gráficos 3D | No aplicable | La prueba se refiere a la presentación de este juego 2D. |

## 9. Limitaciones conocidas

La verificación se hizo en Windows 10 x64 en el equipo de laboratorio. Llenar un monitor panorámico con `aspect = stretch` modifica las proporciones. Con relación conservada, quedan bandas laterales en 16:9.

## 10. Elementos no probados

Otros ordenadores, anfitriones, versiones del emulador y ediciones del juego. Se repitió la ejecución desde una copia en otra ubicación. No consta una segunda reconstrucción íntegra a partir de medios limpios.

## 11. Problemas descartados e intentos fallidos

- La ISO de Windows 3.1 no se montó con el comando utilizado. Se continuó con los siete disquetes.
- `SETUP` no se reconocía en el primer disquete español. El ejecutable presente era `INSTALAR.EXE`.
- El juego llegó a avisar de 16 colores y, en una etapa posterior, de efectos desactivados. Se resolvieron mediante S3 y la instalación del controlador Creative en el directorio de Windows.
- Con el destino de Windows en `None`, los archivos estaban en `C:\SB16\WINDRV` y el controlador no figuraba en `C:\WINDOWS\SYSTEM`. El asistente proponía IRQ 5 y el emulador estaba en IRQ 7.
- Se descartó el instalador de terceros que el anfitrión marcó como sospechoso. La prueba final usó el instalador del CD.

## 12. Fuentes externas

Manual de DOSBox Staging 0.83 sobre [Windows 3.1 y sus controladores](https://www.dosbox-staging.org/0.83/manual/using-dosbox-staging/windows-31/), [montaje](https://www.dosbox-staging.org/0.83/manual/using-dosbox-staging/storage/), [configuración](https://www.dosbox-staging.org/0.83/manual/using-dosbox-staging/configuration/) y [escalado](https://www.dosbox-staging.org/0.83/manual/graphics/rendering/aspect-ratios-and-scaling/). [KB de Microsoft sobre el grupo Inicio](https://ftp.zx.net.nz/pub/archive/ftp.microsoft.com/MISC/KB/en-us/81/606.HTM).

## 13. Evidencias internas

Capturas de la sesión, transcripción de `SET BLASTER`, comprobación de archivos Creative y confirmación del responsable de la reproducción de WAV, el audio en el juego y la repetición desde otra ruta. Las capturas seleccionadas para la guía muestran solo el entorno emulado y sus rutas invitadas.

## 14. Repetición final

El responsable confirmó la ejecución desde la copia, el sonido y la recuperación de una partida. La comprobación se refiere al traslado del paquete montado, no a una reinstalación independiente.

## 15. Estado final

**Funcional con ajustes** en el entorno indicado. Última prueba completa de ejecución portable el 15/11/2026.

## 16. Criterio de cierre

Edición, entorno, componentes, procedimiento y resultados documentados. Validación funcional y traslado confirmados. Una reinstalación desde cero por un segundo operador queda sin verificar.
