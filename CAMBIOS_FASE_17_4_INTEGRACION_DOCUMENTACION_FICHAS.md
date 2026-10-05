# F17.4 — Integración bidireccional entre documentación y fichas

**Fecha:** 04/10/2026  
**Estado:** Completada

## Objetivo

Conectar la documentación pública de F17 con las fichas concretas del catálogo manteniendo una sola fuente de verdad y evitando añadir campos redundantes a `juegos.json`.

## Decisión de arquitectura

La relación se declara exclusivamente en `documentacion.json`, mediante el campo opcional `juegos` de cada documento. El generador valida esas URLs contra `juegos.json` y construye automáticamente la relación inversa.

```text
documentacion.json
      │
      ├── documento → pieza
      │
      └── generador
             │
             └── pieza → documentos
```

No se deben mantener manualmente ambas direcciones.

## Cambios implementados

- índice automático de documentos por URL de pieza;
- bloque condicional **Preservación y compatibilidad** en las fichas;
- agrupación prioritaria de documentación de preservación y guías de ejecución;
- enlaces desde cada documento hacia sus piezas relacionadas utilizando título y número de ficha;
- soporte de múltiples documentos por pieza y múltiples piezas por documento;
- rechazo de referencias a piezas inexistentes;
- rechazo de relaciones duplicadas dentro del mismo documento;
- ausencia total del bloque cuando una pieza todavía no dispone de documentación asociada;
- reutilización exclusiva de componentes y estilos ya existentes (`content-card`, `eyebrow`, `count`, listas y enlaces).

## Fuente única

`juegos.json` no recibe campos nuevos para esta relación. Esto evita inconsistencias entre catálogo y documentación.

## Validación

Se ha realizado una prueba temporal con `Star Wars Jedi Knight: Dark Forces II` (ficha `000200`) asociándolo al estándar de guías de ejecución. La generación comprobó ambos sentidos:

1. ficha → documento;
2. documento → ficha, mostrando título y número de ficha.

La relación temporal se retiró después de la prueba. F17.4 no publica ninguna asociación específica ficticia; la primera relación real se incorporará durante F17.5.

## Definition of Done

F17.4 se considera completada cuando:

- una relación declarada una sola vez aparece correctamente en ambos sentidos;
- una pieza sin relación mantiene su ficha sin bloques vacíos;
- una URL de pieza inexistente provoca error de generación;
- una relación duplicada provoca error de generación;
- no se introducen estilos específicos nuevos;
- `juegos.json` permanece libre de metadatos documentales redundantes.

## Siguiente paso

**F17.5 — Pieza piloto completa.** Aplicar el ciclo real de caracterización, preservación, copia de trabajo, compatibilidad, documentación y publicación sobre una pieza física concreta.
