# PC Game Archive — Próximos evolutivos

Documento vivo para registrar, ordenar y mantener los próximos evolutivos de PC Game Archive.

**Base actual:** F17 — Área documental, preservación y compatibilidad reproducible cerrada  
**Última actualización:** 05/10/2026

---

## Cómo mantener este documento

- Añadir aquí cualquier nueva necesidad, idea o caso de uso que surja.
- No asignar una fase definitiva hasta que el alcance esté suficientemente definido.
- Mantener separados los evolutivos funcionales, los trabajos documentales y las mejoras técnicas.
- Cuando un evolutivo se cierre, retirarlo de la lista activa y registrarlo en **Histórico de evolutivos cerrados**.
- Si una necesidad crece demasiado, dividirla en subfases o entregas independientes.
- Evitar mezclar en una misma fase cambios no relacionados solo por aprovechar una entrega.

---

# Backlog activo

## Líneas operativas consolidadas tras F17

F17 deja de formar parte del backlog activo y pasa a operación continua. Quedan consolidadas las siguientes capacidades:

- área pública `/documentacion/` con fuentes Markdown, SEO, breadcrumbs y sitemap;
- relación bidireccional entre documentación y fichas mediante `documentacion.json`;
- estándar de preservación digital único y versionado, actualmente **v1.0**;
- caracterización previa obligatoria antes de elegir método de adquisición;
- `PLANTILLA_REGISTRO_PRESERVACION.md` para cada pieza preservada;
- estándar y `PLANTILLA_GUIA_EJECUCION.md` para compatibilidad en sistemas actuales;
- primer recorrido completo validado con **Red Baron 3-D, ficha #000215**;
- separación obligatoria entre máster de preservación y copia de trabajo;
- publicación únicamente de resultados respaldados por evidencia real.

Los nuevos soportes, protecciones o escenarios de compatibilidad que aparezcan no constituyen automáticamente una nueva fase: primero se evaluará si pueden resolverse evolucionando el estándar/procedimiento vigente con su versionado correspondiente.

---

## 1. Formalización de las modalidades de incorporación de piezas

**Prioridad:** Alta  
**Estado:** Pendiente de definición jurídica/documental

Formalizar las distintas formas mediante las que una pieza puede incorporarse a PC Game Archive.

### Modalidades previstas

- Compra.
- Donación definitiva.
- Cesión condicionada a la continuidad del proyecto.
- Depósito/custodia.
- Otras modalidades que aparezcan en casos reales.

### Aspectos a definir

- titularidad de la pieza;
- condiciones de conservación;
- posibilidad de digitalización;
- autorización para fotografía y documentación pública;
- atribución del donante/cedente cuando lo solicite;
- redes sociales o identidad pública asociada;
- condiciones de devolución cuando proceda;
- tratamiento de la pieza si PC Game Archive dejase de existir;
- documentación o justificante asociado a cada modalidad.

### Impacto potencial en el catálogo

Revisar si el modelo actual de `procedencia` es suficiente o si debe evolucionar para diferenciar claramente procedencia, modalidad jurídica e identidad pública del aportante.

---

## 2. Enriquecimiento de las fichas de las piezas

**Prioridad:** Media-Alta  
**Estado:** Backlog

Aumentar progresivamente el valor documental de cada pieza más allá de las fotografías y datos básicos actuales.

### Posibles ampliaciones

- contenido exacto de la edición;
- soporte físico incluido;
- número de discos/disquetes;
- manuales, mapas, guías, tarjetas u otros extras;
- estado de conservación;
- idioma de cada elemento;
- requisitos de sistema originales;
- protecciones anticopia relevantes;
- número de serie o referencias editoriales cuando sean útiles y publicables;
- diferencias respecto a otras ediciones del mismo juego;
- relaciones con otras piezas del archivo;
- enlaces a artículos documentales propios;
- estado de preservación digital;
- estado de prueba de compatibilidad en sistemas actuales.

### Criterio

Evitar convertir la ficha en una acumulación indiscriminada de campos. Cada dato nuevo debe aportar valor documental o de preservación.

---

## 3. Seguimiento y analítica del apoyo por pieza

**Prioridad:** Media  
**Estado:** Observar antes de evolucionar

