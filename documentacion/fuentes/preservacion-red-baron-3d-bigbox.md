# Preservación de la pieza

Este registro documenta la adquisición digital de preservación del **CD-ROM de Red Baron 3-D, edición española Big Box**, correspondiente a la ficha **#000215** de PC Game Archive.

La preservación se ha realizado sobre el soporte físico conservado por el archivo. El contenido del máster no se distribuye desde PC Game Archive.

**Estándar aplicado:** [PC Game Archive — Estándar de preservación digital v1.0](../estandar-preservacion-digital/).  
**Fecha de adquisición y verificación:** 05/10/2026.  
**Operador:** PC Game Archive.

## Identificación del soporte

- Título: **Red Baron 3-D**.
- Edición: española Big Box.
- Plataforma indicada en el disco: PC Windows 95/98.
- Idioma indicado en el disco: castellano.
- Soporte: CD-ROM.
- Etiqueta de volumen: `REDBARON_3D`.
- Sistema de ficheros observado en Windows: CDFS.
- Tamaño lógico visible: 718.379.008 bytes.
- Inscripción legible en el anillo interior: `BELIEVE IN CD`.
- Otros códigos del anillo: presentes, pero no transcritos al no disponer de una lectura fotográfica suficientemente fiable.

## Caracterización técnica

La estructura obtenida durante la adquisición contiene **una única pista de datos**, sin pistas de audio adicionales:

```text
FILE "REDBARON_3D.bin" BINARY
  TRACK 01 MODE1/2352
    INDEX 01 00:00:00
```

El fichero BIN resultante tiene un tamaño de **825.018.096 bytes**.

El análisis de protección realizado con Media Preservation Frontend no detectó una protección de copia. Esta afirmación describe el resultado del análisis efectuado sobre esta pieza; no pretende establecer que toda edición de Red Baron 3-D carezca necesariamente de mecanismos de protección.

## Hardware utilizado

- Carcasa externa: XD008.
- Unidad óptica identificada por el sistema: **HL-DT-ST DVDRAM GTB0N**.
- Firmware: **FU03**.
- Conexión utilizada: USB.

## Software y herramientas utilizadas

- **Media Preservation Frontend (MPF) 3.10.0**: frontend empleado para caracterización, escaneo de protección, ejecución y conservación de metadatos de la adquisición.
- **Redumper build b749**: herramienta utilizada para la adquisición raw del CD-ROM.
- **Windows PowerShell**: utilizado para caracterización básica del volumen y cálculo independiente de SHA-256.

Comandos empleados para la comprobación del volumen y la unidad:

```text
Get-Volume -DriveLetter D | Format-List DriveLetter,FileSystemLabel,FileSystem,Size,SizeRemaining,HealthStatus
Get-CimInstance Win32_CDROMDrive | Format-List Drive,Name,Manufacturer,MediaType,PNPDeviceID
```

Comandos utilizados para calcular los SHA-256 propios de PC Game Archive:

```text
Get-FileHash .\REDBARON_3D.bin -Algorithm SHA256
Get-FileHash .\REDBARON_3D.cue -Algorithm SHA256
```

## Parámetros de adquisición

- Programa: **Redumper build b749**.
- Velocidad de lectura: **1x**.
- Reintentos configurados: **20**.
- Unidad lógica utilizada: `D:\`.
- Parámetros registrados por MPF/Redumper: `disc --skeleton --drive=D:\ --speed=1 --retries=20 ...`.
- Write Offset informado por la herramienta: **-102**.
- C2 Error Count: **0**.
- Error Count informado: **0**.

## Procedimiento aplicado

1. Se identificó la pieza física y se documentó el soporte.
2. Windows confirmó la unidad óptica, la etiqueta `REDBARON_3D`, el sistema CDFS y el tamaño lógico visible.
3. MPF realizó el escaneo de protección; no detectó una protección de copia.
4. Se efectuó una primera adquisición con Redumper a **1x** y **20 reintentos** configurados.
5. Se conservaron BIN/CUE, log, SCRAM y los metadatos auxiliares generados por MPF/Redumper.
6. PC Game Archive calculó SHA-256 independientes para BIN y CUE.
7. Se efectuó una segunda adquisición independiente con la misma unidad, software y parámetros.
8. Se calcularon de nuevo los SHA-256 y se comprobó coincidencia exacta entre ambas adquisiciones.
9. La primera adquisición quedó designada como máster de preservación; la segunda se conserva como evidencia independiente de repetibilidad.

## Método de verificación

Se realizaron **dos adquisiciones independientes** del mismo soporte, con la misma unidad, herramienta y parámetros. Los ficheros principales obtenidos en ambas lecturas produjeron los mismos hashes SHA-256.

Este resultado permite considerar la adquisición **verificada por repetición coincidente** dentro del estándar de PC Game Archive.

## Hashes del máster

### REDBARON_3D.bin

```text
SHA-256  1E354950083B85F76623CD5BED2F061C90833EB1431ED2BBBD288BEB125BA66B
SHA-1    02E32BE85C12F12D49C7B7F38B8C771F7084442D
MD5      83B2EDFB3400166CA78D41835C4CC298
CRC32    0E92F1EE
```

### REDBARON_3D.cue

```text
SHA-256  CB27C9E074A1BC07DFBF5A967C5641F216CBB2E166D460DF9418EC78BED501F6
```

## Resultado

**Estado de preservación: verificada.**

La representación de preservación utilizada para esta pieza está formada, como mínimo, por el BIN/CUE generado y por los logs y metadatos de adquisición conservados. La segunda adquisición se mantiene como evidencia independiente de verificación.

No se ha creado todavía la guía de ejecución en sistemas actuales. Esa fase se realizará sobre una **copia de trabajo derivada del máster**, sin modificar el conjunto de preservación verificado.

## Alcance de este registro

Este documento describe exclusivamente la **edición física concreta conservada por PC Game Archive**. Los resultados no deben extrapolarse automáticamente a otras ediciones, países, reediciones o prensados del mismo juego.
