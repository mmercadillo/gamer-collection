# PC Game Archive — Próximos evolutivos

Documento vivo para registrar, ordenar y mantener los próximos evolutivos de PC Game Archive. Contiene únicamente trabajos abiertos en el backlog; las capacidades implantadas se conservan en el histórico y la actividad recurrente se gestiona como operación continua.

**Base de referencia:** biblioteca documental escalable, F17 y F18 cerradas, guías transversales de Windows 3.1 y QuickTime 2.1.2 incorporadas.  
**Última actualización:** 28/11/2026  
**Fuentes de revisión:** `PROXIMOS_EVOLUTIVOS(1).md`, `pcgamearchive.zip`, última entrega `pcgamearchive_quicktime_imagenes_corregidas.zip`, registros de cambios y resultados de las sesiones del laboratorio. La implementación registrada no equivale a una comprobación del despliegue público ni de la recepción efectiva de eventos GA4.

---

## Cómo mantener este documento

- Usar identificadores de backlog estables (`EV-xx`), independientes de la numeración definitiva de fases.
- Ordenar por prioridad y, dentro de cada prioridad, por dependencias, impacto y viabilidad.
- No asignar una fase definitiva hasta definir alcance, entregables y criterios de aceptación.
- Separar evolutivos funcionales, técnicos, documentales y organizativos. Evitar cambios no relacionados en una misma entrega.
- Retirar los trabajos cerrados del backlog y trasladarlos al histórico con fecha y evidencia.
- Diferenciar implementación, validación técnica, aceptación de usuario y despliegue. No declarar validaciones que no se hayan realizado.
- Mantener los datos privados y los másteres fuera del repositorio público. No inventar metadatos ni resultados de laboratorio.

## Prioridades

| Nivel | Interpretación |
|---|---|
| P0 — Crítica | Continuidad del archivo, integridad de los activos o riesgo grave; abordar primero si existe una carencia real. |
| P1 — Alta | Alto valor documental, mejora de control o capacidad que desbloquea trabajos posteriores. |
| P2 — Media | Mejora relevante de calidad, acceso o eficiencia; ejecutar por entregas acotadas. |
| P3 — Baja / condicionada | Inversión dependiente del volumen, recursos, demanda o evidencia suficiente. |

Los nuevos candidatos y su orden son propuestas pendientes de aceptación. Las prioridades no implican una estimación de esfuerzo ni una fecha comprometida.

---

# Backlog activo

## P0 — Continuidad e integridad

### EV-01 — Garantía de conservación y recuperación de los activos digitales

**Tipo:** Técnico / preservación  
**Estado:** Verificar cobertura actual; resolver únicamente las carencias detectadas.

La pérdida del archivo digital, sus fuentes documentales o los másteres es un riesgo más importante que cualquier mejora de presentación. No se presupone que falten copias: debe comprobarse la situación real.

- Inventariar másteres, manifiestos SHA-256, registros, fotografías originales, vídeos, fuentes del sitio y configuraciones reproducibles. Registrar ubicación, responsable, última verificación y copia disponible.
- Definir una estrategia de copias independientes (preferentemente 3-2-1, con una copia fuera de la ubicación principal y protección frente a borrado accidental o ransomware).
- Separar físicamente o mediante permisos los másteres de las copias de trabajo; no sobrescribir los originales.
- Programar verificaciones de integridad de los másteres y pruebas de restauración; registrar incidencias, cambios de soporte y fecha de cada comprobación.
- Documentar recuperación del repositorio, dominio, DNS, cuentas de publicación y configuración de laboratorio; conservar credenciales mediante un gestor seguro, nunca en el repositorio.
- Confirmar el depósito definitivo y las copias de aquellos másteres cuyo cierre de laboratorio aún no acredita este paso, incluyendo In the 1st Degree.

**Criterio de cierre:** inventario y política operativa acordados, cobertura de copias conocida y restauración de una muestra comprobada; incidencias restantes identificadas y priorizadas.

