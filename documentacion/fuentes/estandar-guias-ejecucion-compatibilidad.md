## Propósito

Las guías de ejecución de PC Game Archive documentan cómo conseguir que una **edición física concreta conservada por el archivo** pueda instalarse y ejecutarse en un sistema actual de forma reproducible.

No son tutoriales genéricos sobre un título. Siempre que sea posible parten de una copia de trabajo derivada del máster de preservación de la pieza y dejan constancia del entorno exacto en el que el procedimiento ha sido validado.

> Preservar y ejecutar son procesos distintos. El máster de preservación no se modifica para conseguir compatibilidad.

## Principios obligatorios

### 1. La edición concreta es parte del resultado

Una guía debe identificar la edición probada. No se asumirá que otra edición, reedición, idioma o mercado se comporta igual.

Cuando una guía pueda aplicarse a más de una edición, esa equivalencia debe haberse comprobado o indicarse claramente como no verificada.

### 2. Partir de una copia de trabajo

Las pruebas de instalación, parches, wrappers, conversiones, configuraciones y demás cambios se realizarán sobre una copia o derivado de trabajo.

El máster de preservación debe permanecer inmutable y verificable.

### 3. Documentar el entorno completo

La guía debe registrar, como mínimo cuando sea relevante:

- sistema operativo y versión;
- arquitectura;
- hardware que pueda condicionar el resultado;
- resolución y configuración gráfica relevante;
- dispositivos de audio o entrada relevantes;
- herramientas auxiliares y sus versiones;
- parches, actualizaciones o wrappers utilizados y su procedencia.

No debe utilizarse únicamente la expresión «Windows 11» si una versión concreta del sistema puede influir en el resultado.

### 4. Pasos exactos y ordenados

Los pasos deben poder seguirse sin conocimiento implícito del autor.

Cada acción debe indicar qué se hace, sobre qué fichero o componente, con qué herramienta y qué resultado se espera antes de continuar.

No se omitirán reinicios, cambios de ruta, opciones de instalación, montaje de soportes, parámetros o configuraciones que hayan sido necesarios durante la validación.

### 5. Registrar solo soluciones realmente probadas

Una alternativa encontrada en Internet no se convierte en parte de una guía de PC Game Archive hasta haber sido probada sobre el entorno y la edición documentados.

Las fuentes externas pueden citarse como referencia, pero deben distinguirse de la evidencia obtenida por PC Game Archive.

### 6. No ocultar las limitaciones

Una guía no se considera fallida porque exista una limitación. Debe indicar con precisión qué funciona y qué no.

Ejemplos:

- vídeo correcto pero música ausente;
- campaña funcional pero multijugador no probado;
- aceleración 3D funcional con un wrapper concreto;
- instalación realizada mediante un instalador alternativo;
- determinada resolución no disponible;
- guardado y carga correctos, pero joystick no probado.

### 7. La compatibilidad tiene fecha

Toda guía debe indicar la fecha de la última prueba completa.

Una guía que funcionó en una versión anterior del sistema operativo no debe presentarse indefinidamente como verificada para versiones posteriores sin una nueva prueba.

## Flujo de trabajo

```text
PIEZA FÍSICA
     │
     ▼
MÁSTER DE PRESERVACIÓN VERIFICADO
     │
     ▼
COPIA / DERIVADO DE TRABAJO
     │
     ▼
ENTORNO DE PRUEBAS IDENTIFICADO
     │
     ▼
INSTALACIÓN BASE
     │
     ▼
DETECCIÓN DE INCIDENCIAS
     │
     ▼
AJUSTES / PARCHES / WRAPPERS / CONFIGURACIÓN
     │
     ▼
PRUEBA FUNCIONAL POR SUBSISTEMAS
     │
     ▼
REPETICIÓN DEL PROCEDIMIENTO
     │
     ▼
GUÍA PUBLICABLE
```

## Fase 1 — Identificación de la pieza y punto de partida

Antes de iniciar las pruebas se debe registrar:

- título;
- edición exacta;
- mercado/idioma cuando proceda;
- soporte utilizado;
- número de discos o medios necesarios;
- ficha correspondiente de PC Game Archive;
- origen de la copia de trabajo;
- referencia al registro de preservación cuando exista.

Si todavía no existe un máster de preservación, la guía debe declarar expresamente cuál ha sido el punto de partida y no debe presentar esa fuente como un máster verificado.

## Fase 2 — Entorno anfitrión

Registrar el entorno real de prueba.

Como mínimo:

- sistema operativo;
- versión/build cuando sea relevante;
- arquitectura de 32 o 64 bits;
- CPU/GPU cuando condicionen la compatibilidad;
- memoria cuando sea relevante;
- resolución y escala si afectan al resultado;
- periféricos relevantes.

Las máquinas virtuales, emuladores o capas de compatibilidad forman parte del entorno y deben identificarse con versión.

## Fase 3 — Instalación base

Primero se intentará documentar qué ocurre con la edición sin modificaciones adicionales, siempre que hacerlo sea razonable y seguro para el entorno de pruebas.

Debe registrarse:

- cómo se presenta o monta la copia de trabajo;
- cómo se inicia el instalador;
- ruta utilizada;
- opciones seleccionadas;
- errores o bloqueos encontrados;
- resultado de la instalación.

