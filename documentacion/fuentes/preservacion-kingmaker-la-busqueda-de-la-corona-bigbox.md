# Preservación digital de Kingmaker: La Búsqueda de la Corona — edición española Big Box

La edición física de **Kingmaker: La Búsqueda de la Corona** conservada por PC Game Archive (ficha **#000249**) incluye **dos disquetes de 3,5 pulgadas de alta densidad (1,44 MB)**. Hemos documentado y recuperado una imagen digital convencional de cada soporte mediante dos lecturas físicas independientes, con comprobación de identidad mediante SHA-256.

Este trabajo documenta la recuperación de los datos accesibles de ambos soportes y las limitaciones técnicas del procedimiento empleado.

**Estándar de referencia:** [Estándar de preservación digital de PC Game Archive v1.0](../estandar-preservacion-digital/).  
**Fecha de las comprobaciones:** 12/11/2026.  
**Resultado:** dos imágenes convencionales IMA obtenidas por doble lectura independiente coincidente por soporte; **fidelidad magnética completa no acreditada**.

## La edición física conservada

- **Juego:** Kingmaker: La Búsqueda de la Corona.
- **Edición:** española Big Box, distribuida por Dro Soft / U.S. Gold.
- **Ficha documental:** [Kingmaker en PC Game Archive](../../../juegos/kingmaker-la-busqueda-de-la-corona-bigbox/).
- **Soportes:** Disco 1/2 y Disco 2/2, ambos disquetes de 3,5 pulgadas HD, 1,44 MB.
- **Inspección visual:** ambos discos presentes y sin daños visibles según la inspección realizada.

Cada disquete se ha tratado como una unidad de adquisición independiente, manteniendo la pertenencia de ambos a una única edición física.

## Caracterización y particularidades

La lectura inicial de los directorios mediante Windows permitió identificar en el **Disco 1** los archivos `KING.LZH`, `INSTALL.EXE` y `LHA.EXE`, con número de serie de volumen `4662-15E1`. En el **Disco 2** se identificaron `ESPEECH.LZH` y `EVOICE.LZH`, sistema de archivos FAT informado por Windows y número de serie `3657-15FA`.

Ambos disquetes contienen además un directorio `System Volume Information`, con fecha de noviembre de 2026, posterior a la de los archivos del juego. Esta presencia se registra como **posible modificación posterior**, sin atribuir su creación a un proceso concreto ni afirmar alteraciones de los archivos originales. El Disco 1 estaba protegido contra escritura durante las comprobaciones; el Disco 2 se introdujo inicialmente sin dicha protección y se protegió posteriormente.

En una primera consulta, Windows no devolvió los metadatos del volumen del Disco 1, aunque una lectura posterior del directorio raíz sí permitió acceder a sus archivos. **No se ha realizado una caracterización magnética ni una evaluación especializada de protección anticopia**. Por tanto, la ausencia de errores visibles o la coincidencia de imágenes no debe interpretarse como demostración de ausencia de protección.

## Unidad y procedimiento utilizado

- **Unidad:** disquetera externa USB identificada por Windows como `Y-E DATA USB-FDU USB Device` (fabricante Y-E Data; `VID_057B`, `PID_0000`; revisión informada `5.01`).
- **Herramienta:** **WinImage 11.00, 64 bits**.
- **Operación:** lectura desde el soporte físico mediante **Disk → Read Disk** y guardado de imagen convencional **IMA**.
- **Método de verificación:** dos lecturas físicas independientes por disquete, cada una guardada como fichero separado, y comparación de sus SHA-256.
- **Tamaño de cada imagen:** **1.474.560 bytes**.

La interfaz USB permite recuperar imágenes lógicas de disquetes convencionales, pero el procedimiento empleado **no captura ni acredita información de flujo magnético, temporizaciones especiales o determinadas protecciones anticopia**.

## Adquisiciones y verificación

Se realizaron **dos lecturas físicas independientes por cada disquete**. Las imágenes obtenidas de cada soporte presentan el mismo SHA-256.

### Disco 1 de 2

- **Adquisición 01:** `KINGMAKER_DISCO_1.IMA`
- **Adquisición 02:** `KINGMAKER_DISCO_1-2.IMA`
- **Verificación:** SHA-256 coincidente.

### Disco 2 de 2

- **Adquisición 01:** `KINGMAKER_DISCO_2.IMA`
- **Adquisición 02:** `KINGMAKER_DISCO_2-2.IMA`
- **Verificación:** SHA-256 coincidente.

### SHA-256 del Disco 1

```text
AC37AF63F1EEADF41749DF1CEB989EED902987D8E46D114380B446FC15BF8291
```

### SHA-256 del Disco 2

```text
4272574B157D2AEC9A418FEEFC59D32B3A58BCFB4E8B4AD6AF21DC3EBB56D303
```

La coincidencia entre las adquisiciones de cada soporte demuestra que las dos lecturas realizadas generaron **la misma secuencia de bytes** para su correspondiente imagen convencional. No constituye por sí sola una validación independiente frente a un original de referencia, ni acredita las características magnéticas que no puede exponer la unidad lectora.

## Estado de la preservación

**Adquisición digital convencional: verificada mediante doble lectura coincidente en ambos soportes.** La conservación definitiva de los archivos como referencias inmutables y su respaldo deben documentarse por separado.

PC Game Archive conserva y documenta el resultado de su trabajo de preservación. **Las imágenes del software no se distribuyen desde esta web**.