---

## P1 — Alta prioridad

### EV-02 — Analítica documental avanzada (GA4)

**Tipo:** Funcional / analítica  
**Estado:** Pendiente de diseño e implementación.  
**Contexto:** La biblioteca ya incorpora GA4 básico, páginas individuales, buscador, filtros, categorías y relaciones. No se necesita rehacer esas funcionalidades.

Instrumentar el uso real de la biblioteca para conocer las necesidades de los visitantes y orientar la producción de nuevas guías.

| Evento propuesto | Finalidad |
|---|---|
| `document_view` | Consulta de un artículo; distinguirla de las visitas a los índices. |
| `document_search` | Búsqueda documental efectiva. |
| `document_search_no_results` | Detectar búsquedas sin resultados y posibles necesidades no cubiertas. |
| `document_filter_used` | Uso de facetas y filtros por área. |
| `document_category_click` | Acceso desde el portal a una categoría. |
| `document_related_click` | Navegación entre documentos relacionados. |
| `document_game_click` | Acceso a una ficha desde la documentación. |
| `game_document_click` | Acceso a documentación desde una ficha. |

- Revisar primero el catálogo de eventos existente y reutilizar la infraestructura común; evitar doble medición con `page_view`, eventos automáticos y navegación atrás/adelante.
- Diseñar parámetros de cardinalidad controlada (`document_id`, categoría, origen, tipo de filtro, número de resultados y, cuando corresponda, ID de pieza). Registrar una búsqueda confirmada o estabilizada, no cada pulsación.
- No enviar texto libre de búsquedas de forma indiscriminada: evaluar minimización, tratamiento de posibles datos personales y condiciones de GA4. Revisar también URLs con parámetros de búsqueda y su captura automática; preferir métricas agregadas y vocabularios controlados si no se puede asegurar la exclusión de datos personales.
- Mantener coherencia con las preferencias de consentimiento y la configuración de privacidad existente; revisar antes del despliegue si requieren adaptación.
- Documentar el contrato de eventos y parámetros, configurar las dimensiones personalizadas estrictamente necesarias y preparar una exploración o informe de biblioteca en GA4.
- Verificar en navegador real y DebugView/tiempo real después del despliegue. Separar pruebas locales de las métricas de producción.

**Criterio de cierre:** eventos documentados, emitidos una sola vez por acción definida, parámetros verificados, privacidad revisada y recepción real confirmada. Obtener una primera línea base sin establecer objetivos de crecimiento arbitrarios.

### EV-03 — Formalización de las modalidades de incorporación de piezas

**Tipo:** Organizativo / jurídico-documental  
**Estado:** Pendiente de definición. La procedencia pública y la captación de piezas ya existen (F13 y F15).

- Diferenciar compra, donación definitiva, cesión condicionada a la continuidad del proyecto, depósito/custodia, intercambio y otros casos reales.
- Definir titularidad, condiciones de conservación, devolución, continuidad del proyecto y tratamiento en caso de cese.
- Aclarar las autorizaciones para fotografías, documentación pública, atribución e identidad pública, así como el alcance de la digitalización; la entrega del soporte no implica necesariamente cesión de derechos de propiedad intelectual.
- Preparar modelos de justificante/acuerdo por modalidad, con revisión jurídica adecuada antes de su uso definitivo.
- Mantener los datos contractuales y de contacto en un registro privado; conservar en `procedencia` únicamente información autorizada. Revisar la necesidad de ampliar el modelo público, sin duplicar campos ya implantados.
- Revisar la información pública de donaciones solo cuando se hayan acordado las modalidades y sus condiciones.

**Criterio de cierre:** modalidades y modelos aprobados, registro privado definido y actualización de la web únicamente donde aporte claridad.

### EV-04 — Control de calidad y publicación reproducible

