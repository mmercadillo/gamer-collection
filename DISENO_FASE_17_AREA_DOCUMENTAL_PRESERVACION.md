# PC Game Archive — F17 — Diseño del área documental y protocolo de preservación reproducible

**Estado:** F17.1–F17.4 completadas · F17.5 pendiente  
**Base de partida:** F16.5 — Novedades del archivo  
**Fecha:** 04/10/2026

---

## 1. Propósito

F17 debe crear la infraestructura documental necesaria para que PC Game Archive pueda documentar de forma reproducible:

1. cómo se caracteriza un soporte físico concreto;
2. cómo se realiza su adquisición digital de preservación;
3. cómo se verifica y conserva el resultado;
4. cómo se obtiene una copia o derivado de trabajo;
5. cómo se instala y ejecuta la edición concreta conservada en sistemas actuales;
6. cómo se relaciona toda esa evidencia con la ficha pública de la pieza.

El objetivo no es crear tutoriales genéricos aislados, sino un sistema documental consistente que pueda aplicarse de forma repetible a cada pieza del archivo.

---

## 2. Principios innegociables

### 2.1. La ficha de la pieza es el nodo principal

La ficha del juego representa la edición física concreta conservada por PC Game Archive.

Desde ella podrán relacionarse, cuando existan:

- el registro de preservación de la pieza;
- el procedimiento técnico reutilizable empleado;
- una guía de ejecución/compatibilidad verificada;
- otros documentos relevantes.

No se duplicará la ficha de la pieza dentro de `/documentacion/`.

### 2.2. La metodología es global; la evidencia es específica de cada pieza

No existe una única receta del tipo «todo CD-ROM se convierte en ISO».

El estándar general define **cómo analizar, decidir, adquirir, verificar y documentar**.

Cada pieza determina, a partir de sus características reales, qué procedimiento de adquisición debe aplicarse.

Por tanto:

> **La metodología es reutilizable; la caracterización, la elección del método y el resultado de preservación son específicos de cada pieza/edición.**

### 2.3. Preservación y ejecución son procesos distintos

El objetivo de la preservación es representar el soporte original con la mayor fidelidad razonable y conservar evidencia verificable del proceso.

El objetivo de la compatibilidad es conseguir ejecutar la edición preservada en un entorno actual de forma reproducible.

Una solución válida para jugar hoy no debe utilizarse como criterio para decidir qué información conservar del soporte original.

### 2.4. La copia maestra de preservación no se modifica

Flujo obligatorio:

```text
SOPORTE FÍSICO
      │
      ▼
CARACTERIZACIÓN
      │
      ▼
ADQUISICIÓN DIGITAL
      │
      ▼
MASTER DE PRESERVACIÓN
      │
      ├── hashes
      ├── logs
      ├── metadatos
      ├── incidencias
      └── información auxiliar necesaria
      │
      ▼
VERIFICACIÓN
      │
      ▼
MASTER INMUTABLE
      │
      ▼
COPIA / DERIVADO DE TRABAJO
      │
      ▼
INSTALACIÓN / PRUEBAS / COMPATIBILIDAD
```

Las pruebas, conversiones, parches, wrappers o modificaciones necesarias para ejecutar un juego se realizan sobre una copia de trabajo, nunca sobre el master de preservación.

### 2.5. «Imagen» no implica necesariamente ISO

En F17 se utilizará preferentemente el término **adquisición digital del soporte**.

El resultado puede estar formado por uno o varios ficheros y elementos auxiliares según el soporte y sus características.

No se seleccionará un formato de salida antes de caracterizar el soporte.

### 2.6. La edición concreta importa

No se asumirá que dos ediciones del mismo título tienen la misma estructura, masterización, protección, soporte o comportamiento.

La documentación debe identificar siempre que sea posible la edición física concreta utilizada por PC Game Archive.

### 2.7. Reproducibilidad

Una tercera persona con conocimientos técnicos suficientes debe poder comprender:

- qué pieza se trató;
- qué se observó en el soporte;
- por qué se eligió un determinado procedimiento;
- qué herramientas y versiones se usaron;
- qué resultado se obtuvo;
- cómo se verificó;
- qué incidencias aparecieron;
- qué procedimiento se siguió posteriormente para ejecutarlo.

---

## 3. Modelo documental de F17

F17 distinguirá tres niveles.

### Nivel 1 — Estándar general de PC Game Archive

Define las reglas comunes a cualquier proceso de preservación:

