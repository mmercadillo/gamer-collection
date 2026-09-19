# Fase 14 — Últimas incorporaciones

## Objetivo

Incorporar al modelo documental de PC Game Archive una fecha verificable de entrada de piezas, separada de la numeración de fichas y del calendario de publicación en redes sociales, y utilizarla para ofrecer una vista real de novedades sin crear un segundo catálogo.

## Cambios de datos

- Nuevo campo obligatorio `fecha_incorporacion` en `json_schema.json`.
- Valores admitidos: cadena vacía o fecha ISO `YYYY-MM-DD`.
- Migración de las 1.562 fichas preexistentes a cadena vacía para evitar inventar fechas históricas.
- El validador comprueba formato, validez de calendario y fechas futuras.

## Cambios de generación web

- Nueva sección condicional **Últimas incorporaciones al archivo** en la portada (máximo 6 fichas).
- Nueva ruta canónica `/incorporaciones/`, limitada a las 24 incorporaciones con fecha más recientes.
- No existe paginación ni histórico acumulativo: al entrar una incorporación nueva, la más antigua sale de esta vista cuando se supera el límite de 24.
- La página reutiliza exactamente la estructura base del catálogo (`wrap`, `page-head`, `section-head`, `grid cards`) y no define un layout propio.
- Las fichas individuales muestran **Incorporado al archivo** cuando la fecha está documentada.
- Integración condicional en navegación y sitemap: no se publican enlaces vacíos si todavía no existen fechas documentadas.
- El sitemap incorpora únicamente `/incorporaciones/`; nunca genera páginas `/incorporaciones/pagina/...`.
- El modo de búsqueda de portada oculta también el bloque de últimas incorporaciones para mantener el foco en los resultados.

## Regla documental

`fecha_incorporacion` no se infiere de `num`, Instagram, orden del catálogo, fecha de lanzamiento ni metadatos de archivos. Debe proceder de una fecha documentada.

La vista **Últimas incorporaciones** es deliberadamente efímera: sirve para descubrir qué ha entrado recientemente en el archivo. El catálogo sigue siendo la única navegación exhaustiva de todas las fichas.

## Operación

Para una incorporación nueva:

1. Registrar `fecha_incorporacion` en `juegos.json`.
2. Ejecutar `python validar_catalogo.py`.
3. Ejecutar `python generar_web.py`.
4. Verificar la portada, `/incorporaciones/`, la ficha del juego y `sitemap.xml`.

## Ajuste 14.1

La primera implementación generaba un histórico paginado y utilizaba estilos específicos para `/incorporaciones/`. Se corrige el enfoque para:

- evitar que la página termine duplicando el catálogo a medida que aumente la cobertura de `fecha_incorporacion`;
- limitar la vista a 24 incorporaciones;
- eliminar la paginación;
- utilizar exactamente el layout visual compartido con el catálogo y el resto de páginas generadas.
