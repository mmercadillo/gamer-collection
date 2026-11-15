# Registro de preservación — Lode Runner: The Legend Returns (Big Box)

**Estado:** adquisición única completada. Log, estructura y hashes de referencia revisados con las limitaciones registradas. Compatibilidad no probada.  
**Estándar aplicado:** PC Game Archive — Estándar de preservación digital v1.0.  
**Fecha de apertura del registro:** 15/11/2026.  
**Ficha:** [Lode Runner: The Legend Returns · Big Box](https://www.pcgamearchive.org/juegos/lode-runner-the-legend-returns-bigbox/) · #000250.

## 1. Identificación y estado físico

- Edición catalogada: Big Box española, CD-ROM, para MS-DOS y Windows 3.x. Distribución: Sierra On-Line y Coktel Educative.
- Volumen leído: `LODE_RUNNER_CD`. Número total de soportes del ejemplar, referencia impresa, matriz, códigos SID y estado físico pendientes de documentar.

## 2. Caracterización técnica

- CD mixto de datos y CD-DA. Una sesión y 33 pistas: pista 01 `MODE1/2352`, pistas 02–33 `AUDIO/2352`.
- ImgBurn identifica el sistema de ficheros ISO 9660 y el identificador de implementación `Hybrid Formatter v1.2 (8/29/94)`.
- Extensión informada por ImgBurn: LBA 0–237435, 237.436 sectores, equivalentes a 558.449.472 bytes a 2352 bytes por sector. Los rangos de lectura del log son consecutivos.
- Protección anticopia: no evaluada con la evidencia disponible. TOC independiente: pendiente de documentar.

## 3. Método de adquisición

- Formato BIN/CUE, adecuado para representar la pista de datos y las 32 pistas de audio. Lectura de sectores de 2352 bytes.
- Unidad `HL-DT-ST DVDRAM GTB0N`, firmware `FU03`, `D:`, conexión USB. Estación y versión del sistema operativo pendientes de confirmar.
- Herramienta: ImgBurn, versión e interfaz pendientes de acreditar. Ajuste de `Detection Method: 2-1-3` confirmado por el responsable. `PreGap Snapping`: pendiente de documentar.
- El responsable comunica que reutilizó la configuración de The Secret of Monkey Island (Jewel Case). El registro histórico de esa pieza dejó sin anotar `Detection Method` y `PreGap Snapping`.
- Velocidad solicitada para datos y audio: `4x / 4x`. Velocidad efectiva anunciada por ImgBurn: `10x`. Media registrada: `5,2x`. Máxima observada: `8,5x`. `File Splitting: Auto`.

## 4. Adquisición 01

- Operación de 20:27:34 a 20:36:31. Fecha del 14/11/2026 inferida del nombre del archivo `.ibg` que figura en el log. Duración comunicada por ImgBurn: `00:08:55`.
- Resultado: `Operation Successfully Completed!`. El log aportado no registra avisos, errores explícitos ni reintentos. Registra la exportación del gráfico `.ibg`.
- Archivos: `LODE_RUNNER_CD.BIN`, 558.096.672 bytes según PowerShell en el equipo de adquisición. `LODE_RUNNER_CD.CUE`, examinado, 1.735 bytes. `ImgBurn.log`, examinado, 7.624 bytes.

## 5. Contraste del log con el CUE

- El CUE referencia un único BIN y contiene 33 pistas, con los mismos tipos que el log. Para la pista 02 declara `PREGAP 00:02:00` (150 sectores descritos por separado), `INDEX 00 01:53:00` y `INDEX 01 01:54:00`, separados por 75 sectores en el BIN.
- El log muestra rangos de lectura y el CUE expresa índices relativos al BIN. El primer LBA de lectura de la pista 02 coincide numéricamente con su `INDEX 00`. Frente a los `INDEX 01`, los comienzos del log coinciden en las pistas 03–09 y 11–15, difieren en 1 sector en la pista 10 y en 150 sectores en las pistas 16–33. El log y el CUE por sí solos no permiten atribuir estas diferencias a sectores perdidos ni reconstruir la TOC física.
- El BIN mide 558.096.672 bytes (`237286 × 2352`). La diferencia frente a los 558.449.472 bytes informados por ImgBurn es de 352.800 bytes (`150 × 2352`), coherente con el `PREGAP 00:02:00` declarado en el CUE. Esta concordancia global deja pendiente explicar las diferencias puntuales entre rangos de lectura e índices. Subcanales, offsets de audio y fidelidad física exhaustiva no verificados.

## 6. Verificación y hashes

| Archivo | Bytes | SHA-256 |
| --- | ---: | --- |
| `LODE_RUNNER_CD.BIN` | 558.096.672 | `458d988aad773a130c38b312d2be51278a66c49c484278de71bbf45dd94a0c62` |
| `LODE_RUNNER_CD.CUE` | 1.735 | `3252e3a21509d8e02c31e7bd4e1b82d4f1f05a02517169cd65604d6557d3fba0` |
| `ImgBurn.log` | 7.624 | `b2545b7ad1f3bb6f0754bee414405a316e86aa6f2d4e64458dccf0008592c6c6` |

El tamaño y SHA-256 del BIN se registran a partir de la salida de PowerShell comunicada por el responsable. El CUE adjunto coincide en tamaño y SHA-256 con el original del equipo de adquisición. Conservar el CUE original junto al BIN.

**Decisión operativa del 15/11/2026:** cuando la primera adquisición finalice sin errores registrados, se pasa a una copia de trabajo verificada sin repetir la lectura de rutina. Se reconsiderará una segunda lectura si fallan las pruebas funcionales. Para esta pieza queda documentada la verificación mediante revisión del log y de la estructura y registro de SHA-256, sin contraste entre adquisiciones independientes.

## 7. Máster y copia de trabajo

El BIN/CUE de la adquisición 01 es la referencia para generar la copia de trabajo. Ubicación definitiva de custodia y copias de seguridad pendientes de documentar. Copia de trabajo pendiente de crear y de contrastar mediante SHA-256 con ambos archivos de referencia antes del montaje.

## 8. Compatibilidad

Instalación, arranque y pruebas funcionales: no probados. La elección del entorno de ejecución partirá de lo que contenga la copia de trabajo.
