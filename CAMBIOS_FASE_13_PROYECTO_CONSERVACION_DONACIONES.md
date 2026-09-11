# Fase 13 — Identidad, conservación y donaciones

Fecha: 11/09/2026

## Objetivo

Dar a PC Game Archive una capa institucional y de transparencia que explique qué es el proyecto, cómo se trata el material físico, qué ocurre con una donación y cuáles son los siguientes hitos.

## Cambios realizados

### 1. Nueva página `/proyecto/`

Se genera automáticamente desde `generar_web.py` e incluye:

- Propósito del proyecto.
- Qué hacemos actualmente.
- Principios del archivo.
- Flujo de conservación física y digital.
- Situación actual de la exposición de la colección.
- Roadmap con tres estados: `En funcionamiento`, `En desarrollo` y `Objetivo futuro`.
- Presentación breve de las dos personas que impulsan actualmente PC Game Archive.
- Llamada a la acción hacia la página de aportación de juegos.

La página incorpora:

- canonical propia,
- Open Graph y Twitter Card,
- `AboutPage` y breadcrumbs mediante JSON-LD,
- navegación interna por anclas,
- diseño responsive específico.

### 2. Navegación principal

Se añade `El proyecto` a la navegación principal. El enlace se genera para todas las páginas, por lo que se mantiene tras cualquier regeneración futura.

### 3. Donaciones y transparencia

La landing `/vender-videojuegos-pc-antiguos/` mantiene su función de compra/donación y se amplía con:

- explicación de qué ocurre con el material donado,
- conservación de procedencia cuando el donante lo desea,
- catalogación documental,
- conservación física,
- preservación digital de soportes cuando procede,
- aclaración de que actualmente no existe exposición física permanente,
- enlace directo a `/proyecto/#conservacion`,
- nuevas preguntas frecuentes sobre tratamiento y exposición de las donaciones.

No se crea una segunda landing de donaciones para evitar duplicar intención y contenido con la página de captación existente.

### 4. Portada y contacto

- La portada enlaza a `El proyecto` desde el bloque documental.
- La página de contacto enlaza a `El proyecto` para explicar finalidad, conservación y roadmap.

### 5. Sitemap y generación

- `/proyecto/` se incorpora automáticamente a `sitemap.xml`.
- `generar_web.py` genera la nueva página en cada ejecución.
- `informe_generacion_seo.md` registra la incorporación de la Fase 13.
- La versión del generador pasa a `fase13-proyecto-conservacion-donaciones-2026-09-11`.

## Criterios editoriales

La nueva página diferencia de forma expresa el estado actual de las aspiraciones futuras. No se presenta PC Game Archive como museo, fundación, asociación o colección oficialmente reconocida mientras esos hitos no se hayan materializado.

La preservación digital se describe como preservación y verificación interna de soportes. Cualquier futura modalidad de acceso al software se condiciona expresamente a la viabilidad técnica y al marco de propiedad intelectual aplicable.
