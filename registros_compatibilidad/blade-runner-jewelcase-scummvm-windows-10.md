# PC Game Archive — Registro interno de compatibilidad

- **Pieza:** Blade Runner — Jewel Case (Dinamic Multimedia, edición española, 4 CD-ROM).
- **Ficha:** https://www.pcgamearchive.org/juegos/blade-runner-jewelcase/
- **Entorno:** PCGA-LAB-01; Windows 10 Pro 22H2 x64 según ficha del laboratorio. No se repitió caracterización integral de hardware en esta sesión.
- **Motor:** ScummVM 2026.4.0, variante `Blade Runner (Windows/Spanish)` **sin contenido restaurado**.
- **Estado:** funcional en las pruebas principales; cobertura de toda la aventura no demostrada.

## Punto de partida

Extracciones de los cuatro CD mediante UltraISO (versión no documentada), con imágenes ISO reconstruidas montadas y 27 archivos `.MIX`, `.TLK`, `.DAT` reunidos en carpeta separada para ScummVM. Archivos duplicados cotejados por tamaño y SHA-256. Conjunto de 27 archivos cotejado por SHA-256 con sus fuentes. Manifiesto: `registros_preservacion/blade-runner-jewelcase-sha256.md`.

## Incidencias de instalación nativa

- `INSTALAR.EXE`: ventana de incompatibilidad en Windows 10 x64 (según captura).
- `SETUP.EXE`: mensaje de que no se encuentra `F:\SETUP\INSTALL.EXE`; se comprobó que existía (45.568 bytes).
- Ejecución directa de `INSTALL.EXE`: fallo. Cabecera inspeccionada en PowerShell: firma `NE` (componente heredado de 16 bits).
- No se prosiguió con instalación nativa; se utilizó ScummVM sobre datos propios de la edición española.

## Preparación y ejecución validada

1. Conservar por separado las extracciones de los cuatro CD.
2. Crear carpeta `Blade_Runner_ES_ScummVM`.
3. Reunir archivos `.MIX`, `.TLK`, `.DAT` de las cuatro extracciones. Los cuatro `CDFRAMES.DAT` deben llamarse `CDFRAMES1.DAT` a `CDFRAMES4.DAT`.
4. Si existen duplicados (por ejemplo `A.TLK`, `3.TLK`, `VQA3.MIX`), verificar identidad SHA-256; no renombrarlos según supuesto número del disco.
5. Verificar origen/destino con SHA-256 (27 archivos en la prueba documentada).
6. En ScummVM 2026.4.0, seleccionar la carpeta y elegir `Blade Runner (Windows/Spanish)`, no la variante restaurada.
7. Iniciar; comprobar introducción, juego, audio y guardado/carga.

## Matriz funcional

| Subsistema | Resultado | Evidencia / límite |
|---|---|---|
| Instalación nativa original | No funcional | Componente NE en Windows 10 x64 |
| Preparación de datos para ScummVM | Correcto | 27 archivos seleccionados/verificados frente a extracción |
| Detección en ScummVM | Correcto | `Windows/Spanish` reconocido |
| Arranque | Correcto | Confirmación del operador |
| Menús | No probado | No hay comprobación individual documentada |
| Introducción / cinemáticas observadas | Correcto | Confirmación del operador; no todos los vídeos |
| Gráficos 2D / 3D | Correcto con limitaciones | Juego observado correcto; subsistemas gráficos no evaluados separadamente |
| Voces en español | Correcto | Confirmadas por el operador |
| Música | Correcto | Confirmada por el operador |
| Efectos de sonido | Correcto | Confirmados por el operador |
| Teclado / ratón | Correcto con limitaciones | Jugabilidad confirmada; periféricos no evaluados por separado |
| Gamepad / joystick | No probado | Sin prueba comunicada |
| Inicio de partida | Correcto | Confirmado |
| Juego representativo | Correcto con limitaciones | Juego inicial probado; no recorrido completo |
| Guardado | Correcto | Confirmado |
| Carga y continuación | Correcto | Confirmado |
| Cambio de escena / progresión completa | No probado | No se detallaron escenas posteriores |
| Cambio de CD durante partida | No aplicable al método validado | Datos reunidos en una carpeta; no se acredita disco físico |
| Multijugador | No aplicable | Aventura individual |
| Cierre y segundo arranque | Correcto | Confirmado en la prueba de guardado/carga |

## Limitaciones y repetición

- Reproducción exacta de todos los recursos del juego y todos los finales: no probada.
- No consta reinstalación desde cero con repetición completa de pasos y hashes.
- Procedimiento ejecutado sin parches ni opción de contenido restaurado.
- Estado probado: ScummVM en Windows 10, sin extrapolar a Windows 11 ni a la edición inglesa.

## Evidencia

Capturas de detección ScummVM, manifiesto SHA-256 del conjunto de trabajo, salidas PowerShell y confirmaciones de prueba del operador.
