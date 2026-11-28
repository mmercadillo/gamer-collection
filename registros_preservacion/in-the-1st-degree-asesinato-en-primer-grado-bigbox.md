# Registro interno de preservación — In the 1st Degree: Asesinato en Primer Grado (Big Box)

**Estándar:** v2.0, vigente desde 15/11/2026. **Fecha:** 28/11/2026. **Ficha:** #000260. **Estado técnico global:** `realizada` (controles de adquisición completados; separación y fijación definitiva del máster pendientes de acreditar). **Funcionalidad:** `funcional_con_ajustes`.

## 1. Identificación

- [Ficha PCGA](https://www.pcgamearchive.org/juegos/in-the-1st-degree-asesinato-en-primer-grado-bigbox/). Edición española Big Box, Windows 3.x/95, Brøderbund Software / Electronic Arts Software, según catálogo.
- Dos CD-ROM originales confirmados por el responsable. Referencias impresas, matrices y SID pendientes; no se solicitaron fotografías adicionales por no ser necesarias para decidir el método.

## 2. Estado físico previo

Ambos discos en buen estado según el responsable. Suciedad, arañazos concretos, intervenciones previas y limpieza: no detallados.

## 3–7. Caracterización, adquisición y verificación

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

## 8. Máster / copia digital de referencia

- Tipo: imágenes de sectores de usuario MODE1/2048; no volcados físicos RAW. No se registran sectores omitidos, sustituidos o reconstruidos; no se ha comprobado fidelidad física exhaustiva.
- Origen: CD originales, una lectura independiente por soporte. Archivos resultantes en el equipo de adquisición: `C:\Users\Miguel\git\ISOs\1STDEGREE1.ISO` y `1STDEGREE2.ISO`.
- Manifiesto documental generado en este proyecto: [SHA256SUMS.txt](in-the-1st-degree-asesinato-en-primer-grado-bigbox/SHA256SUMS.txt). Ejecución del comando de creación del manifiesto en el equipo del usuario no acreditada por salida.
- Ubicación definitiva, inmutabilidad y copias de seguridad: pendientes de confirmar. No se identifica el equipo como PCGA-MASTER-01: el sistema acreditado es Windows 10 Pro, no Windows Server 2019. Modelo del equipo no confirmado.
- Reintentos: ninguno registrado; configuración específica de reintentos no aportada. Comparación externa y entre lecturas: no realizadas.

## 9. Copia de trabajo y validación funcional

Copias de trabajo separadas y SHA-256 cotejados. Instalación, arranque, FMV, juego representativo, guardado, carga y cambio de CD validados con QuickTime 2.1.2. Véase el [registro de compatibilidad](../registros_compatibilidad/in-the-1st-degree-asesinato-en-primer-grado-bigbox.md).

## 10. Evidencia y cierre

- Capturas de IsoBuster: carpeta [in-the-1st-degree-asesinato-en-primer-grado-bigbox/img](in-the-1st-degree-asesinato-en-primer-grado-bigbox/img/), cuatro por disco.
- Logs originales de análisis MPF aportados: [in-the-1st-degree-asesinato-en-primer-grado-bigbox/logs](in-the-1st-degree-asesinato-en-primer-grado-bigbox/logs/). Extracto de ImgBurn transcrito de la conversación; archivo original y gráficos IBG no aportados.
- PowerShell: tamaños reales coincidentes y hashes registrados arriba; `Get-CimInstance Win32_OperatingSystem` confirmó Microsoft Windows 10 Pro, 10.0.19045, build 19045, 64 bits.
- Identificación, caracterización, análisis de protección, decisión ISO, adquisición y revisión de logs, tamaños y hashes: completados con los límites descritos.
- Pendientes: confirmar separación/fijación y almacenamiento del máster, revisión de documentos, inspección lógica de las imágenes si procede, validación en equipos adicionales. No se asigna estado global `verificada` hasta acreditar la separación requerida por el estándar.
