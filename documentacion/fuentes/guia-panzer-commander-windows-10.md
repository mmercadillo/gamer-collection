Esta guía explica cómo instalar y ejecutar **Panzer Commander: WWII Tank Simulator** en Windows 10 de 64 bits utilizando la edición española Big Box conservada por PC Game Archive, ficha **#000214**.

El procedimiento que aparece a continuación es la secuencia final validada. No es necesario aplicar otros parches ni reproducir pruebas intermedias: para esta edición, la combinación comprobada es **otvdm 0.9.0 para ejecutar el instalador de 16 bits** y **DDrawCompat 0.7.2 con el juego limitado a 30 FPS**.

> Esta validación corresponde a la edición española original de 1998 probada por PC Game Archive. Otras ediciones, revisiones del ejecutable, sistemas operativos, GPU o controladores pueden comportarse de forma diferente.

## Resultado esperado

Siguiendo esta guía, en el entorno probado se obtuvo el siguiente resultado:

- vídeo de introducción: correcto;
- menú principal: correcto;
- entrada en el escenario 3D: correcta;
- conducción del tanque: correcta;
- disparo: correcto;
- cambio entre distintas vistas: correcto;
- uso de distintas opciones durante una sesión representativa: correcto;
- bloqueo que impedía mantener la ejecución 3D: no reproducido con el limitador configurado a 30 FPS.

El estado de compatibilidad de esta edición se considera **Correcto con limitaciones**, porque Windows 10 x64 necesita una capa para ejecutar el instalador Win16 y un wrapper de DirectDraw configurado específicamente para mantener estable la ejecución 3D.

## Entorno en el que se ha validado

La prueba final se realizó en el entorno de referencia [PCGA-LAB-01](../../laboratorio/pcga-lab-01/), con estas características principales:

- Windows 10 Pro 22H2 de 64 bits;
- build 19045.6466;
- AMD Ryzen 5 PRO 4650U, 6 núcleos y 12 hilos;
- 16 GB de RAM;
- AMD Radeon Graphics;
- controlador gráfico 31.0.21921.11005;
- resolución 1920 × 1080;
- escalado de Windows al 150 %.

La copia de trabajo utilizada por PC Game Archive fue una imagen BIN/CUE verificada y montada con **WinCDEmu 4.1**. Si se utiliza el CD-ROM físico original, el paso de montaje de imagen no es necesario.

## Qué necesitas

### El juego

Esta guía está validada sobre **Panzer Commander: WWII Tank Simulator**, edición española Big Box, lanzamiento original de 1998 para Windows 95.

Ficha documental de la pieza: [Panzer Commander: WWII Tank Simulator — PC Game Archive](/juegos/panzer-commander-wwii-tank-simulator-bigbox/).

La copia conservada por PC Game Archive corresponde a un único CD-ROM con etiqueta de volumen `Pzc_v1_0`.

Hashes SHA-256 de referencia de la copia de preservación utilizada en la prueba:

```text
BIN  E4E57AD97857B91AAC38121B19BA0DF22B54547AC4BBD8F99C348BFFD4FFC688
CUE  9A24EDC5DC96A0BD6D69EE9D00953425A71BB64807CFD4898AB76F174118462E
```

Estos hashes sirven para identificar exactamente la copia probada por PC Game Archive. Una edición diferente puede tener hashes distintos y requerir una validación independiente.

### otvdm 0.9.0

El instalador `SETUP.EXE` incluido en esta edición es un ejecutable **Win16**. Windows 10 de 64 bits no puede ejecutarlo directamente, por lo que se utiliza **otvdm 0.9.0**, perteneciente al proyecto winevdm.

