# Jugar a Lode Runner: The Legend Returns en Windows 10

Guía para la edición española Big Box en CD-ROM, ficha #000250. Probada en **Windows 10 Pro 22H2 x64, compilación 19045.6466**, con **DAEMON Tools Lite 12.6** y **otvdm 0.9.0**. [Ficha del juego](../../../juegos/lode-runner-the-legend-returns-bigbox/) · [Preservación del CD](../../preservacion/lode-runner-the-legend-returns-bigbox/)

[Ver la guía de instalación portable con DOSBox Staging y Windows 3.1](../lode-runner-the-legend-returns-bigbox-portable/)

## 1. Monta el CD en D:

Mantén juntos los archivos `LODE_RUNNER_CD.CUE` y `LODE_RUNNER_CD.BIN`. En **DAEMON Tools Lite**, monta el archivo **CUE** en la unidad virtual **`D:`**. En el Explorador, abre `D:` y comprueba que aparecen `INSTALL.EXE` e `INSTALL.DAT`. Deja la imagen montada mientras instalas y juegas.

Si necesitas seleccionar una unidad virtual existente, puedes indicar la letra desde PowerShell. Ajusta ambas rutas a tu equipo.

```powershell
& 'C:\Herramientas\DAEMON Tools Lite\DTCommandLine.exe' --mount_to --letter D --path 'C:\Imagenes\LODE_RUNNER_CD.CUE'
```

## 2. Abre el instalador

Abre PowerShell. Cambia la ruta de `otvdm.exe` por la de tu copia de **otvdm 0.9.0** y ejecuta las dos líneas.

```powershell
Set-Location 'D:\'
& 'C:\Herramientas\otvdm-v0.9.0\otvdm.exe' 'D:\INSTALL.EXE'
```

En la primera pantalla, escribe la carpeta donde quieras instalar el juego y pulsa **Continue Install**. Guarda esa ruta para el paso 4.

![Pantalla para elegir la carpeta de instalación](./img/01-destino-instalacion.png)

## 3. Completa la instalación

Cuando el asistente pregunte dónde está el CD, deja **`D:\`** y pulsa **Continue**.

![Confirmación de D como unidad del CD](./img/02-unidad-cd-d.png)

Selecciona **Full**, deja **Install Joystick Drivers** desmarcado y pulsa **Install Me!**. Al terminar, comprueba que la carpeta que elegiste contiene `LODERUNN.EXE`.

![Opciones del asistente con Full seleccionado y controladores de joystick desmarcados](./img/03-opciones-instalacion-full.png)

## 4. Arranca el juego

Con la imagen todavía montada en **`D:`**, abre PowerShell. Sustituye las rutas de ejemplo por la carpeta que elegiste y la ubicación de otvdm.

```powershell
Set-Location 'C:\Juegos\lode-runner'
& 'C:\Herramientas\otvdm-v0.9.0\otvdm.exe' '.\LODERUNN.EXE'
```

En el laboratorio se comprobó el primer nivel con teclado, música y efectos, así como el guardado, el segundo arranque y la carga de una partida. La instalación y el arranque se repitieron después usando DAEMON Tools en `D:` durante todo el recorrido.
