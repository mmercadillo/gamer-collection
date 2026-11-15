# Preservación del CD-ROM

Este documento recoge cómo obtuvimos la imagen del CD-ROM de la edición española Big Box de **Lode Runner: The Legend Returns** conservada en PC Game Archive (ficha #000250). La adquisición se documentó con el [estándar de preservación digital](../estandar-preservacion-digital/) v1.0 como referencia. El nombre del gráfico de lectura sitúa la operación el **14 de noviembre de 2026**.

## Un CD con datos y 32 pistas de audio

ImgBurn identificó el volumen `LODE_RUNNER_CD`, con sistema de archivos ISO 9660, una sesión y 33 pistas. La primera es de datos (`MODE1/2352`) y las otras 32 son de audio CD-DA (`AUDIO/2352`). Para conservar ambas partes usamos **BIN/CUE**. El BIN contiene los sectores de datos y audio. El CUE describe cómo se organizan las pistas y sus índices.

## Cómo hicimos la imagen

1. Usamos ImgBurn en modo de lectura con el CD original en la unidad USB `HL-DT-ST DVDRAM GTB0N`, firmware `FU03`.
2. En `Tools → Settings → Read → PreGap Options` utilizamos `Detection Method: 2-1-3`. Solicitamos una velocidad de `4x / 4x` para datos y audio. ImgBurn anunció `10x` como velocidad efectiva y registró una media de `5,2x` y un máximo observado de `8,5x`.
3. La lectura produjo `LODE_RUNNER_CD.BIN` y `LODE_RUNNER_CD.CUE`. ImgBurn registró `Operation Successfully Completed!` en `00:08:55`, sin avisos, errores ni reintentos en el log disponible.
4. Contrastamos el número y los tipos de pista del CUE con el log, comprobamos el tamaño de ambos archivos y calculamos sus SHA-256.

La versión exacta de ImgBurn y el valor de `PreGap Snapping` quedaron sin registrar en la evidencia disponible.

## El pregap de la primera pista de audio

```cue
FILE "LODE_RUNNER_CD.BIN" BINARY
  TRACK 01 MODE1/2352
    INDEX 01 00:00:00
  TRACK 02 AUDIO
    PREGAP 00:02:00
    INDEX 00 01:53:00
    INDEX 01 01:54:00
```

El CUE declara dos segundos de pregap, equivalentes a 150 sectores. ImgBurn informa de 237.436 sectores para el medio y el BIN mide **558.096.672 bytes**, equivalentes a 237.286 sectores de 2352 bytes. La diferencia de 150 sectores es coherente con ese pregap descrito en el CUE. También se observaron diferencias entre algunos índices y los comienzos de los rangos de lectura del log. Su explicación queda pendiente de una comparación con una TOC obtenida independientemente.

## Hashes de la adquisición

- `LODE_RUNNER_CD.BIN` · 558.096.672 bytes · SHA-256 `458d988aad773a130c38b312d2be51278a66c49c484278de71bbf45dd94a0c62`
- `LODE_RUNNER_CD.CUE` · 1.735 bytes · SHA-256 `3252e3a21509d8e02c31e7bd4e1b82d4f1f05a02517169cd65604d6557d3fba0`

Se documentó **una única adquisición**, con revisión del log, contraste de estructura y hashes de referencia. La reproducibilidad entre lecturas, los subcanales, los offsets de audio y la protección anticopia quedan sin evaluar. La instalación, el arranque, el audio en ejecución y la jugabilidad quedan para las pruebas de compatibilidad. PC Game Archive publica este procedimiento y sus resultados. La imagen del juego se conserva para uso interno.
