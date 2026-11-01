# Registro de preservación — Loom (Jewel Case, CD-ROM estadounidense de 1992)

**Estado:** adquisición BIN/CUE verificada por doble lectura coincidente; preservación de subcanales no demostrada. Compatibilidad: **no probada**.  
**Estándar aplicado:** PC Game Archive — Estándar de preservación digital **v1.0**.  
**Fecha de registro y adquisiciones:** 01/11/2026.  
**Ficha:** `juegos/loom-jewelcase/`; identificador de catálogo: `000000` (provisional, no identificador único).  
**Soporte:** 1 CD de 1; edición Jewel Case, mercado estadounidense (1992), inglés; distribución LucasArts / The Software Toolworks.

## 1. Identificación y estado físico

- Pieza: Loom, edición estadounidense CD-ROM Jewel Case conservada por PC Game Archive.
- Estado visual comunicado antes de la lectura: **muy buen estado aparente**.
- Suciedad, arañazos, daño localizado, etiquetas/anotaciones, matriz/ring code, SID: **sin evaluación detallada documentada**.
- Limpieza/intervenciones previas: **no documentadas**.
- Identificador del volumen observado: `LOOMCD`.

## 2. Caracterización previa

- Medio: CD mixto (datos + CD-DA), una sesión, **dos pistas**.
- TOC: pista 1 datos `MODE1`, `INDEX 01` LBA **0**; pista 2 audio `INDEX 01` LBA **22500** (05:02:00); lead-out LBA **268425** (59:41:00).
- Sistema de archivos: **ISO9660**, detectado por ImgBurn; siete archivos examinados por el escaneo MPF (`000.LFL`, `901.LFL`, `902.LFL`, `903.LFL`, `904.LFL`, `DISK01.LEC`, `LOOM.EXE`).
- Escaneo MPF de protecciones: no identificó protecciones conocidas en los archivos analizados; **ausencia de protección no demostrada**.
- Anomalía: lectura problemática alrededor del LBA **22207** antes del `INDEX 01` de la pista 2; Aaru estimó un pregap de **293 sectores**. No afirmar causalidad única, protección o daño del soporte.
- La imagen ISO aislada no representaría la pista CD-DA; se eligió representación BIN/CUE.

## 3. Equipo y herramientas

- Estación: **PCGA-MASTER-01**; mecanismo **HL-DT-ST DVDRAM GTB0N**, firmware **FU03**, conexión **USB**, unidad `D:`.
- Windows anfitrión: el log de Aaru identifica **Windows 10 (10.0.19041.5915, 64 bits)**; ImgBurn reporta **Windows 8 Professional x64 (6.2, build 9200)** por su mecanismo de detección. **Versión del SO no reconciliada; registrar esta discrepancia en vez de dar por cierto el reporte de ImgBurn.**
- MPF: se utilizaron **3.10.0 y 3.11.1** durante el diagnóstico; Redumper build `b767` en las pruebas descritas; Aaru **5.4.2** según su log; DiscImageCreator (versión exacta no documentada).
- Adquisición final: **ImgBurn 2.5.8.0**, interfaz SPTI, lectura de sectores crudos `MODE1/2352` y `AUDIO/2352`.
- Configuración decisiva de ImgBurn: `Tools > Settings > Read > PreGap Options > Detection Method: 2-1-3`; `PreGap Snapping: 0 Frames`; velocidad solicitada datos/audio **MAX/MAX**, efectiva declarada **24x** (datos), velocidad media global **6,1x**.

## 4. Intentos, incidencias y solución

1. **Redumper**: lector no presente en su base de datos; perfil genérico, offset de lectura +102 muestras; errores/warnings cerca de LBA 22207-22220; lecturas suspendidas, **no válidas**.
2. **DiscImageCreator**: finalización con código 1; diagnósticos SCSI `05-64-00 ILLEGAL MODE FOR THIS TRACK` y `05-24-00 INVALID FIELD IN CDB`; **sin adquisición válida**.
3. **Aaru 5.4.2**: registro de `UNRECOVERED READ ERROR` y `ILLEGAL MODE FOR THIS TRACK` alrededor de LBA 22192–22349; `Skipping 512 blocks from errored block 22192`; `Failed crossing into Lead-Out`; imagen `.aaruf` **no reconocida** por `aaru image info`, cabecera con ceros; **sin adquisición válida**.
4. **ImgBurn 2.5.8.0**: métodos predeterminados `1-2-3` y distintas velocidades: bloqueos en `Analysing Tracks... (Session 1, Track 2)`, intentos abortados. Con **Detection Method `2-1-3`**, lectura finalizada con éxito. Esta adaptación corresponde a esta edición/lector; no se generaliza a otros CD.

## 5. Adquisición 01 (válida)

- Fecha: **01/11/2026**. Inicio **20:41:30**, final **20:50:02**, duración **00:08:31**.
- Log: `Reading Track 1 of 2... (MODE1/2352, LBA: 0 - 22206)` y `Reading Track 2 of 2... (AUDIO/2352, LBA: 22207 - 268424)`; `Operation Successfully Completed!`.
- Salida: `LOOMCD.BIN` **630.982.800 bytes**; `LOOMCD.CUE` **157 bytes**.
- Carpeta de adquisición 01 comunicada: `ISO/Nueva carpeta/` (ruta temporal; evitar como nombre definitivo).
- Errores: **ninguno consignado en el log de la lectura exitosa**; ausencia de errores C2 no demostrada (no existe recuento C2 en ese log).