**Tipo:** Técnico / mantenibilidad  
**Estado:** Parcialmente cubierto por generador, validador y pruebas existentes; pendiente consolidar el flujo.

- Revisar los scripts y automatizaciones actuales antes de introducir otros: `generar_web.py`, `validar_catalogo.py`, `corregir_catalogo.py`, `TEST_DOCUMENTACION_TECNICA.py`, `TEST_BIBLIOTECA.py`, `TEST_PROCEDENCIA_F15.py` y `TEST_BIBLIOTECA_JS.cjs`.
- Unificar en un comando o flujo CI las comprobaciones de schema, generación limpia, enlaces internos, referencias de imágenes, duplicados de ID/URL, metadatos SEO y sitemap.
- Validar que no se publican accidentalmente datos privados, másteres, binarios de terceros o datos sintéticos de pruebas.
- Establecer pruebas de navegador real (escritorio y móvil) para catálogo, fichas, biblioteca, filtros, historial de navegación, reproducción audiovisual y CTA de apoyo. Aprovechar el entorno local si la ejecución automatizada está bloqueada.
- Generar en directorio aislado; revisar diferencias, páginas eliminadas y errores antes de publicar. Definir recuperación de la última versión válida y comprobaciones posteriores al despliegue.
- Mantener GitHub Pages y las URL canónicas existentes. No introducir infraestructura adicional sin necesidad demostrada.

**Criterio de cierre:** procedimiento de publicación repetible, regresión automatizada y lista breve de aceptación real. Confirmar qué pruebas de biblioteca siguen pendientes, dado que las pruebas previas de JavaScript se realizaron con DOM simulado.

### EV-05 — Inventario operativo y priorización de preservación de piezas

**Tipo:** Preservación / gestión interna  
**Estado:** Propuesta; evaluar herramientas o registros ya existentes.

Con un catálogo cercano a 1.700 piezas, conviene distinguir inventario físico de resultados de laboratorio y disponer de una cola de trabajo manejable.

- Mantener identificación del ejemplar físico, localización interna, composición de la edición, condición, incidencias y fecha de inspección.
- Priorizar por riesgo de deterioro, rareza, dificultad de sustitución, disponibilidad de hardware, estado de soporte y viabilidad de ejecución; no únicamente por popularidad.
- Distinguir caracterización, adquisición, verificación, copia segura, compatibilidad y documentación. Permitir estados pendientes o parciales sin declarar falsos cierres.
- Registrar qué másteres están depositados y verificados (EV-01) y qué guías requieren revisión.
- Mantener `preservacion.resumen` y `documentacion.json` como contratos públicos actuales; no duplicar resultados técnicos ni publicar ubicaciones físicas privadas.

**Criterio de cierre:** inventario y cola de trabajo utilizables para un lote piloto, con criterios de prioridad y trazabilidad entre pieza, máster y documentación.

### EV-06 — Consolidación y ampliación de procedimientos técnicos reutilizables

**Tipo:** Documental / laboratorio  
**Estado:** Parcial; las guías de Windows 3.1 y QuickTime 2.1.2 ya existen y no se vuelven a planificar.

Orden recomendado para futuras publicaciones, condicionado a evidencias y necesidades reales:

1. Entorno portable MS-DOS con DOSBox Staging: configuración, unidades, instalación multidisco, lanzador y guardado.
2. Digitalización de CD-ROM de datos y de modo mixto/CDDA, incluidos caracterización, selección ISO o BIN/CUE y verificación funcional; reutilizar los estándares vigentes.
3. Digitalización de disquetes: geometría, adquisición, cambio de disco, limitaciones de unidades USB y formatos de imagen.
4. Integridad SHA-256 y gestión de másteres/copias de trabajo, alineada con EV-01.
5. ScummVM: preparación y validación con títulos compatibles; diferenciar soporte del motor y fidelidad a la edición original.
6. Captura de introducciones originales: origen, relación de aspecto, sonido, formato de máster y copias para web/redes/YouTube.
7. Windows 95/98 u otros entornos históricos: únicamente tras validar una solución con licencias y requisitos documentados.

