# Preservación de la pieza

Este registro documenta la adquisición digital del **CD-ROM de The Secret of Monkey Island, edición Jewel Case de 1992**, conservado por PC Game Archive. La representación digital del juego no se distribuye desde esta web.

**Estándar aplicado:** [PC Game Archive — Estándar de preservación digital v1.0](../estandar-preservacion-digital/).  
**Fecha de adquisición y verificación:** 02/11/2026.  
**Estado:** adquisición BIN/CUE verificada por dos lecturas con SHA-256 coincidentes, con limitaciones documentadas.

## Identificación y caracterización

- Pieza: **The Secret of Monkey Island — Jewel Case**, edición europea en CD-ROM de 1992, según la ficha del archivo.
- Soporte físico confirmado: **un CD-ROM**.
- Sesiones: **1**; pistas: **25**; pista 01 de datos `MODE1/2352` y pistas **02–25 de audio CD-DA**.
- Sistema de archivos de la pista de datos: **ISO9660** (ImgBurn); Windows identifica el volumen como `CDFS`.
- Volumen lógico de datos informado por Windows: **45.121.536 bytes**; este dato no incluye la totalidad del audio del soporte.
- TOC: **235.500 sectores**, lead-out en **LBA 235500** (`52:22:00`).
- Inspección física de códigos de fabricación y estado superficial: **no realizada**.
- Protección anticopia: **no evaluada mediante análisis específico**; no puede afirmarse su ausencia.

Por tratarse de un disco mixto con **24 pistas de audio**, una imagen ISO limitada a los archivos de datos no sería una representación adecuada de esta edición. Se seleccionó el formato **BIN/CUE** para describir las pistas, los índices y el audio.

## Descriptor CUE de esta edición: 25 pistas y pregaps

La caracterización del ejemplar de **The Secret of Monkey Island — Jewel Case** determinó una pista de datos y 24 pistas CD-DA. Los datos siguientes proceden del descriptor `Image.cue` remitido durante esta preservación:

```cue
FILE "Image.bin" BINARY
  TRACK 01 MODE1/2352
    INDEX 01 00:00:00
    REM TAOGAP 00:02:18
  TRACK 02 AUDIO
    PREGAP 00:02:00
    INDEX 01 04:55:57
  TRACK 03 AUDIO
    INDEX 00 06:55:62
    INDEX 01 06:58:17
  TRACK 04 AUDIO
    INDEX 00 09:04:02
    INDEX 01 09:06:57
```

El mismo descriptor continúa enumerando las pistas **05 a 25** y termina con:

```cue
  TRACK 24 AUDIO
    INDEX 00 47:20:67
    INDEX 01 47:23:02
  TRACK 25 AUDIO
    INDEX 00 49:38:57
    INDEX 01 49:41:02
```

Los valores mostrados proceden del descriptor CUE registrado durante esta adquisición. `REM TAOGAP 00:02:18` equivale a 168 sectores y `PREGAP 00:02:00` a 150 sectores. El BIN ocupa **553.148.064 bytes** (235.182 sectores de 2352 bytes), mientras que la TOC informa **235.500 sectores** (553.896.000 bytes a 2352 bytes por sector). La diferencia es **318 sectores, 747.936 bytes**, numéricamente igual a 168 + 150.

Esta equivalencia **no demuestra** que los 318 sectores se hayan leído físicamente ni acredita la preservación íntegra de subcanales, offsets o características auxiliares. Los `INDEX 00` y `INDEX 01` de las restantes pistas representan límites internos indicados por ImgBurn; no deben interpretarse como protección anticopia verificada.

## Hardware y método de adquisición

- Estación de preservación: **PCGA-MASTER-01**.
- Lector: **HL-DT-ST DVDRAM GTB0N**, firmware **FU03**, unidad `D:`, conectado por USB.
- Herramienta: **ImgBurn 2.5.8.0**, interfaz SPTI.
- Velocidad configurada: **MAX/MAX** (datos/audio); velocidad media informada **5,0x** y máxima observada **8,4x**.
- En **Tools → Settings → Read → PreGap Options** se mantuvieron los ajustes existentes, sin modificar `Detection Method` ni `PreGap Snapping`. Sus valores numéricos **no quedaron capturados** durante la sesión. El análisis de la pista 2 tardó en avanzar, pero continuó sin intervención.
- El log de ImgBurn identifica Windows 8 Professional x64; la ficha de la estación indica Windows Server 2019. **Esta discrepancia de identificación no se ha reconciliado.**

