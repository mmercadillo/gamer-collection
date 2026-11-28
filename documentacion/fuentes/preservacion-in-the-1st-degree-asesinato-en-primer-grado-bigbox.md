# Preservación de los dos CD-ROM

Documentamos la adquisición digital de **In the 1st Degree: Asesinato en Primer Grado**, edición española Big Box (ficha #000260), realizada el 28 de noviembre de 2026 conforme al [estándar de preservación digital](../estandar-preservacion-digital/) v2.0. El ejemplar contiene dos CD-ROM originales, en buen estado según la inspección del responsable.

## Caracterización de los soportes

Antes de elegir el formato, examinamos cada disco por separado mediante PowerShell e IsoBuster 5.8. Ambos presentan una sesión, una pista de datos Mode 1, sectores de usuario de 2048 bytes y sistema de archivos ISO 9660. No hay pistas CD-DA.

| Parámetro | CD 1 | CD 2 |
| --- | ---: | ---: |
| Etiqueta | `1STDEGREE1` | `1STDEGREE2` |
| Sectores de pista | 332.797 | 325.980 |
| Tamaño lógico en Windows (bytes) | 680.949.760 | 666.988.544 |
| Tamaño de pista (bytes) | 681.568.256 | 667.607.040 |
| Diferencia (bytes) | 618.496 | 618.496 |

La diferencia común de 302 sectores entre el volumen lógico y la pista completa no indica por sí misma pérdida de datos; su causa exacta no se ha determinado. Las imágenes obtenidas cubren el tamaño completo de pista indicado por las herramientas.

El análisis independiente con Media Preservation Frontend 3.11.1 terminó al 100 % en ambos discos sin detectar protecciones anticopia. En el primero identificó módulos Wise Installation Wizard, que son componentes de instalación y no se clasificaron como protección. Este análisis no demuestra la ausencia absoluta de protecciones.

## Método y adquisición

Elegimos ISO porque ambos discos contienen exclusivamente una pista de datos Mode 1 y no se observaron particularidades que exigieran captura RAW. El formato conserva los datos de usuario de los sectores, no las cabeceras, códigos de corrección ni subcanales físicos.

- Entorno: Windows 10 Pro 22H2 x64, build 19045, confirmado mediante PowerShell.
- Lector: HL-DT-ST DVDRAM GTB0N, firmware FU03, USB 2.0, unidad `D:`.
- Herramienta: ImgBurn 2.5.8.0, modo Read (Create image file from disc).
- Velocidad solicitada: 4x para datos y audio; velocidad efectiva indicada: 10x.

| Resultado | CD 1 | CD 2 |
| --- | ---: | ---: |
| Rango LBA | 0–332796 | 0–325979 |
| Duración según log | 00:09:51 | 00:09:40 |
| Velocidad media | 6,5x | 6,5x |
| Velocidad máxima | 9,3x | 9,3x |
| Errores o avisos registrados | 0 | 0 |

Las dos operaciones finalizaron con `Operation Successfully Completed!`. ImgBurn identificó incorrectamente Windows como versión 8; la consulta del sistema confirmó Windows 10. No se observó impacto en la adquisición.

## Verificación e integridad

Contrastamos los rangos y tamaños de pista de los logs con la caracterización previa, comprobamos los tamaños reales de los archivos mediante PowerShell y calculamos SHA-256.

| Archivo | Bytes | SHA-256 |
| --- | ---: | --- |
| `1STDEGREE1.ISO` | 681.568.256 | `473F337AF1827C71D39B4124721E4DF8B225FC34812F722BCA6D6CC7F113DA4C` |
| `1STDEGREE2.ISO` | 667.607.040 | `3916D1038CC66B7BEE1243D57EC0329DD5853DF00213A7379496A27C05D1664B` |

Se documentó una adquisición única por disco conforme al estándar v2.0. No se repitieron las lecturas de rutina al no observar errores o incoherencias de tamaño. Los hashes identifican las imágenes obtenidas; no demuestran por sí solos fidelidad física exhaustiva ni reproducibilidad entre lecturas. No se han cotejado referencias externas ni inspeccionado independientemente el sistema de archivos de las imágenes resultantes.

## Estado y siguientes comprobaciones

Los dos soportes cuentan con imágenes ISO adquiridas sin errores registrados, tamaños coincidentes y hashes de referencia. La fijación del máster en almacenamiento definitivo, su separación efectiva de la copia de trabajo y las copias de seguridad quedan pendientes de confirmación documental.

El primer disco contiene el instalador, componentes QuickTime y recursos multimedia; el segundo contiene recursos `.MHK` y vídeos `.MOV`. La instalación, reproducción de vídeo y audio, cambios de disco, jugabilidad y guardado aún no se han probado. La guía de compatibilidad se elaborará a partir de una copia de trabajo verificada. PC Game Archive no distribuye las imágenes del software.
