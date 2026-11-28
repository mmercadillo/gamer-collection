# Registro interno de compatibilidad — In the 1st Degree (Big Box)

Fecha: 28/11/2026. Pieza #000260, España, dos CD-ROM. Estado: funcional con ajustes. Responsable: operador PC Game Archive. Registro de preservación: ../registros_preservacion/in-the-1st-degree-asesinato-en-primer-grado-bigbox.md. Guía pública: ../documentacion/fuentes/guia-in-the-1st-degree-asesinato-en-primer-grado-bigbox-portable.md.

## 1–4. Identificación, origen, entorno y herramientas

Copias de trabajo separadas en CD, hashes cotejados con las dos ISO de adquisición. Windows 10 Pro 22H2 x64 build 19045; CPU, GPU exacta, RAM anfitriona y modelo de equipo no acreditados. Log OpenGL ATI; audio WASAPI y MIDI Win32. DOSBox Staging 0.83.0 (7b400), Windows 3.1 español, S3 964 1.41B5, SB16 IRQ7 DMA1 HDMA5, MPU-401 inteligente. SmartDrive 4.0, 32 MB emulados. QuickTime original 2.03 y actualización 2.1.2 (WinWorld), SHA-256 FE56FC8E421DD186A8367BC5BA690DB4E54FF166E7A5E11AD777BD9FCCA5A836. La autenticidad del paquete no fue verificada independientemente.

## 5–6. Instalación y ajustes

Base reutilizada de Windows 3.1; cambio de 256 a 64K colores, instalación D:\INSTALL.EXE, MIDI SB16 MIDI Out / Song 2, QuickTime 2.03. Reinicio. Pantalla negra hasta clic; vídeos no funcionales. Pruebas controladas:

| Prueba | Resultado |
| --- | --- |
| Normal 40000 | Fallo FMV |
| Aumento de ciclos | Sin mejora significativa; valores finales no acreditados |
| Dynamic 40000 | Sin mejora |
| Movie Player TITLE.MOV CD | Could not open movie title.mov |
| Movie Player BRODLOGO.MOV CD | Could not open movie brodlogo.mov |
| Copia BRODLOGO.MOV a C:\QTTEST | Mismo error |
| Inventario QTW.INI y DLL/QTC | Implementation=Full; VHDW Component=None; Video Hardware=Not directly supported; componentes presentes |
| Copia de seguridad drives/c | Confirmada por operador |
| QuickTime 2.1.2 | TITLE.MOV desde D: correcto; intro y vídeos del juego correctos |

Causa interna sin determinar. No repetir lectura de medios por este fallo resuelto. No se cambió el contenido del juego. Se volvió a core normal. Se excluyó la configuración global; se modernizaron cycles, mididevice y mount; se retiró el montaje C redundante. Log previo confirmó Windows 3.10, VESA 640x480 16-bit, SB16 y MIDI Win32. Advertencia 32 MB aceptada. Log final de configuración modernizada no aportado.

## 7–8. Procedimiento y matriz

Ver guía pública, configuración y BAT anexos. Guardado/carga, cambio de CD, lanzamiento directo, pantalla completa, cierre al salir de Windows y traslado a otro directorio confirmados por operador. Menús y vídeos respaldados por capturas. Audio general correcto según funcionamiento reportado, sin ensayo instrumental de sincronización ni comprobación separada de cada canal. No se completó el juego entero.

## 9–12. Límites, intentos descartados y fuentes

Ver matriz y referencias de la guía. No probado Windows 11, otro equipo, partida completa ni reconstrucción desde Windows virgen. MIDI Win32 dependiente del anfitrión. No se validó almacenamiento definitivo/backup del máster. El plugin navegador y QuickTime VR adicional no se requerían. Los intentos fallidos quedan en la tabla anterior.

## 13. Evidencias internas

Capturas originales sin recortar en carpeta img del registro (23 PNG). Configuración final y BAT transcritos de la sesión. AUTOEXEC.BAT de base transcrito. Salida de hash y documentación del paquete conservada en logs. No se incluyen imágenes ISO ni instaladores.

## 14–16. Repetición, estado y cierre

Reinicio y ejecución repetidos; traslado a otra ruta validado. No se repitió instalación completa desde Windows limpio, no se certifica equivalencia entre equipos. Estado funcional con ajustes a fecha 28/11/2026. Relación documental y guía pública integradas mediante documentacion.json. Pendientes: validación de equipos adicionales y fijación definitiva del máster. La evidencia de la sesión procede del operador y las capturas; los archivos de configuración son transcripciones.
