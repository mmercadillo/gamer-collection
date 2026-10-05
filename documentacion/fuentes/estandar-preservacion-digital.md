## Propósito

Este estándar define cómo debe abordar PC Game Archive la preservación digital de una pieza física. Su finalidad es obtener una representación verificable del soporte original y conservar evidencia suficiente para comprender, repetir y auditar el proceso en el futuro.

> La preservación no comienza eligiendo un formato de imagen. Comienza caracterizando la pieza y el soporte físico concreto.

## Principios obligatorios

- **La metodología es común; la evidencia es específica de cada pieza.** Dos ediciones del mismo juego pueden requerir tratamientos distintos.
- **Preservación y ejecución son procesos diferentes.** El máster se crea para conservar el soporte; la copia de trabajo se utiliza para instalar, probar o adaptar el juego.
- **El máster de preservación no se modifica.** Parches, wrappers, conversiones o pruebas se realizan sobre derivados.
- **No se presupone que una ISO sea suficiente.** El resultado de la adquisición puede necesitar varios ficheros, descriptores, subcanales, datos de posición, logs u otra información auxiliar.
- **Las protecciones y características especiales forman parte de la caracterización técnica.** Deben documentarse porque pueden condicionar la lectura, la verificación y la futura reproducción.
- **Toda decisión debe ser justificable.** Debe quedar registrado por qué se eligieron un método, una herramienta y un formato concretos.

## Flujo normalizado

```text
PIEZA FÍSICA
    ↓
IDENTIFICACIÓN
    ↓
INSPECCIÓN Y CARACTERIZACIÓN
    ↓
SELECCIÓN DEL PROCEDIMIENTO
    ↓
ADQUISICIÓN DIGITAL
    ↓
VERIFICACIÓN
    ↓
MÁSTER DE PRESERVACIÓN
    ↓
ALMACENAMIENTO + COPIAS DE SEGURIDAD
    ↓
DERIVADO / COPIA DE TRABAJO
    ↓
INSTALACIÓN, PRUEBAS Y COMPATIBILIDAD
```

## 1. Identificación de la pieza

Antes de leer el soporte debe identificarse la edición concreta conservada. Se registrará, cuando esté disponible:

- título;
- edición y variante;
- mercado o país;
- idioma;
- editor y distribuidor;
- referencia comercial;
- identificador interno de la pieza;
- número total de soportes;
- identificación física relevante, incluida matriz o ring code cuando aporte valor documental;
- relación con la ficha pública de PC Game Archive.

No debe utilizarse información de otra edición como sustituto de la observación de la pieza real.

## 2. Inspección física

Antes de cualquier adquisición se documentará el estado del soporte:

- suciedad;
- arañazos;
- deformaciones;
- daños visibles;
- etiquetas o anotaciones;
- intervenciones previas conocidas.

Cualquier limpieza o intervención que pueda influir en la lectura debe registrarse.

## 3. Caracterización técnica

La caracterización determina qué información debe preservarse y qué método es adecuado. Según el soporte se comprobarán, como mínimo cuando proceda:

- tipo de medio;
- número y tipo de pistas;
- presencia de audio;
- número de sesiones;
- sistema de ficheros;
- capacidad y estructura;
- sectores problemáticos o anómalos;
- protección anticopia u otras características especiales;
- información auxiliar necesaria para representar fielmente el soporte.

En soportes ópticos debe seguirse además el procedimiento [Caracterización previa de soportes ópticos](../caracterizacion-soportes-opticos/) publicado por PC Game Archive.

## 4. Selección del procedimiento

El método de adquisición se decide **después** de la caracterización.

No existe una regla del tipo «CD-ROM = ISO». Un CD de datos sencillo, un CD mixto con audio, un disco multisesión o un soporte cuya protección dependa de información adicional pueden necesitar procedimientos distintos.

Si la pieza presenta un caso todavía no cubierto por un procedimiento validado de PC Game Archive:

1. se detiene la adquisición definitiva;
2. se documenta el caso observado;
3. se estudia y valida un procedimiento específico;
4. se incorpora dicho procedimiento al estándar;
5. solo entonces se completa la preservación de la pieza.

## 5. Adquisición digital

La adquisición debe realizarse con herramientas y hardware identificados y reproducibles. El registro debe incluir:

- unidad lectora y, cuando sea relevante, firmware;
- sistema operativo;
- herramienta utilizada;
- versión exacta;
- parámetros o perfil de adquisición;
- fecha;
- resultado;
- ficheros generados;
- logs producidos por la herramienta;
- incidencias observadas.

Siempre que el soporte y el procedimiento lo permitan, PC Game Archive buscará una segunda lectura independiente y comparará los resultados para reforzar la verificación.

## 6. Verificación

Una adquisición no se considera preservada únicamente porque el software haya terminado sin error.

La verificación debe incluir, según proceda:

- revisión del log de lectura;
- comprobación de sectores con errores o comportamiento anómalo;
- comparación entre adquisiciones independientes cuando sea posible;
- comprobación de la estructura esperada;
- hashes de los ficheros resultantes;
- contraste con referencias externas fiables cuando existan, sin sustituir la evidencia de la pieza propia.