**Mejoras concretas de guías existentes (no recrearlas):** capturas reales de QuickTime 2.1.2, prueba de instalación desde Windows 3.1 sin QuickTime previo, reconstrucción completa desde cero del entorno base y validación en otros equipos; documentar disponibilidad y dependencia MIDI del anfitrión. Priorizar estas comprobaciones cuando un nuevo caso las requiera.

**Criterio de cierre por documento:** procedimiento reproducible, versiones y procedencia identificadas, evidencia real, limitaciones, relaciones desde `documentacion.json`, SEO y sitemap. No publicar instaladores, imágenes de discos ni otros binarios sin autorización. Evitar duplicar estándares o guías específicas.

---

## P2 — Media prioridad

### EV-07 — Enriquecimiento verificable de las fichas físicas

**Tipo:** Datos / funcional  
**Estado:** Parcial. Ya existen `incluye`, `soporte`, `idioma`, `mercado`, `anio`, `ean`, `tipo_edicion`, `procedencia`, `preservacion.resumen` y enlaces documentales generados.

- Mejorar la cobertura y precisión de los campos actuales antes de ampliar el schema.
- Evaluar detalle estructurado por componente: cantidad de discos/disquetes, idioma de caja/manual/software por separado, requisitos originales, referencias editoriales y estado de conservación publicable.
- Incorporar diferencias contrastadas entre ediciones y relaciones explícitas entre ejemplares cuando aporten valor (EV-08).
- Las protecciones anticopia y estados técnicos deben derivar de evidencia de laboratorio, no recuperar el antiguo bloque `proteccion` ni recomendaciones especulativas. No duplicar la documentación en `juegos.json`.
- No publicar claves de producto, números de serie sensibles, datos personales ni valores inferidos sin identificar su procedencia.

**Criterio de cierre:** modelo mínimo acordado, compatibilidad con fichas anteriores, migración reversible si procede y piloto con un lote representativo. Eliminar del alcance los campos que no aporten valor real.

### EV-08 — Relaciones entre títulos, ediciones y variantes

**Tipo:** Funcional / arquitectura de información  
**Estado:** Propuesta.

- Distinguir obra o título de edición física concreta, sin alterar la identidad histórica de cada ficha, su `num` ni su URL.
- Facilitar el descubrimiento de Big Box, Jewel Case, ediciones económicas, localizaciones, reediciones y compilaciones relacionadas, manteniendo las diferencias entre ejemplares.
- Evaluar un identificador estable de agrupación y relaciones explícitas revisadas editorialmente; no agrupar por coincidencia automática de título sin validación.
- Probar una sección de ediciones relacionadas y, solo si aporta valor, una vista comparativa de contenidos, mercado, año y soporte.

**Criterio de cierre:** piloto con varias familias de juegos, relaciones verificadas y ausencia de duplicación de fichas o canibalización SEO. Mantener URL y documentos asociados a la edición específica.

### EV-09 — Calidad de datos y mejora de la experiencia de búsqueda del catálogo

**Tipo:** Datos / experiencia de usuario  
**Estado:** Mejora incremental. El buscador y sus taxonomías ya existen.

- Medir cobertura real de metadatos y resolver avisos del validador mediante lotes pequeños revisables; normalizar valores históricos y campos heredados sin inventar información.
- Evaluar sinónimos, búsqueda con y sin acentos, nombres originales/localizados, términos alternativos y tolerancia a errores a partir de consultas reales o casos reproducibles.
- Revisar consistencia de filtros y resultados de catálogo y biblioteca, accesibilidad por teclado y claridad de estados sin resultados.
- Considerar un acceso desde los resultados a piezas con documentación verificada, derivado de `documentacion.json`, sin introducir duplicidad de estado.

**Criterio de cierre:** métricas de cobertura y casos de búsqueda definidos, mejoras validadas y cambios de datos separados de los funcionales.

