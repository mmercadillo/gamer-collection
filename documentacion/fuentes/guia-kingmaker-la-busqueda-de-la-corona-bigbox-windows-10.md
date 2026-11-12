# Kingmaker: La Búsqueda de la Corona — instalación y versión portable en Windows 10

**PC Game Archive · Guía de ejecución y compatibilidad**  
**Pieza:** #000249 · Edición española Big Box · DOS  
**Ficha:** https://www.pcgamearchive.org/juegos/kingmaker-la-busqueda-de-la-corona-bigbox/  
**Fecha de pruebas:** 12/11/2026  
**Estado:** Funcional con emulación DOSBox Staging; portabilidad comprobada en Windows 10

> Esta guía documenta el procedimiento probado con la edición física conservada por PC Game Archive. Está dirigida a quienes disponen legítimamente de su propia copia del juego. No incluye ni distribuye imágenes de disquetes, ejecutables propietarios ni archivos del juego. Las rutas usadas son ejemplos: deben adaptarse a cada equipo. La documentación de preservación física y digital se mantiene en un artículo independiente.

## 1. Identificación de la edición

| Dato | Valor |
|---|---|
| Juego | *Kingmaker: La Búsqueda de la Corona* |
| Edición | Española Big Box |
| Identificador PCGA | `000249` |
| Soportes originales | 2 disquetes de 3,5 pulgadas HD, 1,44 MB |
| Disco 1 | `KING.LZH`, `INSTALL.EXE`, `LHA.EXE` (archivos principales observados) |
| Disco 2 | `ESPEECH.LZH`, `EVOICE.LZH` (archivos principales observados) |
| Versión mostrada por el juego | 1.1 |
| Idioma verificado en pantalla | Español |

## 2. Punto de partida y alcance

Las pruebas partieron de **imágenes IMA de trabajo** derivadas de adquisiciones digitales verificadas por dos lecturas independientes y coincidentes de cada disquete. Los másteres se conservan separadamente en el servidor de preservación; **no se utilizan para instalaciones ni experimentos**.

| Imagen de referencia de trabajo | Tamaño | SHA-256 registrado |
|---|---:|---|
| `KINGMAKER_DISCO_1.IMA` | 1.474.560 bytes | `AC37AF63F1EEADF41749DF1CEB989EED902987D8E46D114380B446FC15BF8291` |
| `KINGMAKER_DISCO_2.IMA` | 1.474.560 bytes | `4272574B157D2AEC9A418FEEFC59D32B3A58BCFB4E8B4AD6AF21DC3EBB56D303` |

Estos hashes corresponden **a las imágenes concretas de PC Game Archive**. No son valores esperables para todas las copias o ediciones de Kingmaker. La coincidencia entre adquisiciones acredita reproducibilidad de los archivos obtenidos, no fidelidad magnética completa.

El resultado funcional de esta guía se refiere a **Windows 10 con DOSBox Staging**. No se ha probado Windows 11, ejecución nativa DOS en hardware original ni portabilidad a otros sistemas operativos.

## 3. Entorno probado

| Componente | Configuración empleada |
|---|---|
| Identificador del laboratorio | `PCGA-LAB-01` |
| Sistema anfitrión | Windows 10 Pro 22H2, x64 |
| Build de referencia del laboratorio | 19045.6466 |
| CPU | AMD Ryzen 5 PRO 4650U |
| Memoria | 16 GB |
| Gráficos | AMD Radeon Graphics |
| Resolución de referencia | 1920 × 1080 |
| Emulador | **DOSBox Staging 0.83.0**, distribución portable |
| Versión/build observada en arranque | 0.83.0 (`7b400`) |
| DOS emulado reportado por `VER` | DOS 5.00 |
| Sonido seleccionado | AdLib / Sound Blaster |
| Ajustes mostrados por instalador | Puerto `220`, IRQ `7`, DMA `1` |

Las opciones de sonido mostradas por el instalador y la selección de AdLib/Sound Blaster fueron comprobadas durante el proceso. No se midió latencia ni se verificaron exhaustivamente todas las variantes de audio.

