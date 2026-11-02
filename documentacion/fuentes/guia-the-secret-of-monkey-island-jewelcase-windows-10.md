Esta guía recoge el procedimiento **probado por PC Game Archive** para ejecutar **The Secret of Monkey Island — edición Jewel Case en CD-ROM** en Windows 10, utilizando una copia de trabajo verificada de la edición conservada en [su ficha del archivo](../../../juegos/the-secret-of-monkey-island-jewelcase/).

El procedimiento validado emplea **IsoBuster 5.8** para extraer los archivos de datos y las 24 pistas de audio, y **ScummVM 2026.4.0** para ejecutar la variante española `CD/DOS/Spanish`. La música funcionó **sin convertir los WAV** una vez situados en el directorio correcto y nombrados exactamente `track01.wav` a `track24.wav`.

> Esta validación corresponde a la edición conservada y al entorno realmente probado. No acredita el funcionamiento de otros prensados, ediciones o sistemas operativos.

## Resultado esperado

- Detección del juego como **The Secret of Monkey Island (CD/DOS/Spanish)**.
- Introducción, gráficos 2D, interacción y diálogos escritos en español correctos.
- Música de las 24 pistas CD-DA reproducida correctamente mediante los WAV extraídos.
- Ausencia de voces de personajes: **comportamiento propio de esta edición**, no una incidencia.
- Guardado, carga y segundo arranque confirmados por la prueba de laboratorio.

## Entorno de prueba

- **Sistema operativo utilizado:** Windows 10 (confirmado durante la sesión).
- **Herramientas:** IsoBuster 5.8 y ScummVM 2026.4.0.
- **Entorno de referencia:** [PCGA-LAB-01](../../laboratorio/pcga-lab-01/). Su ficha documenta un Windows 10 Pro 22H2 x64 con AMD Ryzen 5 PRO 4650U, 16 GB RAM y Radeon Graphics; no se realizó en esta sesión una nueva captura completa de la configuración del anfitrión.
- **Sin conversores de audio, parches ni ajustes adicionales** en el procedimiento final.

## Punto de partida: copia de trabajo verificada

Los archivos de imagen utilizados procedían de un máster BIN/CUE y se copiaron a una carpeta de trabajo independiente. Antes de abrirlos se verificaron los SHA-256 siguientes, ambos coincidentes con los registrados para el máster:

```text
Image.bin  88A546BF6391FA0AE066FBEC5A84F810BBBE363AF3C3FC73B7C24EBF01B982D3
Image.cue  1330620E8A913A3BA9D9DF90C96EBFC2C6B86D1C5A9CEFBEE060B429947A435F
```

Puedes comprobarlos en PowerShell desde la carpeta donde estén los dos archivos:

```powershell
Get-FileHash .\Image.bin -Algorithm SHA256
Get-FileHash .\Image.cue -Algorithm SHA256
```

**No trabajes sobre los archivos del máster de preservación.** Las operaciones siguientes se realizan sobre la copia de trabajo.

## 1. Abrir la imagen en IsoBuster

1. Abre **IsoBuster 5.8**.
2. Selecciona **Archivo → Abrir archivo de imagen** y elige `Image.cue`.
3. Comprueba que aparece **una sesión con 25 pistas**: `Pista 01` de datos y `Pista 02` a `Pista 25` de audio CD-DA.
4. Dentro de `Pista 01` se identificaron las estructuras `ISO9660` y `HFS`; para este procedimiento se utilizó la de **ISO9660**.

![Árbol de IsoBuster con la sesión y las 25 pistas de la imagen de Monkey Island](./img/01-isobuster-pistas.png)

## 2. Extraer los archivos de datos

1. En IsoBuster despliega `Pista 01` y entra en el sistema de archivos **ISO9660**.
2. Extrae su contenido completo, manteniendo los nombres y la estructura original, a una carpeta de trabajo, por ejemplo `datos_extraidos`.
3. Verifica que se mantienen las carpetas de idioma `ENGLISH`, `FRENCH`, `GERMAN`, `ITALIAN` y `SPANISH` y los archivos presentes en la raíz.