- inspección;
- caracterización;
- selección del método;
- adquisición;
- verificación;
- hashes;
- metadatos;
- gestión de errores;
- master de preservación;
- copia de trabajo;
- almacenamiento y backup;
- trazabilidad.

Este documento no debe convertirse en una receta única para todos los soportes.

### Nivel 2 — Procedimientos técnicos reutilizables

Procedimientos aplicables cuando la caracterización de la pieza determina que corresponden.

Ejemplos conceptuales:

- CD de datos;
- CD con datos y audio;
- CD multisesión;
- DVD-ROM;
- disquete;
- soportes con características especiales;
- otros casos que aparezcan en piezas reales.

No se crearán procedimientos por adelantado si todavía no existe un caso real que los justifique.

### Nivel 3 — Registro específico de preservación de una pieza

Documento/evidencia que registra qué se hizo realmente con la edición concreta.

Debe enlazar con:

- su ficha del catálogo;
- el procedimiento reutilizable aplicado;
- la guía de ejecución correspondiente, si existe.

---

## 4. Caracterización obligatoria antes de la adquisición

Antes de generar cualquier master se debe analizar el soporte.

### 4.1. Identificación de la pieza

Registrar al menos cuando sea posible:

- título;
- edición;
- mercado/país;
- idioma;
- editor/distribuidor;
- referencia comercial;
- número total de soportes;
- identificador interno de la pieza;
- fotografías ya asociadas a la ficha;
- identificación física adicional relevante.

### 4.2. Estado físico

Registrar:

- estado general;
- suciedad;
- arañazos;
- deformaciones;
- daños visibles;
- etiquetas/anotaciones;
- cualquier intervención previa conocida.

No debe realizarse ninguna limpieza o intervención relevante sin documentarla.

### 4.3. Caracterización lógica/física del soporte

Según el tipo de soporte, determinar aquello que sea relevante, por ejemplo:

- tipo de medio;
- número y tipo de pistas;
- presencia de audio;
- sesiones;
- sistema de ficheros;
- capacidad utilizada;
- estructura anómala;
- sectores problemáticos;
- información auxiliar necesaria para representar fielmente el soporte;
- cualquier otra característica que condicione la adquisición.

### 4.4. Protecciones y características especiales

Las protecciones anticopia y otros mecanismos especiales forman parte de la caracterización técnica de la edición.

Deben registrarse cuando puedan identificarse de forma fiable porque pueden afectar:

- al método de lectura;
- al formato de preservación;
- a la información auxiliar necesaria;
- a la posibilidad de verificar el master;
- a la forma de utilizar posteriormente una copia de trabajo.

**No debe asumirse una protección únicamente porque exista en otra edición del mismo juego.**

La identificación debe basarse, siempre que sea posible, en evidencia obtenida de la pieza concreta y quedar documentada.

La documentación pública de PC Game Archive tiene finalidad de preservación, investigación y reproducibilidad del archivo; no tiene como objetivo distribuir software protegido ni proporcionar mecanismos destinados a eludir controles de acceso.

---

## 5. Selección del procedimiento de adquisición

La elección se realiza **después de la caracterización**.

Flujo conceptual:

```text
SOPORTE
   │
   ▼
CARACTERIZACIÓN
   │
   ├── estructura normal
   ├── audio / varias pistas
   ├── multisesión
   ├── protección o característica especial
   ├── errores/anomalías
   └── otros casos
   │
   ▼
SELECCIÓN DEL PROCEDIMIENTO ADECUADO
   │
   ▼
ADQUISICIÓN
```

Dos CD-ROM pueden requerir métodos distintos.

Incluso dos ediciones del mismo juego pueden requerir procedimientos distintos.

Por este motivo no se debe etiquetar una pieza simplemente como «CD-ROM preservado mediante ISO» sin haber completado primero su caracterización.

---

## 6. Master de preservación

El resultado de la adquisición constituye un **conjunto de preservación**, no necesariamente un único fichero.

Puede contener, según el caso:

- datos adquiridos del soporte;
- descriptor(es) de estructura;
- datos auxiliares;
- logs de lectura;
- metadatos técnicos;
- registro de incidencias;
- hashes;
- información sobre herramientas/hardware empleados.

### Reglas