F16.3 permite medir el recorrido desde una pieza hasta Ko-fi. Antes de añadir nuevas funcionalidades se debe recopilar histórico suficiente.

### Revisar posteriormente

- número de clics de apoyo desde fichas;
- piezas que generan más interés;
- conversión frente al acceso genérico desde `/apoyar/`;
- comportamiento por dispositivo;
- utilidad real del CTA contextual.

### Posibles evolutivos futuros

Solo si existen datos suficientes:

- indicador de que una pieza ha recibido apoyo de la comunidad;
- número de personas que han apoyado desde una pieza, sin mostrar importes;
- campañas concretas de preservación;
- nuevas vías de apoyo además de Ko-fi.

No implementar contadores o mensajes económicos por pieza sin disponer previamente de un modelo fiable y transparente.

---

## 4. Revisión del tráfico automatizado y procedencia geográfica

**Prioridad:** Media  
**Estado:** En observación

Se ha detectado un incremento significativo de tráfico procedente de China y posteriormente Japón, con patrones compatibles con navegación automatizada o crawlers.

### Pendiente

- continuar recopilando datos;
- diferenciar tráfico humano de automatizado cuando sea posible;
- revisar user agents, páginas de entrada y frecuencia;
- determinar si existe indexación por buscadores, modelos de IA u otros robots;
- evitar bloqueos preventivos mientras no exista impacto negativo demostrable;
- vigilar distorsión de métricas GA4.

---

## 5. SEO técnico y calidad del catálogo

**Prioridad:** Media  
**Estado:** Mantenimiento continuo

Continuar mejorando la calidad técnica y semántica del archivo.

### Líneas abiertas

- revisión de SEO de imágenes;
- mejora progresiva de metadatos;
- revisión de datos estructurados;
- control de sitemap e indexación;
- normalización de valores históricos de `juegos.json`;
- resolución gradual de incidencias detectadas por el validador del catálogo;
- eliminación de inconsistencias de tipos y campos heredados;
- revisión periódica de Search Console.

Las correcciones de datos deben realizarse separadamente de los evolutivos funcionales para facilitar su validación.

---

## 6. Evolución de sostenibilidad y monetización

**Prioridad:** Baja / condicionada a datos  
**Estado:** En espera

F16 incorporó la infraestructura inicial de sostenibilidad mediante Ko-fi y F16.3 añadió apoyo contextual por pieza.

Antes de introducir nuevas vías se debe observar el comportamiento real del proyecto.

### Opciones que pueden reevaluarse en el futuro

- AdSense.
- Afiliación seleccionada.
- Patrocinios compatibles con la independencia del archivo.
- Membresías o apoyo recurrente.
- Campañas concretas de adquisición o restauración de piezas.

### Principio

La monetización debe financiar la conservación y continuidad del archivo sin condicionar su criterio documental ni degradar la experiencia de consulta.

---

# Ideas sin fase asignada

Utilizar esta sección para registrar ideas todavía demasiado inmaduras para formar parte del backlog priorizado.

| Idea | Fecha | Notas |
|---|---|---|
| — | — | — |

---

# Histórico de evolutivos cerrados

Esta sección permite retirar elementos del backlog activo sin perder trazabilidad.

| Evolutivo | Fecha de cierre | Resultado |
|---|---|---|
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

---

# Criterios de priorización

Cuando existan varios candidatos para la siguiente fase, valorar:

1. **Preservación:** cuánto mejora la conservación física o digital del archivo.
2. **Valor documental:** cuánto conocimiento nuevo aporta al visitante.
3. **Reutilización:** si crea una base aprovechable por futuros evolutivos.
4. **Impacto para el usuario:** mejora real de consulta, comprensión o acceso.
5. **Mantenibilidad:** coste futuro de conservar la funcionalidad.
6. **Dependencias:** si desbloquea otros trabajos del backlog.
7. **Datos disponibles:** evitar construir funcionalidades basadas únicamente en hipótesis cuando pueden medirse primero.

---

> Este documento debe considerarse parte de la documentación viva de PC Game Archive y actualizarse cada vez que aparezca un nuevo caso relevante, se redefina una prioridad o se cierre un evolutivo.