### EV-10 — Accesibilidad, rendimiento e imágenes

**Tipo:** Técnico / experiencia de usuario  
**Estado:** Pendiente de auditoría y mejoras justificadas. Ya existen herramientas de optimización de imágenes y diseño adaptable.

- Auditar portada, catálogo, fichas, documentación y vídeos en móvil y escritorio; foco visible, contraste, navegación por teclado, textos alternativos y estructura de encabezados.
- Medir Core Web Vitals y peso de recursos antes de optimizar; revisar tamaños de imagen, carga diferida de galerías, dimensiones reservadas y formatos derivados adecuados. Conservar originales fuera de los derivados web.
- Revisar uso de scripts, CSS e índices de búsqueda; no reducir calidad documental de las fotografías para ganar rendimiento sin evaluación visual.
- Aplicar mejoras de accesibilidad y rendimiento con regresión de SEO y presentación.

**Criterio de cierre:** problemas reproducibles corregidos y comparación antes/después; mantener seguimiento periódico sin prometer una certificación de accesibilidad.

### EV-11 — Crecimiento y descubrimiento de la documentación

**Tipo:** Documental / funcional  
**Estado:** Propuesta condicionada a los datos de EV-02.

- Priorizar guías y mejoras de metadatos a partir de búsquedas sin resultados, lecturas y relaciones consultadas, además de la criticidad de preservación.
- Evaluar un indicador contextual de documentación disponible en los resultados del catálogo y accesos temáticos por tecnología o soporte cuando existan suficientes artículos.
- Mejorar referencias cruzadas útiles, revisión de enlaces externos y versionado editorial de guías desactualizadas.
- No reintroducir listados masivos en la portada de documentación ni crear categorías vacías.

**Criterio de cierre:** necesidades demostradas, navegación probada con usuarios o casos representativos y ninguna pérdida de accesibilidad o indexación. No implica rediseñar de nuevo la biblioteca.

### EV-12 — Flujo de trabajo editorial y audiovisual

**Tipo:** Operativo / técnico  
**Estado:** Propuesta. El canal oficial de YouTube, sección de vídeos y conversión de reels ya existen.

- Definir una lista de comprobación para alta de pieza, imágenes, ficha JSON, publicación social, novedad cuando proceda, guía y vídeo original.
- Mantener fuentes, fechas y duración verificadas; registrar correspondencia entre vídeo, edición física y URL propia/YouTube cuando sea útil.
- Evaluar automatización de tareas repetitivas (validar datos, preparar derivados, detectar archivos ausentes y generar borradores), conservando la revisión humana previa a publicar.
- Considerar subtítulos/transcripción de material propio o autorizado cuando aporten accesibilidad y valor documental. Revisar derechos y condiciones de publicación audiovisual.

**Criterio de cierre:** flujo piloto reproducible que reduzca trabajo manual sin degradar rigor ni introducir publicaciones automáticas sin revisión.

---

## P3 — Baja prioridad / condicionada a datos

### EV-13 — Evolución del apoyo contextual a la conservación

**Tipo:** Funcional / sostenibilidad  
**Estado:** En observación. F16.3 ya permite medir el recorrido desde la pieza hasta Ko-fi.

- Analizar clics, origen contextual frente a genérico, dispositivos y utilidad del CTA. Distinguir clic de aportación confirmada: no asumir una conversión económica por navegar a Ko-fi.
- Valorar campañas específicas, agradecimientos públicos consentidos o indicadores agregados solo si existe un mecanismo fiable y transparente.
- No publicar importes por pieza ni contadores de personas sin evidencia; mantener claro que el apoyo contextual actual contribuye al archivo en su conjunto.

**Condición de activación:** histórico suficiente y necesidad demostrada; cualquier nueva medición de aportaciones deberá tener fuente autorizada y respetar privacidad.

