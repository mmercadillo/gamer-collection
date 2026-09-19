# Fase 14.3 — Orden de últimas incorporaciones

Fecha: 2026-09-19

## Objetivo

Garantizar que las vistas de **Últimas incorporaciones** se presenten siempre por `fecha_incorporacion`, de la fecha más reciente a la más antigua, sin que el orden físico del catálogo ni una fecha futura errónea alteren el resultado.

## Cambios

- `dated_incorporations()` ordena únicamente por `fecha_incorporacion` en orden descendente.
- Cuando varias fichas tienen la misma fecha, se conserva su orden original en `juegos.json`.
- Las fechas futuras se excluyen de la portada y de `/incorporaciones/`; `validar_catalogo.py` continúa notificándolas como `WARN` para que puedan corregirse en origen.
- Se conserva íntegramente la corrección de resolución de imágenes de la Fase 14.2.

## Incidencia detectada en el catálogo recibido

La ficha `num: 000176` (`3 Skulls of the Toltecs`) contiene actualmente:

```json
"fecha_incorporacion": "2027-08-27"
```

Al ser posterior al 19/09/2026, no se utiliza para construir las vistas de novedades hasta que la fecha sea corregida o llegue a ser válida cronológicamente.
