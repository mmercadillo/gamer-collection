# F16.5 — Novedades del archivo

**Fecha:** 04/10/2026  
**Base:** F16.4 — Propiedades globales y fecha de última actualización

## Objetivo

Incorporar un registro editorial cronológico que permita consultar rápidamente la actividad de PC Game Archive más allá de las nuevas incorporaciones al catálogo.

## Cambios realizados

- Nuevo fichero `novedades.json` como fuente de datos editorial.
- Modelo deliberadamente mínimo:
  - `fecha`: obligatorio, formato ISO `YYYY-MM-DD`.
  - `titulo`: obligatorio.
  - `descripcion`: opcional.
  - `url`: opcional.
- El generador valida el fichero y ordena siempre las novedades de más reciente a más antigua.
- Nuevo parámetro opcional `--novedades`, con `novedades.json` como valor por defecto.
- Nueva página canónica `/novedades/` con el histórico completo.
- Nuevo bloque **Novedades** en portada, situado inmediatamente antes de **Últimas incorporaciones al archivo**.
- La portada muestra como máximo las cuatro novedades más recientes.
- Nuevo acceso **Novedades** en la navegación principal.
- `/novedades/` queda incluida en `sitemap.xml`.
- Las URLs de una novedad pueden ser internas, absolutas o externas.
- La sección queda oculta en el modo de búsqueda de portada, igual que otros bloques editoriales.

## Criterio editorial

Las novedades no se derivan automáticamente de `juegos.json`. `novedades.json` es un registro editorial explícito: permite agrupar incorporaciones, anunciar guías, preservación, donaciones, cambios del proyecto u otros hitos sin crear ruido automático.

La redacción de **Novedades** está dirigida al visitante del archivo, no al equipo de desarrollo. Debe evitar nomenclatura interna de fases (`F16`, `F17`, etc.), términos de implementación como «infraestructura» o «integración bidireccional» cuando no aporten valor al lector y cualquier formulación propia de un changelog técnico. Cada entrada debe explicar de forma cercana **qué ha cambiado, qué se ha incorporado o qué puede hacer ahora el visitante**. La trazabilidad técnica y las fases se mantienen exclusivamente en los documentos internos de seguimiento.

## Entradas iniciales

Se incluyen únicamente hitos ya verificables en la base de proyecto utilizada para F16.5:

- cinco incorporaciones con fecha 04/10/2026;
- publicación de la fecha de última actualización mediante propiedades globales;
- apoyo contextual a la conservación de piezas incorporado en F16.3.
