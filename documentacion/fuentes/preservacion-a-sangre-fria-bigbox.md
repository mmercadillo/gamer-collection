# Preservación de la pieza

Este registro documenta la preservación digital de los **tres CD-ROM de A Sangre Fría, edición española Big Box**, correspondiente a la ficha **#000216** de PC Game Archive.

La preservación se ha realizado sobre los tres soportes físicos conservados por el archivo. Los másteres digitales no se distribuyen desde PC Game Archive.

**Estándar aplicado:** [PC Game Archive — Estándar de preservación digital v1.0](../estandar-preservacion-digital/).  
**Fecha de adquisición y verificación:** 06–07/10/2026.  
**Operador:** PC Game Archive.

## Identificación de los soportes

La edición contiene **3 CD-ROM**, identificados físicamente como `CD1 SPAIN`, `CD2 SPAIN` y `CD3 SPAIN`. Esta comprobación permitió corregir el dato histórico del catálogo, que indicaba dos discos.

| Soporte | Etiqueta de volumen | Estructura | Sectores | BIN |
|---|---|---|---:|---:|
| CD1 | `ICB_CD1` | 1 pista MODE2/2352 | 330.458 | 777.237.216 bytes |
| CD2 | `ICB_CD2` | 1 pista MODE2/2352 | 251.952 | 592.591.104 bytes |
| CD3 | `ICB_CD3` | 1 pista MODE2/2352 | 281.325 | 661.676.400 bytes |

El análisis realizado con MPF/Redumper **no detectó protección de copia** en ninguno de los tres soportes. Esta descripción se limita al resultado obtenido sobre esta pieza concreta.

## Hardware y herramientas

- Unidad óptica: **HL-DT-ST DVDRAM GTB0N**.
- Firmware: **FU03**.
- Media Preservation Frontend: **MPF 3.10.0**.
- Adquisición: **Redumper build b749**.
- Reintentos configurados: **20**.
- Velocidad: **4x en CD1** y **12x en CD2/CD3** para las adquisiciones válidas.

En los tres discos las adquisiciones válidas terminaron con **0 errores Redump, 0 muestras SCSI y 0 muestras C2**.

## Verificación por repetición

Cada CD se adquirió dos veces de forma independiente. Después se calcularon SHA-256 de los BIN y CUE obtenidos. En los tres soportes, la segunda adquisición produjo exactamente los mismos SHA-256 que la primera adquisición válida.

### CD1

```text
ICB_CD1.bin  A2E6389E84A0DB8987436313474CD63FBB7BD6840B846696B6168B61C3B75F3F
ICB_CD1.cue  DD098198B8E26D1BA33916A29CEBB8750920C8A25DCC51E15A703D3532FD187E
```

### CD2

```text
ICB_CD2.bin  D7885BE96FBF94A1CBFDC45497FDBAD62E74F8944E0B82470ED7F23B6646C2BA
ICB_CD2.cue  DDA6BAE46D3B7B182A67AEFB376848146302B4C338A8CA176AAE3D2E95FF90BF
```

### CD3

```text
ICB_CD3.bin  14CCBC39339FDF2290AA07FFF4F7FBC3A8C08911D0D263288237B450DF062512
ICB_CD3.cue  FF63F8D352C5D22041254E9A5153761A2021A1E3F7930AA87B07681F67B98A12
```

## Resultado

**Estado de preservación: verificada para los 3/3 soportes.**

Los másteres se mantienen separados de cualquier copia utilizada para instalación o pruebas. Antes de iniciar la validación de compatibilidad se creó una copia de trabajo de los seis ficheros BIN/CUE y se comprobó que sus SHA-256 coincidían con los másteres.

## Incidencias documentadas

Durante el trabajo con CD1 hubo un intento previo a 1x que terminó de forma forzada en un sector concreto. Ese intento se descartó como adquisición de preservación. Las dos adquisiciones posteriores consideradas válidas, realizadas a 4x, finalizaron correctamente y coincidieron entre sí.

## Alcance

Este resultado corresponde exclusivamente a los tres discos de la edición física concreta conservada por PC Game Archive. No debe extrapolarse automáticamente a otros prensados, países o reediciones.