## 4. Herramientas y requisitos

- **DOSBox Staging 0.83.0 para Windows (ZIP portable)**: https://www.dosbox-staging.org/releases/windows/. Se copia el contenido completo de la distribución, incluidos archivos auxiliares.
- **Dos imágenes de trabajo** de los disquetes originales, identificadas como `KINGMAKER_DISCO_1.IMA` y `KINGMAKER_DISCO_2.IMA`.
- **Windows 10 x64** y permiso de escritura en una carpeta de trabajo y en la carpeta portable final.
- **WinImage 11.00 x64** se utilizó previamente para la adquisición de los disquetes, pero **no es necesario para ejecutar el paquete portable una vez instalado**.

No se ha registrado en esta prueba un hash de la distribución de DOSBox ni del ejecutable instalado; conviene conservar esa referencia si se pretende una réplica exacta del entorno en el futuro.

## 5. Preparación de las carpetas de trabajo

Las rutas siguientes son **ejemplos anonimizados**, no rutas obligatorias. En esta guía se utiliza `C:\PCGA\Kingmaker` como raíz de trabajo; puede sustituirse por otra carpeta local, incluidas rutas en otras unidades.

```text
C:\PCGA\Kingmaker\
├── discos\
│   ├── KINGMAKER_DISCO_1.IMA
│   └── KINGMAKER_DISCO_2.IMA
└── DOS_C\                  ← inicialmente vacía
```

Las imágenes utilizadas deben ser copias de trabajo, no los másteres preservados. Las pruebas de instalación crearán archivos en `DOS_C`.

Se puede preparar la carpeta de destino con PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "C:\PCGA\Kingmaker\DOS_C"
```

## 6. Comprobación nativa en Windows 10

Se extrajo `INSTALL.EXE` desde la imagen de trabajo del Disco 1. El archivo presentaba 22.392 bytes y fecha 09/11/1993. Al invocarlo directamente desde PowerShell de Windows 10 x64:

```powershell
.\INSTALL.EXE
```

Windows devolvió el error de que el ejecutable especificado **no era una aplicación válida para esta plataforma**. Por tanto, **la instalación nativa directa no funcionó en el entorno probado**. No se aplicaron parches, permisos elevados ni modos de compatibilidad para intentar forzarla.

## 7. Instalación desde las imágenes en DOSBox Staging

### 7.1. Arrancar DOSBox

Extraer el ZIP portable de DOSBox Staging a una carpeta temporal y abrir su ejecutable `dosbox.exe`. En la sesión de referencia el emulador arrancó y mostró `Z:\>`; el comando `VER` informó de DOS 5.00.

### 7.2. Montar el disco duro virtual y los dos disquetes

En la consola de DOSBox, ejecutar **adaptando la carpeta de ejemplo a la ubicación real de las imágenes**:

```dos
MOUNT C "C:\PCGA\Kingmaker\DOS_C"
MOUNT A "C:\PCGA\Kingmaker\discos\KINGMAKER_DISCO_1.IMA" "C:\PCGA\Kingmaker\discos\KINGMAKER_DISCO_2.IMA" -t floppy
A:
DIR
```

Se comprobó que el directorio `A:` mostraba `KING.LZH`, `INSTALL.EXE` y `LHA.EXE`. En DOSBox Staging 0.83.0 se utilizó `MOUNT`; el comando heredado `IMGMOUNT` mostró un aviso de obsolescencia en esta versión.

**Incidencia observada durante el laboratorio:** inicialmente la imagen no se montaba y se mostraba `Can't create drive from file`. Tras cerrar WinImage y repetir el montaje, la imagen se montó correctamente. Esto es una correlación observada; no se demostró que WinImage fuera la causa exacta del bloqueo. Si ocurre, comprobar ruta, accesibilidad del archivo y posibles programas que lo mantengan abierto antes de alterar la imagen.

### 7.3. Ejecutar el instalador

Con la unidad `A:` activa:

```dos
INSTALL
```

Se comprobó que el instalador original funcionaba en DOSBox y permitía usar esta configuración inicial:

