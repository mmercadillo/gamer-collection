# PC Game Archive — Registro interno de preservación

**Pieza:** Blade Runner — Jewel Case, edición española de Dinamic Multimedia.  
**Ficha:** https://www.pcgamearchive.org/juegos/blade-runner-jewelcase/  
**Identificador de ficha en el catálogo actual:** `000000` (provisional; no asignar otro por inferencia).  
**Inicio de las operaciones:** noviembre de 2026 (pruebas de adquisición relatadas inicialmente el 03/11; confirmación funcional el 09/11).  
**Estándar público consultado:** v1.0. **Criterio operativo:** plantilla actualizada que prioriza funcionalidad verificable; pendiente conciliación/versionado con el estándar público.  
**Estado:** **recuperación funcional con pruebas principales satisfactorias; reproducción íntegra de CD no acreditada; custodia inmutable y respaldo pendientes de confirmación**.

## 1. Identificación

- Título: **Blade Runner**; desarrollo original: Westwood Studios.
- Edición concreta: **Jewel Case, mercado español, distribuida por Dinamic Multimedia** (no equiparar con la Big Box ni la versión inglesa).
- Soporte: **cuatro CD-ROM**; procedencia catalogada: cesión de José Antonio Serrano García.
- Plataforma original declarada: Windows 95/98.
- Referencia comercial / EAN en catálogo: `8426239090551`.
- Números de matriz y ring code: no registrados en este expediente.

## 2. Estado físico previo

- Cuatro CD inspeccionados visualmente y declarados en buen estado por el operador.
- En el CD 1 se observó **un anillo ópticamente diferenciado** en la cara de lectura; fotografía adicional no requerida para el resultado funcional.
- No se ejecutó limpieza o intervención material documentada.
- Se probaron tres ejemplares del CD 1 con errores de lectura semejantes.

## 3. Caracterización técnica y anomalías

- CD 1: TOC comunicado por Redumper: una pista de datos, índice 01 en LBA 0, lead-out en LBA **340640**; estructura de los discos 2–4 **no registrada con el mismo nivel de detalle**.
- MPF 3.10.0: «Buscar protección» devolvió `No protections found`; el análisis demoró sobre `D:\BASE2\BOARD.MIX` (43,03 %) y finalmente terminó en el tercer ejemplar, con velocidad configurada a 2×. **No equivale a ausencia probada de protección.**
- Redumper build `b749`, lector **HL-DT-ST DVDRAM GTB0N**, firmware **FU03**; perfil `GENERIC`; velocidad 2×.
  - Primera prueba: `DATA_C2_SUB`, 20 reintentos, error acumulado alrededor de LBA **18887** (SCSI 9408, Q 18871); interrumpida desde MPF.
  - Segunda prueba desde **PowerShell** con `--auto-detect --retries=0`: detectó `DATA_SUB`; errores alrededor de LBA **18875** (SCSI 1764, Q 149); interrumpida con Ctrl+C en consola.
  - Ambas emitieron `warning: unscrambled sector read`; no se obtuvo máster fiel.
- Windows: la lectura completa de `BASE2\BOARD.MIX` mediante `Get-FileHash` devolvió error de datos CRC en **tres ejemplares**; consulta de metadatos sí funcionaba.
- IsoBuster 5.8: `BOARD.MIX` inicia en LBA **21507**, ocupa **450 bloques** (hasta 21956). Extracción selectiva de ese fichero devolvió `03/10/00` en LBA 21507; extracción RAW de pista 01 falló en **LBA 18872**.
- Se observó físicamente un anillo y hay fallos reproducibles en una zona definida. **Hipótesis: zona deliberadamente ilegible / protección por anillo, sin identificación comercial formal probada.**
- Una lectura completa de `README.TXT` de CD 1 sí devolvió SHA-256 `F78B5CDAAD37CCD0AB6F3EA5A119FE8804DED67AFBE4A8B7C60FE0D84D6ACACA`.

## 4. Decisión de adquisición

- Por repetición de errores en varias herramientas y copias, se detuvo la adquisición sectorial convencional del CD 1.
- El objetivo priorizado fue **recuperar los datos de la edición para instalación y ejecución**, sin reclamar fidelidad física al anillo ni a subcanales.
- Se empleó **UltraISO** (versión no facilitada) para extraer los archivos de los **cuatro CD** a carpetas independientes (`BLADERUNNER_CD1` … `BLADERUNNER_CD4`).
- Se generaron imágenes BIN/CUE reconstruidas, con problemas de montaje en el entorno de prueba; posteriormente se generaron **cuatro ISO reconstruidas** que montaron y mostraron su contenido correctamente.
- **Limitación:** la extracción de archivos/creación de ISO puede perder detalles físicos, disposición sectorial y protección; no consta un mapa completo de sectores sustituidos ni el comportamiento de error específico de UltraISO.

## 5. Adquisición y archivos recuperados

