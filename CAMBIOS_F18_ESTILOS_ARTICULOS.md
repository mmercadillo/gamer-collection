# F18 — Unificación visual de artículos de novedades

- Los artículos ampliados reutilizan `wrap game-detail`, `breadcrumbs`, `content-card`, `eyebrow`, `lead` y los botones ya empleados en las fichas.
- Las galerías utilizan exactamente los componentes CSS existentes de las fichas: `gallery`, `gallery-item`, `gallery-link` y `figcaption`. Mantienen las mismas columnas adaptativas, bordes, proporciones de miniatura y apertura de imagen completa.
- Se elimina la presentación independiente `news-photo-grid`, así como sus estilos duplicados.
- Las fuentes de cada acontecimiento siguen ubicadas únicamente en `contenido/novedades/<identificador>/`, junto con sus fotografías.
- Se conservan la selección y caducidad del destacado, el histórico, el SEO y el modelo JSON existente.
