# Fase 7 — Preparación SEM / Google Ads

## Objetivo

Dejar PC Game Archive preparado para lanzar una campaña Search de captación dirigida a personas que quieren vender o donar videojuegos físicos de PC, sin perder la atribución publicitaria y sin mezclar esa medición con el tráfico orgánico o las búsquedas internas del catálogo.

## Cambios técnicos

### Pruebas locales sin contaminar Analytics

Google Analytics no se inicializa cuando la web se sirve desde `localhost`, `127.0.0.1` o `::1`. Las pruebas locales siguen ejecutando toda la lógica del sitio, pero no generan tráfico en la propiedad de producción.

### Atribución publicitaria en Google Analytics

La web continúa normalizando `page_location` a la URL canónica, pero ahora conserva exclusivamente los parámetros de campaña relevantes cuando están presentes:

- `utm_source`
- `utm_medium`
- `utm_campaign`
- `utm_term`
- `utm_content`
- `utm_id`
- `gclid`
- `gbraid`
- `wbraid`
- `dclid`

Los parámetros funcionales del sitio, como `?q=Activision`, no se incorporan a `page_location`, por lo que no vuelven a fragmentar el informe de páginas.

La atribución detectada se conserva además durante la sesión en `sessionStorage` bajo `pcga_campaign_attribution` para diagnóstico futuro.

### Evento de captación

Los CTA de `/vender-videojuegos-pc-antiguos/` siguen utilizando:

`offer_games_click`

Parámetros:

- `intent`: `sell`, `donate` o `general`
- `channel`: `email` o `instagram`
- `link_url`
- `source_page`

En enlaces `mailto:` el navegador espera brevemente al callback del Google tag antes de abrir el cliente de correo. El mismo clic ya no genera además `contact_click`, evitando duplicar la acción de captación.

`contact_click` queda reservado al contacto general fuera de la captación.

## Prueba local recomendada

Abrir:

`http://localhost:8000/vender-videojuegos-pc-antiguos/?utm_source=google&utm_medium=cpc&utm_campaign=pcga_captacion&utm_term=vender+juegos+pc&utm_content=rsa01&gclid=TEST123`

En la consola del navegador:

`window.PCGA_TRACKING_LOCATION`

Debe contener:

`https://pcgamearchive.org/vender-videojuegos-pc-antiguos/?utm_source=google&utm_medium=cpc&utm_campaign=pcga_captacion&utm_term=vender+juegos+pc&utm_content=rsa01&gclid=TEST123`

Una URL funcional como:

`http://localhost:8000/?q=Activision`

mantiene como `PCGA_TRACKING_LOCATION`:

`https://pcgamearchive.org/`

## Configuración manual necesaria en Google Analytics / Google Ads

El código queda preparado, pero la conversión no puede activarse desde el repositorio.

1. Desplegar la Fase 7.
2. Generar al menos un `offer_games_click` real/de prueba.
3. En Google Analytics 4, marcar `offer_games_click` como evento clave.
4. Vincular la propiedad de Google Analytics 4 con la cuenta de Google Ads.
5. Crear/importar en Google Ads una conversión basada en ese evento clave.
6. Activar el autoetiquetado en Google Ads.
7. Usar `/vender-videojuegos-pc-antiguos/` como URL final de la campaña.

No marcar simultáneamente `contact_click` y `offer_games_click` como conversiones primarias de esta campaña: un contacto de captación debe contar una sola vez.
