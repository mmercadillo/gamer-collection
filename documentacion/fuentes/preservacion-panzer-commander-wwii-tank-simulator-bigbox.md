# Preservación de la pieza

Este registro documenta la adquisición digital de preservación del **CD-ROM de Panzer Commander: WWII Tank Simulator, edición española Big Box**, correspondiente a la ficha **#000214** de PC Game Archive.

La preservación se realizó sobre el soporte físico conservado por el archivo. El máster digital no se distribuye desde PC Game Archive.

**Estándar aplicado:** [PC Game Archive — Estándar de preservación digital v1.0](../estandar-preservacion-digital/).  
**Fecha de adquisición y verificación:** 07/10/2026.  
**Operador:** PC Game Archive.

> Esta adquisición se realizó antes de la formalización de la estación fija PCGA-MASTER-01. Por trazabilidad, este registro conserva el hardware y los parámetros que se utilizaron realmente para esta pieza; no se atribuye retrospectivamente la adquisición al entorno de referencia actual.

## Identificación del soporte

- Título: **Panzer Commander: WWII Tank Simulator**.
- Edición: española Big Box.
- Lanzamiento: original, 1998.
- Plataforma: Windows 95.
- Soporte: 1 CD-ROM.
- Etiqueta de volumen: `Pzc_v1_0`.
- Sistema de ficheros observado en Windows: CDFS.
- Tamaño lógico visible: **615.131.136 bytes**.
- Versión identificada por la herramienta de adquisición: **1.0**.

## Caracterización técnica

La estructura obtenida contiene **una única pista de datos**:

```text
FILE "Pzc_v1_0.bin" BINARY
  TRACK 01 MODE1/2352
    INDEX 01 00:00:00
```

El fichero BIN resultante tiene un tamaño de **706.801.872 bytes**.

El análisis realizado con Media Preservation Frontend / Redumper informó **0 errores de lectura** y **0 errores C2**. El escaneo no detectó una protección de copia. Esta descripción se limita al resultado obtenido sobre esta pieza concreta y no debe interpretarse como una afirmación general sobre todas las ediciones o prensados del juego.

El análisis de ficheros identificó además `SETUP.EXE` como **Wise Installation Wizard Module**. Esta identificación describe el instalador y no constituye por sí misma una protección de copia.

## Hardware utilizado

- Unidad óptica: **TSSTcorp DVD-ROM SH-116AB**.
- Firmware: **FT01**.
- Conexión: **SATA interna**.
- Tipo de medio informado por la herramienta: **CD-ROM**.

## Software y herramientas utilizadas

- **Media Preservation Frontend (MPF) 3.10.0**: frontend utilizado para la adquisición y conservación de evidencias auxiliares.
- **Redumper build b749**: herramienta utilizada para la adquisición raw del CD-ROM.
- **Windows PowerShell**: utilizado para la verificación independiente mediante SHA-256.

La versión completa registrada por MPF fue:

```text
3.10.0-1449d5f3f6071eb7c3ebce4980533e781d6b3133
```

## Parámetros de adquisición

- Programa: **Redumper build b749**.
- Velocidad de lectura: **8x**.
- Reintentos configurados: **20**.
- Write Offset informado: **-6**.
- Error Count: **0**.
- C2 Error Count: **0**.
- Fully Matching IDs informado por la herramienta: **32155**.

Parámetros relevantes registrados por MPF/Redumper:

```text
disc --skeleton --speed=8 --retries=20
```

Las rutas locales de unidad y salida no se publican porque no forman parte de la identificación técnica de la pieza ni son necesarias para reproducir el procedimiento.

## Procedimiento aplicado

1. Se identificó el CD-ROM físico y se comprobó el volumen `Pzc_v1_0`.
2. Se caracterizó el soporte antes de constituir el máster.
3. Se realizó el análisis de protección y de los ficheros relevantes del disco.
4. Se efectuó una primera adquisición raw con Redumper a **8x** y **20 reintentos** configurados.
5. Se conservaron el BIN/CUE y las evidencias auxiliares generadas por MPF/Redumper.
6. PC Game Archive calculó SHA-256 independientes para BIN y CUE.
7. Se efectuó una **segunda adquisición independiente** del mismo soporte con el mismo método.
8. Se recalcularon los SHA-256 de los ficheros principales.
9. BIN y CUE de ambas adquisiciones coincidieron exactamente, por lo que el resultado quedó verificado por repetición.
10. Se constituyó el máster de preservación y, posteriormente, una copia de trabajo separada para las pruebas de compatibilidad.

## Método de verificación

La verificación se basó en **dos adquisiciones independientes coincidentes**. Los SHA-256 del BIN y del CUE obtenidos en la segunda adquisición son idénticos a los de la primera.

La copia de trabajo utilizada más tarde en el laboratorio de compatibilidad se verificó de nuevo contra estos mismos SHA-256 antes de montarla y utilizarla.

## Hashes del máster

### Pzc_v1_0.bin

```text
SHA-256  E4E57AD97857B91AAC38121B19BA0DF22B54547AC4BBD8F99C348BFFD4FFC688
SHA-1    7244205DDC4D3068D49CB9CAFCD74EDEC231A127
MD5      FA602DA09DC109128832380BF3A3EFEC
CRC32    E882941E
```

### Pzc_v1_0.cue

```text
SHA-256  9A24EDC5DC96A0BD6D69EE9D00953425A71BB64807CFD4898AB76F174118462E
```

## Resultado

**Estado de preservación: verificada.**

La representación principal de preservación está formada por el BIN/CUE verificado y por los logs y metadatos auxiliares generados durante la adquisición. La segunda adquisición se conserva como evidencia independiente de repetibilidad.

El máster permanece separado de cualquier copia utilizada para instalación o pruebas. Para el trabajo de compatibilidad se empleó exclusivamente una **copia de trabajo derivada y verificada**.

## Compatibilidad asociada

La ejecución de esta edición se ha validado posteriormente en Windows 10 x64. El instalador Win16 requiere **otvdm 0.9.0** y la ejecución 3D se estabiliza con **DDrawCompat 0.7.2** y:

```ini
FpsLimiter = flipend(30)
```

El procedimiento completo para jugar está documentado en la [guía de ejecución de Panzer Commander en Windows 10](../../guias/panzer-commander-windows-10/).

## Alcance de este registro

Este documento describe exclusivamente la **edición física concreta conservada por PC Game Archive**. Los hashes, resultados de lectura y comportamiento observado no deben extrapolarse automáticamente a otros países, reediciones, revisiones del ejecutable o prensados del mismo juego.