| Parámetro del instalador | Valor empleado |
|---|---|
| Idioma | `Spanish` |
| Voces | `Enabled` |
| Tarjeta de sonido | `Sound Blaster & compatibles` |
| Puerto / IRQ / DMA | `220` / `7` / `1` |
| Unidad de destino | `C:` |
| Directorio de destino | `C:\KING` |

En el menú principal se seleccionó la opción de **instalar Kingmaker en el disco duro**. Cuando el instalador pidió la unidad, se eligió `C`; al proponer `C:\KING`, se aceptó el valor predeterminado.

### 7.4. Cambio al segundo disquete

Durante la instalación apareció la solicitud de insertar el **disco 2**. En la sesión verificada, con **ambas imágenes ya declaradas en el mismo comando `MOUNT A`**, bastó pulsar **Enter** para que el instalador continuase: **no fue necesario pulsar `Ctrl + F4` manualmente**.

Esta es la secuencia realmente observada. No se ha establecido que el mismo comportamiento esté garantizado en todas las versiones de DOSBox ni con otras ediciones. Si en otra instalación el cambio no se produce, comprobar la selección de imágenes antes de seguir; no repetir indefinidamente la lectura ni modificar los originales.

### 7.5. Comprobar la instalación

Al terminar el instalador, se verificó en DOSBox:

```dos
C:
CD \KING
DIR
```

Se identificaron `KING.EXE`, `DMA.CFG` y numerosos recursos del juego (`.VOC`, `.LBM`, `.MUS`, entre otros). El directorio creado en Windows corresponde a:

```text
C:\PCGA\Kingmaker\DOS_C\KING\
```

El contenido instalado quedó disponible en el disco duro virtual sin necesidad de modificar las imágenes de preservación.

## 8. Primera ejecución y ajustes realmente necesarios

Desde DOSBox, con `C:\KING` como directorio actual:

```dos
KING
```

El juego se inició y mostró su configuración de sonido. Se seleccionó **AdLib/Sound Blaster**; se confirmó que la interfaz aparecía en español y que era posible iniciar una partida, con gráficos, música y audio funcionando durante la prueba.

**No se necesitaron parches del juego, wrappers gráficos ni modificaciones de archivos originales**. La intervención necesaria fue utilizar DOSBox Staging para proporcionar un entorno DOS. La primera prueba de ejecución nativa de `INSTALL.EXE` en Windows 10 x64 había fallado.

## 9. Construir Kingmaker Portable

Después de comprobar la instalación, se preparó un paquete autocontenido para uso local. **Cerrar el juego y DOSBox antes de copiar los archivos**, especialmente si existen partidas guardadas.

### 9.1. Estructura final

```text
Kingmaker-Portable\
├── Kingmaker.bat
├── DOSBox\
│   ├── dosbox.exe
│   └── ... resto de archivos y subcarpetas del ZIP portable ...
├── config\
│   └── kingmaker.conf
└── juego\
    └── KING\
        ├── KING.EXE
        ├── DMA.CFG
        └── ... todos los archivos instalados y guardados ...
```

**Importante:** no basta con copiar únicamente `KING.EXE`; debe copiarse **todo el directorio `DOS_C\KING`**, incluidos recursos, configuración y archivos de guardado. En la versión portable funcional validada **no fue necesario incluir las imágenes `.IMA`**, porque se ejecutó el juego ya instalado.

Copiar el contenido completo del ZIP **portable de DOSBox Staging 0.83.0** dentro de `Kingmaker-Portable\DOSBox\`.

### 9.2. Archivo de configuración local

Crear `Kingmaker-Portable\config\kingmaker.conf` con la configuración usada y validada para arrancar a pantalla completa:

```ini
# PC Game Archive - Kingmaker
# DOSBox Staging 0.83.0

[sdl]
fullscreen = on
fullscreen_mode = standard
```

El cambio a pantalla completa también puede alternarse durante la ejecución con **Alt + Enter**. Otros parámetros (escalado, filtros, emulación de sonido detallada) no se modificaron porque el comportamiento inicial fue satisfactorio.

### 9.3. Lanzador portable definitivo

Crear `Kingmaker-Portable\Kingmaker.bat` con el siguiente contenido, correspondiente al lanzador que finalmente funcionó, **añadiendo la configuración local de pantalla completa que se comprobó posteriormente**:

```bat
@echo off
setlocal

