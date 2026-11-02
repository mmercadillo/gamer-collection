# PC Game Archive — Registro interno de compatibilidad

- **Pieza:** The Secret of Monkey Island — Jewel Case (CD-ROM)
- **Ficha:** https://www.pcgamearchive.org/juegos/the-secret-of-monkey-island-jewelcase/
- **Fecha de pruebas:** 2026-11-02
- **Estado:** Funcional con ajustes (IsoBuster 5.8 + ScummVM 2026.4.0)
- **Alcance:** edición española `CD/DOS/Spanish`; partida completa no probada
- **Estándar aplicado:** estándar de guías de ejecución y compatibilidad del proyecto

## Punto de partida

Copia de trabajo separada del máster, verificada por SHA-256:

```text
Image.bin  88A546BF6391FA0AE066FBEC5A84F810BBBE363AF3C3FC73B7C24EBF01B982D3
Image.cue  1330620E8A913A3BA9D9DF90C96EBFC2C6B86D1C5A9CEFBEE060B429947A435F
```

## Entorno

Windows 10 confirmado; se dispone de ficha de referencia PCGA-LAB-01 (Windows 10 Pro 22H2, 19045.6466, Ryzen 5 PRO 4650U, 16 GB RAM, Radeon), pero no se registró en esta sesión otra caracterización completa del hardware. IsoBuster 5.8, ScummVM 2026.4.0.

## Extracción de la imagen

IsoBuster abrió `Image.cue` y mostró 1 sesión, 25 pistas (datos 01, audio 02–25) y sistemas ISO9660 y HFS. Se extrajo ISO9660 completo, preservando directorios ENGLISH/FRENCH/GERMAN/ITALIAN/SPANISH; resultado comunicado sin errores. Se extrajeron 24 pistas en WAV (`Pista 02.wav` ... `Pista 25.wav`).

## Incidencia de audio y resolución

- Primera ejecución detectó la variante `CD/DOS/Spanish` desde `ISO 9660\SPANISH`.
- ScummVM mostró aviso sobre ausencia de pistas CD-DA.
- Se probó `track2.wav` como WAV individual: no se oyó música.
- El responsable incorporó las **24 pistas** en `ISO 9660\SPANISH`, renombradas **`track01.wav` a `track24.wav`**, con correspondencia pista física 02→track01.wav; música confirmada como funcional.
- No se realizó conversión FLAC/MP3/OGG ni se instalaron conversores.

## Pruebas funcionales

- Detección, arranque, introducción, gráficos, diálogos escritos, música, interacción y jugabilidad: correctos, confirmados en sesión.
- Voces: no aplicable (edición sin doblaje de diálogos).
- Guardado, cierre, segundo arranque, carga y continuación: correctos, confirmados.
- Efectos sonoros, teclado específico, gamepad: sin comprobación individual.
- Partida completa, otras ediciones/sistemas, ejecución nativa: no probados.

## Repetición final

Procedimiento final validado con los 24 WAV correctamente nombrados y ubicados; reinicio y carga de partida confirmados. No hay evidencia de una segunda instalación limpia completa con extracción desde cero.

## Evidencias

- Capturas IsoBuster (TOC, ISO9660), ScummVM (detección y aviso de audio).
- Hashes y confirmaciones de sesión del responsable; no se dispone de hashes separados para cada WAV.
- Guía pública: `documentacion/fuentes/guia-the-secret-of-monkey-island-jewelcase-windows-10.md`.

## Estado final

**Funcional con ajustes** — 2026-11-02.