## 6. Adquisición 02 (válida)

- Fecha: **01/11/2026**. Inicio **20:53:45**, final **21:02:16**, duración **00:08:30**.
- Igual herramienta, unidad y parámetros; lectura de ambas pistas; `Operation Successfully Completed!`.
- Carpeta de adquisición 02: `ISO/LOOMCD/` (ruta temporal).
- SHA-256 de **BIN y CUE coincidentes** con adquisición 01.

## 7. Descriptor y precisión de las pistas

```cue
FILE "LOOMCD.BIN" BINARY
  TRACK 01 MODE1/2352
    INDEX 01 00:00:00
  TRACK 02 AUDIO
    PREGAP 00:02:00
    INDEX 00 04:56:07
    INDEX 01 04:58:00
```

- El CUE incluye `INDEX 00` (LBA de archivo **22207**) e `INDEX 01` (LBA de archivo **22350**), separados por **143** sectores, más `PREGAP 00:02:00` (**150** sectores descritos y no almacenados en el BIN). El `INDEX 01` físico de la pista 2 corresponde a LBA **22500** del TOC (22350 + 150).
- BIN: **268275 × 2352** bytes. La diferencia de **150 sectores** frente a la extensión TOC de 268425 sectores es congruente con el pregap sintético del descriptor; **no debe calificarse simplemente como dato perdido ni como copia física exhaustiva**.
- La lectura no prueba preservación íntegra de subcanales, información de posición física ni offsets de audio. BIN/CUE permite representar datos, CD-DA y estructura de índices descrita, con esos límites.

## 8. Verificación y hashes

- Método: **dos adquisiciones independientes con SHA-256 coincidentes** para ambos componentes, más verificación SHA-256 de la copia trasladada a la carpeta de custodia definitiva.
- Manifiesto `SHA256SUMS.txt` validado contra los hashes facilitados:

```text
70BA458BAC6C7D656B188940493FCF57FD65930C0E0F70A683ED1D5129897BD4  LOOMCD.BIN
F25600C48612C0FBB0B957F0F84E02FB2E916EA41DBA90B45D7E4A71F64DF312  LOOMCD.CUE
```

- Los tres archivos (`BIN`, `CUE`, `SHA256SUMS.txt`) se han confirmado **solo lectura**. Esto **no equivale a almacenamiento inmutable/WORM**.
- Prueba de montaje: se aportó captura de la imagen montada con acceso a archivos ISO9660, **sin establecer formalmente validación funcional de PCGA-LAB-01**. La imagen no se distribuye públicamente.
- Comparación con referencia externa de integridad/redump: **no realizada**.

## 9. Máster, copias y cierre

- **Estado de adquisición:** verificada por doble lectura coincidente.
- **Estado integral del máster:** representación BIN/CUE verificada **con limitaciones documentadas**; la preservación de subcanales y exactitud física completa **no está acreditada**.
- **Ubicación lógica:** `PCGA-MASTER-01`, carpeta definitiva `ISO/loom-jewelcase/` según la sesión operativa; ruta de almacenamiento permanente y copia de seguridad externa **pendientes de consignar**.
- **Componentes:** `LOOMCD.BIN`, `LOOMCD.CUE`, `SHA256SUMS.txt`; los logs y resultados de diagnóstico deben conservarse como evidencias asociadas, no embebidos en la imagen.
- **Backups independientes comprobados:** no documentados.
- **Copia de trabajo de laboratorio:** no registrada como creada y verificada en `PCGA-LAB-01`; no atribuir esta condición a una carpeta temporal en MASTER-01.
- **Compatibilidad/ejecución:** **no probada**. Una guía de ejecución requerirá pruebas separadas.

## 10. Definition of Done

- [x] Versión de estándar registrada.
- [x] Edición y soporte identificados.
- [ ] Inspección física detallada y matriz/ring code completados (no documentados).
- [x] Caracterización lógica (TOC, sesiones, pistas y sistema de ficheros).
- [x] Escaneo de protecciones documentado como «no detectado».
- [x] Selección de método justificada y perfil reproducible registrado.
- [x] Dos lecturas válidas y logs finales revisados.
- [x] SHA-256 de BIN/CUE de las dos adquisiciones y la copia de custodia coincidentes.
- [x] Manifiesto SHA256SUMS.txt generado.
- [x] Separación de máster y trabajos temporales identificada.
- [ ] Inmutabilidad real y backups independientes verificados (no acreditados).
- [ ] Verificación física exhaustiva, subcanales/offsets y contraste externo (no acreditados).

## 11. Observaciones

La dificultad de la zona LBA 22207–22500 fue determinante en la selección del método. `Detection Method: 2-1-3` permitió concluir dos adquisiciones reproducibles con el mismo lector. **No afirmar que ese ajuste recupera todos los subcanales o que demuestra ausencia de errores físicos.** La ficha pública de compatibilidad se abordará solo después del cierre documental y la copia de trabajo verificada.
