# Fase 10C — Inferencia conservadora de metadatos

Esta fase incorpora `inferir_campos_fase10c.py` para intentar completar los campos
`anio`, `mercado`, `idioma`, `soporte` y `tipo_edicion` exclusivamente a partir de
información ya existente en cada ficha de `juegos.json`.

## Principios

- No consulta Internet ni usa fuentes externas.
- No sobrescribe campos que ya tengan datos.
- Si la evidencia es ambigua, deja el campo vacío.
- Los valores admitidos se leen dinámicamente de `json_schema.json`.
- Cada candidato se valida contra la definición exacta de su campo antes de aplicarse.
- Tras inferir, se valida el catálogo completo y se comparan los errores antes/después.
- Si aparece un solo error JSON Schema nuevo, el script aborta sin modificar `juegos.json`.
- En modo normal crea un backup antes de escribir.
- Genera informes JSON y CSV con el valor inferido y la evidencia textual utilizada.

## Uso recomendado

Primero revisar sin modificar nada:

```bash
python inferir_campos_fase10c.py --dry-run
```

Después puede generarse una copia separada para comparar:

```bash
python inferir_campos_fase10c.py --output juegos_inferidos.json
```

Solo tras revisar el resultado, aplicar sobre `juegos.json`:

```bash
python inferir_campos_fase10c.py
```

El último comando crea previamente un fichero `juegos.json.bak_fase10c_<fecha>`.

## Reglas de inferencia

### Año

Solo se acepta cuando el texto vincula de forma explícita el año con la edición
catalogada o con su publicación/distribución local. No se utiliza automáticamente
`publicado originalmente en ...`, porque suele ser el año del juego y no necesariamente
el de esa edición física.

### Mercado

Se utilizan expresiones explícitas como `edición española`, `edición europea`,
`distribuida en España`, etc. No se deduce el mercado por el país citado en el argumento,
por el origen del desarrollador ni solo por el nombre del distribuidor.

### Idioma

Se requieren expresiones lingüísticas documentales como `manual en castellano`,
`software en inglés`, `voces en inglés`, `textos en castellano`, `versión en catalán`
o `documentación multilingüe`. Expresiones como `juego francés` o `rol japonés` no se
consideran idioma de la edición.

### Soporte

Se prioriza el inventario `incluye`. Se detectan CD-ROM, DVD-ROM, disquetes de 3,5 y
5,25 pulgadas y, solo cuando están explícitamente incluidos, CD de audio, DVD de vídeo,
USB, etc. Si `incluye` está vacío, únicamente se admiten tags inequívocos de soporte.
No se infiere el soporte a partir del formato de caja.

### Tipo de edición

Solo se reconocen expresiones explícitas como `Edición Coleccionista`, `Edición especial`,
`recopilación que incluye...`, `Anthology`, `reedición económica`, `Budget`, etc.
Las frases dubitativas (`posiblemente`, `potencialmente`, `probablemente`...) se ignoran.

## Resultado del dry-run sobre 1.552 fichas

- `anio`: 13 fichas
- `mercado`: 267 fichas
- `idioma`: 176 fichas
- `soporte`: 262 fichas
- `tipo_edicion`: 106 fichas

Valores inferidos observados, todos permitidos por `json_schema.json`:

- Mercado: España, Europa, Italia, Países Bajos, Portugal.
- Idioma: Español, Inglés, Italiano, Portugués, Neerlandés, Catalán, Multilingüe.
- Soporte: CD-ROM, DVD-ROM, Disquete 3,5", Disquete 5,25", CD de audio, DVD de vídeo, USB.
- Tipo de edición: Compilación, Edición especial, Edición coleccionista, Edición limitada,
  Reedición, Budget, Bundle/Pack y Colección.

## Regresión

La validación completa con `validar_catalogo.py` antes y después de aplicar las
inferencias a una copia temporal produce exactamente el mismo resumen:

- 817 errores preexistentes
- 1.592 avisos preexistentes
- 2 mensajes informativos

El validador JSON Schema directo mantiene 783 errores formales preexistentes antes y
después. No aparece ningún error nuevo por los campos inferidos.

También se ha ejecutado `generar_web.py` sobre una copia temporal del catálogo inferido
sin errores de generación.
