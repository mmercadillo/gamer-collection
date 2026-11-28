# Evolutivo — Entornos y procedimientos técnicos transversales

Fecha: 28/11/2026. Base: `pcgamearchive_in_the_1st_degree_compatibilidad.zip`, última entrega completa de la sesión. Alcance: F01–F07 de la propuesta aprobada; no se han cambiado los datos de catálogo ni la metodología de preservación por pieza.

## 1. Diseño y decisiones

El índice documental real ya incluía cinco categorías (preservación, guías, formatos, historia y entornos de referencia). Se incorpora `tecnica` como sexta categoría, sin fusionar ni renombrar las anteriores. `laboratorio` conserva sus documentos de infraestructura PCGA-MASTER-01 y PCGA-LAB-01; `tecnica` reúne procedimientos reutilizables. Se genera `/documentacion/tecnica/` con todos los documentos de la categoría, independientemente del límite de ocho publicaciones recientes del índice general.

El índice único sigue siendo `documentacion.json`. Los documentos de categoría `tecnica` no se asocian directamente a piezas mediante `juegos`; una guía específica declara los IDs que usa en `referencias_documentales` (opcional). El generador valida tipo, referencias inexistentes, duplicados y autorreferencias, así como la reserva de la ruta técnica. Genera navegación en ambos sentidos sin contaminar las fichas de catálogo. Los enlaces editoriales Markdown remiten al documento de referencia desde el contexto relevante. No se ha añadido un segundo generador ni otra fuente de relaciones.

## 2. Entregables

- Índice: `/documentacion/tecnica/`, enlazado desde el área documental general y las migas de pan de los artículos técnicos.
- Primera guía: `/documentacion/tecnica/windows-31-dosbox-staging-portable/`, independiente de juegos, con diez capturas de las dos sesiones anteriores y módulos opcionales de MCI/CDDA y QuickTime 2.1.2. Configuración base, instalación de Windows, S3, Creative, SmartDrive, MIDI, montaje ISO y BIN/CUE, portabilidad, arranque automático y validación.
- Refactorización de las guías portables de Lode Runner e In the 1st Degree, con las mismas URL y enlaces al procedimiento común. Se conservan los ajustes propios de cada edición, las 18 capturas de la guía In the 1st Degree y todos los registros y ficheros de evidencia anteriores. Las imágenes comunes de Lode Runner se copian a la ruta técnica, sin eliminar las originales. No se modifica la guía alternativa de ejecución nativa de Lode Runner ni su exportación HTML histórica.
- Corrección de un error editorial preexistente en la guía de In the 1st Degree: un reemplazo había incrustado el BAT en la línea `call AUTOEXEC.BAT` y en el árbol de directorios. El bloque INI se ha cotejado literalmente con el fichero validado del registro técnico. También se unifica el nombre del BAT mencionado en la introducción de Lode Runner con el que aparece en sus instrucciones.
- `README.md`, plantilla de compatibilidad, prompt maestro del proyecto y `PROXIMOS_EVOLUTIVOS.md` actualizados para futuras sesiones.
- `TEST_DOCUMENTACION_TECNICA.py`: pruebas de regresión sin dependencias de terceros.

## 3. Validación

- `python generar_web.py`: generación completa correcta, 1.625 juegos, 37 novedades y 27 documentos (antes 26).
- `python TEST_DOCUMENTACION_TECNICA.py`: 11 pruebas superadas; incluye referencia desconocida, duplicada, circular consigo misma, tipo inválido, ruta reservada, asociación indebida a pieza, enlace bidireccional, configuración original, SEO e imágenes con salida independiente.
- Comparación con la base: se conservan las 26 URL documentales anteriores; sitemap incorpora exactamente dos URL nuevas, sin pérdida ni duplicados.
- Revisión de 29 páginas documentales (27 artículos y 2 índices): canonical, título, descripción, H1, JSON-LD y enlaces internos; no se detectaron enlaces internos rotos. 42 referencias a imágenes de artículos resueltas, 10 en la nueva guía y 18 en In the 1st Degree.
- Catálogo, schema, novedades y propiedades globales permanecen idénticos byte a byte. No se ha añadido una novedad editorial sin solicitud explícita.
- Se han mantenido los archivos anteriores, incluido el material interno de evidencias. No se incorporan ejecutables comerciales, imágenes ISO, disquetes ni instaladores de terceros.

## 4. Límites

La validación corresponde a la generación estática y sus referencias, no a un despliegue en GitHub Pages ni a una nueva sesión de emulación. La guía transversal sintetiza procedimientos efectivamente probados en dos sesiones, pero no se ha ejecutado íntegramente desde cero como una única reconstrucción independiente. Tampoco se ha probado otro equipo físico o Windows 11. La salida MIDI Win32 sigue dependiendo del anfitrión. Se conservan estas limitaciones en la documentación pública. No se han comprobado nuevamente los destinos de enlaces externos históricos.

Para regenerar desde la raíz: `python generar_web.py`. Para comprobar las regresiones: `python TEST_DOCUMENTACION_TECNICA.py`.