1. El master se conserva sin modificaciones posteriores.
2. Se calculan hashes sobre los elementos que formen parte del conjunto de preservación.
3. Se registra la herramienta y versión utilizada.
4. Cuando sea relevante, se registra el dispositivo lector y su identificación.
5. Los errores o sectores problemáticos no se ocultan: forman parte del registro.
6. Una adquisición parcialmente legible debe registrarse como tal y no como preservación verificada.

---

## 7. Verificación

Crear los ficheros no significa haber terminado la preservación.

La verificación deberá determinar, según el procedimiento aplicable:

- que la lectura terminó de acuerdo con los criterios definidos;
- que la estructura resultante corresponde con la observada;
- que los elementos necesarios están presentes;
- que los hashes quedan registrados;
- que no se han producido errores no documentados;
- que el resultado puede conservarse y reproducirse con las herramientas previstas.

### Estados conceptuales de preservación

El modelo futuro debe permitir distinguir al menos:

- `no_realizada`;
- `realizada`;
- `verificada`;
- `parcial`;
- `no_legible`.

Estos estados deberán concretarse antes de implementarse en el modelo de datos.

---

## 8. Copia o derivado de trabajo

Tras verificar el master puede crearse una copia/derivado destinado a:

- montaje;
- instalación;
- pruebas;
- conversión a formatos más cómodos;
- extracción temporal;
- aplicación de actualizaciones;
- wrappers;
- configuración de compatibilidad;
- pruebas en máquinas virtuales/emuladores;
- otras intervenciones necesarias para estudiar la ejecución actual.

Cualquier transformación aplicada al derivado debe poder distinguirse del master de preservación.

---

## 9. Guías de ejecución y compatibilidad

Las guías de ejecución serán específicas de una edición probada siempre que sea posible.

No deben limitarse a afirmar «funciona en Windows 11».

### Contenido mínimo

- título y edición probada;
- pieza de PC Game Archive relacionada;
- origen de la copia de trabajo;
- sistema anfitrión;
- versión concreta del sistema operativo;
- hardware relevante cuando pueda afectar al resultado;
- herramientas y versiones utilizadas;
- requisitos previos;
- pasos exactos;
- actualizaciones/parches utilizados;
- configuración aplicada;
- resultado esperado;
- limitaciones conocidas;
- advertencias;
- fecha de última verificación.

### Verificación por subsistemas

Cuando proceda, registrar separadamente:

- instalación;
- arranque;
- interfaz/menús;
- vídeo/cinemáticas;
- sonido;
- música;
- gráficos 2D/3D;
- entrada/controles;
- inicio de partida;
- guardado;
- carga;
- multijugador;
- otros subsistemas relevantes.

Estados conceptuales de compatibilidad:

- `no_probada`;
- `funcional`;
- `funcional_con_ajustes`;
- `parcial`;
- `no_funcional`.

---

## 10. Integración con la ficha de la pieza

La ficha será el punto de entrada público.

Cuando exista información suficiente podrá mostrar una sección **Preservación y compatibilidad**.

Ejemplo conceptual:

```text
Preservación digital
✓ Adquisición realizada y verificada
Soporte: CD con datos y audio
Ver registro de preservación →

Compatibilidad actual
✓ Probado en Windows 11
Ver guía paso a paso →
```

### Regla de interfaz

Si una pieza todavía no dispone de preservación o guía de ejecución, no se mostrarán bloques vacíos, botones deshabilitados ni mensajes «próximamente» de forma masiva.

---

## 11. Arquitectura documental propuesta

Estructura conceptual inicial:

```text
/documentacion/
│
├── preservacion/
│   ├── [procedimientos generales y técnicos]
│   └── ...
│
└── guias/
    ├── [guías específicas de ejecución]
    └── ...
```

El contenido específico de una pieza se relacionará con su ficha y no duplicará la ficha completa dentro de `/documentacion/`.

La infraestructura de fuentes, metadatos y generación quedó implementada en F17.1. Desde F17.2, el cuerpo documental se mantiene en fuentes Markdown y se renderiza mediante un subconjunto controlado soportado por `generar_web.py`.

---

## 12. Checklist obligatoria para cada nueva pieza que se preserve

Esta lista debe revisarse **siempre** antes de considerar preservada una pieza.

### A. Identificación

- [ ] He confirmado la edición física concreta.
- [ ] He identificado todos los soportes incluidos.
- [ ] He relacionado el proceso con la ficha correcta de PC Game Archive.

### B. Inspección

- [ ] He registrado el estado físico relevante.
- [ ] He documentado cualquier limpieza o intervención realizada.