Esta fase sirve para distinguir el comportamiento original de las soluciones añadidas posteriormente.

## Fase 4 — Resolución de compatibilidad

Cada intervención debe documentarse de forma independiente y justificada.

Puede incluir, según el caso:

- actualizaciones oficiales;
- modos de compatibilidad del sistema;
- instaladores alternativos;
- wrappers gráficos o de sonido;
- emuladores o entornos como DOSBox o ScummVM cuando correspondan;
- máquinas virtuales;
- configuración de resolución, audio o entrada;
- parches comunitarios compatibles con la finalidad documental del archivo.

Para cada elemento se registrará:

- nombre;
- versión;
- procedencia;
- finalidad;
- paso exacto de aplicación;
- efecto observado.

PC Game Archive documentará procedimientos de preservación y compatibilidad. La documentación pública no tendrá como finalidad distribuir software protegido ni proporcionar instrucciones cuyo objetivo sea eludir controles de acceso o licencias.

## Fase 5 — Matriz de validación funcional

No basta con comprobar que aparece el menú principal. La guía debe registrar explícitamente el estado de los subsistemas relevantes.

Utilizar, adaptando cuando proceda, la siguiente matriz:

- [ ] Instalación
- [ ] Arranque
- [ ] Menús
- [ ] Vídeos/cinemáticas
- [ ] Gráficos 2D
- [ ] Gráficos 3D
- [ ] Sonido
- [ ] Música
- [ ] Teclado/ratón
- [ ] Gamepad/joystick
- [ ] Inicio de una partida
- [ ] Juego durante un periodo representativo
- [ ] Guardado
- [ ] Carga de partida
- [ ] Cambio de nivel/escena cuando proceda
- [ ] Multijugador, si procede
- [ ] Cierre correcto

Cada elemento debe quedar marcado como:

- **Correcto**;
- **Correcto con limitaciones**;
- **No funcional**;
- **No probado**;
- **No aplicable**.

Cuando una categoría tenga limitaciones, deben describirse.

## Fase 6 — Repetición

Antes de publicar una guía debe repetirse el procedimiento desde un estado suficientemente limpio para confirmar que no depende de cambios accidentales, ficheros residuales o conocimiento no documentado.

Siempre que sea viable se comprobará que:

1. la copia de trabajo de partida es la esperada;
2. el entorno está identificado;
3. los pasos publicados son suficientes;
4. el resultado final coincide con la matriz de validación.

Si la repetición obliga a realizar un paso no documentado, la guía todavía no está terminada.

## Estructura mínima de una guía pública

Una guía de ejecución debe contener al menos:

1. **Edición probada**.
2. **Estado de la guía y fecha de última prueba**.
3. **Entorno probado**.
4. **Punto de partida / copia de trabajo**.
5. **Requisitos y herramientas**.
6. **Procedimiento paso a paso**.
7. **Matriz de validación funcional**.
8. **Limitaciones conocidas**.
9. **Problemas y soluciones** cuando existan.
10. **Fuentes externas** utilizadas, diferenciadas de las pruebas propias.
11. **Relación con la pieza y con su preservación**.

## Estados de compatibilidad

PC Game Archive utilizará conceptualmente los siguientes estados:

### No probada

No se ha realizado una validación suficiente en un entorno actual.

### Funcional

Los elementos necesarios para una experiencia normal han sido validados sin limitaciones relevantes conocidas.

### Funcional con ajustes

La ejecución es satisfactoria, pero requiere pasos, herramientas o configuraciones adicionales que quedan documentados.

### Parcial

El juego puede ejecutarse, pero existen limitaciones relevantes que impiden considerar completa la experiencia documentada.

### No funcional

Tras las pruebas realizadas no se ha conseguido una ejecución utilizable en el entorno documentado.

El estado siempre debe interpretarse junto con la matriz funcional y la fecha de prueba.

## Criterio de actualización

Una guía debe revisarse cuando cambie cualquiera de estos elementos de forma relevante:

- sistema operativo anfitrión;
- herramienta principal de compatibilidad;
- parche o wrapper recomendado;
- procedimiento de instalación;
- evidencia obtenida sobre la edición;
- limitaciones conocidas.

Las revisiones deben actualizar la fecha del documento y la fecha de última prueba cuando se haya repetido la validación completa.

## Definition of Done de una guía

Una guía de PC Game Archive solo se considera **verificada** cuando:

- la edición concreta está identificada;
- el punto de partida está documentado;
- el entorno está descrito con precisión suficiente;
- todas las herramientas y versiones relevantes están registradas;
- los pasos pueden repetirse sin conocimiento implícito;
- existe una matriz funcional cumplimentada;
- las limitaciones y elementos no probados son visibles;
- el procedimiento ha sido repetido desde un estado suficientemente limpio;
- la fecha de última prueba está registrada;
- las fuentes externas están diferenciadas de las pruebas propias;
- la guía enlaza con la pieza correspondiente cuando esa integración esté disponible.

> El objetivo no es demostrar que un título «arranca», sino conservar conocimiento reproducible sobre cómo ejecutar hoy la edición física concreta que PC Game Archive conserva.
