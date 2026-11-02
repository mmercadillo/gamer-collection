# Registro de preservación — The Secret of Monkey Island (Jewel Case, CD-ROM)

**Estado:** adquisición BIN/CUE verificada por hashes SHA-256 coincidentes de dos lecturas declaradas independientes, con incidencia documental aceptada en el segundo log; representación de pregaps con limitaciones; **sin validación exhaustiva física/subcanales**.  
**Estándar aplicado:** PC Game Archive — Estándar de preservación digital **v1.0**.  
**Fecha de registro y adquisiciones:** 02/11/2026.  
**Ficha:** https://www.pcgamearchive.org/juegos/the-secret-of-monkey-island-jewelcase/ ; identificador de catálogo **pendiente de confirmar** (no utilizar el marcador `000000` como identificador único).  
**Soporte:** **1 CD de 1**, edición Jewel Case; los demás datos editoriales se remiten a la ficha y requieren contraste si se incorporan aquí como evidencia técnica.

## 1. Identificación y estado físico

- Pieza: *The Secret of Monkey Island*, edición Jewel Case conservada por PC Game Archive.
- Número de soportes: **un CD-ROM**, confirmado por la persona responsable.
- Inspección visual detallada: **omitida expresamente por decisión operativa**; no se documentan suciedad, arañazos, daños, etiquetas ni intervenciones.
- Matriz/ring code, mastering/mould SID y otras inscripciones: **no examinados**.
- Etiqueta del volumen: no informada por Windows.

## 2. Caracterización previa

- Medio: **CD mixto de datos y CD-DA**, sesión única, **25 pistas**.
- TOC inicial aportada por ImgBurn: pista 01 **Mode 1** desde LBA 0; pistas **02–25 Audio**; lead-out **LBA 235500** (`52:22:00`).
- Sistema de ficheros: **CDFS** informado por Windows; **ISO9660** reportado por ImgBurn.
- Volumen lógico Windows: **45.121.536 bytes**; ese tamaño no representa la totalidad de las pistas de audio.
- TOC completa: **235.500 sectores**; longitud equivalente a 553.896.000 bytes a 2352 bytes/sector, **no** tamaño obligatorio de un BIN con pregaps sintéticos.
- Protección anticopia: **no evaluada mediante escaneo específico**; no afirmar ausencia.
- Método seleccionado: **BIN/CUE**, para mantener datos, 24 pistas CD-DA e índices; una ISO de la pista de datos por sí sola sería insuficiente.

## 3. Equipo y herramientas

- Estación de custodia/preservación: **PCGA-MASTER-01**, según confirmación del responsable.
- Lector real identificado por PowerShell: **HL-DT-ST DVDRAM GTB0N**, firmware **FU03**, unidad `D:`, conexión **USB** (`USB 2.0` en log).
- Herramienta de adquisición: **ImgBurn 2.5.8.0**, interfaz **SPTI**.
- Sistema operativo: el log de ImgBurn informa `Microsoft Windows 8 Professional x64 Edition (6.2, Build 9200)`; **no se considera identificación concluyente del SO anfitrión**. La ficha de referencia PCGA-MASTER-01 indica Windows Server 2019 Standard x64; diferencia de detección **no reconciliada en esta sesión**.
- Parámetros efectivos de lectura: **Data/Audio MAX/MAX**, sectores `MODE1/2352` y `AUDIO/2352`; velocidad de lectura efectiva informada **24x**, media global **5,0x**, máxima observada **8,4x**.
- Configuración de **Tools → Settings → Read → PreGap Options**: se mantuvo sin cambios durante esta preservación. **No se registraron los valores exactos de `Detection Method` ni de `PreGap Snapping`**, por lo que no pueden afirmarse como valores verificados. El análisis de la pista 2 avanzó sin intervención.

### Parámetros de la pestaña Read y reproducibilidad

Se trabajó desde **ImgBurn 2.5.8.0 → Create image file from disc** con lector `D:` y adquisición BIN/CUE. En el log se registran `Read Speed (Data/Audio): MAX / MAX`, `MODE1/2352`, `AUDIO/2352` y `File Splitting: Auto`. Durante esta preservación **no se cambiaron** las opciones de `Tools → Settings → Read → PreGap Options`. El análisis de la pista 2 tardó, pero prosiguió sin actuación.