![Archivos y directorios de idioma de la edición observados en IsoBuster](./img/02-isobuster-datos.png)

En el laboratorio la extracción terminó sin errores.

## 3. Extraer las 24 pistas de audio CD-DA

1. Desde el mismo `Image.cue` abierto en IsoBuster, selecciona `Pista 02`.
2. Utiliza la opción de **extraer audio a un archivo WAV** y guarda el archivo; la primera extracción produjo `Pista 02.wav`.
3. Repite el procedimiento para `Pista 03` hasta `Pista 25`, conservando los WAV originales extraídos en una carpeta de trabajo separada.
4. Se obtuvieron **24 WAV**, cuya extracción se comunicó como completada.

## 4. Preparar los WAV: paso imprescindible para que se oiga la música

En esta edición, **la nomenclatura y la ubicación de los archivos fueron determinantes**. En la validación inicial ScummVM mostraba un aviso de pistas de audio y, con `track2.wav`, no se oyó música. El resultado correcto se obtuvo al colocar **todos** los WAV en el directorio de idioma español y renombrar las **copias** mediante numeración secuencial de **dos cifras**:

- `Pista 02.wav` → **`track01.wav`**
- `Pista 03.wav` → **`track02.wav`**
- `Pista 04.wav` → **`track03.wav`**
- …
- `Pista 25.wav` → **`track24.wav`**

**Importante:** la numeración de audio empieza en `01` aunque el CD físico empieza el audio en `Pista 02`, ya que `Pista 01` contiene datos. Usa el patrón **`trackXX.wav`**, con `01`, `02`, ..., `24`; no cambies el formato WAV ni conviertas a FLAC, MP3 u otro formato para reproducir el procedimiento probado.

Copia esos 24 ficheros junto a los datos de juego **dentro de `ISO 9660\SPANISH`** (la carpeta `SPANISH` del contenido ISO9660 extraído). Conserva sin modificaciones los WAV procedentes de IsoBuster y el BIN/CUE de trabajo.

La disposición utilizada para ejecutar la variante española es, de manera esquemática:

```text
ISO 9660/
└── SPANISH/
    ├── [archivos originales de la edición española]
    ├── track01.wav
    ├── track02.wav
    ├── ...
    └── track24.wav
```

**No basta con dejarlos en una carpeta `audio_extraido` separada**: en la prueba final se colocaron en el directorio desde el que ScummVM detectó esta variante.

## 5. Detectar la edición española en ScummVM

1. Abre **ScummVM 2026.4.0**.
2. Pulsa **Añadir juego / Add Game**.
3. Navega **hasta la carpeta `ISO 9660\SPANISH`**, no te detengas en la raíz de `datos_extraidos`.
4. Comprueba que detecta **The Secret of Monkey Island**, variante **`CD/DOS/Spanish`**.
5. Añade el juego y ejecútalo manteniendo la configuración utilizada durante la prueba; no fue necesario aplicar ajustes especiales.

![Detección de The Secret of Monkey Island CD/DOS/Spanish al seleccionar el subdirectorio SPANISH](./img/03-scummvm-deteccion.png)

## 6. Diagnóstico: juego sin música o aviso de pistas de audio

Durante la primera ejecución **el juego arrancó, pero ScummVM avisó de que no encontraba las pistas CD-DA**. La prueba con un WAV aislado llamado `track2.wav` no produjo sonido.

![Aviso de ScummVM sobre las pistas de audio durante el primer arranque](./img/04-scummvm-aviso-audio.png)

**Solución validada en PC Game Archive:** copiar todas las pistas WAV a `ISO 9660\SPANISH` y renombrarlas como **`track01.wav` hasta `track24.wav`**, preservando la correspondencia entre la pista física 02 y `track01.wav`. Tras hacerlo, **la música se escuchó correctamente**, sin realizar ninguna conversión de audio.

