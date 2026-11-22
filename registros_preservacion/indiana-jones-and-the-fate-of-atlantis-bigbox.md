# Registro interno de preservación — Indiana Jones and the Fate of Atlantis

- **Fecha de apertura:** 22/11/2026.
- **Estándar aplicable:** Estándar de preservación digital de PC Game Archive v2.0, vigente desde el 15/11/2026.
- **Estado:** cinco adquisiciones sectoriales convencionales únicas verificadas. Manifiesto SHA-256 creado y cotejado según el operador. Cierre de adquisición documentado para revisión.

## 1. Identificación

| Campo | Datos declarados en el catálogo |
| --- | --- |
| Edición | Big Box española para MS-DOS, 1992 |
| Idioma | Castellano |
| Desarrollador / distribuidor en España | LucasArts / Erbe Software |
| Identificador de la pieza | `indiana-jones-and-the-fate-of-atlantis-bigbox`. El catálogo tiene `num: "000000"`, pendiente de un identificador definitivo. |
| Soportes | Cinco disquetes de 3,5 pulgadas de alta densidad, numerados del 1 al 5 |
| Depósitos legales | M-22196-1992 a M-22200-1992 según la ficha. Correspondencia exacta por etiqueta pendiente de cotejo. |
| Documentación auxiliar | La ficha menciona que el manual original contiene los códigos de verificación. Presencia e integridad en este ejemplar pendientes de confirmar. |