Descarga oficial: [winevdm / otvdm v0.9.0 en GitHub](https://github.com/otya128/winevdm/releases/tag/v0.9.0).

En la prueba de PC Game Archive se utilizó `otvdm.exe` de forma portable, sin instalar winevdm globalmente en Windows.

Referencia del ejecutable probado:

```text
otvdm.exe
Versión utilizada: 0.9.0
SHA-256: DCD73D3EACE703B237AAF33D52BB3BE8075B0DF7E6393712CF30319C75B3DC38
```

### DDrawCompat 0.7.2

Para la ejecución del juego se utiliza **DDrawCompat 0.7.2**.

Descarga oficial: [DDrawCompat v0.7.2 en GitHub](https://github.com/narzoul/DDrawCompat/releases/tag/v0.7.2).

Referencia exacta de la DLL validada:

```text
ddraw.dll
FileVersion: v0.7.2
ProductVersion: v0.7.2
Tamaño: 3653632 bytes
SHA-256: 94895CF6EDE8FD0F74EE1447FDC08B7044A9C65A1A25A49A4DF893A0370975A3
```

### WinCDEmu 4.1, solo si se usa una imagen BIN/CUE

PC Game Archive realizó la prueba desde una copia de trabajo BIN/CUE montada con **WinCDEmu 4.1**.

Si se dispone del CD-ROM físico original y se utiliza directamente, este componente no es necesario.

## 1. Preparar el CD o la imagen de trabajo

### Si utilizas el CD-ROM físico

1. Inserta el CD-ROM original de Panzer Commander en la unidad óptica.
2. Espera a que Windows reconozca el disco.
3. No necesitas utilizar el inicio automático del CD.
4. Identifica la letra que Windows ha asignado a la unidad, por ejemplo `E:`.

### Si utilizas una imagen BIN/CUE creada legalmente desde tu propio soporte

1. Mantén los ficheros BIN y CUE juntos en la misma carpeta.
2. Instala WinCDEmu 4.1 si todavía no está instalado.
3. Monta el fichero `.cue`, no el `.bin` directamente.
4. Comprueba que Windows expone una nueva unidad de CD-ROM.
5. En la copia validada por PC Game Archive, el volumen aparece como `Pzc_v1_0` y utiliza el sistema de archivos CDFS.

Puedes comprobarlo desde PowerShell con:

```powershell
Get-Volume
```

En los ejemplos de esta guía se utilizará `E:` como letra de la unidad. Si Windows asigna otra letra, sustitúyela en los comandos siguientes.

## 2. Descargar y preparar otvdm

1. Abre la [página oficial de la versión 0.9.0 de winevdm](https://github.com/otya128/winevdm/releases/tag/v0.9.0).
2. Descarga `otvdm-v0.9.0.zip`.
3. Extrae el contenido completo del ZIP en una carpeta estable de tu equipo.
4. Por ejemplo, puedes utilizar:

```text
C:\Tools\otvdm-v0.9.0\
```

5. Comprueba que dentro de esa carpeta existe `otvdm.exe`.

Si quieres verificar que utilizas exactamente el mismo ejecutable que PC Game Archive, abre PowerShell en la carpeta de otvdm y ejecuta:

```powershell
Get-FileHash ".\otvdm.exe" -Algorithm SHA256
```

Para la copia utilizada en esta validación debe aparecer:

```text
DCD73D3EACE703B237AAF33D52BB3BE8075B0DF7E6393712CF30319C75B3DC38
```

## 3. Instalar Panzer Commander

No ejecutes `SETUP.EXE` directamente desde el Explorador de Windows. El instalador de esta edición es Win16 y Windows 10 x64 no puede iniciarlo de forma nativa.

Abre PowerShell y ejecuta el instalador a través de otvdm. Si otvdm está en `C:\Tools\otvdm-v0.9.0` y el CD está montado como `E:`, utiliza:

```powershell
& "C:\Tools\otvdm-v0.9.0\otvdm.exe" "E:\SETUP.EXE"
```

El asistente de instalación de Panzer Commander debe abrirse normalmente.

Durante la instalación:

1. Sigue el asistente de forma normal.
2. Para reproducir exactamente el entorno validado, instala el juego en:

```text
C:\Panzer Commander
```

3. Completa la copia de archivos del juego.
4. Si el instalador ofrece instalar **DirectX 5**, selecciona **No**.
5. Finaliza el asistente.

En la configuración validada por PC Game Archive no fue necesario instalar DirectX 5 desde el CD.

El ejecutable instalado y utilizado durante la validación tiene esta referencia:

```text
C:\Panzer Commander\Panzer.exe
Tamaño: 1271808 bytes
SHA-256: 51009483F17B07F51B6CE950A8B27A87D76D81AE4E2A61952B881B70415756AF
```

Puedes comprobarlo con:

```powershell
Get-FileHash "C:\Panzer Commander\Panzer.exe" -Algorithm SHA256
```

Si el hash no coincide, no significa necesariamente que el fichero sea incorrecto: puede tratarse de otra revisión o edición. Sí significa que no es exactamente el ejecutable sobre el que PC Game Archive validó esta guía.

## 4. Comprobar que Windows no fuerza un modo de compatibilidad

La configuración validada no necesita activar el modo Windows 95, Windows 98, Windows XP ni ninguna otra capa manual de compatibilidad de Windows.

Antes de continuar:

1. Haz clic con el botón derecho sobre `C:\Panzer Commander\Panzer.exe`.
2. Abre **Propiedades**.
3. Entra en la pestaña **Compatibilidad**.
4. Asegúrate de que **Ejecutar este programa en modo de compatibilidad para** está desmarcado.
5. No actives manualmente opciones de color reducido, resolución 640 × 480, DPI o ejecución como administrador salvo que estés diagnosticando un entorno diferente al validado aquí.

La solución descrita en esta guía parte de un `Panzer.exe` sin capas manuales de compatibilidad de Windows.

## 5. Instalar DDrawCompat 0.7.2 junto al juego

1. Abre la [página oficial de DDrawCompat v0.7.2](https://github.com/narzoul/DDrawCompat/releases/tag/v0.7.2).
2. Descarga `DDrawCompat-v0.7.2.zip`.
3. Extrae el ZIP en una carpeta temporal.
4. Localiza `ddraw.dll`.
5. Copia únicamente esa DLL a la carpeta donde está `Panzer.exe`:

```text
C:\Panzer Commander\ddraw.dll
```

La carpeta debe contener, entre otros ficheros:

```text
C:\Panzer Commander\Panzer.exe
C:\Panzer Commander\ddraw.dll
```

Puedes verificar la DLL con PowerShell:

```powershell
Get-FileHash "C:\Panzer Commander\ddraw.dll" -Algorithm SHA256
```

La versión utilizada por PC Game Archive devuelve:

```text
94895CF6EDE8FD0F74EE1447FDC08B7044A9C65A1A25A49A4DF893A0370975A3
```

## 6. Crear la configuración necesaria de DDrawCompat

En la misma carpeta del juego crea un fichero llamado exactamente:

```text
DDrawCompat.ini
```

Su contenido debe ser únicamente:

```ini
FpsLimiter = flipend(30)
```

El resultado final debe quedar así:

```text
C:\Panzer Commander\Panzer.exe
C:\Panzer Commander\ddraw.dll
C:\Panzer Commander\DDrawCompat.ini
```

También puedes crear el fichero desde PowerShell con:

```powershell
Set-Content `
  "C:\Panzer Commander\DDrawCompat.ini" `
  "FpsLimiter = flipend(30)" `
  -Encoding ASCII
```

Y comprobar su contenido con:

```powershell
Get-Content "C:\Panzer Commander\DDrawCompat.ini"
```

Debe devolver exactamente:

```text
FpsLimiter = flipend(30)
```

Esta es la configuración específica necesaria para la estabilidad 3D observada durante la validación. No hace falta añadir otras opciones al fichero para reproducir el resultado de PC Game Archive.

## 7. Mantener el CD disponible

Mantén el CD-ROM original introducido o la imagen BIN/CUE montada mientras juegas.

El procedimiento validado se realizó con el volumen del juego disponible durante toda la ejecución. Esto evita problemas con recursos que el juego pueda consultar directamente desde el CD.

## 8. Ejecutar el juego

Puedes iniciar el juego desde su acceso directo o directamente desde `Panzer.exe`.

Desde PowerShell:

```powershell
Set-Location "C:\Panzer Commander"
.\Panzer.exe
```

Con la configuración validada, el vídeo inicial debe reproducirse correctamente y el juego debe permitir acceder al menú y entrar en la parte 3D.

Durante la prueba final de PC Game Archive se verificó de forma práctica que era posible:

- entrar en un escenario 3D;
- conducir el tanque;
- disparar;
- cambiar de vista;
- utilizar distintas opciones del juego;
- continuar jugando sin reproducir el bloqueo observado cuando el limitador de 30 FPS no está activo.

## 9. Confirmar que DDrawCompat ha cargado la configuración

Al ejecutar `Panzer.exe`, DDrawCompat genera un fichero de log en la carpeta del juego:

```text
C:\Panzer Commander\DDrawCompat-Panzer.log
```

Su existencia es una comprobación útil de que la DLL está siendo cargada.

Puedes revisar las opciones relevantes con:

```powershell
Select-String `
    "C:\Panzer Commander\DDrawCompat-Panzer.log" `
    -Pattern "__COMPAT_LAYER|FpsLimiter|CpuAffinity|PalettizedTextures|AlternatePixelCenter"
```

En la configuración validada por PC Game Archive se obtuvo:

```text
Environment variable __COMPAT_LAYER = ""
AlternatePixelCenter = off
CpuAffinity = 1
FpsLimiter = flipend(30)
PalettizedTextures = off
```

`CpuAffinity = 1`, `PalettizedTextures = off` y `AlternatePixelCenter = off` son valores que DDrawCompat 0.7.2 aplica o conserva por defecto en esta prueba. **No es necesario añadirlos manualmente al fichero `DDrawCompat.ini`.**

La línea importante que debe aparecer como configuración cargada desde el directorio del juego es:

```text
FpsLimiter = flipend(30)
```

## 10. Si el instalador no arranca

Si al ejecutar `SETUP.EXE` directamente Windows muestra un mensaje equivalente a que el ejecutable no es una aplicación válida para esta plataforma, no intentes corregirlo con el modo de compatibilidad de Windows.

Utiliza el instalador mediante otvdm:

```powershell
& "C:\Tools\otvdm-v0.9.0\otvdm.exe" "E:\SETUP.EXE"
```

Recuerda sustituir `E:` por la letra real de tu CD o unidad virtual.

## 11. Si el juego entra en 3D pero termina bloqueándose

Comprueba estos puntos en este orden:

1. `ddraw.dll` debe estar en la misma carpeta que `Panzer.exe`.
2. La DLL debe ser la versión 0.7.2 utilizada en esta guía si quieres reproducir exactamente la configuración validada.
3. `DDrawCompat.ini` debe estar también en la misma carpeta que `Panzer.exe`.
4. El nombre debe ser exactamente `DDrawCompat.ini`, evitando extensiones ocultas como `DDrawCompat.ini.txt`.
5. El contenido debe incluir exactamente `FpsLimiter = flipend(30)`.
6. Ejecuta el juego una vez y comprueba que se crea `DDrawCompat-Panzer.log`.
7. Busca en el log la línea de `FpsLimiter` y confirma que muestra `flipend(30)`.
8. Comprueba en las propiedades de `Panzer.exe` que Windows no tenga activado manualmente un modo de compatibilidad.
9. Mantén el CD o la imagen montada durante la partida.

Si `DDrawCompat-Panzer.log` no aparece, DDrawCompat no está siendo cargado y debe revisarse la ubicación o el nombre de `ddraw.dll`.

## 12. Configuración final de referencia

Para esta edición, la configuración mínima validada es:

```text
Windows 10 Pro 22H2 x64
Panzer Commander: WWII Tank Simulator — edición española Big Box
Instalador ejecutado con otvdm 0.9.0
DirectX 5 del CD: no instalado
DDrawCompat 0.7.2 junto a Panzer.exe
DDrawCompat.ini: FpsLimiter = flipend(30)
Modo de compatibilidad de Windows: no utilizado
CD o imagen de trabajo disponible durante la ejecución
```

No es necesario modificar `Panzer.exe`, aplicar un parche binario ni añadir más opciones de DDrawCompat para reproducir el resultado obtenido en esta prueba.

## Limitaciones de la validación

Esta guía documenta lo que PC Game Archive ha probado directamente sobre la edición indicada.

- Windows 11: no probado en esta validación.
- Otras ediciones o revisiones de Panzer Commander: no probadas.
- Otros ejecutables con hash diferente: no validados por esta guía.
- Gamepad o joystick: no validado expresamente durante la prueba final.
- Multijugador: no probado.
- Campaña completa y todas las misiones: no probadas de principio a fin.

## Referencias técnicas

- [winevdm / otvdm v0.9.0 — versión utilizada para ejecutar el instalador Win16](https://github.com/otya128/winevdm/releases/tag/v0.9.0)
- [DDrawCompat v0.7.2 — versión utilizada durante la validación](https://github.com/narzoul/DDrawCompat/releases/tag/v0.7.2)
- [Configuración de DDrawCompat — FpsLimiter](https://github.com/narzoul/DDrawCompat/wiki/Configuration)
- [DDrawCompat issue #200 — Panzer Commander](https://github.com/narzoul/DDrawCompat/issues/200)

**Última prueba completa:** 18/10/2026.
