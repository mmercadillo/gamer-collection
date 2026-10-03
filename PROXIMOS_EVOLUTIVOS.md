# PC Game Archive — Próximos evolutivos

Documento vivo para registrar, ordenar y mantener los próximos evolutivos de PC Game Archive.

**Base actual:** F16.3 — Apoyo contextual a la conservación de piezas  
**Última actualización:** 03/10/2026

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

## 1. Área documental de PC Game Archive

**Prioridad:** Alta  
**Estado:** Pendiente de definición funcional  
**Propuesta inicial:** F17

Crear una sección documental propia dentro de PC Game Archive que permita publicar contenidos de preservación, historia, formatos y conocimiento técnico sin depender únicamente de las fichas de los juegos.

### Alcance previsto

- Nueva sección `/documentacion/`.
- Categorías y navegación propia.
- URLs limpias y permanentes.
- Breadcrumbs.
- Metadatos SEO y datos estructurados cuando proceda.
- Integración con sitemap.
- Enlaces bidireccionales entre artículos y piezas del catálogo.
- Plantilla reutilizable para nuevos contenidos.
- Posibilidad de relacionar varios artículos con una misma pieza.

### Primeros contenidos candidatos

- Preservación de CD-ROM y DVD-ROM.
- Preservación de disquetes.
- Qué es una edición Big Box.
- Formatos y soportes físicos de juegos de PC.
- Compatibilidad de juegos antiguos con sistemas actuales.
- Historia y documentación de editoras/distribuidoras relevantes.

---

## 2. Procedimientos de preservación digital

**Prioridad:** Alta  
**Estado:** Pendiente de diseño

Definir y documentar un procedimiento reproducible para preservar digitalmente los soportes físicos del archivo.

### Alcance previsto

- Procedimiento para CD-ROM/DVD-ROM.
- Procedimiento para disquetes.
- Creación de imágenes de preservación.
- Herramientas recomendadas por tipo de soporte.
- Verificación de lectura e integridad.
- Hashes y algoritmos admitidos.
- Convenciones de nombres.
- Metadatos mínimos de preservación.
- Registro de errores de lectura o daños.
- Copias maestras y copias de trabajo.
- Estrategia de copias de seguridad.
- Política de no modificación de los originales digitales.
- Documentación de cualquier intervención realizada sobre el soporte.

### Objetivo

Que otra persona pueda repetir el proceso sobre una pieza y obtener un resultado compatible con el estándar de PC Game Archive.

---

## 3. Guías de ejecución y compatibilidad — “Guías burros”

**Prioridad:** Alta  
**Estado:** Pendiente de diseño

Crear guías muy prácticas y reproducibles para ejecutar juegos antiguos en equipos actuales.

### Casos a cubrir

- Ejecución nativa en Windows 10/11.
- Modos de compatibilidad.
- Parches oficiales y comunitarios.
- Wrappers gráficos o de sonido.
- DOSBox y derivados.
- ScummVM.
- Máquinas virtuales.
- Versiones antiguas de Windows cuando sean necesarias.
- Instaladores de 16 bits y otras incompatibilidades históricas.
- Configuración de resolución, audio y aceleración gráfica.

### Criterios

Cada guía debería indicar, como mínimo:

- juego/edición probada;
- sistema anfitrión;
- herramientas y versiones utilizadas;
- pasos exactos;
- resultado esperado;
- limitaciones conocidas;
- advertencias;
- fecha de la última prueba.

---

## 4. Formalización de las modalidades de incorporación de piezas

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

## 5. Enriquecimiento de las fichas de las piezas

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

## 6. Relación entre pieza física, preservación digital y documentación

**Prioridad:** Media-Alta  
**Estado:** Backlog conceptual

Definir un modelo que permita reflejar claramente las tres capas del archivo:

1. **pieza física conservada**;
2. **copia o evidencia de preservación digital**;
3. **documentación pública asociada**.

Esto permitirá saber en el futuro, por ejemplo, qué piezas están únicamente catalogadas, cuáles han sido digitalizadas y cuáles además tienen una guía de ejecución verificada.

---

## 7. Seguimiento y analítica del apoyo por pieza

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

## 8. Revisión del tráfico automatizado y procedencia geográfica

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

## 9. SEO técnico y calidad del catálogo

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

## 10. Evolución de sostenibilidad y monetización

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
