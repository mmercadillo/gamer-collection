# Registro de preservación — Kingmaker: La Búsqueda de la Corona (Big Box, 2 disquetes)

**Ficha:** #000249 — https://www.pcgamearchive.org/juegos/kingmaker-la-busqueda-de-la-corona-bigbox/  
**Fecha de sesión:** 12/11/2026.  
**Estándar de referencia:** Preservación digital PC Game Archive v1.0 (05/10/2026).  
**Resultado:** adquisición IMA convencional de ambos disquetes repetida de forma independiente y con SHA-256 coincidente. Fidelidad magnética no comprobada; másteres inmutables y respaldos pendientes de acreditar; compatibilidad no probada.

## Identificación y estado previo

- Edición española Big Box; dos disquetes de 3,5 pulgadas HD (1,44 MB), ambos presentes y sin daños visibles según el operador.
- Disco 1/2: protegido contra escritura antes de introducirlo.
- Disco 2/2: inicialmente sin protección de escritura; tras identificarlo, fue expulsado y protegido.
- No se documentaron fotografías de las etiquetas, examen magnético ni diagnósticos de superficie.

## Unidad y caracterización

- Lector: Y-E DATA USB-FDU USB Device; USB `VID_057B&PID_0000`; revisión USBSTOR declarada `5.01`; modelo mecánico preciso no confirmado.
- Equipo anfitrión real de adquisición: no identificado inequívocamente en esta sesión. No atribuir automáticamente a PCGA-MASTER-01.
- Unidad lógica `A:`.
- Disco 1: el primer `Win32_LogicalDisk` no devolvió FileSystem/Size; `dir A:\ /a` sí permitió listar el volumen `4662-15E1` con `KING.LZH` (1.285.791 B), `INSTALL.EXE` (22.392 B), `LHA.EXE` (34.283 B).
- Disco 2: volumen FAT, `3657-15FA`, tamaño lógico informado 1.457.664 B; `ESPEECH.LZH` (1.138.347 B), `EVOICE.LZH` (280.441 B).
- Ambos: `System Volume Information` (10/11/2026). La atribución de modificación a Windows es plausible pero no demostrada. No se borró ni reparó.
- Protecciones/formato físico especial: no evaluados con herramientas especializadas; estructura magnética no capturada.

## Decisión de adquisición

- Herramienta: WinImage 11.00 x64, `Disk → Read Disk`, imagen IMA sin compresión.
- Finalidad: adquisición convencional de sectores accesibles para conservación y futura validación funcional, sin atribuir fidelidad magnética.
- Parámetros detallados de velocidad, reintentos y registros de lectura por sector: no aportados / no acreditados.
- Fuente: disquetera USB Y-E Data; no hay informe de sector por sector ni log especializado aportado.

## Adquisiciones y comprobación SHA-256

| Soporte | Fichero | Tamaño | SHA-256 |
|---|---|---:|---|
| 1/2 ADQ01 | `KINGMAKER_DISCO_1.IMA` | 1474560 | `AC37AF63F1EEADF41749DF1CEB989EED902987D8E46D114380B446FC15BF8291` |
| 1/2 ADQ02 | `KINGMAKER_DISCO_1-2.IMA` | no comunicado por separado; mismo hash | `AC37AF63F1EEADF41749DF1CEB989EED902987D8E46D114380B446FC15BF8291` |
| 2/2 ADQ01 | `KINGMAKER_DISCO_2.IMA` | 1474560 | `4272574B157D2AEC9A418FEEFC59D32B3A58BCFB4E8B4AD6AF21DC3EBB56D303` |
| 2/2 ADQ02 | `KINGMAKER_DISCO_2-2.IMA` | 1474560 | `4272574B157D2AEC9A418FEEFC59D32B3A58BCFB4E8B4AD6AF21DC3EBB56D303` |

El operador confirmó expresamente que ADQ02 de cada soporte procede de una nueva lectura física completa y no de copiar la imagen anterior. La comparación de hash demuestra identidad de bytes entre las imágenes de cada disco. No existen logs técnicos sectoriales aportados.

## Copia digital de referencia y límites

- Tipo: imagen convencional IMA; **no** captura de flujo magnético.
- Adquisición lógica: doble lectura reproducible, imágenes coincidentes.
- Fidelidad física integral: **no demostrada**; protección anticopia: **no evaluada**.
- Custodia inmutable: no acreditada; manifestación SHA256SUMS, copias de seguridad y ubicación definitiva: pendientes.
- Ruta de trabajo local comunicada en la sesión: directorio `Kingmaker` bajo repositorio local de imágenes; evitar exposición en documentación pública y repositorios de código.
- Copias de trabajo: pendientes de creación y verificación de hash.
- Windows 10 / instalación / juego / guardado-carga: **no probados**.

## Pendientes antes del cierre operativo integral

- [x] Identificar ambos soportes y registrar inspección visual.
- [x] Obtener dos imágenes convencionales independientes por soporte.
- [x] Comparar los SHA-256 de ambos pares.
- [ ] Registrar custodia definitiva, fijación de referencias y respaldos.
- [ ] Crear y verificar copias de trabajo.
- [ ] Probar instalación y ejecución con evidencia reproducible en Windows 10; completar guía independiente.
- [ ] Resolver o explicitar en el estándar aplicable la metodología específica para disquetes USB, si es necesaria para calificar el estado técnico.

No se distribuye software ni se modifica `juegos.json` hasta existir evidencia de los resultados correspondientes.
