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