### EV-14 — Escalabilidad adicional de la biblioteca

**Tipo:** Técnico  
**Estado:** En espera. Paginación de 24 elementos, búsqueda, filtros y generación estática ya implementados.

Las pruebas existentes cubren 1.000, 3.500 y 10.000 documentos sintéticos. El índice global alcanzó unos 6,08 MB sin comprimir en el último escenario; no constituye por sí mismo un problema actual.

- Medir tamaño real del índice, tiempo de descarga y respuesta de filtros en dispositivos modestos.
- Evaluar carga diferida, segmentación por categoría o índices compactos si las mediciones justifican el coste.
- Mantener navegación HTML sin JavaScript, URL permanentes, canonical y sitemap; conservar el buscador global como no indexable.
- No migrar a un backend, motor externo o nueva infraestructura por anticipación.

**Condición de activación:** degradación observada o previsión cercana sustentada en métricas de crecimiento y rendimiento.

### EV-15 — Interoperabilidad y acceso a datos documentales

**Tipo:** Estratégico / datos  
**Estado:** Idea para evaluación.

- Evaluar exportaciones controladas de metadatos públicos, feeds de novedades o documentación y formatos interoperables para investigadores y proyectos afines.
- Definir alcance, versión, licencia de los metadatos propios, atribución y exclusiones de contenidos de terceros antes de ofrecer descargas masivas.
- Reutilizar las fuentes existentes; no crear una API dinámica si un formato estático satisface la necesidad.

**Condición de activación:** demanda demostrada, licencias aclaradas y coste de mantenimiento asumible.

### EV-16 — Sostenibilidad y nuevas vías de financiación

**Tipo:** Estratégico / sostenibilidad  
**Estado:** En espera de datos. Ko-fi y apoyo contextual ya implantados.

- Reevaluar AdSense, afiliación seleccionada, patrocinios, membresías y campañas de adquisición o restauración únicamente si benefician la continuidad.
- Considerar costes, carga administrativa, impacto en privacidad, experiencia y confianza de la comunidad; mantener independencia editorial.
- No introducir publicidad intrusiva ni compromisos de conservación que el archivo no pueda cumplir.

**Condición de activación:** datos de uso y apoyo suficientes, necesidad económica definida y modelo transparente.

### EV-17 — Colaboraciones, investigación y exposición futura

**Tipo:** Estratégico / organizativo  
**Estado:** Idea para evaluación.

- Explorar colaboración con otros archivos, coleccionistas, investigadores y entidades culturales para identificar ediciones, completar material y compartir conocimiento técnico.
- Valorar mecanismos de aportación de correcciones y testimonios con revisión editorial, reconocimiento autorizado y trazabilidad de fuentes.
- Evaluar exposición física temporal o acceso de investigación con recursos, seguros, custodia y condiciones de derechos adecuados.

**Condición de activación:** capacidad operativa y acuerdos claros; no presentar el proyecto como institución o exposición permanente mientras no se materialice.

---

# Operación continua (fuera del backlog de funcionalidades)

Estas actividades ya cuentan con capacidades o procedimientos establecidos. Se mantienen de forma recurrente y solo originan un nuevo evolutivo cuando se detecta una carencia concreta.

