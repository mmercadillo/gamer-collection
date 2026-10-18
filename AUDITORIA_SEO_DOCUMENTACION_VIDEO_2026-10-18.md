# Auditoría SEO — fichas, preservación, guías e introducciones (18/10/2026)

## Alcance
Revisión estática de `generar_web.py`, `documentacion.json`, `juegos.json`, `json_schema.json` y generación local. No equivale a una auditoría de Search Console ni a una verificación del despliegue público.

## Ya implementado
- Fichas de videojuegos: HTML indexable, `canonical`, Open Graph, `VideoGame`, `WebPage`, `BreadcrumbList`, sitemap.
- Documentación: URL propia, título/descripcion específicos, `TechArticle`, `BreadcrumbList`, fecha de publicación y actualización, enlaces a fichas, sitemap.
- Los vínculos con las fichas proceden de `documentacion.json`, fuente única de relaciones.

## Mejora aplicada (corrección de arquitectura multimedia)
- `video_intro=true` activa el reproductor y referencia `videos/<slug>.mp4` aunque el binario **no esté dentro del ZIP fuente**.
- El JSON-LD `VideoObject` se genera desde los metadatos declarados (`video_intro_fecha`, `video_intro_duracion`) sin condicionar la generación a archivos locales.
- `thumbnailUrl` referencia `videos/<slug>.webp`: **la miniatura real debe crearse a partir del vídeo y publicarse junto al MP4**, aunque ambos queden excluidos del ZIP de código. No se generan imágenes ficticias.
- Si no consta fecha real de publicación se omite `VideoObject` y se advierte; el reproductor sigue apareciendo.
- En el vídeo se mantiene `preload="none"` y no se fuerza la descarga completa en la carga inicial.
- Un `VideoObject` correcto en el código no garantiza indexación ni rich results; comprobar mediante la URL pública y Search Console.

## Panzer Commander
El catálogo declara `video_intro=true`, fecha `2026-10-18` y duración comprobada `PT2M27S`. La generación local produce tanto el reproductor como el marcado SEO, aun sin contener el MP4 original.

Para generar su miniatura desde PowerShell en el directorio raíz **que sí contiene el MP4 desplegable**:

```powershell
ffmpeg -ss 00:00:15 -i "videos/panzer-commander-wwii-tank-simulator-bigbox.mp4" -frames:v 1 -vf "scale=640:-2" -c:v libwebp -quality 78 "videos/panzer-commander-wwii-tank-simulator-bigbox.webp"
```

Revisar que el fotograma elegido represente la intro antes de publicar la miniatura. La subida del MP4 y del WebP es un paso de despliegue externo al ZIP.

## Verificación de la corrección
- Generación real con 1.572 fichas y 11 documentos completada sin multimedia local.
- Ficha generada de Panzer Commander: reproductor y `VideoObject` presentes, referencia MP4 por slug y miniatura WebP.
- El ZIP fuente no incluye multimedia pesada; no se alteran rutas de documentación ni del catálogo.

## Pendiente de comprobación externa
- Search Console: cobertura/indexación efectiva de guías y documentos, consultas reales, canonicals elegidos por Google.
- Rendimiento en dispositivos y Core Web Vitals.
- Revisión de resultados enriquecidos con la URL publicada.
- La ficha sigue siendo principalmente documental: el marcado no garantiza resultados enriquecidos de vídeo. No se añade `HowTo` indiscriminadamente ni un sitemap audiovisual vacío.
