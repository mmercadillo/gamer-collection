# Registro interno de compatibilidad — Indiana Jones and the Fate of Atlantis (Big Box)

- **Edición:** española Big Box de Erbe Software; cinco disquetes HD de 3,5 pulgadas.
- **Ficha:** `juegos/indiana-jones-and-the-fate-of-atlantis-bigbox/`.
- **Pruebas realizadas:** 22/11/2026; **confirmación funcional final:** 27/11/2026.
- **Sistema:** PCGA-LAB-01, Windows 10 Pro 22H2 x64, versión 10.0.19045; valores adicionales de hardware en ficha del laboratorio, sin nueva medición durante este ensayo.
- **Emulador:** DOSBox Staging 0.83.0, copia portable bajo directorio `dosbox/`.
- **Guía:** `documentacion/fuentes/guia-indiana-jones-and-the-fate-of-atlantis-bigbox-windows-10-portable.md`.
- **Lanzador:** `recursos/compatibilidad/indiana-jones-and-the-fate-of-atlantis-bigbox/Indiana_Atlantis_Portable_Menu.bat`.

## Copias de trabajo

Cinco imágenes IMA verificadas por SHA-256 antes de instalar. Cada una de 1.474.560 bytes. Se mantienen separados los archivos originales de adquisición y la carpeta de trabajo. **Adquisiciones únicas**, sin comparación de lecturas independientes.

| Disco | Imagen | SHA-256 |
|---|---|---|
| 01 | `INDIANA_ATLANTIS_DISCO_01.IMA` | `8622A956CA89C413515361BA54DD176B4EF22394A08804ECE92A0E0C81F97CFC` |
| 02 | `INDIANA_ATLANTIS_DISCO_02.IMA` | `D673AF27EEDE3A1E220A5CBD99309C73CBC74595850FBC2701432CC5975EDB3D` |
| 03 | `INDIANA_ATLANTIS_DISCO_03.IMA` | `1A73F3425677CF60A36548A14F41987620982B81D773FFE3744AB777AC8D6816` |
| 04 | `INDIANA_ATLANTIS_DISCO_04.IMA` | `34B637DB24487C369A0DD533276F458AE5EF3B155BC761F44CC8EEADD3FC67D9` |
| 05 | `INDIANA_ATLANTIS_DISCO_05.IMA` | `2E8B79914C55DC166F9DC531833E15F6E61E06C4EC6C6C9DE282447F36A613CB` |

## Secuencia observada

1. Se prepara copia completa de DOSBox Staging, carpeta `DOS_C` y cinco imágenes IMA en la raíz de trabajo.
2. Se monta `DOS_C` como C: y el conjunto de cinco imágenes como A:, protegidas contra escritura.
3. El instalador original muestra idioma español y elige C: como unidad de destino.
4. Se confirma el uso de `Ctrl+F4` para avanzar entre disquetes a petición del instalador.
5. El instalador informa «Instalación completa»; ruta de instalación C:\ATLANTIS, físicamente DOS_C/ATLANTIS.
6. La ejecución de `ATLANTIS` muestra la pantalla de bienvenida y después el mecanismo de verificación con el manual.
7. Inicialmente faltaba el manual y se interrumpió el ensayo en esa comprobación. Posteriormente el operador confirma que el juego ya funciona correctamente, incluidos música, efectos y guardado y carga.
8. Se probó un archivo BAT con menú `[1] Jugar / [2] Instalar o reinstalar / [3] Salir`. El operador confirmó que el lanzador funciona perfectamente. Posteriormente confirmó también que funcionan la reinstalación sobre una instalación existente, el traslado del paquete a otro equipo y el cierre seguido de un segundo arranque. No se ha documentado por separado si la reinstalación conserva sin cambios las partidas anteriores.

## Evaluación

- **Correcto:** adquisición de copias de trabajo, instalación, cambio de disquetes, arranque, juego, música, efectos, guardado, carga, arranque desde menú, reinstalación sobre una instalación existente, traslado del paquete portable a otro equipo, cierre y segundo arranque.
- **No probado:** preservación de partidas preexistentes tras la reinstalación (comprobación diferenciada), campaña completa, cinemáticas por separado, gamepad y Windows 11.
- **No aplicable:** gráficos 3D, multijugador.
- **Limitación documental:** no hay log automatizado de pruebas de audio ni de partidas; se conserva la confirmación del usuario y las capturas anteriores.

**Estado final:** Funcional en el entorno verificado, con lanzador relativo y traslado del paquete a otro equipo probados. La reinstalación y el segundo arranque también se han confirmado. No distribuir imágenes ni binarios propietarios.
