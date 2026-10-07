# Registro de preservación — A Sangre Fría

**Estado:** Preservación verificada · compatibilidad Windows 10 verificada  
**Ficha PCGA:** #000216  
**URL:** `juegos/a-sangre-fria-bigbox/`  
**Fecha de adquisición/verificación:** 06–07/10/2026  
**Estándar aplicado:** PC Game Archive — Estándar de preservación digital v1.0

## 1. Identificación

- Título: A Sangre Fría
- Edición / variante: edición española Big Box
- Mercado: España
- Idioma: Español
- Distribución: Ubisoft
- EAN: 3307212296885
- Identificador interno: 000216
- Soportes físicos: 3 CD-ROM
- Identificación impresa: `CD1 SPAIN`, `CD2 SPAIN`, `CD3 SPAIN`
- Etiquetas de volumen: `ICB_CD1`, `ICB_CD2`, `ICB_CD3`
- Matriz / ring codes: no transcritos en este laboratorio

## 2. Estado físico previo

- Estado general: no clasificado mediante escala específica.
- Suciedad / arañazos / daños visibles: no documentados de forma individual en este laboratorio.
- Intervenciones previas conocidas: no documentadas.
- Resultado operativo: los tres soportes pudieron adquirirse y verificarse sin errores C2 ni SCSI en las adquisiciones consideradas válidas.

## 3. Caracterización técnica por soporte

| Soporte | Volumen | Pistas | Tipo | Sectores | BIN | Protección | Errores |
|---|---|---:|---|---:|---:|---|---|
| CD1 | `ICB_CD1` | 1 | MODE2/2352 | 330.458 | 777.237.216 bytes | no detectada | Redump 0 / SCSI 0 / C2 0 |
| CD2 | `ICB_CD2` | 1 | MODE2/2352 | 251.952 | 592.591.104 bytes | no detectada | Redump 0 / SCSI 0 / C2 0 |
| CD3 | `ICB_CD3` | 1 | MODE2/2352 | 281.325 | 661.676.400 bytes | no detectada | Redump 0 / SCSI 0 / C2 0 |

Cada disco se caracterizó de forma independiente. En los tres casos el CUE final contiene una única pista de datos `TRACK 01 MODE2/2352`.

La indicación de protección se registra como **no detectada** por el análisis efectuado, no como afirmación absoluta de ausencia.

## 4. Hardware y software de adquisición

- Unidad óptica: HL-DT-ST DVDRAM GTB0N
- Firmware: FU03
- Perfil: CD-ROM
- Frontend: Media Preservation Frontend 3.10.0
- Herramienta: Redumper build b749
- Reintentos: 20
- Write Offset informado: -102
- CD1 — adquisiciones válidas: 4x
- CD2 — adquisiciones: 12x
- CD3 — adquisiciones: 12x
- Advertencia conservada en logs: la unidad no figura en la base de datos de Redumper y se usa configuración genérica.
- Advertencia conservada en logs: datos de subcanal no disponibles; Redumper genera entradas TOC index 0.

## 5. Incidencia previa en CD1

Antes de las dos adquisiciones válidas del CD1 se realizó un intento a 1x que terminó con `forced stop` en LBA 147724. Ese intento no se utilizó como adquisición de preservación y se conserva únicamente como trazabilidad interna. Posteriormente se realizaron dos adquisiciones completas a 4x que coincidieron exactamente.

## 6. Adquisiciones y SHA-256

### CD1 — `ICB_CD1`

- BIN SHA-256: `A2E6389E84A0DB8987436313474CD63FBB7BD6840B846696B6168B61C3B75F3F`
- CUE SHA-256: `DD098198B8E26D1BA33916A29CEBB8750920C8A25DCC51E15A703D3532FD187E`
- Redumper: CRC32 `5321222c`, MD5 `a21baf115e9b5fb069f8b9c4f1b5c6bd`, SHA-1 `7fbfa17276064e9b9f4444230358698ca209d265`
- Verificación: adquisición 01 y 02 coincidentes para BIN y CUE.

### CD2 — `ICB_CD2`

- BIN SHA-256: `D7885BE96FBF94A1CBFDC45497FDBAD62E74F8944E0B82470ED7F23B6646C2BA`
- CUE SHA-256: `DDA6BAE46D3B7B182A67AEFB376848146302B4C338A8CA176AAE3D2E95FF90BF`
- Redumper: CRC32 `2f242de6`, MD5 `f091ed003b55f3f562ec340987cf1a02`, SHA-1 `0b07de1b62182c40cf50bd654ce2f81e15a6e8fb`
- Verificación: adquisición 01 y 02 coincidentes para BIN y CUE.

### CD3 — `ICB_CD3`

- BIN SHA-256: `14CCBC39339FDF2290AA07FFF4F7FBC3A8C08911D0D263288237B450DF062512`
- CUE SHA-256: `FF63F8D352C5D22041254E9A5153761A2021A1E3F7930AA87B07681F67B98A12`
- Redumper: CRC32 `8b00d15d`, MD5 `243ad9efadc59870b79547f9f7816f25`, SHA-1 `0573e0c54beaed679e202156253885d61b276d95`
- Verificación: adquisición 01 y 02 coincidentes para BIN y CUE.

## 7. Verificación

Los tres soportes se verificaron mediante **dos adquisiciones independientes coincidentes**. Los SHA-256 de BIN y CUE de cada segunda adquisición coinciden exactamente con los de su primera adquisición válida.

**Resultado global:** los 3/3 soportes requeridos están preservados y verificados.

## 8. Máster de preservación

- Estado: `verificada`
- Representación principal por soporte: BIN/CUE
- Evidencias asociadas: logs y metadatos generados por MPF/Redumper
- Cada soporte dispone de su `SHA256SUMS.txt`.
- Los másteres se mantienen separados de las copias de trabajo y no se utilizan para instalación o pruebas.
- Copias de seguridad: no documentadas en este registro.

## 9. Copia de trabajo

Se creó una copia de trabajo completa con los seis ficheros BIN/CUE. Antes de utilizarla en la máquina de pruebas se recalcularon los seis SHA-256 y todos coincidieron con los másteres de origen.

## 10. Corrección documental detectada

El catálogo indicaba previamente `2 CD-ROM`. La evidencia física confirma **3 CD-ROM** (`CD1 SPAIN`, `CD2 SPAIN`, `CD3 SPAIN`), por lo que `juegos.json` se corrige a `3 CD-ROM`.

## 11. Definition of Done de preservación

- [x] Versión del estándar registrada.
- [x] Edición exacta identificada.
- [x] Tres soportes identificados individualmente.
- [x] Cada soporte caracterizado de forma independiente.
- [x] Protecciones/características especiales evaluadas.
- [x] Método de adquisición documentado por soporte.
- [x] Hardware, firmware, software, versiones y parámetros registrados.
- [x] Logs conservados.
- [x] Errores e incidencias revisados.
- [x] SHA-256 calculados.
- [x] Dos adquisiciones coincidentes por soporte.
- [x] Másteres constituidos y separados de la copia de trabajo.
- [x] Copia de trabajo completa verificada contra los másteres.

## 12. Compatibilidad asociada

La copia de trabajo se montó con **WinCDEmu 4.1** y se validó en Windows 10 Pro build 19045. La instalación utiliza los tres discos, solicita correctamente los cambios CD1 → CD2 → CD3 y, una vez instalada, requiere el CD1 montado para arrancar. El resultado completo se conserva en `registros_compatibilidad/a-sangre-fria-bigbox-windows-10.md`.
