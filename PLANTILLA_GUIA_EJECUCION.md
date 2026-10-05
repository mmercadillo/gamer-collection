# PC Game Archive — Plantilla de guía de ejecución y compatibilidad

> Plantilla operativa obligatoria para documentar una guía de ejecución antes de publicarla. No eliminar apartados: marcar como `No aplicable` o `No probado` cuando corresponda.

## 1. Identificación

- **Título:**
- **Edición exacta:**
- **Mercado/idioma:**
- **URL de la pieza en PC Game Archive:**
- **Soporte(s):**
- **Registro de preservación relacionado:**
- **Fecha de inicio de pruebas:**
- **Fecha de última prueba completa:**
- **Responsable de la prueba:**

## 2. Punto de partida

- **Origen de la copia de trabajo:**
- **Derivada de máster verificado:** Sí / No
- **Identificador/hash de referencia del máster o derivado:**
- **Observaciones:**

## 3. Entorno anfitrión

- **Sistema operativo:**
- **Versión/build:**
- **Arquitectura:**
- **CPU:**
- **GPU:**
- **RAM:**
- **Resolución/escala:**
- **Audio relevante:**
- **Periféricos relevantes:**
- **VM/emulador/capa de compatibilidad y versión:**

## 4. Herramientas, actualizaciones y componentes adicionales

Para cada elemento:

- **Nombre:**
- **Versión:**
- **Procedencia/URL:**
- **Finalidad:**
- **Hash o referencia de integridad, si procede:**

## 5. Instalación base

### 5.1. Preparación de la copia de trabajo

1.
2.
3.

### 5.2. Instalación

1.
2.
3.

### 5.3. Resultado sin ajustes adicionales

- **Resultado:**
- **Errores observados:**
- **Logs/capturas/evidencia interna:**

## 6. Ajustes de compatibilidad

Documentar cada intervención por separado.

### Ajuste 1

- **Problema que resuelve:**
- **Herramienta/parche/configuración:**
- **Versión:**
- **Procedencia:**
- **Pasos exactos:**
  1.
  2.
  3.
- **Resultado:**

### Ajuste 2

- **Problema que resuelve:**
- **Herramienta/parche/configuración:**
- **Versión:**
- **Procedencia:**
- **Pasos exactos:**
  1.
  2.
  3.
- **Resultado:**

## 7. Procedimiento final reproducible

Esta sección debe contener únicamente la secuencia final validada, sin mezclar intentos fallidos.

1.
2.
3.
4.
5.

## 8. Matriz de validación funcional

Usar uno de estos valores: `Correcto`, `Correcto con limitaciones`, `No funcional`, `No probado`, `No aplicable`.

| Subsistema | Estado | Observaciones |
|---|---|---|
| Instalación | | |
| Arranque | | |
| Menús | | |
| Vídeos/cinemáticas | | |
| Gráficos 2D | | |
| Gráficos 3D | | |
| Sonido | | |
| Música | | |
| Teclado/ratón | | |
| Gamepad/joystick | | |
| Inicio de partida | | |
| Juego representativo | | |
| Guardado | | |
| Carga | | |
| Cambio de nivel/escena | | |
| Multijugador | | |
| Cierre | | |

## 9. Limitaciones conocidas

-

## 10. Elementos no probados

-

## 11. Problemas descartados / intentos fallidos

Registrar para trazabilidad interna aquello que se probó y se descartó.

-

## 12. Fuentes externas utilizadas

Distinguir siempre referencia externa de evidencia propia.

-

## 13. Evidencias internas

- logs;
- capturas;
- ficheros de configuración;
- hashes;
- notas de prueba;
- cualquier otra evidencia necesaria para repetir el procedimiento.

## 14. Repetición final

- [ ] Partida desde copia de trabajo conocida.
- [ ] Entorno identificado.
- [ ] Procedimiento ejecutado desde estado suficientemente limpio.
- [ ] No han sido necesarios pasos fuera de la guía.
- [ ] Resultado coincide con la matriz funcional.
- [ ] Limitaciones reproducidas/documentadas.
- [ ] Fecha de última prueba actualizada.

## 15. Estado final

- **Estado:** No probada / Funcional / Funcional con ajustes / Parcial / No funcional
- **Fecha de última prueba:**
- **Observaciones finales:**

## 16. Definition of Done

- [ ] Edición exacta identificada.
- [ ] Punto de partida documentado.
- [ ] Entorno completo registrado.
- [ ] Herramientas y versiones registradas.
- [ ] Pasos finales reproducibles.
- [ ] Matriz funcional completada.
- [ ] Limitaciones visibles.
- [ ] Elementos no probados visibles.
- [ ] Procedimiento repetido.
- [ ] Fuentes externas diferenciadas de pruebas propias.
- [ ] Relación con la pieza documentada.