Si reproduces la prueba y no escuchas música, comprueba primero **la ruta, el número de archivos, la numeración con dos dígitos y la extensión `.wav`**. La sesión no acreditó que otras nomenclaturas o conversiones sean necesarias.

## 7. Jugar, guardar y cargar

Una vez preparado el audio, el juego se ejecutó con gráficos, música, interacción por ratón y diálogos de texto en español correctos según las pruebas realizadas. **No hay voces habladas de los personajes en esta edición**; no debe confundirse esa característica con una avería de sonido.

Se confirmó también el **guardado de partida, cierre del juego, segundo arranque, carga de la partida y continuación de la jugabilidad**. No se ha acreditado una partida completa de principio a fin.

## Procedimiento final reproducible

1. Copiar `Image.bin` y `Image.cue` a una carpeta de trabajo separada y comprobar sus SHA-256.
2. Abrir `Image.cue` en IsoBuster 5.8 y comprobar la sesión de 25 pistas.
3. Extraer completo el sistema de archivos ISO9660 respetando carpetas e idiomas.
4. Extraer a WAV las pistas físicas 02–25 (24 archivos).
5. Crear copias de esos WAV con los nombres **`track01.wav` a `track24.wav`** y colocarlas en **`ISO 9660\SPANISH`**.
6. En ScummVM 2026.4.0, añadir el juego seleccionando **esa carpeta `SPANISH`** y verificar la detección `CD/DOS/Spanish`.
7. Iniciar, comprobar la reproducción musical, jugar y realizar una prueba de guardado, cierre, segundo arranque y carga.

## Matriz funcional de la edición probada

- **Instalación:** `No aplicable` — ejecución desde datos extraídos y ScummVM.
- **Arranque:** `Correcto` — ejecución confirmada.
- **Menús:** `Correcto` — interacción y opciones de guardado/carga utilizadas.
- **Vídeos/cinemáticas:** `Correcto` — introducción visualizada durante las pruebas.
- **Gráficos 2D:** `Correcto` — jugabilidad confirmada.
- **Gráficos 3D:** `No aplicable`.
- **Sonido (efectos):** `No probado` individualmente — no se realizó comprobación desglosada de efectos.
- **Música:** `Correcto` — 24 WAV identificados y música escuchada.
- **Voces:** `No aplicable` — esta edición presenta diálogos escritos.
- **Teclado/ratón:** `Correcto` para la interacción con ratón; el teclado no se evaluó por separado.
- **Gamepad/joystick:** `No probado`.
- **Inicio de partida:** `Correcto`.
- **Juego representativo:** `Correcto` — confirmado por el responsable.
- **Guardado:** `Correcto`.
- **Carga:** `Correcto`.
- **Cambio de escena:** `Correcto` durante la jugabilidad comunicada, sin recorrido completo documentado.
- **Cambio de disco:** `No aplicable` — un solo CD físico.
- **Multijugador:** `No aplicable`.
- **Cierre:** `Correcto`.
- **Segundo arranque:** `Correcto`.

## Limitaciones y elementos no probados

- Validación específica de esta edición y del entorno Windows 10 utilizado.
- Sin partida completa de principio a fin documentada.
- Sin pruebas específicas de gamepad, joystick, otros sistemas operativos u otras ediciones.
- Efectos sonoros y teclado no sometidos a pruebas aisladas documentadas.
- No se probó aquí una ejecución nativa de MS-DOS ni desde una unidad virtual sin ScummVM.

## Fuentes y documentación relacionada

- [Ficha de The Secret of Monkey Island — Jewel Case](../../../juegos/the-secret-of-monkey-island-jewelcase/).
- [Preservación digital de esta edición](../../preservacion/the-secret-of-monkey-island-jewelcase/).
- [Sitio oficial de IsoBuster](https://www.isobuster.com/).
- [Sitio oficial de ScummVM](https://www.scummvm.org/downloads/).

## Estado final

**Funcional con ajustes**, mediante extracción de datos y audio desde la copia de trabajo y reproducción en ScummVM 2026.4.0. Los resultados corresponden a las pruebas realizadas el **02/11/2026**.
