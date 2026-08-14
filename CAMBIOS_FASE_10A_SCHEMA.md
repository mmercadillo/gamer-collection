# PC Game Archive — Fase 10A: evolución del schema

Esta fase amplía el modelo de datos sin modificar `juegos.json`.

## Nuevos campos obligatorios

Todos se añaden al final de la ficha y admiten un valor vacío válido:

- `anio`: `""` o año de cuatro dígitos como string.
- `mercado`: `[]` o lista de mercados/territorios permitidos.
- `idioma`: `[]` o lista de idiomas permitidos.
- `soporte`: `[]` o lista de soportes permitidos.
- `tipo_edicion`: `[]` o lista de clasificaciones de edición permitidas.

Los valores permitidos se encuentran en `json_schema.json`.

## Migración

`migrar_campos_fase10.py` añade únicamente los campos que falten con estos valores:

```json
"anio": "",
"mercado": [],
"idioma": [],
"soporte": [],
"tipo_edicion": []
```

No sobrescribe datos existentes.

Prueba sin modificar:

```bash
python migrar_campos_fase10.py --dry-run
```

Migración real:

```bash
python migrar_campos_fase10.py
```

Antes de escribir crea un backup `juegos.json.bak_fase10_YYYYMMDD_HHMMSS` y usa escritura atómica.

## Validación realizada

- Schema Draft 2020-12 válido.
- Catálogo original: 783 errores formales preexistentes contra el schema anterior.
- Copia migrada: 783 errores formales contra el nuevo schema.
- Los conjuntos de errores son idénticos: los nuevos campos vacíos no introducen regresiones.
- `generar_web.py` genera correctamente las 1.552 fichas usando una copia migrada.
- El `juegos.json` incluido en este ZIP NO ha sido migrado.
