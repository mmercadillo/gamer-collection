@echo off
setlocal
cd /d "%~dp0dosbox-staging-v0.83.0_win3X"
dosbox.exe --noprimaryconf --conf dosbox.conf
endlocal