| Línea | Actividad y control |
|---|---|
| Catalogación | Incorporar piezas, fotografiar, validar JSON, mantener procedencia autorizada y fechas reales, sin inventar datos históricos. |
| Preservación y compatibilidad | Estándar v1.0 y posteriores revisiones controladas; caracterización previa, adquisición apropiada, SHA-256, separación máster/copia de trabajo, registro y guía por pieza cuando proceda. Aplicar el criterio vigente de no repetir una lectura correcta de forma rutinaria; justificar relecturas y límites. |
| Biblioteca | Alta mediante `documentacion.json`, fuentes Markdown, facetas contrastadas, relaciones, imágenes y limitaciones; reutilizar las guías transversales. |
| SEO técnico | Revisar Search Console, cobertura, sitemap, robots, canonical, datos estructurados, metadatos e imágenes; corregir incidencias concretas. La búsqueda documental permanece fuera del sitemap. |
| GA4 y tráfico | Revisar tráfico real y automatizado, especialmente patrones geográficos anómalos previamente observados en China y Japón. Analizar páginas de entrada, frecuencia y señales disponibles; no atribuir tráfico a bots o modelos de IA sin evidencia. No presuponer acceso a logs/user agents de GitHub Pages ni bloquear preventivamente. |
| Apoyo | Observar eventos existentes de Ko-fi y CTA contextual, distinguir clics de pagos confirmados, respetar privacidad. |
| Difusión | Publicaciones en redes, vídeos, novedades editoriales y canal oficial de YouTube; conservar consistencia documental. |
| Seguridad y continuidad | Revisar permisos, actualizaciones, cuentas, dominio y copias de seguridad conforme a la política que se establezca en EV-01. |
| Publicación | Regeneración, validación, revisión de cambios y despliegue controlado; aplicar EV-04 cuando se consolide. |

Los casos nuevos de soportes, protecciones y compatibilidad no constituyen automáticamente una fase: evaluar primero si basta con ampliar el estándar o publicar una guía reutilizable. No alterar `preservacion.resumen` sin evidencia verificada ni duplicar la relación documental en el catálogo.

---

# Histórico de evolutivos cerrados

Se conserva la trazabilidad anterior. Los trabajos del 28/11 se registran como implementados y entregados; cuando la aceptación completa, el despliegue o una prueba específica no están acreditados, se mantienen como comprobaciones operativas o pendientes concretos en el backlog, no como funcionalidades por rehacer.

| Evolutivo | Fecha de cierre | Resultado |
|---|---|---|
| Guía técnica QuickTime 2.1.2 y corrección de evidencias | 28/11/2026 | Guía independiente, relaciones con entorno base e In the 1st Degree, retirada de tres capturas 2.03; 28 documentos. Pendientes de evidencia complementaria en EV-06. |
| Biblioteca documental escalable | 28/11/2026 | Portal compacto, índices independientes, buscador global, facetas, ordenación, URL con estado, paginación de 24, HTML estático, SEO y pruebas de escala hasta 10.000 documentos. Implementación entregada y valoración favorable del usuario; pruebas completas de navegador real no acreditadas (EV-04). |
| Corrección de navegación documental | 28/11/2026 | Categorías vacías ocultas, índices permanentes y acceso a los entornos de referencia. |
| In the 1st Degree — preservación y compatibilidad | 28/11/2026 | Dos ISO verificadas, solución FMV con QuickTime 2.1.2, guardado/carga, cambio de CD, arranque portable y guía ilustrada. Depósito definitivo pendiente de confirmar (EV-01). |
| Documentación técnica transversal | 28/11/2026 | Categoría `tecnica`, índice propio, relaciones documentales, guía común Windows 3.1 y refactorización de dos guías específicas. |
| Canal oficial de YouTube | 14/11/2026 | Integración en pie, contacto y vídeos; `Organization.sameAs`, evento de salida social y novedad editorial. |
| F18 — Novedades destacadas y organización editorial | 29/10/2026 | Destacado único de portada, vigencia de 14 días, artículos con contenido y recursos propios; estilos y organización consolidados. |
| Modelo mínimo de preservación en catálogo | 06/10/2026 | Sustitución del bloque legado `proteccion` por `preservacion.resumen` respaldado por evidencia real. |
| F17 — Área documental, preservación y compatibilidad reproducible | 05/10/2026 | F17.1–F17.6 cerradas. Área documental, estándares versionados, integración con fichas y piloto completo de Red Baron 3-D desde pieza física hasta guía de ejecución en Windows 10. |
| F17.6 — Validación y cierre | 05/10/2026 | Lecciones del piloto consolidadas, Definition of Done validado y estándar v1.0 declarado estable. |
| F17.5 — Piloto real Red Baron 3-D | 05/10/2026 | Preservación verificada por doble adquisición coincidente, copia de trabajo validada y guía reproducible de Windows 10 publicada. |
| F17.4 — Integración documentación-fichas | 05/10/2026 | Relación bidireccional generada desde `documentacion.json` sin duplicar datos en el catálogo. |
| F17.3 — Estándar de guías de ejecución | 04/10/2026 | Estándar y plantilla de compatibilidad reproducible por edición y entorno. |
| F17.2 — Estándar y procedimientos de preservación | 04/10/2026 | Estándar público, caracterización de soportes ópticos, publicación Markdown y plantilla operativa por pieza. |
| F17.1 — Arquitectura del área documental | 04/10/2026 | `/documentacion/`, índice `documentacion.json`, navegación, SEO, breadcrumbs y sitemap. |
| F16.5 — Novedades del archivo | 04/10/2026 | `novedades.json`, bloque en portada, histórico `/novedades/`, navegación y sitemap. |
| F16.4 — Propiedades globales y fecha de última actualización | 04/10/2026 | `propiedades.json` como configuración transversal inicial y fecha de última actualización visible en portada. |
| F16.3 — Apoyo contextual a la conservación de piezas | 03/10/2026 | CTA por pieza, contexto en `/apoyar/`, integración con Ko-fi y analítica GA4. |
| F16 — Sostenibilidad | Septiembre–octubre 2026 | Página de apoyo, integración Ko-fi y medición inicial; fecha exacta de cierre global no revisada. |
| F15 — Procedencia pública | Septiembre 2026 | Campo de procedencia, identidad autorizada y enlaces a redes sociales. |
| F14 — Últimas incorporaciones | Septiembre 2026 | Fecha de incorporación y listado reciente ordenado por fecha. |
| F13 — Proyecto, conservación y donaciones | 11/09/2026 | Página institucional, información para donantes, flujo de conservación y hoja de ruta pública. |

