# Fase 10B — Adaptación de `generar_web.py` al nuevo modelo de datos

Base: `pcgamearchive_fase10A.zip`.

## Alcance

Se adapta exclusivamente `generar_web.py` para reconocer los cinco campos añadidos en la Fase 10A:

- `anio`
- `mercado`
- `idioma`
- `soporte`
- `tipo_edicion`

Los campos siguen siendo obligatorios en el schema y admiten su representación vacía. No se modifica ningún valor de `juegos.json` en esta fase.

## Comportamiento

Mientras los campos estén vacíos, no se añade contenido visual a las fichas y la salida generada se mantiene igual que en Fase 10A.

Cuando estén documentados:

- se muestran de forma condicional en la ficha del juego;
- pasan a formar parte de la búsqueda global;
- `anio` enriquece `VideoGame` con `datePublished`;
- `idioma` enriquece `VideoGame` con `inLanguage`.

No se generan todavía nuevas taxonomías, landings o URLs para estos campos. Esa explotación se reserva para una fase posterior, una vez exista información real suficiente en el catálogo.

## Regresión

Con los 1.552 registros actuales y los cinco campos vacíos se comparó una generación completa antes/después:

- mismos 2.060 ficheros generados;
- 2.059 ficheros idénticos byte a byte;
- única diferencia: la fecha/hora de `informe_generacion_seo.md`;
- mismo sitemap y mismas URLs;
- mismo índice de búsqueda efectivo;
- sin cambios visuales en las fichas.

También se probó una copia temporal con una ficha que contenía valores en los cinco campos. La ficha mostró correctamente los metadatos y estos entraron en la búsqueda global. Esa prueba no forma parte del catálogo entregado.
