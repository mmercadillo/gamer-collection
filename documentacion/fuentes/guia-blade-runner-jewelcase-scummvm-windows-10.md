Esta guía describe cómo se ha conseguido ejecutar **Blade Runner — edición española Jewel Case de Dinamic Multimedia**, conservada por [PC Game Archive](../../../juegos/blade-runner-jewelcase/), en **Windows 10 mediante ScummVM 2026.4.0**. El objetivo es reproducir la edición española conservada, no sustituirla por la edición inglesa ni por la opción de contenido restaurado.

## Resultado comprobado

En el entorno probado se reconoció la variante `Blade Runner (Windows/Spanish)`, se reprodujo la introducción y el juego arrancó correctamente. Se comprobaron voces en español, música, efectos y escenas audiovisuales observadas. También funcionaron guardar, cerrar, volver a abrir, cargar y continuar la partida. No se ha comprobado toda la aventura ni todos los finales.

## Material necesario

- Archivos **recuperados legítimamente de los cuatro CD-ROM** de esta edición española.
- Un equipo Windows 10; prueba realizada en el entorno de referencia [PCGA-LAB-01](../../laboratorio/pcga-lab-01/). No se realizó una nueva caracterización completa del hardware durante esta sesión.
- **ScummVM 2026.4.0**, utilizado en las pruebas.
- Espacio suficiente para una carpeta de trabajo con aproximadamente 1,84 GiB de datos seleccionados.

Las imágenes ISO reconstruidas pueden conservarse por separado, pero **no es necesario montarlas para jugar con el procedimiento final validado**.

## Preparar los archivos de los cuatro discos

1. Conservar intactos los archivos extraídos de los cuatro CD, cada uno en una carpeta independiente.
2. Crear un directorio de trabajo vacío, por ejemplo `Blade_Runner_ES_ScummVM`.
3. Copiar a él los archivos de datos con extensiones `.MIX`, `.TLK` y `.DAT` de los cuatro CD.
4. Cambiar el nombre de **cada** `CDFRAMES.DAT` según su disco: `CDFRAMES1.DAT`, `CDFRAMES2.DAT`, `CDFRAMES3.DAT` y `CDFRAMES4.DAT`.
5. Si un nombre está repetido en discos diferentes (como `A.TLK`, `3.TLK` o `VQA3.MIX` en la extracción probada), **comprobar que los bytes coinciden** antes de conservar una única copia. No renombrar por intuición `3.TLK` ni `VQA3.MIX` como si fueran archivos del disco 4.
6. Verificar mediante SHA-256 que cada fichero copiado coincide con su fuente. En la prueba de PC Game Archive se obtuvieron **27 archivos**.

Por ejemplo, para calcular la huella SHA-256 de un archivo en PowerShell:

```powershell
Get-FileHash '.\Blade_Runner_ES_ScummVM\STARTUP.MIX' -Algorithm SHA256
```

El hash demuestra que dos ficheros son idénticos entre sí, pero no que la extracción procedente del CD original estuviera libre de sectores sustituidos.

## Ejecutar en ScummVM

1. Abrir **ScummVM 2026.4.0**.
2. Elegir **Añadir juego** y seleccionar el directorio `Blade_Runner_ES_ScummVM` que contiene los datos reunidos. Si el juego ya estaba añadido, abrir sus opciones y modificar la ruta del juego para apuntar a esta carpeta.
3. Si ScummVM ofrece dos variantes, elegir **`Blade Runner (Windows/Spanish)`**, **no** `Blade Runner with restored content (Windows/Spanish)`.
4. Guardar la configuración y pulsar **Start**.
5. Comprobar que la introducción se reproduce, el juego inicia, se escucha el doblaje español y puede guardarse y cargar una partida.

## Por qué no usamos el instalador original

El CD 1 contiene un `INSTALL.EXE` con cabecera **NE** (formato heredado de Windows de 16 bits), que no se ejecutó en Windows 10 x64. El lanzador `SETUP.EXE` no pudo iniciarlo aunque el fichero existía. En el método probado se ejecuta el videojuego mediante ScummVM **sin utilizar el instalador del CD**.

## Matriz funcional de esta edición

| Funcionalidad | Estado | Alcance |
|---|---|---|
| Detección española y arranque | Correcto | ScummVM 2026.4.0 |
| Introducción / escenas observadas | Correcto | No todos los vídeos |
| Juego e interacción inicial | Correcto | No partida completa |
| Voces en español | Correcto | Confirmadas |
| Música y efectos | Correcto | Confirmados |
| Guardar, cerrar, volver a abrir y cargar | Correcto | Continuación confirmada |
| Todas las rutas y finales | No probado | Sin recorrido exhaustivo |
| Gamepad / joystick | No probado | Sin evidencia |
| Instalador original en Windows 10 x64 | No funcional | Componente de 16 bits |

## Limitaciones

El procedimiento está validado sobre esta **edición española de Dinamic Multimedia** y con los archivos recuperados que se probaron. Las imágenes ISO reconstruidas no son una copia física bit a bit y no permiten deducir que todos los recursos del disco original se recuperaron sin sustituciones. La funcionalidad probada no equivale a haber completado todos los finales.

Para conocer las incidencias de lectura y el alcance exacto de la recuperación, consulta el [documento de preservación de la pieza](../../preservacion/blade-runner-jewelcase/).

**Últimas pruebas comunicadas:** 09/11/2026.
