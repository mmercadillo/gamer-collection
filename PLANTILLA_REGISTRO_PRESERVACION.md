# PC Game Archive — Plantilla de registro de preservación de una pieza

Esta plantilla debe utilizarse como checklist operativa al abordar una nueva pieza. No sustituye el estándar público de preservación ni el procedimiento específico que corresponda al soporte.

## Finalidad permanente de la preservación en PC Game Archive

**El objetivo prioritario, para esta y todas las futuras preservaciones, es conservar el videojuego como software utilizable y verificablemente funcional a largo plazo, no reproducir por sí mismo todas las particularidades físicas de su soporte original.** Se pretende preservar la edición concreta, sus datos necesarios, instalación, ejecución y experiencia de juego.

- Una imagen que pueda montarse **no basta** para considerar la preservación funcional completada: deben probarse instalación y ejecución y documentarse las funcionalidades relevantes conforme a `PLANTILLA_GUIA_EJECUCION.md`.
- La representación fiel del soporte físico aporta valor y se procurará cuando sea viable, **pero no es un fin excluyente** si una característica física o protección impide una copia convencional y existe un derivado funcional verificable.
- Los sectores no legibles, sustituidos, omitidos o reconstruidos **no se ocultarán**. Se registrarán por separado, con método, alcance, procedencia y limitaciones. Una imagen con datos sustituidos no puede describirse como copia física íntegra o volcado bit a bit verificado.
- Se distinguirá expresamente entre **integridad del fichero digital** (SHA-256 y copias), **fidelidad al soporte original** (adquisición y errores documentados) y **funcionalidad del videojuego** (pruebas reales). Ninguna prueba demuestra automáticamente las otras dos.
- Se conservará inmutable una **copia de referencia de los archivos obtenidos**, y se utilizarán copias de trabajo independientes para instalaciones, reparaciones, parches y compatibilidad. Si la copia de referencia es un derivado funcional, deberá identificarse claramente como tal, sin atribuirle fidelidad física no demostrada.
- No repetir indefinidamente lecturas fallidas ni exigir fotografías o comprobaciones que no aporten a una decisión técnica. Si aparecen anomalías, evaluar un procedimiento específico, documentarlo y avanzar a la validación funcional cuando exista una imagen candidata.

**Compatibilidad con el estándar:** este enfoque expresa el objetivo del proyecto y el criterio de valoración funcional. Si la versión vigente del estándar exige una adquisición físicamente íntegra para calificar un «máster verificado», no cambiar esa calificación por la vía de esta plantilla: conservar el estado técnico real y tramitar una actualización versionada del estándar antes de adoptar nuevas categorías de cierre.


Antes de iniciar el trabajo debe registrarse la **versión vigente del Estándar de preservación digital de PC Game Archive**. El registro conservará esa versión aunque el estándar evolucione posteriormente.

- Versión del estándar aplicada:
- Fecha de inicio del registro:

## 1. Identificación

- Título:
- Edición / variante:
- URL de la ficha PCGA:
- Mercado / país:
- Idioma:
- Editor / distribuidor:
- Referencia comercial:
- Identificador interno:
- Soporte nº / total:
- Matriz / ring code / identificación física relevante:

## 2. Estado físico previo

- Estado general:
- Suciedad:
- Arañazos:
- Daños visibles:
- Etiquetas / anotaciones:
- Intervenciones previas conocidas:
- Limpieza o intervención realizada antes de la lectura:

## 3. Caracterización técnica

- Tipo de soporte:
- Sesiones:
- Pistas:
- Audio:
- Sistema(s) de ficheros:
- Capacidad / estructura relevante:
- Sectores problemáticos o anomalías:
- Protección / característica especial:
- Estado de la identificación: confirmado / probable / no detectado / no evaluado
- Evidencias conservadas:
- Impacto conocido o hipotético sobre la instalación/ejecución (separar evidencia e hipótesis):

## 4. Decisión de adquisición

- Procedimiento seleccionado:
- Justificación:
- Hardware / unidad lectora:
- Firmware, si es relevante:
- Sistema operativo:
- Herramienta:
- Versión:
- Perfil / parámetros:
- Finalidad de la adquisición: fidelidad física / recuperación funcional / diagnóstico (indicar cuál):
- Tratamiento previsto de zonas ilegibles o protecciones y justificación:

## 5. Adquisición

