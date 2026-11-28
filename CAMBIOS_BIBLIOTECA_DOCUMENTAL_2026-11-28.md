# Biblioteca documental escalable — 28/11/2026

Base: pcgamearchive_documentacion_navegacion_corregida.zip. Portal reducido a cuatro áreas activas y cinco novedades documentales. Índices independientes de preservación, guías, técnica y entornos; búsqueda global, filtros por categoría, ordenación y paginación de 24 elementos, estado mediante URL y navegación contextual. HTML paginado para acceso sin JavaScript; búsqueda global noindex,follow. Fuentes en biblioteca/, metadatos en documentacion.json, generación en generar_web.py. Sin infraestructura adicional ni datos sintéticos en producción.

## Evidencia de validación

- Generación completa: 1625 juegos, 37 novedades y 27 documentos.
- Regresión documental: 12/12. Regresión procedencia: correcta.
- Escala aislada: 1000 documentos / 44 páginas / 606917 bytes de índice global; 3500 / 147 / 2128124 bytes; 10000 / 419 / 6083559 bytes. Se verifican el total de registros, límite de 24, canonical, enlaces de paginación y limpieza de páginas sobrantes al reducir el volumen.
- JavaScript: datos reales y 10000 sintéticos, búsqueda, facetas, ordenación, paginación, parámetros URL, restauración, estado vacío y reset mediante DOM simulado.
- Sitemap: ninguna URL anterior eliminada; tres nuevas de índices de categorías. El buscador global no se incorpora al sitemap.
- Ningún archivo previo eliminado.

## Limitaciones y aceptación pendiente

Chromium del entorno de trabajo bloquea el acceso local por política administrativa (ERR_BLOCKED_BY_ADMINISTRATOR). Pendiente prueba visual y de interacción en navegador real, especialmente móvil, navegación atrás/adelante y enlaces bajo el servidor de despliegue. La prueba simulada no sustituye esa aceptación. Con 10000 documentos el índice global pesa aproximadamente 6 MB sin comprimir; evaluar segmentación o carga diferida cuando el crecimiento real lo justifique. No se ha desplegado la web. Los metadatos ausentes no se infieren.

## Prueba de aceptación local

Abrir /documentacion/ y confirmar que solo aparecen las cuatro áreas activas y cinco publicaciones recientes; abrir cada área; buscar QuickTime desde la portada y desde Guías, combinar filtros, ordenar, limpiar, recargar y comprobar parámetros de URL. Abrir un documento y regresar; comprobar a anchura móvil. Para paginación con el catálogo actual, usar búsqueda global sin filtros (27 documentos: 24 + 3). Verificar acceso a los índices con JavaScript desactivado.
