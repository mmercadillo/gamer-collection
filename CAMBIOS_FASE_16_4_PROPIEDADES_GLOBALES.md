# F16.4 — Propiedades globales y fecha de última actualización

## Objetivo

Introducir un fichero de configuración transversal del proyecto y utilizarlo inicialmente para publicar en portada la fecha de la última actualización del archivo.

## Cambios

- Nuevo fichero `propiedades.json`.
- Propiedad inicial `ultima_actualizacion` en formato ISO `YYYY-MM-DD`.
- `generar_web.py` lee `propiedades.json` mediante el argumento opcional `--propiedades` (por defecto `propiedades.json`).
- La portada muestra `Última actualización del archivo · <fecha>` bajo la descripción principal.
- El generador transforma la fecha ISO a una fecha legible en español.
- La generación falla explícitamente si el fichero no existe, no contiene un objeto JSON, falta `ultima_actualizacion` o la fecha no cumple el formato ISO.

## Criterio de diseño

`propiedades.json` queda reservado para configuración global y transversal del sitio. No debe convertirse en un contenedor de constantes puramente técnicas del generador.