**No existe captura ni exportación de los valores concretos de `Detection Method` y `PreGap Snapping`** de esta sesión. Por tanto, deben constar como *no registrados*, no como `1-2-3`, `2-1-3` o `0 Frames`. La ausencia de un cambio observado no demuestra los valores predeterminados efectivos de la instalación. En una nueva adquisición se deberán registrar los valores de la pestaña `Read` antes de comenzar.

## 4. Intentos, incidencias y solución

1. Durante el análisis de pistas ImgBurn permaneció un tiempo en `Analysing Tracks… (Session 1, Track 2)`; posteriormente avanzó sin requerir cambios de configuración.
2. Primer log final: lectura concluida, sin errores explícitos.
3. Segundo log comunicado: termina con `Operation Successfully Completed!`, pero muestra **líneas anómalas** (pista 15 repetida, falta la 14, algunas fronteras LBA distintas y nombre temporal del fichero `.ibg` aparentemente heredado de la primera lectura). El responsable **acepta expresamente esta incidencia documental** y continúa sin recuperar el log original para reconciliarla.
4. El cotejo SHA-256 de los dos pares BIN/CUE fue coincidente. **Esta coincidencia no subsana ni explica las anomalías textuales del segundo log.**

## 5. Adquisición 01

- Fecha: **02/11/2026**; operación indicada por ImgBurn desde **14:40:37** hasta **14:49:41**; duración informada **00:09:02**.
- Fuente: `HL-DT-ST DVDRAM GTB0N FU03 (D:)`; **1 sesión / 25 pistas**.
- Destino original: `C:\Users\Miguel\git\ISO,s\Image.bin`, con descriptor asociado `Image.cue`.
- Resultado de ImgBurn: `Operation Successfully Completed!`.
- Componentes: `Image.bin` **553.148.064 bytes**; `Image.cue` **1.630 bytes**.
- Errores explícitos del log: **ninguno registrado**. Sin informe C2 ni subcanales acreditado.
- Los archivos se trasladaron posteriormente a `C:\Users\Miguel\git\ISO,s\the-secret-of-monkey-island-jewelcase\`.

## 6. Adquisición 02

- Fecha: **02/11/2026**; segundo log presentado indica inicio de operación **15:40:37** y fin **15:49:41**, con duración **00:09:02**.
- Destino declarado: `C:\Users\Miguel\git\ISO,s\Image.bin` y `Image.cue`, liberado tras trasladar la adquisición 01 a otra carpeta.
- Misma unidad y parámetros generales; segundo log informa `Operation Successfully Completed!` y no muestra errores explícitos.
- **Reserva documental:** las inconsistencias descritas en el apartado 4 impiden considerar el segundo log completamente reconciliado; la aceptación de la incidencia queda registrada como decisión del responsable.
- SHA-256 de ambos archivos coincidentes con los de la adquisición 01.

## 7. Descriptor y precisión de las pistas

- El descriptor `Image.cue` de **esta edición de Monkey Island**, proporcionado durante esta sesión, declara **25 pistas**, `TRACK 01 MODE1/2352` y `TRACK 02` a `25 AUDIO`; no se reutiliza el descriptor de LOOM.
- Incluye índices `INDEX 00`/`INDEX 01` para numerosas pistas y las siguientes líneas relevantes:

```cue
FILE "Image.bin" BINARY
  TRACK 01 MODE1/2352
    INDEX 01 00:00:00
    REM TAOGAP 00:02:18
  TRACK 02 AUDIO
    PREGAP 00:02:00
    INDEX 01 04:55:57