Fuente del inventario inicial: [ficha de la edición](https://www.pcgamearchive.org/juegos/indiana-jones-and-the-fate-of-atlantis-bigbox/) y su entrada en `juegos.json` de `pcgamearchive.zip`. Estos datos identifican el expediente y quedan sujetos a cotejo con el ejemplar.

## 2. Estado físico previo

| Soporte declarado | Etiqueta / depósito legal cotejados | Estado exterior | Protección contra escritura |
| --- | --- | --- | --- |
| Disquete 1 de 5 | Presente según el operador. Depósito legal pendiente de transcripción. | Correcto según el operador | Pendiente |
| Disquete 2 de 5 | Presente según el operador. Depósito legal pendiente de transcripción. | Correcto según el operador | Pendiente |
| Disquete 3 de 5 | Presente según el operador. Depósito legal pendiente de transcripción. | Correcto según el operador | Pendiente |
| Disquete 4 de 5 | Presente según el operador. Depósito legal pendiente de transcripción. | Correcto según el operador | Pendiente |
| Disquete 5 de 5 | Presente según el operador. Depósito legal pendiente de transcripción. | Correcto según el operador | Pendiente |

**Evidencia del 22/11/2026:** el operador confirma que los disquetes están correctos. La confirmación se aplica al inventario y estado exterior general. Quedan pendientes el detalle de las inscripciones, la posición de la pestaña contra escritura y la confirmación específica del manual.

**Siguiente acción:** revisar este registro y el documento público de preservación antes de iniciar compatibilidad.

## 3. Caracterización técnica

### Disquete 1 de 5

- Evidencia del 22/11/2026: salida del operador de `Win32_LogicalDisk` y `dir A:\ /a`.
- Unidad `A:`, volumen `920826A 002`, sistema de archivos `FAT` según Windows.
- Tamaño lógico informado por CIM: 1.457.664 bytes. Espacio libre indicado por DIR: 3.072 bytes.
- Número de serie: CIM devuelve el campo vacío. DIR muestra `0000-0000`.
- Directorio raíz legible. DIR informa 2 archivos y 0 subdirectorios.

| Archivo | Tamaño (bytes) |
| --- | ---: |
| `INSTALL.EXE` | 34.649 |
| `PCVIQA_A.ND4` | 1.419.388 |

Lectura de todos los sectores y geometría de la imagen aún pendientes. La protección documental mencionada por el catálogo queda pendiente de cotejo. Las características físicas especiales siguen sin evaluar con una herramienta especializada.

### Disquete 2 de 5

- Evidencia del 22/11/2026: salida de `Win32_LogicalDisk` y `dir A:\ /a`.
- CIM confirma la unidad `A:` y devuelve vacíos el nombre, el número de serie, el sistema de archivos y el tamaño.
- DIR muestra el volumen `920826A 003`, serie `0000-0000` y 3.072 bytes libres. Directorio raíz legible con 1 archivo y 0 subdirectorios.
- Archivo: `PCVIQA_B.ND4`, 1.454.088 bytes. El cotejo posterior de la imagen confirmó el volumen y el directorio. El subtipo FAT y los parámetros exactos de geometría no se identificaron de forma independiente.

### Disquete 3 de 5

- Evidencia del 22/11/2026: salida de `Win32_LogicalDisk` y `dir A:\ /a`.
- CIM confirma la unidad `A:` y devuelve vacíos el nombre, el número de serie, el sistema de archivos y el tamaño.
- DIR muestra el volumen `920826A 001`, serie `0000-0000` y 3.072 bytes libres. Directorio raíz legible con 1 archivo y 0 subdirectorios.
- Archivo: `PCVIQA_C.ND4`, 1.454.088 bytes. La etiqueta lógica se registra tal como figura en el listado. El cotejo con la imagen confirmó el volumen y el directorio. Sistema de archivos y geometría sin identificación independiente.

### Disquete 4 de 5

- Evidencia del 22/11/2026: salida de `Win32_LogicalDisk` y `dir A:\ /a`.
- CIM confirma la unidad `A:` y devuelve vacíos el nombre, el número de serie, el sistema de archivos y el tamaño.
- DIR muestra el volumen `920826A 006`, serie `0000-0000` y 3.072 bytes libres. Directorio raíz legible con 1 archivo y 0 subdirectorios.
- Archivo: `PCVIQA_D.ND4`, 1.454.088 bytes. Sistema de archivos y geometría sin confirmar.

### Disquete 5 de 5

- Evidencia del 22/11/2026: salida de `Win32_LogicalDisk` y `dir A:\ /a`.
- Unidad `A:`, volumen `920826A 004`, sistema de archivos `FAT` según Windows. CIM informa 1.457.664 bytes de tamaño lógico.
- CIM devuelve el número de serie vacío. DIR muestra `0000-0000` y 12.800 bytes libres. Directorio raíz legible con 1 archivo y 0 subdirectorios.
- Archivo: `PCVIQA_E.ND4`, 1.444.773 bytes. Geometría exacta pendiente de confirmar.

## 4. Decisión de adquisición

Para el disquete 1 se selecciona una primera adquisición sectorial convencional. Windows reconoce un volumen FAT legible y lista su directorio raíz. Se evaluará si la lectura sectorial se completa y si la imagen es coherente con la geometría observada.

- Referencia: WinImage 11.00 x64, paquete `wima64110`. Captura de «About WinImage» confirma la versión 11.00 en modo de 64 bits.
- Procedimiento previsto: `Disk > Use drive A:`, `Disk > Read disk`. Desactivar la omisión de pistas vacías y el truncamiento antes de guardar como IMA sin comprimir. Registrar el estado efectivo de las opciones y cualquier error de lectura.
- Imagen prevista: `disco-01/adq-01/INDIANA_ATLANTIS_DISCO_01.IMA`.
- [Documentación de los ajustes de WinImage](https://www.winimage.com/wimushlp/wini28z8.htm).

### Disquete 2 de 5

- Se selecciona una primera adquisición sectorial convencional con la misma unidad y WinImage 11.00 x64. El directorio del original es legible. Se comprobará si la herramienta completa la lectura y si la imagen es coherente con el inventario y su geometría.
- Archivo previsto: `INDIANA_ATLANTIS_DISCO_02.IMA`, sin compresión. Mantener desactivadas la omisión de pistas vacías y la opción de truncar la imagen.

### Disquete 3 de 5

- Se selecciona una primera adquisición sectorial convencional con la misma unidad y WinImage 11.00 x64. El directorio del original es legible. Se verificará el resultado de la lectura y el cotejo con el inventario.
- Archivo previsto: `INDIANA_ATLANTIS_DISCO_03.IMA`, sin compresión. Mantener desactivadas la omisión de pistas vacías y la opción de truncar la imagen.

### Disquete 4 de 5

- Se selecciona una primera adquisición sectorial convencional con la misma unidad y WinImage 11.00 x64. El directorio del original es legible. Se verificará el resultado de la lectura y se cotejará el inventario.
- Archivo previsto: `INDIANA_ATLANTIS_DISCO_04.IMA`, sin compresión. Mantener desactivadas la omisión de pistas vacías y la opción de truncar la imagen.

### Disquete 5 de 5

- Se selecciona una primera adquisición sectorial convencional con la misma unidad y WinImage 11.00 x64. Windows reconoce el volumen FAT y el directorio raíz es legible.
- Archivo previsto: `INDIANA_ATLANTIS_DISCO_05.IMA`, sin compresión. Mantener desactivadas la omisión de pistas vacías y la opción de truncar la imagen.

### Entorno de lectura

- Evidencia del operador del 22/11/2026, obtenida en PowerShell con la unidad vacía mediante `Get-CimInstance Win32_OperatingSystem` y `Get-PnpDevice -PresentOnly`.
- Sistema anfitrión: Microsoft Windows 10 Pro x64, versión `10.0.19045`, compilación `19045`. Identificador del equipo pendiente.
- Lector: Y-E DATA USB-FDU USB Device, conexión USB, clase PnP `FloppyDisk`, estado `OK`. Dispositivo USB `VID_057B&PID_0000`, también con estado `OK`.
- Revisión declarada por USBSTOR: `5.01`. Firmware interno y modelo del mecanismo no confirmados. Letra observada con el disquete 1: `A:`.

## 5. Adquisición

### Disquete 1 de 5 — adquisición 01, 22/11/2026

- El operador comunica que la operación de lectura terminó sin errores.
- Evidencia de la versión: captura [00-version-winimage.png](indiana-jones-and-the-fate-of-atlantis-bigbox/img/00-version-winimage.png), diálogo «About WinImage». La captura acredita la versión y el modo de 64 bits.
- Archivo guardado: `INDIANA_ATLANTIS_DISCO_01.IMA`. El operador obtuvo su tamaño y su SHA-256 con PowerShell. Configuración efectiva de WinImage pendiente de confirmación. No se ha aportado un log sectorial.
### Disquete 2 de 5 — adquisición 01, 22/11/2026

- El operador comunica que la operación de lectura terminó sin errores.
- Archivo guardado: `INDIANA_ATLANTIS_DISCO_02.IMA`. El operador obtuvo su tamaño y SHA-256 con PowerShell. Cotejo del directorio raíz completado. Sin log sectorial aportado.

### Disquete 3 de 5 — adquisición 01, 22/11/2026

- El operador comunica que la lectura terminó sin errores.
- Archivo guardado: `INDIANA_ATLANTIS_DISCO_03.IMA`. El operador obtuvo su tamaño y SHA-256 con PowerShell. Cotejo del directorio raíz completado. Sin log sectorial aportado.

### Disquete 4 de 5 — adquisición 01, 22/11/2026

- El operador comunica que la lectura terminó sin errores.
- Archivo guardado: `INDIANA_ATLANTIS_DISCO_04.IMA`. El operador obtuvo su tamaño y SHA-256 con PowerShell. Cotejo del directorio raíz completado. Sin log sectorial aportado.

### Disquete 5 de 5 — adquisición 01, 22/11/2026

- El operador comunica que la lectura terminó sin errores.
- Archivo guardado: `INDIANA_ATLANTIS_DISCO_05.IMA`. El operador obtuvo su tamaño y SHA-256 con PowerShell. Cotejo del directorio raíz completado. Sin log sectorial aportado.

## 6. Verificación

### Disquete 1 de 5

- El tamaño de 1.474.560 bytes coincide con el esperado para una imagen sectorial estándar de un disquete de 3,5 pulgadas HD. SHA-256 registrado en la sección 7.
- Cotejo del 22/11/2026 en WinImage. La captura [01-cotejo-disquete-01.png](indiana-jones-and-the-fate-of-atlantis-bigbox/img/01-cotejo-disquete-01.png) muestra la misma etiqueta `920826A 002` y los mismos archivos y tamaños del directorio raíz del original: `INSTALL.EXE` (34.649 bytes) y `PCVIQA_A.ND4` (1.419.388 bytes).
- **Resultado:** adquisición única verificada en tamaño, huella registrada y estructura visible del directorio raíz. La lectura terminó sin errores según el operador. Sin log sectorial aportado. Sin comprobación de reproducibilidad entre lecturas, fidelidad magnética ni funcionalidad.

### Disquete 2 de 5

- El tamaño de 1.474.560 bytes coincide con el esperado para una imagen sectorial estándar de un disquete de 3,5 pulgadas HD. SHA-256 registrado en la sección 7.
- Cotejo del 22/11/2026 en WinImage. La captura [02-cotejo-disquete-02.png](indiana-jones-and-the-fate-of-atlantis-bigbox/img/02-cotejo-disquete-02.png) muestra la etiqueta `920826A 003` y un único archivo raíz, `PCVIQA_B.ND4` (1.454.088 bytes). Coinciden con el listado del original.
- **Resultado:** adquisición única verificada en tamaño, huella registrada y estructura visible del directorio raíz. La lectura terminó sin errores según el operador. Sin log sectorial aportado. Sin comprobación de reproducibilidad entre lecturas, fidelidad magnética ni funcionalidad.

### Disquete 3 de 5

- El tamaño de 1.474.560 bytes coincide con el esperado para una imagen sectorial estándar de un disquete de 3,5 pulgadas HD. SHA-256 registrado en la sección 7.
- La captura [03-cotejo-disquete-03.png](indiana-jones-and-the-fate-of-atlantis-bigbox/img/03-cotejo-disquete-03.png) muestra en WinImage la etiqueta `920826A 001` y un único archivo en la raíz, `PCVIQA_C.ND4` (1.454.088 bytes). Coinciden con el inventario del original.
- **Resultado:** adquisición única verificada en tamaño, huella registrada y estructura visible del directorio raíz. La lectura terminó sin errores según el operador. Sin log sectorial aportado. Reproducibilidad entre lecturas, fidelidad magnética y funcionalidad sin evaluar.

### Disquete 4 de 5

- El tamaño de 1.474.560 bytes coincide con el esperado para una imagen sectorial estándar de un disquete de 3,5 pulgadas HD. SHA-256 registrado en la sección 7.
- La captura [04-cotejo-disquete-04.png](indiana-jones-and-the-fate-of-atlantis-bigbox/img/04-cotejo-disquete-04.png) muestra en WinImage la etiqueta `920826A 006` y un único archivo en la raíz, `PCVIQA_D.ND4` (1.454.088 bytes). Coinciden con el inventario del original.
- **Resultado:** adquisición única verificada en tamaño, huella registrada y estructura visible del directorio raíz. La lectura terminó sin errores según el operador. Sin log sectorial aportado. Reproducibilidad entre lecturas, fidelidad magnética y funcionalidad sin evaluar.

### Disquete 5 de 5

- Imagen de 1.474.560 bytes, tamaño esperado para el formato sectorial estándar de 3,5 pulgadas HD. SHA-256 en la sección 7.
- La captura [05-cotejo-disquete-05.png](indiana-jones-and-the-fate-of-atlantis-bigbox/img/05-cotejo-disquete-05.png) muestra en WinImage la etiqueta `920826A 004` y un único archivo raíz, `PCVIQA_E.ND4` (1.444.773 bytes). Coinciden con el inventario del original.
- **Resultado:** adquisición única verificada en tamaño, huella registrada y estructura visible del directorio raíz. La lectura terminó sin errores según el operador. Sin log sectorial aportado. Reproducibilidad entre lecturas, fidelidad magnética y funcionalidad sin evaluar.

## 7. Hashes

| Soporte | Adquisición | Archivo | Bytes | SHA-256 |
| --- | --- | --- | ---: | --- |
| Disquete 1 de 5 | 01 | `INDIANA_ATLANTIS_DISCO_01.IMA` | 1.474.560 | `8622A956CA89C413515361BA54DD176B4EF22394A08804ECE92A0E0C81F97CFC` |
| Disquete 2 de 5 | 01 | `INDIANA_ATLANTIS_DISCO_02.IMA` | 1.474.560 | `D673AF27EEDE3A1E220A5CBD99309C73CBC74595850FBC2701432CC5975EDB3D` |
| Disquete 3 de 5 | 01 | `INDIANA_ATLANTIS_DISCO_03.IMA` | 1.474.560 | `1A73F3425677CF60A36548A14F41987620982B81D773FFE3744AB777AC8D6816` |
| Disquete 4 de 5 | 01 | `INDIANA_ATLANTIS_DISCO_04.IMA` | 1.474.560 | `34B637DB24487C369A0DD533276F458AE5EF3B155BC761F44CC8EEADD3FC67D9` |
| Disquete 5 de 5 | 01 | `INDIANA_ATLANTIS_DISCO_05.IMA` | 1.474.560 | `2E8B79914C55DC166F9DC531833E15F6E61E06C4EC6C6C9DE282447F36A613CB` |

Fuente: salidas de `Get-Item` y `Get-FileHash -Algorithm SHA256` del 22/11/2026 para los cinco disquetes.

El operador confirma que el cotejo de los cinco archivos frente a las huellas registradas finalizó correctamente y que se creó `SHA256SUMS.txt` en la carpeta de adquisición.

## 8. Máster o copia digital de referencia

- **Estado técnico:** las cinco adquisiciones están verificadas en el alcance descrito en la sección 6.
- **Estado funcional:** `no_probada`.
- Conjunto digital de referencia identificado: cinco imágenes IMA convencionales de la adquisición 01, listadas en la sección 7. Total: 7.372.800 bytes.
- El conjunto de referencia consta de los cinco archivos IMA y el manifiesto `SHA256SUMS.txt`. El operador confirmó su creación y cotejo en la carpeta de adquisición. Por decisión del operador, este cierre se limita a la adquisición y verificación del conjunto digital. Ubicación definitiva, fijación del máster y respaldo quedan sin verificar.

## 9. Copia de trabajo

Pendiente de documentar la preservación y revisar la referencia.

## 9 bis. Validación funcional

Pendiente de la revisión de la preservación. Instalación, arranque, partida, gráficos, música, sonido, guardado y carga figuran como no probados.

## 10. Cierre

- [x] Registrar la versión del estándar e identificar la ficha de referencia.
- [x] Confirmar el inventario y el estado exterior general de los cinco disquetes mediante la comprobación del operador.
- [ ] Completar el detalle de etiquetas y la confirmación de las pestañas de protección contra escritura.
- [x] Registrar el volumen y el directorio raíz de cada disquete.
- [ ] Evaluar características físicas especiales y confirmar documentalmente el manual.
- [x] Documentar y verificar las cinco adquisiciones, tamaños, SHA-256 y cotejo del directorio raíz.
- [x] Verificar las cinco huellas y crear el manifiesto `SHA256SUMS.txt` en la carpeta de adquisición.
- Custodia y respaldos excluidos del alcance de este cierre a petición del operador.
- [ ] Revisar el registro interno y el documento público de preservación antes de las pruebas de compatibilidad.
- [ ] Vincular el registro de validación funcional cuando haya evidencia.

## 11. Observaciones

La ficha menciona el manual como parte de la verificación anticopia. Su presencia específica, estado y digitalización quedan sin confirmar. La instalación y la ejecución se documentarán tras la revisión de preservación.
