# F17.2 — Estándar y procedimientos de preservación

## Objetivo

Cerrar el estándar operativo de preservación digital de PC Game Archive y publicarlo como documentación reproducible antes de abordar la primera pieza piloto.

F17.2 no pretende definir por adelantado una receta distinta para cada protección o soporte. Define el método común de trabajo y el procedimiento de caracterización que permite decidir posteriormente qué adquisición corresponde a una pieza concreta.

## Cambios implementados

- Publicación del **Estándar de preservación digital de PC Game Archive**.
- Publicación del procedimiento **Caracterización previa de soportes ópticos**.
- Nuevo soporte de contenido documental en Markdown mediante un subconjunto controlado renderizado por el propio generador, sin añadir dependencias externas de runtime.
- Generación automática de páginas documentales individuales a partir de `documentacion.json` + fuente Markdown.
- Datos estructurados `TechArticle`, canonical, breadcrumbs, fechas de publicación/revisión y metadatos SEO por documento.
- Validación del fichero fuente de cada documento:
  - obligatorio para documentos publicados;
  - ruta relativa al proyecto;
  - extensión `.md`;
  - prohibición de salir del directorio del proyecto;
  - fallo explícito si el fichero no existe;
  - fallo explícito ante bloques de código sin cerrar.
- Inclusión automática de los documentos en `/documentacion/` y `sitemap.xml`.
- Creación de `PLANTILLA_REGISTRO_PRESERVACION.md` como checklist operativa para cada pieza.
- Actualización de la documentación de diseño, README, backlog y Novedades.

## Decisiones normativas

### 1. Caracterizar antes de adquirir

No se selecciona ISO, BIN/CUE, MDF/MDS u otro formato únicamente por tratarse de un CD o DVD. Primero se documenta la estructura real del soporte, sus pistas, sesiones, audio, anomalías, protecciones y demás características relevantes.

### 2. La metodología es global; la evidencia es específica

El estándar general y los procedimientos reutilizables son comunes. La caracterización, la elección del método, los logs, hashes y resultados pertenecen siempre a la pieza/edición concreta.

### 3. Preservación y compatibilidad son procesos separados

El máster de preservación se crea para representar y verificar el soporte original. Las instalaciones, conversiones, parches, wrappers o pruebas de ejecución se realizan sobre una copia o derivado de trabajo.

### 4. El máster es inmutable

El conjunto que constituye el máster no se modifica después de su validación. Cualquier transformación debe crear un derivado trazable.

### 5. SHA-256 como mínimo de integridad propio

PC Game Archive utilizará SHA-256 como hash mínimo de integridad para los ficheros del máster. Se conservarán otros algoritmos cuando herramientas o referencias externas los necesiten.

### 6. Segunda lectura cuando proceda

Cuando el soporte y el procedimiento lo permitan, se buscará realizar adquisiciones independientes y comparar sus resultados. El mero fin de una lectura sin error no basta para declarar una pieza verificada.

### 7. No inventar procedimientos específicos

Si una pieza presenta una característica no cubierta por un procedimiento validado, se documentará el caso, se estudiará y validará el método correspondiente y solo después se completará su preservación.

## Modelo de contenido documental

`documentacion.json` sigue siendo el índice de metadatos. El cuerpo de cada documento se mantiene fuera del JSON:

```text
documentacion.json
        │
        └── contenido → documentacion/fuentes/<documento>.md
                              │
                              ▼
                         generar_web.py
                              │
                              ▼
                   /documentacion/.../index.html
```

El generador admite un subconjunto deliberadamente limitado de Markdown:

- encabezados H2-H4;
- párrafos;
- listas ordenadas y no ordenadas;
- checklist textual;
- blockquotes;
- bloques de código fenced;
- código inline;
- negrita;
- enlaces HTTP(S) y relativos.

No se admite HTML crudo. Esto mantiene el formato de autoría legible, versionable y seguro sin introducir una dependencia externa solo para renderizar documentación.

## Documentos públicos creados

### Estándar de preservación digital

URL:

```text
/documentacion/preservacion/estandar-preservacion-digital/
```

Define identificación, inspección, caracterización, selección del procedimiento, adquisición, verificación, hashes, máster, copia de trabajo, almacenamiento, metadatos, estados y Definition of Done.

### Caracterización previa de soportes ópticos

URL:

```text
/documentacion/preservacion/caracterizacion-soportes-opticos/
```

Define qué comprobar antes de decidir cómo adquirir un CD-ROM o DVD-ROM y establece un árbol de decisión conceptual sin anticipar procedimientos todavía no validados sobre piezas reales.

## Plantilla operativa por pieza

`PLANTILLA_REGISTRO_PRESERVACION.md` se utilizará al abordar cada soporte real. Incluye:

- identificación;
- estado físico;
- caracterización;
- decisión y justificación del método;
- hardware/software/versiones;
- adquisición y logs;
- verificación;
- hashes;
- estado del máster;
- derivado de trabajo;
- checklist de cierre.

## Criterio de cierre de F17.2

F17.2 se considera completada cuando:

- el estándar está escrito y publicado;
- existe un procedimiento previo de caracterización de soportes ópticos;
- el generador puede publicar documentación versionada desde fuentes Markdown;
- existe una plantilla obligatoria de registro por pieza;
- el build rechaza documentos con fuentes inexistentes o inválidas;
- el sitemap y el hub documental incluyen automáticamente los documentos publicados.

Los procedimientos concretos de adquisición se crearán conforme aparezcan casos reales. Esta decisión es intencionada y forma parte del estándar.

## Siguiente entrega

**F17.3 — Estándar y plantilla de guías de ejecución/compatibilidad.**

## Corrección de maquetación documental — 04/10/2026

Tras validar la navegación real de los artículos de `/documentacion/` se detectó que el selector CSS global `header` aplicaba el comportamiento `position: sticky` tanto a la cabecera principal como al encabezado interno de los artículos. Esto provocaba solapamientos de capas durante el scroll.

Correcciones realizadas:

- el comportamiento sticky queda limitado a `.site-header`, que es la cabecera principal de la web;
- se elimina la maquetación específica introducida para los artículos documentales;
- los artículos reutilizan los componentes visuales ya existentes en PC Game Archive: `page-head`, `wrap`, `content-card`, `landing-editorial`, `eyebrow`, `lead` y `count`;
- se eliminan los estilos CSS específicos `documentation-article`, `documentation-article-head`, `documentation-body`, `documentation-meta` y `documentation-related`;
- el contenido documental conserva la misma navegación, SEO, breadcrumbs y datos estructurados de F17.2.

### Criterio consolidado

La documentación de F17 debe reutilizar el sistema visual existente de PC Game Archive. No se crearán estilos de página específicos cuando los componentes ya disponibles permitan resolver la maquetación de forma consistente.
