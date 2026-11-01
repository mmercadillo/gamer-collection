# Preservación de la pieza

Este registro documenta la adquisición digital del **CD-ROM de Loom, edición estadounidense de 1992 en formato Jewel Case**, conservado por PC Game Archive. La representación digital del juego no se distribuye desde esta web.

**Estándar aplicado:** [PC Game Archive — Estándar de preservación digital v1.0](../estandar-preservacion-digital/).  
**Fecha de adquisición y verificación:** 01/11/2026.  
**Estado:** adquisición BIN/CUE verificada por doble lectura coincidente, con limitaciones de alcance documentadas.

## Identificación y caracterización

- Pieza: **Loom — Jewel Case**, edición estadounidense en CD-ROM de 1992.
- Soporte: **un CD mixto** con una pista de datos `MODE1/2352` y una pista de audio CD-DA.
- Sesiones: **1**; pistas: **2**.
- Sistema de archivos de datos: **ISO9660**; etiqueta del volumen: `LOOMCD`.
- Pista de datos: desde LBA 0.
- Pista de audio: `INDEX 01` físico en LBA 22500.
- Lead-out: LBA 268425.
- El escaneo de archivos efectuado con Media Preservation Frontend **no identificó protecciones conocidas**. Esto no demuestra ausencia absoluta de protección.

Por tratarse de un CD con música en una pista independiente, una ISO que conserve únicamente los archivos no representaría el soporte completo. El formato de adquisición elegido fue **BIN/CUE**, con una descripción explícita de las pistas y su separación.

## Particularidad técnica: la transición entre datos y audio

Durante la caracterización se identificaron problemas de lectura en el entorno del LBA **22207**, previo al comienzo de la pista de audio. Las herramientas de diagnóstico detectaron un intervalo de **293 sectores** entre ese punto y el índice 01 de la pista de audio.

El descriptor CUE obtenido en la adquisición final documenta esta estructura:

```text
FILE "LOOMCD.BIN" BINARY
  TRACK 01 MODE1/2352
    INDEX 01 00:00:00
  TRACK 02 AUDIO
    PREGAP 00:02:00
    INDEX 00 04:56:07
    INDEX 01 04:58:00
```

Este descriptor representa **143 sectores entre índices 00 y 01** dentro de la imagen y **150 sectores de pregap declarados**. La posición del índice 01 resulta coherente con el TOC del soporte original. Esa coherencia no implica que se hayan capturado todos los datos físicos auxiliares.

## Hardware y método de adquisición

- Estación de preservación: **PCGA-MASTER-01**.
- Lector: **HL-DT-ST DVDRAM GTB0N**, firmware **FU03**, conectado por USB.
- Herramienta de la adquisición verificada: **ImgBurn 2.5.8.0**.
- Configuración determinante: `Read → PreGap Options → Detection Method: 2-1-3`, con `PreGap Snapping: 0 Frames`.
- Velocidad configurada: `MAX/MAX` (datos/audio).

Otros programas de preservación utilizados durante el diagnóstico no completaron una adquisición reconocible. La configuración indicada permitió superar el análisis del pregap y obtener dos lecturas completas. Se trata de un **procedimiento constatado para esta edición y unidad lectora**, no de una configuración universal para todos los CD mixtos.

## Adquisición y verificación

Se realizaron **dos adquisiciones independientes el 1 de noviembre de 2026**, con la misma unidad y parámetros. Ambas terminaron correctamente según sus registros y produjeron los mismos hashes SHA-256 para los dos archivos principales.

- Primera adquisición válida: **8 min 31 s**.
- Segunda adquisición válida: **8 min 30 s**.
- `LOOMCD.BIN`: **630.982.800 bytes**.
- `LOOMCD.CUE`: **157 bytes**.
- Comparación SHA-256: **coincidencia exacta** de ambas adquisiciones.

## Hashes de la representación preservada

### LOOMCD.BIN

```text
SHA-256  70BA458BAC6C7D656B188940493FCF57FD65930C0E0F70A683ED1D5129897BD4
```

### LOOMCD.CUE

```text
SHA-256  F25600C48612C0FBB0B957F0F84E02FB2E916EA41DBA90B45D7E4A71F64DF312
```

El conjunto principal se ha trasladado a la carpeta de custodia de PC Game Archive, sus hashes se han vuelto a comprobar y se ha generado un manifiesto `SHA256SUMS.txt`. Los archivos se han marcado como solo lectura para limitar alteraciones accidentales.

## Resultado y límites

**Resultado: adquisición BIN/CUE verificada por repetición coincidente.** La comprobación acredita que las dos lecturas produjeron los mismos bytes y que el descriptor representa las dos pistas conocidas.

La representación **no acredita por sí sola la captura integral de subcanales, offsets de audio ni otras características físicas** del soporte. El atributo de solo lectura tampoco equivale a un almacenamiento realmente inmutable. Estas limitaciones quedan abiertas en el expediente técnico interno.

La **compatibilidad y ejecución del juego en sistemas actuales todavía no han sido validadas** mediante el procedimiento de laboratorio de PC Game Archive. Esa documentación se publicará de manera independiente cuando existan pruebas reproducibles.

## Alcance

Este trabajo corresponde exclusivamente al ejemplar físico de **Loom — edición estadounidense Jewel Case en CD-ROM** custodiado por PC Game Archive. No deben extrapolarse estos resultados a las ediciones en disquetes, otras reediciones o diferentes prensados del juego.
