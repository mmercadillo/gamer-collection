# Registro de preservación — Panzer Commander: WWII Tank Simulator

**Estado:** Preservación verificada · compatibilidad Windows 10 verificada  
**Ficha PCGA:** #000214  
**URL:** `juegos/panzer-commander-wwii-tank-simulator-bigbox/`  
**Fecha de adquisición/verificación:** 07/10/2026  
**Estándar aplicado:** PC Game Archive — Estándar de preservación digital v1.0

## 1. Identificación

- Título: Panzer Commander: WWII Tank Simulator
- Edición / variante: edición española Big Box
- Mercado: España
- Idioma: Español
- Distribución: Strategic Simulations, Inc. / Mindscape / Proein Software
- Identificador interno: 000214
- Soporte nº / total: 1 / 1 CD-ROM
- Etiqueta de volumen: `Pzc_v1_0`
- Versión identificada por la herramienta: 1.0
- Sistema de ficheros: CDFS
- Tamaño lógico visible: 615.131.136 bytes
- Matriz / ring code: no transcrito en este registro

## 2. Estado físico previo

- Estado general: no clasificado mediante escala específica en este trabajo.
- Suciedad / arañazos / daños visibles: no documentados de forma individual.
- Intervenciones previas conocidas: no documentadas.
- Resultado operativo: el soporte pudo adquirirse sin Error Count ni C2 Error Count.

## 3. Caracterización técnica

- Tipo de soporte: CD-ROM
- Pistas: 1
- Tipo de pista: MODE1/2352
- Audio: no se detectan pistas de audio adicionales en el CUE obtenido
- BIN: 706.801.872 bytes
- Protección: no detectada por el análisis realizado
- `SETUP.EXE`: identificado como Wise Installation Wizard Module
- Error Count: 0
- C2 Error Count: 0
- Fully Matching IDs: 32155

Cuesheet:

```text
FILE "Pzc_v1_0.bin" BINARY
  TRACK 01 MODE1/2352
    INDEX 01 00:00:00
```

## 4. Decisión de adquisición

- Procedimiento: adquisición raw mediante Redumper con salida BIN/CUE y evidencias auxiliares.
- Hardware real utilizado: TSSTcorp DVD-ROM SH-116AB.
- Firmware: FT01.
- Conexión: SATA interna.
- Frontend: Media Preservation Frontend 3.10.0.
- Frontend build: `3.10.0-1449d5f3f6071eb7c3ebce4980533e781d6b3133`.
- Herramienta: Redumper build b749.
- Velocidad: 8x.
- Reintentos: 20.
- Write Offset: -6.
- Parámetros registrados: `disc --skeleton --drive=F:\ --speed=8 --retries=20 --image-path=ISO\Pzc_v1_0 --image-name=Pzc_v1_0`.

Esta adquisición es anterior a la formalización de PCGA-MASTER-01. Por trazabilidad no se atribuye retrospectivamente a la unidad óptica de la estación de referencia actual.

## 5. Adquisiciones

Se realizaron dos adquisiciones independientes del soporte con el mismo método. Los ficheros BIN y CUE obtenidos coincidieron por SHA-256.

Metadatos Redumper del BIN:

- CRC32: `e882941e`
- MD5: `fa602da09dc109128832380bf3a3efec`
- SHA-1: `7244205ddc4d3068d49cb9cafcd74edec231a127`

No se registraron errores de lectura ni errores C2 en la adquisición considerada válida.

## 6. Verificación

SHA-256 PC Game Archive:

- BIN: `E4E57AD97857B91AAC38121B19BA0DF22B54547AC4BBD8F99C348BFFD4FFC688`
- CUE: `9A24EDC5DC96A0BD6D69EE9D00953425A71BB64807CFD4898AB76F174118462E`

**Resultado:** adquisición 01 y adquisición 02 coincidentes para BIN y CUE.

## 7. Máster de preservación

- Estado: `verificada`
- Representación principal: BIN/CUE
- Evidencias asociadas: logs, TOC/full TOC, hashes, skeleton/subcode/state y metadatos generados por MPF/Redumper
- Máster: inmutable; no se utiliza directamente en pruebas de compatibilidad
- Segunda adquisición: conservada como evidencia independiente de repetibilidad

## 8. Copia de trabajo

Se creó una copia de trabajo derivada del máster. Antes de utilizarla en PCGA-LAB-01 se recalcularon los SHA-256 del BIN y del CUE y ambos coincidieron con el máster de preservación.

## 9. Definition of Done de preservación

- [x] Versión del estándar aplicada registrada.
- [x] Edición identificada.
- [x] Soporte caracterizado.
- [x] Protección/características especiales evaluadas.
- [x] Método de adquisición documentado.
- [x] Hardware, firmware, software y parámetros registrados.
- [x] Logs y evidencias auxiliares conservados.
- [x] Errores revisados.
- [x] SHA-256 calculados.
- [x] Dos adquisiciones independientes coincidentes.
- [x] Máster separado de la copia de trabajo.
- [x] Copia de trabajo verificada antes de las pruebas de compatibilidad.

## 10. Compatibilidad asociada

La copia de trabajo verificada se montó con WinCDEmu 4.1 y se validó posteriormente en PCGA-LAB-01 sobre Windows 10 Pro 22H2 x64. El instalador Win16 se ejecutó con otvdm 0.9.0; DirectX 5 no se instaló. La ejecución 3D quedó estable con DDrawCompat 0.7.2 y `FpsLimiter = flipend(30)`.

El detalle se conserva en `registros_compatibilidad/panzer-commander-wwii-tank-simulator-bigbox-windows-10.md`.