- CD 1: inventario `BladeRunner_CD1_SHA256.csv` de **587 archivos** legibles con SHA-256 y tamaños registrados. Esto prueba legibilidad actual, no equivalencia bit a bit con la edición física.
- CD 2–4: se confirmó su extracción y montaje de ISO reconstruidas, **sin inventarios individuales completos conservados en esta conversación**.
- Se preparó una copia de trabajo para ScummVM, reunida desde los cuatro directorios, tomando archivos `.MIX`, `.TLK` y `.DAT`, renombrando por disco `CDFRAMES.DAT` a `CDFRAMES1.DAT` … `CDFRAMES4.DAT`.
- Los duplicados de mismo nombre se aceptaron solo tras comparar **tamaño y SHA-256**. En particular, `A.TLK`, `3.TLK` y `VQA3.MIX` no se renombraron arbitrariamente.
- Resultado: **27 archivos**, **1.978.139.834 bytes** en total, copia y hashes SHA-256 coincidentes con los archivos fuente de las carpetas extraídas.
- Manifiesto íntegro adjunto: `registros_preservacion/blade-runner-jewelcase-sha256.md` y fichero CSV de evidencia.

## 6. Incidencia sobre BOARD.MIX

- Una extracción anterior: SHA-256 `56C8D359FDD63D742770A482D61F1E522E28F44D6F937A18F269D90FA31530E2`, tamaño 921221 bytes.
- Extracción **actual** en `BLADERUNNER_CD1` y copia funcional: SHA-256 `089A930F25FDDB836ED15C2F7E217C5849E8455D5181883A7EA20B647DA34FFC`, mismo tamaño.
- La variación entre extracciones no tiene explicación técnica probada; puede ser relevante para sectores recuperados, pero **no ha impedido las pruebas funcionales realizadas**.
- No describir ninguno de los dos ficheros como idéntico al original sin nueva evidencia.

## 7. Verificación

- Todos los archivos de la copia ScummVM se copiaron desde los directorios extraídos, con verificación SHA-256 origen/destino sin errores.
- Se calculó manifiesto de 27 hashes desde la copia de trabajo; se conserva el listado aportado por el operador.
- No se acreditan: doble adquisición físicamente coincidente, integridad sectorial íntegra, preservación de subcanales, verificación independiente de las cuatro ISO, copias de seguridad verificadas.

## 8. Copia digital de referencia y custodia

- **Candidato funcional:** directorio `Blade_Runner_ES_ScummVM` con los 27 archivos verificados.
- **Fuentes conservadas según operador:** cuatro directorios extraídos y cuatro ISO reconstruidas.
- **Estado de fijación:** no consta confirmación de marcado inmutable, manifiesto externo de las ISO ni segundo respaldo comprobado. No afirmar constitución definitiva del máster.
- **Categorías:** integridad digital del conjunto de 27 archivos **verificada frente a fuentes extraídas**; fidelidad física **no verificada**; funcionalidad **validada en pruebas principales**.

## 9. Copia de trabajo

- Ubicación operativa original: `C:\Users\Miguel\git\ISOs\Blade_Runner_ES_ScummVM` (**ruta interna, no publicar**).
- Se creó sin alterar las extracciones; los 27 archivos se verificaron contra su origen.
- Uso: ejecución del juego con ScummVM 2026.4.0 sobre PCGA-LAB-01.

## 9 bis. Validación funcional

- ScummVM **2026.4.0** reconoció `Blade Runner (Windows/Spanish)` desde los datos de esta edición; se eligió la variante **sin contenido restaurado**.
- Introducción, inicio de partida, jugabilidad probada, voces españolas, música, efectos, cinemáticas observadas: **correctos**, confirmados por el operador.
- Guardado, cierre, nuevo arranque, carga y continuación de partida: **correctos**, confirmados por el operador.
- **No probados**: recorrido completo, todas las rutas y finales, todas las escenas, exhaustividad de recursos de cada CD y repetición desde una copia de trabajo completamente limpia.
- Instalador del CD 1 bajo Windows 10 x64: `INSTALL.EXE` (firma **NE**, Windows 16 bits) no ejecutable; `SETUP.EXE` falla al llamar al componente. La ruta ScummVM **no necesita usarlo**.
- Guía relacionada: `registros_compatibilidad/blade-runner-jewelcase-scummvm-windows-10.md`.

## 10. Cierre y checklist

- [x] Edición y cuatro soportes identificados.
- [x] Anomalías del CD 1 caracterizadas y registradas.
- [x] Extracción de archivos de cuatro CD comunicada.
- [x] Conjunto funcional de 27 archivos verificado con SHA-256.
- [x] Pruebas principales de juego, audio y guardado/carga correctas.
- [ ] Integridad física sectorial de cada CD demostrada (**no requerida para la validación funcional**, pero debe declararse).
- [ ] Cobertura de escenas/rutas/finales suficiente para afirmar funcionalidad exhaustiva.
- [ ] Copia de referencia declarada inmutable y copia de seguridad verificada.
- [ ] Inventarios/errores exactos de UltraISO y hashes de las cuatro ISO preservados.
- [ ] Actualizar formalmente el estándar público si se incorpora la categoría de «preservación funcional validada» como cierre normativo.

**Estado final documentable:** **preservación funcional con pruebas principales satisfactorias; cierre de custodia pendiente**.

## 11. Observaciones

La existencia de una protección Ring PROTECH no está demostrada de forma inequívoca. La denominación comercial de la edición concreta y la sustitución exacta de sectores quedan fuera de lo probado. La ausencia de coincidencia entre hashes de `BOARD.MIX` en extracciones distintas no debe ocultarse.