rem PC Game Archive - Kingmaker Portable
rem DOSBox Staging 0.83.0

set "BASE=%~dp0"

"%BASE%DOSBox\dosbox.exe" ^
    --noprimaryconf ^
    --nolocalconf ^
    --conf "%BASE%config\kingmaker.conf" ^
    "%BASE%juego\KING\KING.EXE"

endlocal
```

`%~dp0` resuelve la carpeta que contiene el propio `.bat`, evitando rutas de usuario y letras de unidad fijas. El argumento final indica a DOSBox el ejecutable DOS a abrir; esta variante **sí arrancó Kingmaker**, a diferencia de una primera variante de lanzador con órdenes `-c MOUNT` y comillas anidadas que no inició el juego.

La configuración del archivo `.conf` se carga expresamente; las opciones de línea de comandos impiden que las configuraciones primaria y local ajenas se utilicen en esta ejecución. El paquete debe conservar sus archivos unidos: no mover por separado `dosbox.exe`, `kingmaker.conf` o la carpeta `juego`.

### 9.4. Ejecución

Hacer doble clic en `Kingmaker.bat`. En la prueba, DOSBox arrancó Kingmaker correctamente desde el paquete y, tras añadir `kingmaker.conf`, lo hizo directamente a pantalla completa.

Atajos útiles del entorno probado:

| Teclas | Acción |
|---|---|
| `Alt + Enter` | Alternar entre pantalla completa y ventana |
| `Ctrl + F10` | Capturar o liberar el ratón |
| `Ctrl + F9` | Cerrar DOSBox inmediatamente; utilizar preferentemente la salida normal del juego |

## 10. Validación de portabilidad

La prueba de portabilidad se realizó **copiando la carpeta completa `Kingmaker-Portable` a otra ubicación de Windows 10** y lanzando allí `Kingmaker.bat`, sin cambiar ninguna ruta en los archivos de configuración.

**Resultados comunicados y comprobados en la sesión de laboratorio:**

1. El paquete arrancó el juego desde la ubicación original.
2. El paquete volvió a arrancarlo tras trasladarlo a otra carpeta.
3. El juego permitió iniciar una partida y utilizar música y sonido.
4. Se probó el guardado y posteriormente se confirmó la **carga de la partida guardada desde la nueva ubicación**.
5. Se probó el inicio directo a pantalla completa mediante `kingmaker.conf`.

La prueba acredita independencia de la ruta original **en el mismo entorno Windows 10 utilizado**. No constituye una prueba de funcionamiento en todos los equipos, versiones de Windows o plataformas.

## 11. Matriz de validación funcional

Criterio: `Correcto`, `Correcto con limitaciones`, `No funcional`, `No probado`, `No aplicable`.

| Subsistema | Estado | Evidencia / alcance |
|---|---|---|
| Instalación nativa en Windows 10 x64 | No funcional | `INSTALL.EXE` rechazado por Windows |
| Instalación mediante DOSBox Staging | Correcto | Instalación realizada con los dos disquetes |
| Arranque | Correcto | `KING.EXE` llega a la interfaz del juego |
| Menús | Correcto | Selección de sonido e inicio de partida |
| Vídeos / cinemáticas | No probado | No se registró prueba específica |
| Gráficos 2D | Correcto | Gráficos visibles durante la partida |
| Gráficos 3D | No probado | Sin prueba ni conclusión de aplicabilidad |
| Sonido | Correcto | Audio perceptible durante la prueba |
| Música | Correcto | Música perceptible durante la prueba |
| Teclado / ratón | Correcto con limitaciones | Interacción con el juego posible; no se validaron todos los controles |
| Gamepad / joystick | No probado | Sin prueba específica |
| Inicio de partida | Correcto | Partida iniciada satisfactoriamente |
| Juego representativo | Correcto con limitaciones | Se jugó, sin documentar una campaña extensa |
| Guardado | Correcto | Guardado confirmado en laboratorio |
| Carga | Correcto | Carga confirmada tras trasladar el paquete |
| Cambio de nivel / escena | No probado | Sin prueba específica registrada |
| Cambio de disquete durante instalación | Correcto | Solicitud del segundo disco resuelta pulsando Enter con las dos imágenes montadas |
| Dependencia de discos durante el juego | Correcto con limitaciones | Arranque y partida en paquete sin IMA; no se probaron todos los escenarios de juego |
| Multijugador | No probado | No se registró prueba específica |
| Cierre normal del juego | No probado | Sin registro específico de comprobación |
| Segundo arranque tras cerrar el juego | Correcto | Se arrancó tras trasladar el paquete |
| Portabilidad de rutas | Correcto | Funcionó desde una segunda ubicación en Windows 10 |
| Pantalla completa | Correcto | Inicio directo mediante archivo de configuración |

## 12. Limitaciones conocidas

- Es necesaria una capa de emulación: el instalador original no se ejecutó directamente en Windows 10 x64.
- La reproducción funcional se ha validado con **DOSBox Staging 0.83.0**; otras versiones no se han ensayado en este expediente.
- La prueba se realizó en Windows 10; **no hay resultados propios para Windows 11, Linux, macOS ni otros anfitriones**.
- La portabilidad entre carpetas del mismo equipo no acredita automáticamente portabilidad entre ordenadores con hardware o configuraciones distintas.
- No se verificó cada rama, escenario, dispositivo de entrada o sistema secundario del juego.
- El paquete es un **derivado privado de trabajo**: la guía no autoriza la redistribución del software del juego o de sus imágenes.

## 13. Elementos no probados

- Compatibilidad y comportamiento en Windows 11.
- Campaña completa y pruebas prolongadas de estabilidad.
- Cinemáticas, gráficos 3D, joystick/gamepad y multijugador, en su caso.
- Comportamiento de todos los modos de audio disponibles.
- Cierre normal repetido, reinstalación a partir de cero en un segundo ordenador o replicación mediante una versión distinta de DOSBox.

## 14. Problemas descartados e intentos fallidos (trazabilidad de laboratorio)

Estos datos se incluyen en el **registro técnico** de la experiencia, pero no forman parte de la secuencia final necesaria para el usuario:

- `INSTALL.EXE` no pudo ejecutarse nativamente en Windows 10 x64.
- El montaje inicial de una imagen `.IMA` falló con `Can't create drive from file`; tras cerrar WinImage y reintentar, se montó.
- La primera instalación se interrumpió al solicitar el segundo disquete, porque inicialmente solo se había montado la primera imagen. Se limpió la carpeta de instalación y se repitió con ambas imágenes especificadas.
- Un primer `Kingmaker.bat` basado en una secuencia de opciones `-c` no arrancó el juego; se sustituyó por un lanzador que pasa la ruta del ejecutable directamente a DOSBox.

## 15. Fuentes y evidencias

**Evidencia propia PC Game Archive (12/11/2026):** capturas del instalador español, del montaje en DOSBox, del directorio instalado, del menú de selección de sonido, pruebas de inicio de partida, guardado, carga, traslado del paquete y pantalla completa; hashes SHA-256 de las imágenes obtenidas previamente. Los resultados de guardado, traslado y reproducción sonora se confirmaron durante la sesión, aunque no se adjunta en esta guía un log automático de cada acción.

**Referencia de software:** [Sitio oficial de DOSBox Staging](https://www.dosbox-staging.org/), distribución portable de Windows 0.83.0. Esta referencia no sustituye los resultados de las pruebas propias.

**Estado final:** **Funcional con ajustes / emulación**, con **paquete portable validado en Windows 10** dentro del alcance de las pruebas indicadas. La versión portable y la instalación son derivados de uso privado, diferenciados de los másteres de preservación.

---

*PC Game Archive — expediente de compatibilidad de Kingmaker, ficha #000249. Documento independiente del artículo de preservación de los disquetes.*