### C. Caracterización

- [ ] He identificado el tipo exacto de soporte.
- [ ] He analizado la estructura lógica/física relevante.
- [ ] He comprobado si existen pistas de audio, sesiones u otras particularidades.
- [ ] He investigado/determinado si existen protecciones o características especiales que afecten a la adquisición.
- [ ] No he supuesto que esta edición es idéntica a otra edición del mismo título.

### D. Selección del método

- [ ] He elegido el procedimiento de adquisición después de caracterizar el soporte.
- [ ] Puedo justificar por qué ese procedimiento es adecuado para esta pieza.
- [ ] He identificado qué información debe conservarse además de los datos de usuario, si procede.

### E. Adquisición

- [ ] He registrado herramienta y versión.
- [ ] He registrado hardware lector cuando es relevante.
- [ ] He conservado logs y datos auxiliares requeridos por el procedimiento.
- [ ] He documentado errores, sectores problemáticos o anomalías.

### F. Verificación

- [ ] He verificado el resultado según el procedimiento aplicable.
- [ ] He calculado y registrado hashes.
- [ ] He asignado un estado de preservación coherente con la evidencia disponible.
- [ ] No he marcado como «verificada» una adquisición parcial o con errores sin resolver.

### G. Conservación

- [ ] El master está separado de las copias de trabajo.
- [ ] El master no se modifica para realizar pruebas.
- [ ] Existe al menos una estrategia de copia de seguridad conforme al estándar vigente.

### H. Ejecución actual, si se aborda

- [ ] He creado/utilizado una copia de trabajo derivada del master.
- [ ] He identificado exactamente el entorno probado.
- [ ] He registrado herramientas, parches, wrappers o configuraciones utilizadas.
- [ ] He documentado los pasos de forma reproducible.
- [ ] He verificado los subsistemas relevantes.
- [ ] He registrado limitaciones y elementos no probados.
- [ ] He anotado la fecha de la última prueba.

### I. Publicación

- [ ] La ficha enlaza correctamente con la documentación disponible.
- [ ] La documentación enlaza de vuelta a la pieza.
- [ ] No se publica contenido del software preservado cuando no corresponda.
- [ ] La información pública diferencia claramente preservación y ejecución.

---

## 13. Definition of Done de una pieza preservada

Una pieza **no** se considerará preservada únicamente porque exista un fichero de imagen.

Para poder marcarla como preservada debe existir, como mínimo:

1. identificación inequívoca de la pieza/edición;
2. caracterización suficiente del soporte;
3. selección justificada del método de adquisición;
4. adquisición completada y registrada;
5. logs/incidencias conservados cuando proceda;
6. hashes registrados;
7. verificación conforme al procedimiento aplicable;
8. master separado de las copias de trabajo;
9. registro documental asociado a la pieza.

Para marcarla además como **compatibilidad verificada**, debe existir una guía reproducible basada en una copia de trabajo y una prueba real documentada.

---

## 14. Caso piloto de F17

F17 no se cerrará únicamente con la infraestructura documental implementada.

Debe validarse mediante al menos una pieza real de extremo a extremo:

```text
PIEZA FÍSICA
     ↓
CARACTERIZACIÓN
     ↓
SELECCIÓN DEL PROCEDIMIENTO
     ↓
ADQUISICIÓN
     ↓
VERIFICACIÓN
     ↓
MASTER DE PRESERVACIÓN
     ↓
COPIA DE TRABAJO
     ↓
INSTALACIÓN / COMPATIBILIDAD
     ↓
GUÍA REPRODUCIBLE
     ↓
PUBLICACIÓN Y ENLACE DESDE LA FICHA
```

El piloto debe utilizarse para detectar defectos del modelo antes de extenderlo al resto de la colección.

`Star Wars Jedi Knight: Dark Forces II` es un candidato inicial por reunir características suficientemente ricas para poner a prueba el modelo, pero la elección definitiva deberá realizarse al iniciar el piloto sobre la pieza física disponible.

---

## 15. Descomposición propuesta de F17

- **F17.1 — Arquitectura documental y modelo de generación.**
- **F17.2 — Estándar y procedimientos de preservación.**
- **F17.3 — Estándar y plantilla de guías de ejecución.**
- **F17.4 — Integración bidireccional con las fichas.**
- **F17.5 — Pieza piloto completa.**
- **F17.6 — Validación, correcciones y cierre de F17.**

