# Preservación digital de Indiana Jones and the Fate of Atlantis — edición española Big Box

El 22 de noviembre de 2026 obtuvimos cinco imágenes sectoriales de los disquetes de la edición española que distribuyó Erbe Software para MS-DOS en 1992. Cada imagen corresponde a un disquete de 3,5 pulgadas de alta densidad y ocupa 1.474.560 bytes. Verificamos el tamaño, la huella SHA-256 y el directorio raíz de cada imagen.

[Ficha de la edición en PC Game Archive](https://www.pcgamearchive.org/juegos/indiana-jones-and-the-fate-of-atlantis-bigbox/) · [Estándar de preservación digital de PC Game Archive v2.0](https://www.pcgamearchive.org/documentacion/preservacion/estandar-preservacion-digital/)

## Qué contiene cada disquete

El primer disquete reúne el instalador y el primer archivo ND4. Cada uno de los otros cuatro contiene el siguiente archivo de la serie. Las etiquetas de volumen siguen un orden distinto al de los disquetes físicos. El tercer disquete, por ejemplo, lleva la etiqueta `920826A 001`.

| Disquete | Etiqueta de volumen | Archivos en el directorio raíz |
| --- | --- | --- |
| 1 de 5 | `920826A 002` | `INSTALL.EXE` (34.649 bytes), `PCVIQA_A.ND4` (1.419.388 bytes) |
| 2 de 5 | `920826A 003` | `PCVIQA_B.ND4` (1.454.088 bytes) |
| 3 de 5 | `920826A 001` | `PCVIQA_C.ND4` (1.454.088 bytes) |
| 4 de 5 | `920826A 006` | `PCVIQA_D.ND4` (1.454.088 bytes) |
| 5 de 5 | `920826A 004` | `PCVIQA_E.ND4` (1.444.773 bytes) |

Windows identificó como FAT los volúmenes 1 y 5. La consulta CIM dejó vacíos los metadatos de los discos 2, 3 y 4. El comando `dir A:\ /a` permitió consultar la etiqueta y el directorio raíz de los cinco originales.

## Cómo se obtuvieron las imágenes

Usamos una disquetera externa USB Y-E DATA USB-FDU (`VID_057B`, `PID_0000`, revisión USBSTOR `5.01`) en Windows 10 Pro x64, compilación 19045. Con WinImage 11.00 de 64 bits, seleccionamos la unidad `A:`, ejecutamos **Disk → Read disk** y guardamos cada lectura como imagen IMA sin comprimir. Las cinco lecturas terminaron sin errores comunicados durante la operación.

Después abrimos los IMA en WinImage y cotejamos la etiqueta del volumen, los nombres y el tamaño de los archivos visibles con el listado previo de cada disquete. PowerShell calculó el SHA-256 de cada imagen y volvió a comprobar las cinco huellas antes de crear el manifiesto `SHA256SUMS.txt`.

## Huellas de las imágenes

```text
8622A956CA89C413515361BA54DD176B4EF22394A08804ECE92A0E0C81F97CFC  INDIANA_ATLANTIS_DISCO_01.IMA
D673AF27EEDE3A1E220A5CBD99309C73CBC74595850FBC2701432CC5975EDB3D  INDIANA_ATLANTIS_DISCO_02.IMA
1A73F3425677CF60A36548A14F41987620982B81D773FFE3744AB777AC8D6816  INDIANA_ATLANTIS_DISCO_03.IMA
34B637DB24487C369A0DD533276F458AE5EF3B155BC761F44CC8EEADD3FC67D9  INDIANA_ATLANTIS_DISCO_04.IMA
2E8B79914C55DC166F9DC531833E15F6E61E06C4EC6C6C9DE282447F36A613CB  INDIANA_ATLANTIS_DISCO_05.IMA
```

## Alcance de la preservación

El resultado documentado es una adquisición sectorial convencional por disquete. La comprobación cubre el tamaño de cada archivo IMA, su huella y la coincidencia del directorio raíz visible. La reproducibilidad entre lecturas y las características del flujo magnético quedan sin evaluar.

El conjunto digital de referencia reúne los cinco IMA y su manifiesto. La documentación de custodia y respaldos queda fuera del alcance de este cierre. La instalación, la ejecución y la verificación mediante el manual original quedarán para la fase de compatibilidad. La ficha de la edición identifica el manual como fuente de los códigos que solicita el juego.