- Fecha:
- Intento / lectura nº:
- Resultado:
- Ficheros generados:
- Logs:
- Errores / incidencias:
- Sectores omitidos, sustituidos o reconstruidos (rango, cantidad, valor de relleno y evidencia, si aplica):
- Segunda adquisición realizada: sí / no
- Resultado de la comparación, si procede:

## 6. Verificación

- Método aplicado:
- Estructura revisada:
- Logs revisados:
- Referencia externa contrastada, si existe:
- Resultado:
- Fecha de verificación:
- Verificación de fidelidad física (resultado y límites):
- Verificación funcional (enlace al registro de compatibilidad / estado):

## 7. Hashes

Registrar SHA-256 de todos los ficheros que formen parte del máster o copia digital de referencia, y de sus derivados relevantes. Un hash prueba identidad/integridad posterior del fichero, **no** que se recuperaron todos los sectores ni que el juego funciona.

```text
SHA256  fichero
```

## 8. Máster / copia digital de referencia

- Tipo: adquisición fiel del soporte / imagen de recuperación funcional / otro (explicar):
- Estado técnico de adquisición según el estándar vigente: no_realizada / realizada / verificada / parcial / no_legible
- Estado de funcionalidad: no_probada / en_pruebas / funcional_verificada / funcional_con_limitaciones / no_funcional
- Ubicación lógica:
- Elementos que componen la copia de referencia:
- Fuente y cadena de derivación:
- Sectores ilegibles / datos sustituidos o reconstruidos, con detalle:
- Limitaciones conocidas:
- Inmutabilidad de la referencia y fecha de fijación:
- Copias de seguridad verificadas:

**Nota:** `funcional_verificada` requiere evidencia de pruebas de juego, no solo una imagen generada o montable. No equivale automáticamente a `verificada` como adquisición fiel del soporte.

## 9. Copia de trabajo

- Creada: sí / no
- Derivada de:
- Transformaciones realizadas para crearla:
- Uso previsto:
- SHA-256 de la copia de trabajo y comprobación contra la referencia, cuando sea idéntica:
- Diferencias autorizadas respecto a la referencia:

## 9 bis. Validación funcional del videojuego

- Registro y guía de ejecución relacionados:
- Entorno de laboratorio y fecha:
- Instalación desde las imágenes: correcto / con limitaciones / no funcional / no probado
- Arranque y acceso al juego: correcto / con limitaciones / no funcional / no probado
- Juego representativo: correcto / con limitaciones / no funcional / no probado
- Vídeos, gráficos, música y sonido (detallar):
- Guardado y carga (resultado):
- Cambios de disco y dependencia del disco original (si aplica):
- Otras funciones relevantes y no probadas:
- Repetición del procedimiento desde estado conocido:
- Evidencias (capturas, logs y registro de compatibilidad):
- Conclusión funcional y limitaciones:

En ediciones multi-CD, **no declarar la edición funcionalmente preservada** hasta disponer de todos los discos necesarios y completar las pruebas pertinentes. Utilizar la matriz detallada de `PLANTILLA_GUIA_EJECUCION.md`; esta sección solo recoge el resumen y su enlace.

## 10. Cierre / Definition of Done

- [ ] Versión del estándar aplicada registrada.
- [ ] Edición identificada.
- [ ] Estado físico registrado.
- [ ] Caracterización completada antes de elegir el método.
- [ ] Protecciones/características especiales evaluadas.
- [ ] Procedimiento elegido y justificado.
- [ ] Hardware/software/versiones registrados.
- [ ] Logs conservados.
- [ ] Errores e incidencias revisados.
- [ ] SHA-256 calculados.
- [ ] Verificación realizada.
- [ ] Máster separado de la copia de trabajo.
- [ ] Tipo de copia de referencia y fidelidad física declarados sin ambigüedad.
- [ ] Sectores ausentes/sustituidos/reconstruidos documentados, si existen.
- [ ] Todos los soportes necesarios de la edición contemplados.
- [ ] Pruebas de instalación y ejecución efectuadas y registradas, o marcadas explícitamente como pendientes.
- [ ] Matriz funcional y limitaciones vinculadas con la guía de ejecución.
- [ ] Estado técnico de adquisición y estado funcional asignados por separado, coherentes con la evidencia.
- [ ] No se declara «preservación funcional completada» sin pruebas reproducibles suficientes.
- [ ] Estado final asignado de forma coherente con la evidencia.

## 11. Observaciones

- 