```

- `REM TAOGAP 00:02:18` corresponde numéricamente a **168 sectores**; `PREGAP 00:02:00` a **150 sectores**.
- BIN: **235.182 × 2352 = 553.148.064 bytes**. Frente a la extensión TOC de 235.500 sectores existe una diferencia de **318 sectores = 747.936 bytes**, consistente numéricamente con **168 + 150**; esta equivalencia **no prueba por sí sola** el tratamiento físico completo del `TAOGAP` ni la reproducción exhaustiva del disco.
- El descriptor no demuestra conservación de subcanales, offsets de audio ni características físicas completas. La representación documentada es **BIN/CUE con límites conocidos**.

## 8. Verificación y hashes

- Método: comparación SHA-256 entre la primera adquisición trasladada a la carpeta de custodia y la segunda adquisición mantenida en la ruta original. El responsable confirma que corresponden a dos operaciones separadas.
- Ambos archivos coinciden **byte a byte según SHA-256**:

```text
88A546BF6391FA0AE066FBEC5A84F810BBBE363AF3C3FC73B7C24EBF01B982D3  Image.bin
1330620E8A913A3BA9D9DF90C96EBFC2C6B86D1C5A9CEFBEE060B429947A435F  Image.cue
```

- `SHA256SUMS.txt` generado y contenido contrastado con los valores anteriores; tamaño **154 bytes**.
- `Image.bin`, `Image.cue` y `SHA256SUMS.txt`: atributo **`IsReadOnly=True`** verificado por PowerShell. No equivale a WORM/inmutabilidad técnica.
- Contraste con referencia externa de integridad: **no realizado**.

## 9. Máster, copias y cierre

- **Estado de adquisición:** doble lectura con SHA-256 coincidentes; incidencia del segundo log aceptada.
- **Estado integral:** imagen **BIN/CUE reproducible con limitaciones documentadas**; protección, subcanales, offsets y cobertura física completa **no acreditados**.
- **Ubicación lógica de custodia:** `PCGA-MASTER-01` — carpeta `ISO,s/the-secret-of-monkey-island-jewelcase/`, confirmada por el responsable como almacenamiento definitivo.
- **Componentes constituidos:** `Image.bin`, `Image.cue`, `SHA256SUMS.txt`; conservar logs e información de lectura como **evidencias asociadas**.
- **Protección de escritura:** atributo solo lectura aplicado; **inmutabilidad real no acreditada**.
- **Copias de seguridad independientes comprobadas:** **no se ha aportado evidencia específica** de ellas.
- **Copia de trabajo:** no creada ni verificada; **fuera del alcance acordado**.
- **Compatibilidad y ejecución:** **no abordadas por petición expresa**. No generar guía de compatibilidad.

## 10. Definition of Done — alcance de preservación únicamente

- [x] Versión del estándar registrada.
- [x] Edición y número de soportes identificados.
- [ ] Inspección física detallada y códigos de fabricación (omitidos).
- [x] Caracterización lógica: sistema de ficheros, TOC, sesiones y pistas.
- [ ] Evaluación específica de protecciones (no realizada).
- [x] Selección de BIN/CUE justificada.
- [x] Lector, firmware, herramienta, versión y parámetros de adquisición documentados.
- [x] Dos adquisiciones declaradas independientes y SHA-256 coincidentes.
- [ ] Reconciliación completa del segundo log (incidencia aceptada expresamente).
- [x] Descriptor CUE revisado, diferencia de sectores contextualizada.
- [x] Manifiesto `SHA256SUMS.txt` creado.
- [x] Archivos de custodia confirmados en solo lectura.
- [ ] Inmutabilidad técnica y backups independientes comprobados (no acreditados).
- [ ] Subcanales, offsets, verificación física exhaustiva y contraste externo (no acreditados).
- [ ] Copia de trabajo verificada (fuera de alcance).

## 11. Observaciones

La edición contiene una proporción significativa de audio CD-DA (24 pistas): **una ISO de datos no constituye una preservación suficiente de este soporte**. Dos adquisiciones BIN/CUE produjeron hashes idénticos; ello prueba reproducibilidad de los archivos obtenidos, **no** preservación física perfecta. La incidencia textual del segundo log y los límites de los pregaps se conservan de forma explícita para auditoría futura. Este expediente se limita a **preservación digital**, sin inferir compatibilidad en sistemas actuales ni distribuir software protegido.
