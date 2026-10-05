# Registro de preservación — Red Baron 3-D

**Estado:** Preservación verificada · compatibilidad Windows 10 verificada  
**Ficha PCGA:** #000215  
**URL:** `juegos/red-baron-3d-bigbox/`  
**Fecha de adquisición/verificación:** 05/10/2026
**Estándar aplicado:** PC Game Archive — Estándar de preservación digital v1.0

## 1. Identificación

- Título: Red Baron 3-D
- Edición / variante: edición española Big Box
- Mercado: España
- Idioma: Español
- Distribución: Sierra On-Line / Coktel Educative
- EAN: 3348542050372
- Identificador interno: 000215
- Soporte nº / total: 1 / 1 CD-ROM
- Etiqueta del disco: REDBARON_3D
- Inscripción legible del anillo: BELIEVE IN CD
- Otros códigos de matriz/ring: visibles en fotografías, no transcritos por falta de nitidez suficiente

## 2. Estado físico previo

- Evidencia: fotografías del anverso, reverso y anillo interior realizadas antes de la adquisición.
- Estado detallado de suciedad/arañazos: no clasificado mediante escala específica en este primer piloto.
- Daños que impidieran la lectura: ninguno observado durante la adquisición.
- Intervenciones previas conocidas: no documentadas.

## 3. Caracterización técnica

- Tipo de soporte: CD-ROM
- Unidad lógica durante el trabajo: D:\
- Sistema de ficheros visible: CDFS
- Etiqueta: REDBARON_3D
- Tamaño lógico visible: 718.379.008 bytes
- Pistas: 1
- Tipo de pista: MODE1/2352
- Audio: no se detectan pistas de audio en el CUE obtenido
- Cuesheet:

```text
FILE "REDBARON_3D.bin" BINARY
  TRACK 01 MODE1/2352
    INDEX 01 00:00:00
```

- Protección: no detectada por el escaneo realizado con MPF
- Resultado textual MPF: `No protections found`
- Error Count: 0
- C2 Error Count: 0

## 4. Decisión de adquisición

- Procedimiento: adquisición raw de CD mediante Redumper, produciendo BIN/CUE y evidencias auxiliares.
- Justificación: soporte óptico de una pista MODE1/2352; el procedimiento conserva los sectores raw y genera logs/metadatos verificables.
- Carcasa: XD008
- Unidad óptica real: HL-DT-ST DVDRAM GTB0N
- Firmware: FU03
- Sistema operativo anfitrión: Windows
- Frontend: Media Preservation Frontend 3.10.0
- Herramienta: Redumper build b749
- Velocidad: 1x
- Reintentos: 20
- Parámetros registrados por MPF/Redumper: `disc --skeleton --drive=D:\ --speed=1 --retries=20 ...`
- Write Offset informado: -102

## 5. Adquisición 01

Ficheros generados:

- `REDBARON_3D.bin` — 825.018.096 bytes
- `REDBARON_3D.cue` — 77 bytes
- `REDBARON_3D.log` — 3.245 bytes
- `REDBARON_3D.scram` — 931.563.288 bytes
- `REDBARON_3D_logs.zip` — 1.539.992 bytes
- `!submissionInfo.txt` — 2.808 bytes
- `!protectionInfo.txt` — 330 bytes

Hashes informados por Redumper para `REDBARON_3D.bin`:

- CRC32: `0e92f1ee`
- MD5: `83b2edfb3400166ca78d41835c4cc298`
- SHA-1: `02e32be85c12f12d49c7b7f38b8c771f7084442d`

SHA-256 PC Game Archive:

- BIN: `1E354950083B85F76623CD5BED2F061C90833EB1431ED2BBBD288BEB125BA66B`
- CUE: `CB27C9E074A1BC07DFBF5A967C5641F216CBB2E166D460DF9418EC78BED501F6`

## 6. Adquisición 02 y verificación

Se realizó una segunda adquisición independiente con la misma unidad, herramienta y parámetros.

SHA-256 obtenidos:

- BIN: `1E354950083B85F76623CD5BED2F061C90833EB1431ED2BBBD288BEB125BA66B`
- CUE: `CB27C9E074A1BC07DFBF5A967C5641F216CBB2E166D460DF9418EC78BED501F6`

**Resultado:** coincidencia exacta entre las dos adquisiciones para BIN y CUE.

## 7. Máster de preservación

- Estado: `verificada`
- Representación principal: BIN/CUE
- Evidencia auxiliar: logs, submission info, protection info y fichero SCRAM generado por Redumper/MPF
- Adquisición 02: conservar como evidencia independiente de repetibilidad
- Máster: no modificar
- Copia de trabajo: creada y verificada mediante SHA-256 antes de las pruebas de compatibilidad
- Copias de seguridad: pendientes de registrar dentro del piloto si no se han efectuado todavía

## 8. Definition of Done de preservación

- [x] Edición identificada.
- [x] Estado físico documentado mediante evidencia fotográfica.
- [x] Soporte caracterizado antes de seleccionar el método definitivo.
- [x] Protecciones/características especiales evaluadas.
- [x] Procedimiento elegido y justificado.
- [x] Hardware/software/versiones registrados.
- [x] Logs conservados.
- [x] Errores e incidencias revisados.
- [x] SHA-256 calculados.
- [x] Verificación por segunda adquisición coincidente.
- [x] Máster separado de cualquier copia de trabajo.
- [x] Registro de preservación asociado a la pieza.

## 9. Compatibilidad asociada

La copia de trabajo se montó con **WinCDEmu 4.1** y se utilizó para validar la edición en Windows 10 Pro 22H2 build 19045. El resultado y la matriz funcional se conservan en `registros_compatibilidad/red-baron-3d-bigbox-windows-10.md` y se publican en la guía asociada. El máster de preservación permanece sin modificar.
