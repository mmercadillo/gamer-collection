Un doble clic en **StartLodeRunner.bat** monta el CD, arranca Windows 3.1 a pantalla completa y abre el juego. Esta guía reproduce la instalación que probamos con la **edición española Big Box en CD-ROM**, con vídeo a **640 × 480 y 256 colores**, música desde las pistas del disco y efectos de sonido mediante una Sound Blaster 16 emulada.

La prueba se realizó el **15 de noviembre de 2026** en **Windows 10 Pro 22H2 x64, compilación 19045.6466**, con **DOSBox Staging 0.83.0** y **Windows 3.1 en español**.

[Ficha de la edición](https://www.pcgamearchive.org/juegos/lode-runner-the-legend-returns-bigbox/) · [Preservación del CD](https://www.pcgamearchive.org/documentacion/preservacion/lode-runner-the-legend-returns-bigbox/) · [Guía de ejecución con DAEMON Tools y otvdm](https://www.pcgamearchive.org/documentacion/guias/lode-runner-the-legend-returns-bigbox-windows-10/)

## 1. Prepara el emulador y los medios de instalación

Necesitarás:

- El **ZIP portable para Windows x64 de DOSBox Staging 0.83.0**. Descomprime el paquete completo, incluidos sus recursos. [Descargas de DOSBox Staging para Windows](https://www.dosbox-staging.org/releases/windows/)
- Los **siete disquetes de instalación de Windows 3.1 en español**. En esta guía se llaman `disk01.img` a `disk07.img`.
- Una **copia de trabajo BIN/CUE de tu CD de Lode Runner**. La imagen de la edición probada tiene una pista de datos y 32 pistas de audio. Mantén juntos `LODE_RUNNER_CD.CUE` y `LODE_RUNNER_CD.BIN` y conserva el nombre del BIN referenciado por el CUE.
- Los paquetes **S3 Vision 964 v1.41B5** (`s3-964-141B5.ZIP`) y **Creative Sound Blaster 16 para Windows 3.1** (`SB16W3X.ZIP`), enlazados en los apartados de vídeo y audio del manual. [Windows 3.1 en el manual de DOSBox Staging](https://www.dosbox-staging.org/0.83/manual/using-dosbox-staging/windows-31/)

## 2. Instala una base reutilizable de Windows 3.1

### Prepara la unidad C:

Usa una copia independiente de DOSBox Staging como base de trabajo. Junto a `dosbox.exe`, crea la carpeta `drives\c`. Se verá como **`C:` dentro de DOSBox** cuando lo arranques con esa carpeta como directorio de trabajo.
### Monta los disquetes

Coloca temporalmente los siete disquetes en una carpeta llamada `win31-disks` junto a `dosbox.exe`. Abre DOSBox desde ahí y ejecuta estas líneas en su consola. Si ya tienes las imágenes en otra carpeta, adapta las rutas de la primera línea.

```dos
MOUNT A "win31-disks\disk01.img" "win31-disks\disk02.img" "win31-disks\disk03.img" "win31-disks\disk04.img" "win31-disks\disk05.img" "win31-disks\disk06.img" "win31-disks\disk07.img" -t floppy
A:\INSTALAR.EXE
```

### Completa la instalación

Instala Windows en **`C:\WINDOWS`**. Cuando el asistente pida el siguiente disquete, pulsa **Ctrl + F4** para avanzar a la siguiente imagen montada y confirma en el instalador.
### Comprueba el arranque

Al terminar, elige **Regresar a MS-DOS**. Puedes cerrar y volver a abrir DOSBox desde la misma carpeta para retirar los disquetes de la sesión. Comprueba que se abre el **Administrador de programas** con estos comandos.

```dos
C:
CD \WINDOWS
WIN
```

![Pantalla final del instalador de Windows 3.1 con la opción Regresar a MS-DOS](./img/01-windows-31-instalado.png)

Guarda una copia de esta base cuando DOSBox esté cerrado. Para el juego, copia **toda la carpeta del emulador**, incluida `drives\c`, dentro de `lode-runner-portable` con el nombre `dosbox-staging-v0.83.0`. Crea `img` al mismo nivel que esa carpeta y coloca allí el BIN y el CUE. Los disquetes pueden quedarse con el material de instalación. Volverás a usar el cuarto al instalar el controlador de audio CD.

[Montaje de unidades e intercambio de disquetes en el manual de DOSBox Staging](https://www.dosbox-staging.org/0.83/manual/using-dosbox-staging/storage/)

## 3. Monta el CD e instala el juego en Windows 3.1

Abre el `dosbox.exe` de la copia del juego desde su propia carpeta. En la consola de DOSBox, monta el **CUE** y verifica que el instalador aparece en **`D:`**.

```dos
MOUNT D "..\img\LODE_RUNNER_CD.CUE"
DIR D:\INSTALL.EXE
C:
CD \WINDOWS
WIN
```

En el **Administrador de programas**, abre **Archivo → Ejecutar**, escribe `D:\INSTALL.EXE` y acepta. Puedes usar `C:\LODERUNN` como carpeta de destino. Mantén **`D:\`** como unidad del CD cuando el asistente la solicite. Selecciona **Full** y deja **Install Joystick Drivers** desmarcado para jugar con teclado. Al acabar verás **Lode Runner CD** en el grupo **Sierra**.

![Grupo Sierra en Windows 3.1 con el acceso Lode Runner CD](./img/02-grupo-sierra.png)

## 4. Activa la música del CD con Audio CD [MCI]

Windows 3.1 necesita el controlador **Audio CD [MCI]** para que esta edición pueda reproducir las pistas del disco. Haz este paso con la imagen del juego montada en **`D:`**.

### Monta el cuarto disquete

Si ya estás en Windows 3.1, sal al DOS emulado. Monta en **`A:`** el cuarto disquete de Windows. El ejemplo usa la ruta temporal del paso 2. Si ya hay un disquete montado en `A:`, puedes cerrar y volver a abrir DOSBox para empezar con esa unidad libre. En una nueva sesión vuelve a montar también el CD en `D:`.

```dos
MOUNT A "win31-disks\disk04.img" -t floppy
C:
CD \WINDOWS
WIN
```

### Añade el controlador

En Windows 3.1 abre **Principal → Panel de control → Controladores → Agregar… → Audio CD [MCI]**.
### Confirma la detección del CD-ROM

Si Windows solicita el **disquete 4**, indica **`A:\`**. Al terminar, debe aparecer el mensaje de que se ha detectado una unidad de CD-ROM.

![Confirmación del controlador MCI y detección de la unidad de CD-ROM](./img/03-audio-cd-mci.png)

## 5. Instala el controlador S3 para jugar a 256 colores

1. Cierra Windows 3.1 y haz una copia de `drives\c\WINDOWS` antes de cambiar el controlador. Comprueba que la máquina emulada es **`svga_s3`**, el tipo de máquina que indica el manual para este controlador. Si lo fijas en la configuración, usa `machine = svga_s3` dentro de `[dosbox]`.
2. Descomprime el controlador **S3 Vision 964 v1.41B5** en `dosbox-staging-v0.83.0\drives\c\DRIVERS\S3` del paquete del juego. Dentro de Windows 3.1 esa carpeta será **`C:\DRIVERS\S3`**. Comprueba que contiene `OEMSETUP.INF`.
3. Abre Windows y, en el grupo **Principal**, abre **Instalar Windows**. En **Opciones → Cambiar configuración del sistema**, abre la lista **Pantalla** y selecciona **Otro** para cargar el controlador. Indica `C:\DRIVERS\S3` y elige el modo **S3 de 640 × 480 y 256 colores**.
4. Si aparece el aviso **Insertar S3 Flat Model Driver Disk**, vuelve a indicar **`C:\DRIVERS\S3`**. Termina el asistente y vuelve a iniciar Windows 3.1 para aplicar el modo.

![El instalador del controlador de pantalla solicita la ruta C:\DRIVERS\S3](./img/04-controlador-s3.png)

El modo S3 elimina el aviso de Lode Runner sobre el funcionamiento a 16 colores. El tamaño con el que verás la imagen en el monitor se ajusta más adelante desde DOSBox.

## 6. Instala la Sound Blaster 16 y comprueba los efectos

La música y los efectos siguen rutas distintas. En la prueba inicial se oía la música del CD y el juego avisaba de que desactivaría los efectos. Para reproducir estos efectos, Windows 3.1 necesitaba el controlador de la **Sound Blaster 16** emulada.

### Consulta el hardware emulado

Descomprime `SB16W3X.ZIP` en `dosbox-staging-v0.83.0\drives\c\DRIVERS\SB16W3X`. Sal de Windows 3.1 y, **en el DOS emulado**, comprueba los valores de la tarjeta antes de ejecutar el instalador.

```dos
SET BLASTER
C:
CD \DRIVERS\SB16W3X
INSTALL.EXE
```

![SET BLASTER muestra el puerto 220, IRQ 7, DMA 1 y DMA alto 5](./img/05-set-blaster.png)

### Indica la ruta de Windows

Si el instalador ofrece el tipo de instalación, elige **Full Installation**. En la pantalla de rutas, deja **`C:\SB16`** para el software de la tarjeta y **`C:\`** como unidad de arranque. En **Microsoft Windows 3.1 path** escribe **`C:\WINDOWS`**. Si queda en **None**, el instalador puede dejar los archivos en `C:\SB16\WINDRV` sin incorporarlos a Windows.
### Configura la tarjeta

Ajusta los valores del instalador a los que devuelva **`SET BLASTER`**. En el laboratorio devolvió `A220 I7 D1 H5 T6`. El instalador proponía IRQ 5 y hubo que cambiarla a **7**.

| Ajuste de Creative | Valor utilizado |
| --- | --- |
| Base I/O address | 220 |
| MIDI Port address | 330 |
| Interrupt setting (IRQ) | 7 |
| Low DMA setting | 1 |
| High DMA setting | 5 |

### Reproduce un WAV

Una vez finalizada la instalación, comprueba que existe **`C:\WINDOWS\SYSTEM\SB16SND.DRV`** y arranca Windows de nuevo. En **Accesorios → Transmisor de medios**, elige **Dispositivo → Sonido** y reproduce **`C:\WINDOWS\TADA.WAV`**. Un WAV audible confirma la reproducción digital de Windows.
### Comprueba el audio del juego

Cierra el Transmisor de medios, abre **Sierra → Lode Runner CD** y entra en un nivel. Comprueba la música de fondo y un efecto de juego, por ejemplo al recoger una pieza de oro.

![El Transmisor de medios se encuentra en el grupo Accesorios de Windows 3.1](./img/06-transmisor-de-medios.png)

## 7. Automatiza el montaje y arranca a pantalla completa

Junto a `dosbox.exe`, usa un fichero **`dosbox-staging.conf`** propio del paquete. Si tu copia todavía usa la configuración principal del anfitrión, puedes copiar la de **`%LOCALAPPDATA%\DOSBox\dosbox-staging.conf`** para conservar los ajustes que ya funcionan. Si no existe, crea el fichero con el Bloc de notas usando **Todos los archivos** para guardarlo con extensión `.conf`.

Edita las secciones existentes. Si falta alguna, créala una sola vez. El bloque muestra solo los ajustes de arranque y pantalla. Conserva los ajustes del emulador y de audio que usaste para verificar el juego.

```ini
[sdl]
fullscreen = on

[render]
aspect = stretch
viewport = fit
integer_scaling = off

[autoexec]
mount d "..\img\LODE_RUNNER_CD.CUE"
C:
CD \WINDOWS
WIN
```

El montaje va antes de `WIN` para que el CD esté disponible al arrancar Windows. Con `aspect = stretch`, la imagen llena el monitor y se ensancha en una pantalla panorámica. Para conservar las proporciones, usa **`aspect = auto`** y deja los otros ajustes de escalado tal como están. En un monitor 16:9 quedarán bandas a los lados. **Alt + Intro** alterna entre pantalla completa y ventana.

[Configuración portable](https://www.dosbox-staging.org/0.83/manual/using-dosbox-staging/configuration/) · [Proporciones y escalado](https://www.dosbox-staging.org/0.83/manual/graphics/rendering/aspect-ratios-and-scaling/)

## 8. Abre el juego directamente y crea el lanzador

En Windows 3.1, abre el grupo **Sierra** y mantén pulsada **Ctrl** mientras arrastras **Lode Runner CD** al grupo **Inicio** del Administrador de programas. Se conserva el acceso de Sierra y la copia del grupo Inicio se ejecuta cada vez que arranca Windows. Sal de Windows normalmente para guardar el cambio.

Crea **`Jugar a Lode Runner.bat`** en la raíz de **`lode-runner-portable`**. Desde el Bloc de notas, selecciona **Todos los archivos** al guardarlo.

```bat
@echo off
setlocal
set "DOSBOX_DIR=%~dp0dosbox-staging-v0.83.0"
start "" /d "%DOSBOX_DIR%" "%DOSBOX_DIR%\dosbox.exe"
```

`%~dp0` toma la ruta del propio lanzador. El parámetro `/d` inicia DOSBox con su carpeta como directorio de trabajo. Así, la ruta `..\img\LODE_RUNNER_CD.CUE` sigue funcionando al mover el conjunto.

| Dentro de `lode-runner-portable` | Qué contiene |
| --- | --- |
| `Jugar a Lode Runner.bat` | Lanzador situado en la raíz |
| `dosbox-staging-v0.83.0\` | DOSBox, sus recursos y `dosbox-staging.conf` |
| `dosbox-staging-v0.83.0\drives\c\` | Windows 3.1, el juego instalado y su estado persistente |
| `img\` | `LODE_RUNNER_CD.CUE` y `LODE_RUNNER_CD.BIN` |

[Comportamiento del grupo Inicio en Windows 3.1, documentación de Microsoft archivada](https://ftp.zx.net.nz/pub/archive/ftp.microsoft.com/MISC/KB/en-us/81/606.HTM)

## 9. Verifica la portabilidad

Cierra DOSBox, copia **toda** la carpeta a otra ubicación y deja desmontado el CD en el Windows anfitrión. Ejecuta **`Jugar a Lode Runner.bat`** desde la copia y comprueba que el juego se abre directamente a pantalla completa. Entra en un nivel, escucha la música y los efectos y guarda una partida. Cierra el juego y DOSBox. Vuelve a ejecutar el lanzador y carga la partida.

En el laboratorio se confirmaron el arranque desde otra ubicación, la música del CD, los efectos y la recuperación de una partida después de cerrar y volver a abrir. La validación corresponde a la edición y al entorno indicados al principio de la guía.
