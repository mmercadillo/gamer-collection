Esta guía documenta el procedimiento probado por PC Game Archive para instalar y ejecutar **la edición española Big Box de Red Baron 3-D conservada en la ficha #000215** sobre Windows 10 Pro.

No pretende afirmar que todas las ediciones del juego se comporten igual. Los resultados corresponden a esta edición concreta y al entorno descrito a continuación.

## Punto de partida

La prueba se realizó desde una **copia de trabajo derivada del máster de preservación verificado** de la pieza.

Los ficheros utilizados fueron:

- `REDBARON_3D.bin`
- `REDBARON_3D.cue`

Antes de iniciar las pruebas se comprobó que ambos ficheros conservaban los mismos SHA-256 que el máster:

- BIN: `1E354950083B85F76623CD5BED2F061C90833EB1431ED2BBBD288BEB125BA66B`
- CUE: `CB27C9E074A1BC07DFBF5A967C5641F216CBB2E166D460DF9418EC78BED501F6`

La copia de trabajo se mantuvo separada del máster de preservación.

## Equipo utilizado

- Sistema operativo: Windows 10 Pro 22H2
- Build: 19045
- Procesador: Intel Core i5-3470
- Memoria: 16 GB RAM
- Gráficos: Intel HD Graphics
- Driver gráfico: 10.18.10.4358
- Resolución utilizada durante la prueba: 1360 × 768

## Software utilizado

### WinCDEmu

- Versión: **4.1**
- Finalidad: montar la copia de trabajo BIN/CUE como unidad óptica virtual.

No fue necesario utilizar ningún wrapper, parche comunitario, modo de compatibilidad ni máquina virtual.

## Preparar la copia de trabajo

1. Crear una carpeta independiente del máster de preservación.
2. Copiar a ella `REDBARON_3D.bin` y `REDBARON_3D.cue`.
3. Verificar los SHA-256 antes de comenzar las pruebas.
4. No modificar los ficheros que forman el máster de preservación.

En PowerShell puede comprobarse la integridad con:

```powershell
Get-FileHash .\REDBARON_3D.bin -Algorithm SHA256
Get-FileHash .\REDBARON_3D.cue -Algorithm SHA256
```

## Montar el CD

1. Instalar WinCDEmu 4.1.
2. Montar `REDBARON_3D.cue` con WinCDEmu.
3. Comprobar que Windows reconoce el volumen con la etiqueta `REDBARON_3D`.
4. En la prueba de PC Game Archive, la imagen se montó como unidad `E:`.

La unidad virtual mostró:

- sistema de archivos: CDFS;
- etiqueta: `REDBARON_3D`;
- tamaño lógico: 718.379.008 bytes.

## Instalación

1. Abrir la unidad virtual montada.
2. Ejecutar `SETUP.EXE` directamente.
3. Realizar la instalación normalmente.

En el entorno probado **no fue necesario**:

- activar un modo de compatibilidad;
- ejecutar el instalador como administrador;
- instalar parches adicionales;
- modificar manualmente archivos del juego.

La instalación finalizó correctamente.

## Ejecución

Después de instalar:

1. Ejecutar Red Baron 3-D normalmente desde el acceso directo o el ejecutable instalado.
2. Mantener montada la copia de trabajo si el juego la requiere durante el uso.
3. No aplicar modos de compatibilidad ni elevación administrativa mientras no sean necesarios.

En el equipo probado el juego arrancó correctamente sin ajustes adicionales.

## Resultado de las pruebas

- **Instalación:** Correcto.
- **Arranque:** Correcto.
- **Menú principal:** Correcto.
- **Vídeo y gráficos:** Correcto en la prueba realizada.
- **Sonido:** Correcto.
- **Música:** Correcto.
- **Teclado y ratón:** Correcto.
- **Inicio de partida:** Correcto.
- **Juego durante la prueba:** Correcto.
- **Guardado de partida:** Correcto.
- **Carga de partida:** Correcto.
- **Cierre y segundo arranque:** Correcto.
- **Gamepad/joystick:** No probado.
- **Multijugador:** No probado.

## Estado de compatibilidad

**Funcional en el entorno probado, sin ajustes adicionales.**

La edición española Big Box conservada por PC Game Archive pudo instalarse y ejecutarse directamente en Windows 10 Pro 22H2. No fueron necesarios parches, wrappers, modos de compatibilidad ni privilegios de administrador durante las pruebas realizadas.

## Limitaciones de esta validación

Esta guía describe exclusivamente el entorno probado. No permite extrapolar automáticamente el resultado a:

- otras ediciones o reediciones de Red Baron 3-D;
- Windows 11 u otras versiones de Windows;
- otras GPU o controladores;
- multijugador;
- joystick o gamepad.

Los apartados no probados se mantienen expresamente como tales.

## Relación con la preservación

La guía utiliza una copia de trabajo derivada del máster digital verificado de esta misma pieza. El procedimiento de preservación puede consultarse en el [registro de preservación de Red Baron 3-D](../../preservacion/red-baron-3d-bigbox/).

**Última prueba:** 05/10/2026.