## Configuración de ImgBurn y procedimiento de lectura

El procedimiento documentado utiliza **ImgBurn 2.5.8.0** en el modo **Create image file from disc**, con la unidad `HL-DT-ST DVDRAM GTB0N FU03 (D:)` como origen. Se seleccionó como destino un fichero `Image.bin` con descriptor asociado `Image.cue`, manteniendo los dos componentes de cada adquisición en ubicaciones separadas para su comparación.

**Configuración de lectura registrada:**

- **Modo de operación:** `Create image file from disc`.
- **Herramienta e interfaz:** ImgBurn 2.5.8.0, SPTI.
- **Unidad de origen:** `D:` — HL-DT-ST DVDRAM GTB0N, firmware FU03.
- **Velocidad solicitada (datos/audio):** `MAX / MAX`, según el log.
- **Formato de los sectores leídos:** `MODE1/2352` para datos y `AUDIO/2352` para audio, según el log.
- **Opciones de pregap (`Tools → Settings → Read → PreGap Options`):** no se modificaron durante esta sesión.
- **`Detection Method`:** valor exacto no registrado.
- **`PreGap Snapping`:** valor exacto no registrado.
- **Opciones de tratamiento de errores:** no se documentaron cambios; los logs no muestran errores explícitos.


En el análisis previo a la adquisición, ImgBurn permaneció durante un intervalo en `Analysing Tracks… (Session 1, Track 2)`. La lectura avanzó sin modificar la pestaña `Read` ni aplicar ajustes correctivos. **No se debe reproducir como requisito un valor de `Detection Method` o de `PreGap Snapping` que no haya sido comprobado.**

El proceso completó la lectura de la sesión con **25 pistas** y produjo un BIN y un CUE. Se realizó una segunda adquisición, manteniendo el mismo lector y las opciones de lectura, tras separar los resultados de la primera. Se calcularon hashes SHA-256 para ambos pares y se contrastó su coincidencia. La reproducción exacta de opciones no capturadas requeriría documentarlas expresamente en una nueva sesión; no se deducen de este registro.

## Adquisición y verificación

Se realizaron **dos adquisiciones declaradas independientes el 2 de noviembre de 2026**, con la misma unidad y configuración. Ambas presentaron `Operation Successfully Completed!` y generaron archivos BIN/CUE cuyos **SHA-256 coinciden exactamente**.

- Primera adquisición: **9 min 02 s**, sin errores explícitos en el log entregado.
- Segunda adquisición: el log aportado declara **9 min 02 s** y finalización correcta.
- `Image.bin`: **553.148.064 bytes**.
- `Image.cue`: **1.630 bytes**.
- Se observan inconsistencias textuales en el segundo log (numeración de pistas, límites LBA y nombre del archivo de gráficas). **La incidencia se ha aceptado expresamente sin reconciliar el log original**. La coincidencia de hashes no explica esas diferencias.

## Hashes de la representación preservada

### Image.bin

```text
SHA-256  88A546BF6391FA0AE066FBEC5A84F810BBBE363AF3C3FC73B7C24EBF01B982D3
```

### Image.cue

```text
SHA-256  1330620E8A913A3BA9D9DF90C96EBFC2C6B86D1C5A9CEFBEE060B429947A435F
```

Se generó y comprobó el manifiesto **`SHA256SUMS.txt`**. Los dos archivos de imagen y el manifiesto se encuentran en la ubicación de custodia confirmada por el responsable, con el atributo de **solo lectura** activado. Esto protege frente a algunas modificaciones accidentales, pero no acredita inmutabilidad WORM ni copias de seguridad independientes verificadas.

## Resultado y límites

**Resultado: representación BIN/CUE reproducible mediante dos adquisiciones con SHA-256 coincidentes**, con incidencia documental aceptada en el segundo log.

El procedimiento no acredita una reproducción física integral del disco: **subcanales, offsets de audio, cobertura exhaustiva de pregaps y protecciones no han sido verificados**. Tampoco se ha aportado evidencia específica de una copia de seguridad independiente comprobada.

Este trabajo se limita a **preservación digital**. No se han realizado pruebas de instalación, ejecución o compatibilidad; por ello **no se declara ningún resultado funcional**.

## Alcance

La evidencia corresponde al ejemplar físico de **The Secret of Monkey Island — edición Jewel Case CD-ROM** custodiado por PC Game Archive. No debe extrapolarse a otros prensados, soportes o ediciones del juego.
