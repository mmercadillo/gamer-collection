# PCGA-MASTER-01 — Estación de preservación

**Proyecto:** PC Game Archive  
**Identificador público del entorno:** PCGA-MASTER-01  
**Última caracterización:** 18/10/2026

## Función

PCGA-MASTER-01 es la estación de referencia utilizada por PC Game Archive para:

- caracterización de soportes físicos;
- adquisición digital;
- verificación de adquisiciones;
- cálculo de hashes;
- constitución de másteres de preservación;
- conservación de los másteres y de su evidencia técnica asociada.

Los másteres no se utilizan directamente para instalación, parcheado o pruebas de compatibilidad. Las pruebas se realizan sobre copias de trabajo verificadas en [PCGA-LAB-01](/documentacion/laboratorio/pcga-lab-01/).

## Metodología asociada

Este entorno aplica el [Estándar de preservación digital de PC Game Archive](/documentacion/preservacion/estandar-preservacion-digital/) y, para soportes ópticos, el procedimiento de [Caracterización previa de soportes ópticos](/documentacion/preservacion/caracterizacion-soportes-opticos/).

La ficha del entorno no sustituye la evidencia específica registrada para cada pieza: cada preservación conserva el hardware, firmware, herramienta, versión, parámetros, velocidad, reintentos, logs y resultados realmente utilizados.

## Hardware de referencia

- **Equipo:** HP ProLiant DL360e Gen8.
- **Sistema operativo:** Windows Server 2019 Standard x64.
- **Build:** 17763.9376.
- **BIOS:** HP P73.
- **CPU:** 2 × Intel Xeon E5-2430L v2 @ 2.40 GHz.
- **Núcleos / hilos:** 12 núcleos / 24 hilos en total.
- **Memoria:** ~384 GiB.

## Unidad óptica de preservación

- **Modelo:** HL-DT-ST DVDRAM GTB0N.
- **Tipo:** DVD Writer.
- **Firmware:** FU03.
- **Conexión observada por el sistema:** USB.

Esta unidad constituye el lector óptico de referencia de PCGA-MASTER-01 mientras no se documente expresamente una excepción.

## Unidad de disquete

**Estado:** pendiente de incorporación.

PC Game Archive está preparando una unidad de disquete dedicada a preservación. Cuando se incorpore se documentarán, como mínimo:

- fabricante y modelo;
- interfaz;
- firmware, si aplica;
- herramienta de adquisición;
- formatos de preservación empleados;
- procedimiento de verificación;
- prueba inicial de lectura.

Hasta entonces no se declarará PCGA-MASTER-01 como entorno operativo para preservación de disquetes.

## Software de preservación

Software de referencia actual:

- **Media Preservation Frontend (MPF):** `MPF.UI_3.10.0_net10.0-windows_win-x64_release`.

MPF integra distintas herramientas de adquisición. El backend realmente utilizado, su versión/build y sus parámetros se registran siempre en el expediente de cada pieza.

## Flujo operativo

```text
SOPORTE FÍSICO
      ↓
CARACTERIZACIÓN
      ↓
ADQUISICIÓN 01
      ↓
ADQUISICIÓN 02
      ↓
VERIFICACIÓN
      ↓
SHA-256 / MANIFIESTO
      ↓
MÁSTER DE PRESERVACIÓN
      ↓
COPIA DE TRABAJO VERIFICADA
      ↓
PCGA-LAB-01
```

## Reglas de operación

1. Cada soporte se caracteriza antes de seleccionar el método de adquisición.
2. Cuando el procedimiento lo permite, se realizan dos adquisiciones independientes.
3. Si las adquisiciones no coinciden, el máster no se declara válido hasta resolver la discrepancia.
4. El mínimo propio de integridad de PC Game Archive es SHA-256.
5. El máster constituido se mantiene inmutable.
6. Nunca se instala, monta, parchea o prueba directamente desde el máster.
7. Toda copia enviada a PCGA-LAB-01 se verifica contra el máster de origen.
8. Cualquier cambio de lector, firmware o software de adquisición que pueda afectar a la reproducibilidad debe quedar documentado.

## Información no publicada

Por seguridad operativa, esta ficha pública no expone:

- rutas internas de almacenamiento;
- nombres de host;
- números de serie;
- identificadores PNP/USB completos;
- topología de discos y volúmenes;
- estructura interna de copias de seguridad.

Estos datos no son necesarios para comprender ni reproducir el procedimiento documental de PC Game Archive.

---

Esta ficha describe el entorno de referencia. Cada preservación conserva además su propia evidencia técnica específica.