La numeración podrá ajustarse si durante el diseño aparecen dependencias que aconsejen otra división, pero no debe perderse ninguna de las responsabilidades anteriores.

---

## 15.1. Estado de las entregas

### F17.1 — Arquitectura documental y modelo de generación — COMPLETADA

F17.1 establece:

- `/documentacion/` como hub público;
- `documentacion.json` como índice único de metadatos documentales;
- categorías documentales controladas;
- URLs canónicas, breadcrumbs, SEO, datos estructurados y sitemap;
- validación de relaciones documento → pieza contra `juegos.json`;
- principio de fuente única: la relación se declara en `documentacion.json` y la relación inversa se genera automáticamente desde F17.4;
- ausencia deliberada de contenidos ficticios: los documentos se incorporan únicamente cuando existe contenido real y validado; F17.2 y F17.3 ya han publicado los primeros estándares.

El cuerpo documental se autorará en Markdown mediante el subconjunto controlado implementado en F17.2; `documentacion.json` permanece como índice de metadatos y relaciones.

### F17.2 — Estándar y procedimientos de preservación — COMPLETADA

F17.2 establece y publica:

- el estándar general de preservación digital de PC Game Archive;
- el procedimiento de caracterización previa de soportes ópticos;
- SHA-256 como hash mínimo propio de integridad;
- separación estricta entre máster y copia de trabajo;
- verificación posterior a la adquisición y segunda lectura cuando proceda;
- estados conceptuales de preservación;
- `PLANTILLA_REGISTRO_PRESERVACION.md` como checklist operativa por pieza;
- fuentes Markdown versionadas y publicación automática de documentos individuales.

F17.2 no crea por anticipación procedimientos de adquisición específicos. Cuando una pieza real requiera un caso nuevo, el procedimiento se documentará y validará antes de reutilizarlo.

### F17.3 — Estándar y plantilla de guías de ejecución — COMPLETADA

F17.3 establece y publica:

- el estándar de guías de ejecución y compatibilidad de PC Game Archive;
- separación formal entre máster de preservación y copia/derivado de trabajo;
- identificación obligatoria de la edición física probada;
- registro del sistema anfitrión, build, arquitectura y hardware relevante;
- trazabilidad de herramientas, actualizaciones, wrappers y configuraciones;
- obligación de distinguir evidencia propia de referencias externas;
- matriz de validación funcional por subsistemas;
- estados conceptuales de compatibilidad;
- repetición del procedimiento antes de declarar una guía verificada;
- `PLANTILLA_GUIA_EJECUCION.md` como hoja de trabajo obligatoria por guía.

Una guía no se considera verificada porque el juego alcance el menú principal. Debe documentar qué subsistemas se han probado, cuáles funcionan con limitaciones y cuáles no se han probado.


### F17.4 — Integración bidireccional con las fichas — COMPLETADA

F17.4 establece:

- `documentacion.json` permanece como única fuente de verdad para la relación documento → pieza;
- `juegos.json` no incorpora campos duplicados de documentación;
- el generador construye automáticamente un índice inverso pieza → documentos;
- una ficha con documentación asociada muestra un bloque **Preservación y compatibilidad** reutilizando los componentes visuales existentes;
- el bloque solo se genera cuando existe al menos un documento real relacionado;
- los documentos muestran **Piezas relacionadas** utilizando título y número de ficha en lugar de exponer únicamente la URL técnica;
- una misma pieza puede relacionarse con varios documentos y un documento con varias piezas;
- las relaciones inexistentes o duplicadas se rechazan durante la generación;
- F17.4 no publica relaciones ficticias: la asociación real se estrenará en F17.5 con la pieza piloto.

La bidireccionalidad no implica duplicación de datos. La relación se declara una sola vez en `documentacion.json` y todas las vistas derivadas se generan automáticamente.

## 16. Regla de trabajo para futuras sesiones

Antes de abordar la preservación o compatibilidad de una nueva pieza, se debe consultar este documento y utilizar su checklist.

Si un caso real demuestra que el estándar es insuficiente:

1. no se improvisará una excepción silenciosa;
2. se documentará el nuevo caso;
3. se actualizará el estándar/procedimiento correspondiente;
4. se dejará trazabilidad del cambio;
5. solo después se continuará aplicando el nuevo criterio a otras piezas.

Este documento es parte de la documentación viva de PC Game Archive y debe evolucionar con la experiencia real obtenida durante la preservación de la colección.