---

# Criterios de priorización y cierre

1. **Continuidad e integridad:** protección de piezas, activos digitales y capacidad de recuperación.
2. **Preservación y valor documental:** conocimiento contrastado, trazabilidad y utilidad histórica.
3. **Reutilización y dependencias:** capacidades que desbloquean otros trabajos.
4. **Impacto para el usuario:** mejora real de acceso, descubrimiento y comprensión.
5. **Mantenibilidad:** minimizar duplicidad, complejidad y coste recurrente.
6. **Evidencia y datos disponibles:** priorizar necesidades demostradas; medir antes de introducir funcionalidades especulativas.
7. **Privacidad, derechos y sostenibilidad:** proteger datos, respetar licencias e independencia documental.

Para cerrar un evolutivo: alcance acordado, cambios identificados, pruebas pertinentes ejecutadas, limitaciones documentadas, aceptación y despliegue diferenciados, histórico actualizado. Si una parte queda pendiente, conservar solo esa parte en el backlog.

## Próxima secuencia recomendada

1. Confirmar la cobertura de conservación y recuperación (EV-01); resolver cualquier carencia crítica detectada.
2. Abordar la analítica documental avanzada (EV-02) como siguiente evolutivo funcional de la web, aprovechando la arquitectura recién consolidada.
3. Avanzar la formalización de incorporaciones (EV-03) en paralelo si surgen casos reales, y consolidar el flujo de publicación (EV-04).
4. Planificar el inventario y la priorización de piezas (EV-05); ampliar las guías reutilizables (EV-06) conforme al trabajo del laboratorio.
5. Seleccionar mejoras P2 según los datos obtenidos. Reevaluar P3 únicamente al cumplirse sus condiciones de activación.

> Este documento debe mantenerse vivo. No es un compromiso de calendario ni de alcance completo. Las propuestas nuevas deben validarse antes de convertirse en fases definitivas.
