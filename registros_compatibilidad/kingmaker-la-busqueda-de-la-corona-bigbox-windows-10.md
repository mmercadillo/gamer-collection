# PC Game Archive — Registro interno de compatibilidad de Kingmaker (#000249)

- **Edición:** Kingmaker: La Búsqueda de la Corona — española Big Box, 2 disquetes HD de 3,5 pulgadas.
- **Fecha de pruebas:** 12/11/2026.
- **Entorno:** PCGA-LAB-01, Windows 10 Pro 22H2 x64.
- **Emulador:** DOSBox Staging 0.83.0 (7b400), portable.
- **Origen:** imágenes IMA de trabajo, derivadas de adquisiciones convencionales independientes coincidentes; másteres separados.
- **Guía relacionada:** `documentacion/fuentes/guia-kingmaker-la-busqueda-de-la-corona-bigbox-windows-10.md`.

## Imágenes de trabajo

- Disco 1: `KINGMAKER_DISCO_1.IMA`; 1.474.560 bytes; SHA-256 `AC37AF63F1EEADF41749DF1CEB989EED902987D8E46D114380B446FC15BF8291`.
- Disco 2: `KINGMAKER_DISCO_2.IMA`; 1.474.560 bytes; SHA-256 `4272574B157D2AEC9A418FEEFC59D32B3A58BCFB4E8B4AD6AF21DC3EBB56D303`.

## Instalación y ejecución observadas

1. Ejecutar `INSTALL.EXE` directamente en Windows 10 x64: error «no es una aplicación válida para esta plataforma».
2. DOSBox Staging: montar carpeta de instalación como `C:` y ambos IMA como unidad `A:` mediante `MOUNT`.
3. Instalar en `C:\KING` con idioma Spanish, voces Enabled y Sound Blaster, puerto 220, IRQ 7, DMA 1.
4. Al solicitar el segundo disco, fue suficiente pulsar Enter con ambas imágenes montadas en la misma unidad; no se precisó Ctrl+F4 en la sesión.
5. Ejecutar `KING.EXE`: pantalla inicial, interfaz en español, inicio de partida, gráficos, sonido y música correctos.
6. Guardado y carga confirmados; reproducción de la partida guardada tras copiar el paquete portable a otra carpeta.
7. Arranque portable con `Kingmaker.bat` usando `%~dp0`, DOSBox Staging portable y `kingmaker.conf`; pantalla completa verificada.

## Incidencias relevantes

- Montaje inicial de imagen: `Can't create drive from file`; se resolvió tras cerrar WinImage y reintentar, sin causalidad demostrada.
- Primera instalación interrumpida al pedir disco 2, al haberse montado inicialmente solo el disco 1.
- Primer lanzador basado en comandos `-c` no llegó a ejecutar el juego; se sustituyó por ejecución directa de `KING.EXE` desde DOSBox.

## Limitaciones

No se probó campaña completa, Windows 11 ni otros equipos. No se verificaron de manera exhaustiva modos alternativos de sonido, gamepad, multijugador o cinemáticas.

**Estado:** Funcional con emulación en el entorno probado, incluyendo versión portable con guardado/carga y pantalla completa.
