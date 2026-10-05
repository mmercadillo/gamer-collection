## Objetivo

Este procedimiento desarrolla el [Estándar de preservación digital de PC Game Archive](../estandar-preservacion-digital/) y define qué debe comprobarse **antes de adquirir digitalmente un CD-ROM o DVD-ROM**. Su función no es decidir de antemano el formato de salida, sino reunir la evidencia necesaria para elegir después el procedimiento de adquisición adecuado.

> Un soporte óptico no se clasifica únicamente por lo que pone en la caja. La estructura real del disco es la que determina cómo debe preservarse.

## 1. Identificación del soporte

Registrar:

- pieza y edición a la que pertenece;
- número de disco dentro de la edición;
- tipo indicado físicamente, si consta;
- etiqueta y referencias impresas;
- matriz o ring code cuando pueda leerse sin manipulación destructiva;
- estado físico general.

Cada disco de una edición multidisco debe caracterizarse por separado.

## 2. Inspección física previa

Comprobar y documentar:

- suciedad;
- arañazos;
- grietas;
- delaminación u otros daños visibles;
- deformación;
- etiquetas añadidas;
- anotaciones;
- signos de una intervención previa.

Si se realiza una limpieza, debe anotarse qué se hizo y antes de qué lectura.

## 3. Estructura del disco

Antes de elegir el método de adquisición se debe determinar, cuando sea técnicamente posible:

- número de sesiones;
- número de pistas;
- tipo de cada pista;
- presencia de audio CD;
- presencia de datos;
- sistema o sistemas de ficheros detectados;
- capacidad utilizada;
- estructura multisesión;
- comportamiento de lectura anómalo.

Ejemplos de resultados de caracterización diferentes:

```text
Caso A
1 sesión
1 pista de datos
sin audio
sin anomalías conocidas
```

```text
Caso B
1 sesión
1 pista de datos
varias pistas de audio CD
```

```text
Caso C
estructura de datos aparentemente convencional
+ protección o característica especial que requiere información adicional
```

Los tres casos pueden necesitar procedimientos de adquisición diferentes aunque físicamente todos sean «CD-ROM».

## 4. Protecciones y características especiales

Debe evaluarse si existen indicios de mecanismos que puedan afectar a la adquisición o a la futura representación funcional del soporte.

El registro debe distinguir entre:

- **confirmado**, cuando existe evidencia técnica suficiente;
- **probable**, cuando existen indicios pero falta confirmación;
- **no detectado**, cuando las comprobaciones realizadas no identifican una característica especial;
- **no evaluado**, cuando todavía no se ha realizado la comprobación necesaria.

No se utilizará «sin protección» como sinónimo de «no se ha encontrado nada todavía».

La protección observada en otra edición, reedición o mercado no se atribuirá automáticamente a la pieza conservada.

## 5. Evidencias que deben conservarse

La caracterización debería conservar, según las herramientas empleadas:

- informe de estructura de pistas y sesiones;
- identificación del sistema de ficheros;
- resultado de detección de protección;
- logs de herramientas de análisis;
- fotografías o notas físicas relevantes;
- cualquier dato que justifique la elección posterior del método.

## 6. Árbol de decisión inicial

El siguiente árbol es conceptual. No sustituye los procedimientos técnicos específicos que se irán validando con casos reales.

```text
SOPORTE ÓPTICO
      │
      ▼
¿CD o DVD?
      │
      ├── CD
      │    │
      │    ├── ¿solo datos?
      │    ├── ¿datos + audio?
      │    ├── ¿multisesión?
      │    ├── ¿errores/anomalías intencionadas?
      │    └── ¿protección o información auxiliar relevante?
      │
      └── DVD
           │
           ├── ¿estructura de datos convencional?
           ├── ¿multicapa u otra particularidad relevante?
           └── ¿protección o información auxiliar relevante?

                  ↓
        SELECCIONAR PROCEDIMIENTO
```

## 7. Criterio para abrir un procedimiento nuevo

PC Game Archive no creará procedimientos específicos por anticipación. Se abrirá uno nuevo cuando una pieza real demuestre que el caso no queda cubierto por un procedimiento ya validado.

Ejemplos de familias que podrán aparecer conforme el archivo las necesite:

- CD de datos;
- CD mixto datos + audio;
- CD multisesión;
- DVD-ROM;
- soportes con información de subcanal relevante;
- soportes cuya representación funcional necesite datos de posición u otra información auxiliar;
- discos con errores o estructuras deliberadamente anómalas.

## 8. Resultado de la caracterización

El proceso termina con una ficha técnica interna suficiente para responder a cuatro preguntas:

1. **¿Qué soporte concreto tenemos?**
2. **¿Qué características del original deben conservarse?**
3. **¿Qué procedimiento de adquisición corresponde?**
4. **¿Qué evidencias necesitaremos después para demostrar que la adquisición es válida?**

Si no pueden responderse con suficiente confianza, no debe declararse definido el método de preservación de la pieza.

## 9. Relación con la copia de trabajo

La caracterización puede anticipar dificultades futuras de ejecución, pero **no debe optimizarse la adquisición para jugar inmediatamente**.

El orden obligatorio es:

```text
caracterizar
   ↓
preservar con fidelidad suficiente
   ↓
verificar el máster
   ↓
crear derivado de trabajo
   ↓
resolver compatibilidad
```

Esto evita descartar información del soporte original solo porque no sea necesaria para una solución de compatibilidad actual.

## Referencias técnicas de apoyo

- [Library of Congress — ISO Disk Image File Format](https://www.loc.gov/preservation/digital/formats/fdd/fdd000348.shtml)
- [Redump — Disc Dumping Guide](https://wiki.redump.info/Disc_Dumping_Guide_%28MPF%29)
- [Redump — SecuROM](https://wiki.redump.info/SecuROM)
- [Redump — MDF/MDS Dumping Guide](https://wiki.redump.info/MDF/MDS_Dumping_Guide)

Estas referencias ilustran por qué diferentes estructuras y protecciones pueden requerir información distinta de una imagen ISO convencional.
