# Indiana Jones and the Fate of Atlantis — instalación y ejecución portable en Windows 10

| Información | Detalle |
|---|---|
| **Documento** | PC Game Archive · Guía de compatibilidad y ejecución |
| **Edición probada** | Española Big Box de Erbe Software, cinco disquetes HD de 3,5 pulgadas, MS-DOS |
| **Ficha de la pieza** | [Indiana Jones and the Fate of Atlantis (Big Box)](https://www.pcgamearchive.org/juegos/indiana-jones-and-the-fate-of-atlantis-bigbox/) |
| **Documento relacionado** | [Guía de preservación digital](https://www.pcgamearchive.org/documentacion/preservacion/indiana-jones-and-the-fate-of-atlantis-bigbox/) |
| **Última confirmación funcional** | 27/11/2026 |
| **Resultado** | Juego instalado y jugable en Windows 10 mediante una copia portable de DOSBox Staging 0.83.0; música, efectos, guardado y carga confirmados por el operador |

Esta guía está orientada a quienes poseen legítimamente la edición física. **No incluye imágenes de los disquetes ni los archivos comerciales del juego.** Documenta un procedimiento realmente probado por PC Game Archive y distingue los resultados confirmados de los que no se han evaluado.

## 1. La edición y su conservación digital

El punto de partida son las **cinco imágenes IMA de trabajo** obtenidas de los disquetes originales con WinImage 11.00 x64, y comprobadas contra su manifiesto `SHA256SUMS.txt`. La preservación se documenta por separado; no se trabaja directamente sobre los archivos de referencia. Cada imagen tiene **1.474.560 bytes** y corresponde a una **adquisición sectorial única** con lectura sin errores comunicados y cotejo de estructura. No se hizo una segunda adquisición independiente ni se evaluó la fidelidad magnética de bajo nivel.

| Disco | Imagen de trabajo | Tamaño (bytes) | SHA-256 de referencia de PCGA |
|---|---|---:|---|
| `01` | `INDIANA_ATLANTIS_DISCO_01.IMA` | 1.474.560 | `8622A956CA89C413515361BA54DD176B4EF22394A08804ECE92A0E0C81F97CFC` |
| `02` | `INDIANA_ATLANTIS_DISCO_02.IMA` | 1.474.560 | `D673AF27EEDE3A1E220A5CBD99309C73CBC74595850FBC2701432CC5975EDB3D` |
| `03` | `INDIANA_ATLANTIS_DISCO_03.IMA` | 1.474.560 | `1A73F3425677CF60A36548A14F41987620982B81D773FFE3744AB777AC8D6816` |
| `04` | `INDIANA_ATLANTIS_DISCO_04.IMA` | 1.474.560 | `34B637DB24487C369A0DD533276F458AE5EF3B155BC761F44CC8EEADD3FC67D9` |
| `05` | `INDIANA_ATLANTIS_DISCO_05.IMA` | 1.474.560 | `2E8B79914C55DC166F9DC531833E15F6E61E06C4EC6C6C9DE282447F36A613CB` |

Los hashes identifican únicamente los volcados de esta pieza física, no todas las ediciones existentes. La secuencia de etiquetas de volumen observada en los discos originales no sigue una numeración consecutiva, por lo que se conserva sin corregir:

| Disco físico | Etiqueta observada | Archivos raíz observados |
|---|---|---|
| 01 | `920826A 002` | INSTALL.EXE (34.649 bytes), PCVIQA_A.ND4 (1.419.388 bytes) |
| 02 | `920826A 003` | PCVIQA_B.ND4 (1.454.088 bytes) |
| 03 | `920826A 001` | PCVIQA_C.ND4 (1.454.088 bytes) |
| 04 | `920826A 006` | PCVIQA_D.ND4 (1.454.088 bytes) |
| 05 | `920826A 004` | PCVIQA_E.ND4 (1.444.773 bytes) |

## 2. Entorno y herramientas

- **Equipo de pruebas:** PCGA-LAB-01, Windows 10 Pro 22H2 de 64 bits, compilación 19045. El registro de laboratorio contiene sus características de hardware de referencia; no se midió rendimiento en otros equipos.
- **Emulación utilizada:** DOSBox Staging **0.83.0**, copia completa e independiente de la distribución portable para Windows, incluido su ejecutable `dosbox.exe` y archivos auxiliares. [Distribuciones oficiales de DOSBox Staging](https://www.dosbox-staging.org/releases/windows/).
- **Herramienta de adquisición previa:** WinImage 11.00 x64, no necesaria para jugar una vez obtenidas las imágenes IMA.
- **Archivos necesarios:** cinco imágenes de trabajo de los disquetes originales, DOSBox Staging y el lanzador `Indiana_Atlantis_Portable_Menu.bat`.
- **Intervenciones:** montaje de unidades DOS y ejecución mediante emulación; no se documentaron parches aplicados al juego ni la necesidad de Windows 3.1.

## 3. Preparar la carpeta portable

Crea una carpeta de trabajo con esta estructura **relativa**. Puedes elegir cualquier nombre o unidad para la carpeta principal:

```text
IndianaJonesFateOfAtlantis-Trabajo/
├── Indiana_Atlantis_Portable_Menu.bat
├── dosbox/
│   ├── dosbox.exe
│   └── ... (resto de los archivos de DOSBox Staging)
├── DOS_C/
│   └── ATLANTIS/           (aparecerá después de instalar)
├── INDIANA_ATLANTIS_DISCO_01.IMA
├── INDIANA_ATLANTIS_DISCO_02.IMA
├── INDIANA_ATLANTIS_DISCO_03.IMA
├── INDIANA_ATLANTIS_DISCO_04.IMA
└── INDIANA_ATLANTIS_DISCO_05.IMA
```

`DOS_C` representa `C:` dentro del DOS emulado. La aplicación se instala en `C:\ATLANTIS`, que corresponde físicamente a `DOS_C\ATLANTIS`. Mantén los IMA de trabajo separados de las imágenes maestras de preservación.

Antes de instalar, coteja los hashes de las cinco imágenes de trabajo con `SHA256SUMS.txt` y conserva el manifiesto junto a la copia de referencia. El conjunto se verificó **5 de 5** antes de la prueba de compatibilidad.

## 4. Lanzador con menú: jugar, instalar o salir

Guarda el siguiente contenido como **`Indiana_Atlantis_Portable_Menu.bat`** en la raíz. Es el mismo lanzador con menú que se probó correctamente en el laboratorio. Sus rutas se resuelven desde el propio fichero mediante `%~dp0`, sin depender de la letra de unidad ni de una ruta personal. El script comprueba la presencia del emulador, de `DOS_C` y, para instalar, de los cinco IMA; antes de reinstalar pide confirmación.

```bat
@echo off
setlocal EnableExtensions DisableDelayedExpansion
pushd "%~dp0" || exit /b 1

rem PC Game Archive - Indiana Jones and the Fate of Atlantis
rem Lanzador portable: DOSBox Staging 0.83.0

:menu
cls
echo ========================================================
echo   PC GAME ARCHIVE - INDIANA JONES: FATE OF ATLANTIS
echo ========================================================
echo.
echo   [1] Jugar
echo   [2] Instalar / reinstalar desde los 5 disquetes
echo   [3] Salir
echo.
choice /c 123 /n /m "Selecciona una opcion [1-3]: "
if errorlevel 3 goto :salir
if errorlevel 2 goto :instalar
if errorlevel 1 goto :jugar
goto :menu

:comprobar_base
if not exist "dosbox\dosbox.exe" (
    echo ERROR: Falta dosbox\dosbox.exe.
    goto :fallo
)
if not exist "DOS_C\." (
    echo ERROR: Falta la carpeta DOS_C.
    goto :fallo
)
exit /b 0

:jugar
cls
call :comprobar_base
if errorlevel 1 goto :volver
set "JUEGO_ENCONTRADO="
for %%E in (EXE COM BAT) do (
    if exist "DOS_C\ATLANTIS\ATLANTIS.%%E" set "JUEGO_ENCONTRADO=SI"
)
if not defined JUEGO_ENCONTRADO (
    echo No se encuentra DOS_C\ATLANTIS\ATLANTIS.EXE/COM/BAT.
    echo Primero instala el juego con la opcion 2.
    goto :volver
)
echo Iniciando el juego...
"dosbox\dosbox.exe" --working-dir "%CD%" --noprimaryconf --nolocalconf ^
    -c "MOUNT C DOS_C" ^
    -c "C:" ^
    -c "CD \ATLANTIS" ^
    -c "ATLANTIS"
if errorlevel 1 echo AVISO: DOSBox ha finalizado con error.
goto :volver

:instalar
cls
call :comprobar_base
if errorlevel 1 goto :volver
for %%N in (01 02 03 04 05) do (
    if not exist "INDIANA_ATLANTIS_DISCO_%%N.IMA" (
        echo ERROR: Falta INDIANA_ATLANTIS_DISCO_%%N.IMA.
        goto :volver
    )
)
if exist "DOS_C\ATLANTIS\." (
    echo ATENCION: Ya existe DOS_C\ATLANTIS.
    echo Reinstalar puede sobrescribir archivos y partidas guardadas.
    echo Se recomienda hacer una copia de DOS_C\ATLANTIS antes.
    echo.
    choice /c SN /n /m "Deseas continuar con la reinstalacion? [S/N]: "
    if errorlevel 2 goto :menu
)
echo.
echo Durante la instalacion cambia de disquete con Ctrl+F4.
echo Las imagenes se montan en modo solo lectura.
echo.
"dosbox\dosbox.exe" --working-dir "%CD%" --noprimaryconf --nolocalconf ^
    -c "MOUNT C DOS_C" ^
    -c "MOUNT A INDIANA_ATLANTIS_DISCO_0?.IMA -t floppy -ro" ^
    -c "A:" ^
    -c "INSTALL"
if errorlevel 1 echo AVISO: DOSBox ha finalizado con error.
goto :volver

:fallo
exit /b 1

:volver
echo.
pause
goto :menu

:salir
popd
endlocal
exit /b 0
```

El menú ofrece:

1. **Jugar:** monta `DOS_C` como `C:` y ejecuta `ATLANTIS` desde `C:\ATLANTIS`. No es necesario montar los disquetes para esta opción.
2. **Instalar / reinstalar:** monta los cinco IMA como `A:` en solo lectura, inicia `INSTALL` y solicita confirmación si existe `DOS_C\ATLANTIS`. **Antes de reinstalar, realiza una copia de las partidas**, ya que el instalador podría sobrescribir datos existentes.
3. **Salir:** termina el lanzador.

El lanzamiento de DOSBox desde el `.bat` se realiza en la máquina Windows anfitriona; los comandos de montaje se ejecutan dentro del emulador.

## 5. Instalar desde los cinco disquetes

1. Comprueba que `DOS_C` existe y está vacía si es la primera instalación. Conserva los cinco IMA con los nombres indicados.
2. Ejecuta el `.bat` mediante doble clic y selecciona **2 — Instalar / reinstalar**.
3. El instalador original, en castellano, permite seleccionar **`C:`** como destino; confirma esa unidad. Se instala en **`C:\ATLANTIS`**.
4. Durante la copia, cuando se solicite el siguiente disquete, pulsa **Ctrl+F4** en DOSBox para avanzar a la siguiente imagen montada y confirma el cambio en el instalador. En la prueba fue necesario utilizar este atajo.
5. Espera a que aparezca **«Instalación completa»**. Sal con **Esc** y cierra el emulador cuando proceda.

Si falta un IMA, el lanzador cancela la opción de instalación antes de abrir el emulador. Si una lectura o instalación fallara, no modifiques la imagen de preservación: revisa la copia de trabajo y el registro técnico.

## 6. Arrancar y jugar sin reinstalar

1. Ejecuta `Indiana_Atlantis_Portable_Menu.bat`.
2. Selecciona **1 — Jugar**. DOSBox monta automáticamente `DOS_C` como unidad `C:` y arranca `ATLANTIS` desde `C:\ATLANTIS`.
3. En la prueba se alcanzó la pantalla inicial **«Pulsa la tecla Enter para empezar a jugar»** y, a continuación, la verificación original con piedras y manual.
4. El usuario confirmó posteriormente el funcionamiento del juego, la música, los efectos de sonido, el guardado y la recuperación de partidas.

El manual forma parte del mecanismo de comprobación original. La guía **no reproduce combinaciones de verificación** ni evita esta comprobación; se necesita la documentación correspondiente a la edición.

## 7. Qué significa «portable» en esta prueba

El lanzador usa rutas relativas y el juego se instala dentro de `DOS_C`, en la misma carpeta del emulador. No requiere instalar DOSBox globalmente en el sistema. Se comprobó **el arranque desde el menú y el traslado del paquete completo a otro equipo**, con funcionamiento correcto confirmado por el operador. Esta validación de portabilidad corresponde a los equipos realmente probados y no constituye una certificación general para cualquier sistema operativo o configuración.

Si cambias la ubicación del paquete, mueve la **carpeta completa** sin alterar la estructura interna. Puedes conservar las imágenes IMA de trabajo para futuras reinstalaciones o preparar una copia de juego para uso personal con los discos almacenados por separado, siempre que adaptes el lanzador de instalación.

## 8. Matriz funcional de la prueba

| Subsistema | Estado | Evidencia o límite |
|---|---|---|
| Instalación desde los cinco IMA | Correcto | Instalador en español; mensaje de instalación completa |
| Cambio de disquetes | Correcto | Uso necesario y confirmado de Ctrl+F4 |
| Arranque del juego | Correcto | Capturas de pantalla inicial y comprobación del manual |
| Inicio y jugabilidad | Correcto | Confirmación posterior de ejecución y funcionamiento del juego |
| Gráficos 2D | Correcto | Pantallas capturadas y funcionamiento confirmado |
| Música | Correcto | Confirmación expresa del usuario |
| Efectos de sonido | Correcto | Confirmación expresa del usuario |
| Teclado/ratón | Correcto | Navegación, instalación y jugabilidad confirmadas en conjunto; no se realizó una prueba independiente por periférico |
| Guardado de partidas | Correcto | Confirmación expresa del usuario |
| Carga de partidas | Correcto | Confirmación expresa del usuario |
| Lanzador con menú | Correcto | Opción de jugar probada; funcionamiento del menú confirmado |
| Reinstalación sobre partida existente | Correcto | Reinstalación probada y funcionamiento confirmado por el operador; no se documenta por separado el estado de las partidas preexistentes tras reinstalar |
| Traslado del paquete a otro equipo | Correcto | Traslado y ejecución del paquete portable confirmados por el operador |
| Campaña completa | No probado | Se confirma funcionamiento, no finalización integral |
| Vídeos/cinemáticas | No probado | Sin comprobación específica registrada |
| Gráficos 3D | No aplicable | Aventura gráfica 2D |
| Gamepad/joystick | No probado | No evaluado |
| Multijugador | No aplicable | No corresponde al modo de juego documentado |
| Cierre y segundo arranque | Correcto | Cierre y nuevo arranque confirmados por el operador |

## 9. Limitaciones y alcance

La compatibilidad queda **confirmada en Windows 10 con DOSBox Staging 0.83.0 para esta edición física concreta**. No se ensayó Windows 11 ni se certificaron otros equipos. La primera adquisición de cada disquete fue única; no se realizaron lecturas dobles. La prueba de guardado/carga y música/sonido se recoge a partir de confirmación del operador, no de un log automatizado.

No se incluyen imágenes, claves del manual, ejecutables comerciales ni una copia lista para jugar. El `.bat` es únicamente un lanzador de comandos y puede reutilizarse con una copia legítima del juego.

## 10. Resultado final

**Estado: funcional con emulación y paquete portable probado en otro equipo.** Las cinco imágenes de trabajo permitieron instalar el juego, arrancarlo y utilizarlo con música, efectos y partidas guardadas. La documentación permite repetir el procedimiento desde los medios originales digitalizados y distingue las verificaciones realizadas de las pruebas no efectuadas.
