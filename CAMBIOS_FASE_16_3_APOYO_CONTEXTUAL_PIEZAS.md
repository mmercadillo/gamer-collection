# Fase 16.3 — Apoyo contextual a la conservación de piezas

Fecha: 2026-10-03


## Ajuste de ubicación del CTA

El bloque **“Ayuda a conservar esta pieza”** se muestra como una segunda tarjeta independiente dentro de la columna izquierda de la ficha, inmediatamente debajo de la tarjeta que contiene la imagen principal y las acciones de Instagram/catálogo. Así permanece visible en el primer recorrido sin mezclarse con la tarjeta de la imagen ni desplazarse al final del contenido documental.

## Objetivo

Permitir que una persona que consulta una pieza concreta de PC Game Archive pueda realizar una aportación contextual a su conservación, manteniendo una comunicación transparente sobre el destino general de los fondos y reutilizando la infraestructura de sostenibilidad incorporada en Fase 16.

## Flujo funcional

1. El usuario consulta `/juegos/<slug>/`.
2. La ficha muestra el bloque **Ayuda a conservar esta pieza**.
3. El CTA conduce a `/apoyar/?juego=<slug>`.
4. `/apoyar/` resuelve el título desde `assets/js/search-index.js` y muestra el contexto de la pieza.
5. La salida a Ko-fi continúa siendo externa y se registra en GA4 con el contexto del juego.

No se enlaza Ko-fi directamente desde cada ficha. PC Game Archive conserva así el contexto, la transparencia y la analítica, y mantiene desacoplado el proveedor de pago.

## Presentación en ficha

El nuevo bloque explica que la aportación ayuda a:

- conservación física de la edición;
- documentación;
- preservación digital;
- infraestructura necesaria para mantener el archivo accesible.

Se incluye además la aclaración:

> Las aportaciones contribuyen al mantenimiento general de PC Game Archive y no quedan asignadas exclusivamente a una pieza concreta.

## Página `/apoyar/`

Cuando recibe el parámetro `juego`, la página busca `/juegos/<slug>/` en `window.PCGA_SEARCH_INDEX`.

Si existe coincidencia:

- muestra `Estás apoyando la conservación de <título>`;
- explica que el usuario ha llegado desde la documentación de esa pieza;
- adapta el CTA a `Apoyar la conservación de esta pieza en Ko-fi`.

Si el parámetro no existe, es inválido o no corresponde a una pieza del catálogo, `/apoyar/` mantiene su comportamiento general de Fase 16.

## Analítica GA4

### `game_support_click`

Se registra al pulsar el CTA de una ficha:

- `game_title`
- `game_slug`
- `game_num`
- `game_format`
- `source_page`

### `support_page_view`

Mantiene el evento existente y añade:

- `support_context`: `game` o `general`
- `game_slug`: slug cuando existe contexto

### `support_click`

Mantiene el evento existente y añade:

- `support_context`: `game` o `general`
- `game_slug`: slug cuando existe contexto

## Modelo de datos

No se añade ningún campo a `juegos.json` ni a `json_schema.json`.

El apoyo económico es una capacidad transversal de PC Game Archive y no forma parte de los metadatos documentales de una pieza.

## Seguridad y robustez

- El slug recibido por query string no se inserta como HTML.
- El título se obtiene únicamente del índice generado del catálogo y se escribe mediante `textContent`.
- Un slug desconocido no muestra contexto personalizado.
- La salida a Ko-fi mantiene `target="_blank"` y `rel="noopener noreferrer"`.

## Compatibilidad

La URL general `/apoyar/` sigue funcionando sin parámetros y mantiene el comportamiento anterior.