### Hash de referencia

PC Game Archive utilizará **SHA-256** como hash mínimo de integridad para sus ficheros de preservación. Podrán conservarse hashes adicionales cuando una herramienta, una base de referencia o un procedimiento concreto los requiera.

## 7. Máster de preservación

El conjunto resultante puede contener más de un fichero. El concepto de máster comprende todos los elementos necesarios para conservar y verificar la adquisición:

```text
master/
├── datos de la adquisición
├── descriptores necesarios
├── información auxiliar necesaria
├── logs/
├── hashes.sha256
└── metadatos de preservación
```

El máster:

- no se modifica;
- no se parchea;
- no se convierte para facilitar la ejecución;
- no se utiliza como espacio de pruebas;
- debe poder verificarse posteriormente mediante sus hashes.

## 8. Copia o derivado de trabajo

Cuando sea necesario instalar, montar, convertir, parchear o modificar contenidos, se crea una copia de trabajo derivada del máster.

Debe mantenerse la trazabilidad:

```text
PIEZA → MÁSTER → DERIVADO DE TRABAJO → GUÍA DE EJECUCIÓN
```

Una guía de compatibilidad debe indicar de qué máster o registro de preservación procede su copia de trabajo.

## 9. Almacenamiento y copias de seguridad

El estándar de PC Game Archive exige separar conceptualmente:

- el soporte físico original;
- el máster digital;
- las copias de seguridad del máster;
- las copias de trabajo.

La existencia de una única copia digital no constituye preservación suficiente. Los detalles de infraestructura, número de réplicas, ubicaciones y periodicidad de controles se documentarán como política operativa independiente para poder evolucionarlos sin cambiar este procedimiento.

## 10. Metadatos mínimos del registro de preservación

Cada pieza preservada deberá disponer, como mínimo, de evidencia sobre:

- identificación de la pieza;
- soporte tratado;
- estado físico observado;
- caracterización técnica;
- protección o características especiales detectadas, si existen;
- procedimiento seleccionado y justificación;
- hardware y software utilizados;
- fecha de adquisición;
- resultado de la lectura;
- incidencias;
- ficheros que componen el máster;
- hashes SHA-256;
- método de verificación;
- fecha y resultado de la verificación;
- existencia de copia de trabajo, si procede.

## 11. Estados de preservación

El modelo debe poder representar al menos estos estados conceptuales:

- `no_realizada`: todavía no se ha efectuado la adquisición;
- `realizada`: existe una adquisición documentada pendiente de completar su verificación;
- `verificada`: la adquisición cumple el estándar y sus controles definidos;
- `parcial`: solo ha podido preservarse parte del soporte o existe una limitación conocida;
- `no_legible`: no ha sido posible obtener una adquisición suficiente con el procedimiento empleado.

Un estado distinto de `verificada` debe conservar la explicación de la limitación o incidencia.

## 12. Definition of Done de una pieza preservada

Una pieza solo puede declararse **preservada y verificada** cuando se cumplen todos estos puntos:

- [ ] La edición concreta está identificada.
- [ ] El estado físico previo está registrado.
- [ ] El soporte ha sido caracterizado antes de elegir el método.
- [ ] Se han identificado o evaluado protecciones y características especiales relevantes.
- [ ] El procedimiento elegido está documentado y justificado.
- [ ] Hardware, software y versiones están registrados.
- [ ] La adquisición ha finalizado y se conservan sus logs.
- [ ] Se han revisado errores, anomalías e incidencias.
- [ ] Se han calculado hashes SHA-256 del conjunto de preservación.
- [ ] Se ha ejecutado el método de verificación definido para ese procedimiento.
- [ ] El máster está separado de cualquier copia de trabajo.
- [ ] Existe un registro de preservación asociado a la pieza.

Si cualquiera de estos puntos no puede cumplirse, el registro debe reflejarlo y no presentará la pieza como `verificada`.

## 13. Qué no publica necesariamente PC Game Archive

Documentar una adquisición no implica distribuir públicamente su contenido. PC Game Archive puede publicar metodología, metadatos, hashes, logs seleccionados, incidencias y evidencia de preservación sin ofrecer descargas de software protegido.

## Referencias técnicas de apoyo

El estándar propio se apoya, entre otras referencias, en prácticas y documentación técnica de preservación digital y adquisición de soportes ópticos:

- [Library of Congress — ISO Disk Image File Format](https://www.loc.gov/preservation/digital/formats/fdd/fdd000348.shtml)
- [Digital Preservation Coalition — Getting Started](https://www.dpconline.org/component/content/article/getting-started)
- [Redump — Disc Dumping Guide](https://wiki.redump.info/Disc_Dumping_Guide_%28MPF%29)
- [Redump — MDF/MDS Dumping Guide](https://wiki.redump.info/MDF/MDS_Dumping_Guide)

Estas referencias no sustituyen el procedimiento de PC Game Archive: sirven para fundamentar y contrastar decisiones técnicas concretas.
