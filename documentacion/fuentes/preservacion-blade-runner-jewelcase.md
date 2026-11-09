Este registro explica cómo PC Game Archive ha recuperado una **copia digital funcional de Blade Runner, edición española Jewel Case distribuida por Dinamic Multimedia**, a partir de los cuatro CD-ROM conservados en [su ficha del archivo](../../../juegos/blade-runner-jewelcase/). Las imágenes y los archivos del videojuego no se distribuyen desde esta web.

**Estándar de referencia:** [Estándar de preservación digital v1.0](../estandar-preservacion-digital/). La validación funcional y la fidelidad física se describen por separado, porque una no demuestra la otra.

## La dificultad de esta edición

Durante la lectura del primer CD se observaron errores repetidos en tres ejemplares de la edición española. Redumper e IsoBuster encontraron errores cerca del LBA 18.872 y Windows no consiguió leer por completo `BASE2/BOARD.MIX`. La superficie del CD presentaba un anillo diferenciado.

Estos datos son compatibles con una región de lectura anómala, posiblemente relacionada con una protección física, pero **no permiten identificar de forma definitiva su mecanismo comercial**. La búsqueda automática de MPF no identificó una protección conocida.

## Recuperación de los datos

Se utilizaron las extracciones de archivos de los cuatro CD realizadas con **UltraISO**, en lugar de insistir en volcados sectoriales que no terminaban. También se reconstruyeron cuatro imágenes ISO que pudieron montarse y cuyo contenido pudo visualizarse.

Para ejecutar el juego se preparó un conjunto de **27 archivos de datos** procedentes de los cuatro discos. Los nombres repetidos se contrastaron mediante tamaños y SHA-256 y los cuatro `CDFRAMES.DAT` se conservaron con nombres individuales (`CDFRAMES1.DAT` a `CDFRAMES4.DAT`). Se verificó por SHA-256 que los archivos de la copia de trabajo coincidían con sus respectivas fuentes extraídas.

La recuperación **no acredita una imagen bit a bit idéntica a los CD originales**: pueden haberse perdido sectores no legibles y características físicas de la edición. La extracción de una copia anterior de `BOARD.MIX` produjo un hash diferente al de la utilizada en las pruebas; esta diferencia se conserva en el registro interno.

## Resultado funcional comprobado

En **Windows 10, mediante ScummVM 2026.4.0**, el conjunto fue reconocido como `Blade Runner (Windows/Spanish)`. Se utilizó la modalidad original, sin activar contenido restaurado.

Se confirmaron **introducción, inicio y jugabilidad, voces españolas, música, efectos y vídeos observados**, así como **guardado, cierre, nuevo arranque, carga y continuación de partida**. El instalador histórico no pudo ejecutarse directamente en Windows 10 x64 debido a un componente de 16 bits.

## Alcance y límites

**Resultado: recuperación funcional validada en las pruebas principales.** No se han documentado recorridos completos de la aventura, todas sus rutas y finales, ni una verificación sectorial íntegra de los cuatro soportes. El estado de custodia inmutable y la copia de seguridad verificada permanecen pendientes de confirmación.

El procedimiento concreto de ejecución se explica en la [guía para jugar a Blade Runner en Windows 10 con ScummVM](../../guias/blade-runner-jewelcase-scummvm-windows-10/).
