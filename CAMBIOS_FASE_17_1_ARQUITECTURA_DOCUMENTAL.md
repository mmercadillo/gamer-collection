# F17.1 — Arquitectura del área documental

## Objetivo

Crear la infraestructura base del área documental de PC Game Archive sin publicar todavía procedimientos o guías que no hayan sido validados sobre casos reales.

## Cambios implementados

- Nueva ruta canónica `/documentacion/`.
- Nueva entrada **Documentación** en la navegación principal.
- Breadcrumbs y metadatos SEO propios.
- Datos estructurados `CollectionPage` y `BreadcrumbList` para el hub documental.
- Inclusión de `/documentacion/` en `sitemap.xml`.
- Nuevo fichero `documentacion.json` como índice central de metadatos documentales.
- Nuevo parámetro `--documentacion` en `generar_web.py`.
- Validación estricta de los documentos y de sus relaciones con las piezas existentes de `juegos.json`.
- Preparación del generador para listar contenidos documentales cuando empiecen a publicarse.
- El índice nace vacío: F17.1 no crea artículos ficticios ni anticipa procedimientos todavía no validados.

## Categorías iniciales

- `preservacion` — Preservación digital.
- `guias` — Guías de ejecución.
- `formatos` — Formatos y soportes.
- `historia` — Historia y contexto.

Las categorías son controladas por el generador. Su ampliación debe responder a una necesidad documental real.

## Modelo de `documentacion.json`

Cada documento futuro tendrá como mínimo:

```json
{
  "id": "identificador-unico",
  "titulo": "Título público",
  "categoria": "preservacion",
  "fecha": "2026-10-04",
  "url": "documentacion/preservacion/ejemplo/"
}
```

Campos opcionales previstos:

```json
{
  "actualizado": "2026-10-04",
  "descripcion": "Resumen del documento.",
  "juegos": [
    "juegos/slug-de-la-pieza/"
  ],
  "contenido": "ruta/a/la/fuente-del-documento"
}
```

### Reglas

- `id`, `titulo`, `categoria`, `fecha` y `url` son obligatorios.
- `id` y `url` deben ser únicos.
- Las fechas usan ISO `YYYY-MM-DD`.
- Las URLs documentales deben comenzar por `documentacion/` y terminar en `/`.
- Cualquier valor de `juegos` debe coincidir exactamente con una URL existente de `juegos.json`.
- `documentacion.json` será la única fuente de verdad de las relaciones documento → pieza.
- La relación inversa pieza → documento se resolverá automáticamente desde el generador cuando se implemente F17.4; no se duplicará en `juegos.json`.

## Decisión sobre el contenido

F17.1 define únicamente el índice y la arquitectura. El formato definitivo de autoría y renderizado del cuerpo de los documentos se cerrará antes de publicar el primer procedimiento en F17.2. No se incorpora todavía una dependencia Markdown ni un parser propio sin un caso real que lo justifique.

## Estado al cierre

F17.1 deja disponible la infraestructura documental y el contrato de metadatos. El siguiente paso es **F17.2 — Estándar y procedimientos de preservación**, partiendo del diseño rector `DISENO_FASE_17_AREA_DOCUMENTAL_PRESERVACION.md`.
