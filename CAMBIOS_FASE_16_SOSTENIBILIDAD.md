# Fase 16 — Sostenibilidad y monetización responsable

Fecha: 2026-09-27

## Alcance implementado

- Nueva página canónica `/apoyar/` para explicar la sostenibilidad económica de PC Game Archive.
- Integración externa con Ko-fi: `https://ko-fi.com/pcgamearchive`.
- Diferenciación explícita entre aportar material físico y apoyar económicamente el proyecto.
- Compromiso editorial: el catálogo, las fichas, fotografías, búsqueda y contenidos documentales continúan siendo públicos.
- Navegación principal ampliada con `Apoyar`.
- CTA adicional desde `/proyecto/` hacia `/apoyar/`.
- `/apoyar/` incluida en `sitemap.xml`, con canonical, metadata social, BreadcrumbList y WebPage JSON-LD.
- Instrumentación GA4:
  - `support_page_view`: visita a la página de apoyo.
  - `support_click`: salida hacia Ko-fi, con `provider`, `link_url` y `source_page`.
- La integración no depende de Stripe. El método de pago disponible actualmente se comunica como PayPal.

## Fuera de alcance deliberadamente

- AdSense y banners publicitarios.
- Afiliación comercial.
- Membresías y contenido exclusivo.
- Paywall.
- Patrocinios.
- Objetivos/Goals de Ko-fi.

Estas vías quedan reservadas para evolutivos posteriores y deberán respetar la independencia documental del archivo.
