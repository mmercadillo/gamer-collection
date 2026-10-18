# Registro de compatibilidad — Panzer Commander: WWII Tank Simulator / Windows 10

**Estado:** Correcto con limitaciones  
**Ficha PCGA:** #000214  
**URL:** `juegos/panzer-commander-wwii-tank-simulator-bigbox/`  
**Fecha de última prueba:** 18/10/2026  
**Responsable:** PC Game Archive

## 1. Identificación

- Título: Panzer Commander: WWII Tank Simulator
- Edición: española Big Box, lanzamiento original
- Mercado / idioma: España / Español
- Soporte: 1 CD-ROM
- Registro de preservación: `registros_preservacion/panzer-commander-wwii-tank-simulator-bigbox.md`

## 2. Punto de partida

Copia de trabajo derivada del máster BIN/CUE verificado.

| Fichero | SHA-256 |
|---|---|
| `Pzc_v1_0.bin` | `E4E57AD97857B91AAC38121B19BA0DF22B54547AC4BBD8F99C348BFFD4FFC688` |
| `Pzc_v1_0.cue` | `9A24EDC5DC96A0BD6D69EE9D00953425A71BB64807CFD4898AB76F174118462E` |

Los hashes de la copia de trabajo coincidieron con el máster antes de iniciar las pruebas.

## 3. Entorno anfitrión

- Entorno: PCGA-LAB-01
- Sistema operativo: Windows 10 Pro 22H2 x64
- Build: 19045.6466
- CPU: AMD Ryzen 5 PRO 4650U, 6 núcleos / 12 hilos
- RAM: 16 GB
- GPU: AMD Radeon Graphics
- Driver GPU: 31.0.21921.11005
- Resolución: 1920 × 1080
- Escalado: 150 %

## 4. Herramientas

- WinCDEmu 4.1: montaje de BIN/CUE.
- otvdm 0.9.0: ejecución del instalador Win16.
- DDrawCompat 0.7.2: compatibilidad de DirectDraw/Direct3D.

Referencias verificadas:

```text
otvdm.exe
SHA-256 DCD73D3EACE703B237AAF33D52BB3BE8075B0DF7E6393712CF30319C75B3DC38

ddraw.dll
Tamaño 3653632 bytes
FileVersion v0.7.2
ProductVersion v0.7.2
SHA-256 94895CF6EDE8FD0F74EE1447FDC08B7044A9C65A1A25A49A4DF893A0370975A3
```

## 5. Instalación

1. Se montó `Pzc_v1_0.cue` con WinCDEmu 4.1.
2. Windows expuso el volumen `Pzc_v1_0`, CDFS, 615.131.136 bytes.
3. `SETUP.EXE` se identificó como ejecutable NE/Win16 y no es ejecutable de forma nativa en Windows 10 x64.
4. Se ejecutó el instalador mediante otvdm 0.9.0.
5. El juego se instaló en `C:\Panzer Commander`.
6. El instalador ofreció DirectX 5; se seleccionó **No**.
7. La instalación finalizó correctamente.

Referencia del ejecutable instalado:

```text
Panzer.exe
Tamaño: 1271808 bytes
SHA-256: 51009483F17B07F51B6CE950A8B27A87D76D81AE4E2A61952B881B70415756AF
```

## 6. Configuración final de ejecución

Se copió `ddraw.dll` de DDrawCompat 0.7.2 junto a `Panzer.exe` y se creó `DDrawCompat.ini` con una única opción explícita:

```ini
FpsLimiter = flipend(30)
```

No se activó modo manual de compatibilidad de Windows.

El log final confirmó:

```text
__COMPAT_LAYER = ""
AlternatePixelCenter = off
CpuAffinity = 1
FpsLimiter = flipend(30)
PalettizedTextures = off
```

`CpuAffinity = 1`, `PalettizedTextures = off` y `AlternatePixelCenter = off` son valores por defecto de DDrawCompat 0.7.2 en esta prueba; no se añadieron manualmente al INI.

## 7. Matriz funcional final

| Subsistema | Estado | Observaciones |
|---|---|---|
| Instalación | Correcto con ajuste | `SETUP.EXE` Win16 ejecutado mediante otvdm 0.9.0 |
| DirectX 5 del CD | No necesario | No instalado |
| Vídeo de introducción | Correcto | Reproducción completa con DDrawCompat |
| Menú principal | Correcto | Navegación verificada |
| Entrada al escenario 3D | Correcto | Verificada |
| Conducción | Correcto | Verificada durante sesión representativa |
| Disparo | Correcto | Verificado |
| Cambios de vista | Correcto | Verificados |
| Opciones del juego | Correcto | Varias opciones utilizadas durante la prueba |
| Estabilidad 3D | Correcto con ajuste | Sin bloqueo observado con `FpsLimiter = flipend(30)` |
| Gamepad/joystick | No probado | — |
| Multijugador | No probado | — |
| Campaña completa | No probado | No se completó íntegramente |

## 8. Procedimiento final reproducible

1. Partir del CD original o de una copia de trabajo legal y verificada.
2. Montar el CUE si se utiliza BIN/CUE.
3. Ejecutar `SETUP.EXE` mediante otvdm 0.9.0.
4. No instalar DirectX 5 desde el CD.
5. Copiar `ddraw.dll` de DDrawCompat 0.7.2 junto a `Panzer.exe`.
6. Crear `DDrawCompat.ini` con `FpsLimiter = flipend(30)`.
7. Mantener el CD o la imagen montada durante la ejecución.
8. Ejecutar `Panzer.exe` sin modo manual de compatibilidad de Windows.

## 9. Limitaciones

- Validación realizada sobre esta edición española Big Box y este ejecutable concreto.
- Windows 11: no probado.
- Otras ediciones o revisiones: no probadas.
- Gamepad/joystick: no validado expresamente.
- Multijugador: no probado.
- Campaña completa y todas las misiones: no probadas de principio a fin.

## 10. Estado final

**Correcto con limitaciones.** La edición es instalable y jugable en Windows 10 Pro 22H2 x64 mediante otvdm 0.9.0 para el instalador Win16 y DDrawCompat 0.7.2 con limitación a 30 FPS para la ejecución 3D.
