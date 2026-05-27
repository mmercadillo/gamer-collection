#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador estático SEO/SEM para PC Game Archive.

Lee juegos.json como fuente maestra y genera una web estática indexable:
  - index.html
  - bigbox.html
  - series.html
  - contacto.html
  - robots.txt
  - sitemap.xml
  - assets/css/styles.css
  - assets/js/catalogo.js
  - assets/js/search-index.js
  - una página HTML por juego en la ruta definida por juego["url"]

Uso recomendado:
  python generar_web_v7.py

Uso alternativo generando en otra carpeta:
  python generar_web.py --catalogo juegos.json --out dist
  python generar_web.py --base-url https://pcgamearchive.org

Notas:
  - Por defecto genera in-place, en el directorio actual.
  - No modifica juegos.json.
  - No copia ni sobrescribe imágenes, carpetas img ni otros assets documentales de los juegos.
  - Solo sobrescribe ficheros generados: HTML, sitemap.xml, robots.txt, assets/css/styles.css, assets/js/catalogo.js, assets/js/search-index.js e informe_generacion_seo.md.
  - Buscador funcional por título, formato y serie en index.html.
  - Los enlaces internos a juegos apuntan explícitamente a index.html para funcionar también abriendo la web en local con file://.
  - En detalle de juego, la imagen principal se muestra completa sin recorte y los botones tienen separación respecto a las series/chips.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import quote

SITE_NAME = "PC Game Archive"
DEFAULT_BASE_URL = "https://pcgamearchive.org"
GA_ID = "G-SQN0WTMVP3"
OG_IMAGE = "/og/og-image.png"
PENDING_NUM = "000000"

SEO_LANDING_PAGES = [
    {"filename":"videojuegos-clasicos-pc.html","label":"PC clásico","title":"Videojuegos clásicos de PC · MS-DOS, Windows y Big Box","h1":"Videojuegos clásicos de PC","description":"Archivo documental de videojuegos clásicos de PC: MS-DOS, Windows 95/98, Big Box, CD-ROM, disquetes y ediciones físicas históricas.","lead":"PC Game Archive documenta videojuegos clásicos de PC en formato físico, con especial atención a cajas grandes, CD-ROM, disquetes, manuales, ediciones españolas y compatibilidad histórica con MS-DOS y Windows.","filter":{}},
    {"filename":"juegos-pc-big-box.html","label":"Big Box PC","title":"Juegos PC Big Box · Colección y archivo de cajas grandes","h1":"Juegos PC Big Box","description":"Catálogo de juegos de PC en formato Big Box: cajas grandes, manuales, disquetes, CD-ROM y ediciones físicas clásicas de los años 80, 90 y 2000.","lead":"Selección de ediciones Big Box de PC documentadas como piezas físicas: caja exterior, soporte original, manuales, material promocional y contexto histórico.","filter":{"formato":"Big Box"}},
    {"filename":"juegos-msdos.html","label":"MS-DOS","title":"Juegos MS-DOS de PC · Archivo físico y preservación","h1":"Juegos MS-DOS de PC","description":"Archivo de juegos MS-DOS en formato físico para PC: aventuras gráficas, estrategia, rol, simuladores, disquetes, CD-ROM y ediciones españolas.","lead":"Recorrido por juegos de PC para MS-DOS documentados desde su edición física original, incluyendo soporte, género, distribuidoras y contexto de preservación.","filter":{"plataforma":"MsDos"}},
    {"filename":"juegos-windows-95-98.html","label":"Windows 95/98","title":"Juegos Windows 95 y Windows 98 · PC clásico en CD-ROM","h1":"Juegos Windows 95 y Windows 98","description":"Catálogo de juegos clásicos de PC para Windows 95 y Windows 98: CD-ROM, Big Box, ediciones españolas, aventuras, estrategia, rol y simulación.","lead":"Documentación de juegos para Windows 95 y Windows 98, una etapa central del CD-ROM, la aceleración 3D, las localizaciones al castellano y el auge de las grandes cajas de PC.","filter":{"plataforma_any":["Win95","Win98"]}},
    {"filename":"ediciones-espanolas-pc.html","label":"Ediciones españolas","title":"Ediciones españolas de juegos de PC · Archivo documental","h1":"Ediciones españolas de juegos de PC","description":"Documentación de ediciones españolas y europeas de videojuegos clásicos de PC: cajas, manuales en castellano, distribuidoras, localizaciones y material físico.","lead":"PC Game Archive presta especial atención a las ediciones españolas y europeas: localización, distribuidoras, manuales en castellano, variantes físicas y materiales incluidos.","filter":{"text_terms":["españ","castellano","erbe","proein","dinamic","fx interactive","dro soft","virgin interactive españa","havas interactive españa"]}},
    {"filename":"aventuras-graficas-pc.html","label":"Aventuras gráficas","title":"Aventuras gráficas clásicas de PC · Point and click y MS-DOS","h1":"Aventuras gráficas clásicas de PC","description":"Catálogo de aventuras gráficas clásicas de PC: point and click, LucasArts, Sierra, MS-DOS, Windows, Big Box y ediciones físicas en castellano.","lead":"Selección de aventuras gráficas y point and click documentadas en formato físico, desde MS-DOS hasta Windows 95/98, con especial atención a ediciones Big Box y material impreso.","filter":{"genero_terms":["aventura gráfica","point and click"]}},
]

ROOT_PAGES = {
    "index.html",
    "bigbox.html",
    "series.html",
    "contacto.html",
    *(p["filename"] for p in SEO_LANDING_PAGES),
    "sitemap.xml",
    "robots.txt",
}


def load_json(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("juegos"), list):
        return data["juegos"]
    raise ValueError("El catálogo debe ser una lista JSON o un objeto con propiedad 'juegos'.")


def h(value: Any) -> str:
    return html.escape(str(value), quote=True)


def text(value: Any, fallback: str = "—") -> str:
    if value is None:
        return fallback
    if isinstance(value, str):
        return value.strip() or fallback
    if isinstance(value, list):
        return ", ".join(str(v) for v in value if str(v).strip()) or fallback
    return str(value)


def truncate(value: str, max_len: int = 155) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    if len(value) <= max_len:
        return value
    return value[: max_len - 1].rsplit(" ", 1)[0].rstrip(".,;:") + "…"


def abs_url(base_url: str, path: str) -> str:
    base = base_url.rstrip("/")
    clean = (path or "").lstrip("/")
    return f"{base}/{clean}" if clean else f"{base}/"


def rel_prefix_for(path: str) -> str:
    # Para juegos/<slug>/index.html => ../../
    depth = len([p for p in Path(path).parts[:-1] if p])
    return "../" * depth


def img_path(game: dict[str, Any], filename: str = "001.jpg") -> str:
    return f"{game.get('url', '').rstrip('/')}/img/{filename}"


def game_href(game: dict[str, Any], prefix: str = "") -> str:
    """Devuelve enlace navegable a ficha.

    En producción, la URL canónica sigue siendo /juegos/<slug>/, pero para
    pruebas locales con file:// los navegadores suelen mostrar el índice del
    directorio si el enlace acaba en /. Por eso los enlaces HTML internos
    apuntan explícitamente a index.html.
    """
    url = str(game.get("url", ""))
    if url.endswith("/"):
        return prefix + url + "index.html"
    return prefix + url


def existing_gallery(project_root: Path, game: dict[str, Any]) -> list[str]:
    url = str(game.get("url", ""))
    img_dir = project_root / url / "img"
    if not img_dir.exists():
        return []
    files = sorted(
        f.name for f in img_dir.iterdir()
        if f.is_file() and f.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    )
    return [f"{url.rstrip('/')}/img/{name}" for name in files]


def nav(active: str, prefix: str = "") -> str:
    items = [
        ("index.html", "Inicio"),
        ("videojuegos-clasicos-pc.html", "PC clásico"),
        ("juegos-pc-big-box.html", "Big Box PC"),
        ("juegos-msdos.html", "MS-DOS"),
        ("series.html", "Series"),
        ("contacto.html", "Contacto"),
    ]
    links = []
    for href, label in items:
        cls = ' class="active"' if href == active else ""
        links.append(f'<a{cls} href="{prefix}{href}">{label}</a>')
    links.append('<a href="https://www.instagram.com/pc_game_archive/" target="_blank" rel="noopener">Instagram</a>')
    return "\n".join(links)


def head(title: str, description: str, canonical: str, prefix: str = "", image: str | None = None, extra_jsonld: list[dict[str, Any]] | None = None) -> str:
    image_url = image or abs_url(DEFAULT_BASE_URL, OG_IMAGE)
    jsonld = ""
    for obj in extra_jsonld or []:
        jsonld += f'\n<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False, separators=(",", ":"))}</script>'
    return f'''<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{h(title)}</title>
<meta name="description" content="{h(description)}" />
<meta name="robots" content="index,follow" />
<meta name="theme-color" content="#111111" />
<link rel="canonical" href="{h(canonical)}" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="{SITE_NAME}" />
<meta property="og:title" content="{h(title)}" />
<meta property="og:description" content="{h(description)}" />
<meta property="og:url" content="{h(canonical)}" />
<meta property="og:image" content="{h(image_url)}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{h(title)}" />
<meta name="twitter:description" content="{h(description)}" />
<meta name="twitter:image" content="{h(image_url)}" />
<link rel="icon" href="{prefix}favicon.ico" sizes="any" />
<link rel="icon" type="image/png" sizes="48x48" href="{prefix}favicon-48x48.png" />
<link rel="icon" type="image/png" sizes="96x96" href="{prefix}favicon-96x96.png" />
<link rel="apple-touch-icon" href="{prefix}apple-touch-icon.png" />
<link rel="manifest" href="{prefix}site.webmanifest" />
<link rel="stylesheet" href="{prefix}assets/css/styles.css" />
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_ID}');</script>{jsonld}'''


def layout(title: str, description: str, canonical: str, active: str, body: str, prefix: str = "", subtitle: str = "Archivo físico de videojuegos de PC · Big Box · MS-DOS · Windows", image: str | None = None, jsonld: list[dict[str, Any]] | None = None) -> str:
    return f'''<!doctype html>
<html lang="es">
<head>
{head(title, description, canonical, prefix, image, jsonld)}
</head>
<body>
<header id="top">
  <div class="wrap header-row">
    <a class="brand" href="{prefix}index.html" aria-label="PC Game Archive">
      <img class="logo" src="{prefix}logo.png" alt="PC Game Archive logo">
      <span><strong>PC Game Archive</strong><small>{h(subtitle)}</small></span>
    </a>
    <nav class="nav" aria-label="Navegación principal">
      {nav(active, prefix)}
    </nav>
  </div>
</header>
{body}
<footer>
  <div class="wrap footrow">
    <p>PC Game Archive · <a href="mailto:contacto@pcgamearchive.org">contacto@pcgamearchive.org</a> · <a href="https://www.instagram.com/pc_game_archive/" target="_blank" rel="noopener">Instagram</a></p>
    <button class="to-top" type="button" data-scroll-top>Subir</button>
  </div>
</footer>
<script>
document.addEventListener('click',function(e){{
  var btn=e.target.closest('[data-scroll-top]');
  if(!btn) return;
  e.preventDefault();
  window.scrollTo({{top:0,behavior:'smooth'}});
  if(history.replaceState){{history.replaceState(null,'',location.pathname+location.search);}}
}});
</script>
</body>
</html>
'''


def card(game: dict[str, Any], prefix: str = "") -> str:
    url = game_href(game, prefix)
    img = prefix + img_path(game)
    title = text(game.get("titulo"))
    tags = [game.get("formato", "")] + (game.get("plataforma") or [])[:2]
    tag_html = "".join(f'<span class="tag">{h(t)}</span>' for t in tags if t)
    return f'''<a class="game-card" href="{h(url)}">
  <img src="{h(img)}" alt="{h('Portada de ' + title)}" loading="lazy" width="420" height="315" onerror="this.classList.add('missing');this.removeAttribute('src')" />
  <span class="game-card-body">
    <strong>{h(title)}</strong>
    <small>{h(text(game.get('genero')))}</small>
    <span class="tagrow">{tag_html}</span>
  </span>
</a>'''


def taxonomy_link(kind: str, value: str, prefix: str = "") -> str:
    return f'{prefix}index.html?{kind}={quote(value)}'


def build_search_index(games: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Genera un índice ligero para búsqueda en cliente."""
    index: list[dict[str, Any]] = []
    for g in games:
        index.append({
            "titulo": g.get("titulo", ""),
            "url": g.get("url", ""),
            "formato": g.get("formato", ""),
            "serie": g.get("serie") or [],
            "genero": g.get("genero") or [],
            "plataforma": g.get("plataforma") or [],
        })
    return index


def write_assets(out: Path, games: list[dict[str, Any]]) -> None:
    (out / "assets/css").mkdir(parents=True, exist_ok=True)
    (out / "assets/js").mkdir(parents=True, exist_ok=True)
    (out / "assets/css/styles.css").write_text(CSS, encoding="utf-8")
    search_index_js = "window.PCGA_SEARCH_INDEX=" + json.dumps(build_search_index(games), ensure_ascii=False, separators=(",", ":")) + ";\n"
    (out / "assets/js/search-index.js").write_text(search_index_js, encoding="utf-8")
    (out / "assets/js/catalogo.js").write_text(JS, encoding="utf-8")


def generate_index(games: list[dict[str, Any]], out: Path, base_url: str) -> None:
    bigbox = sum(1 for g in games if g.get("formato") == "Big Box")
    dvd_case = sum(1 for g in games if g.get("formato") == "DVD Case")
    jewel_case = sum(1 for g in games if g.get("formato") == "Jewel Case")
    initial_games = games[:24]
    cards = "\n".join(card(g) for g in initial_games)
    series_values = sorted({str(s) for g in games for s in (g.get("serie") or []) if str(s).strip()}, key=str.lower)
    series_options = "\n          ".join(f'<option value="{h(s)}">{h(s)}</option>' for s in series_values)
    desc = "Archivo y colección de videojuegos clásicos de PC en formato Big Box, MS-DOS y Windows. Preservación, catálogo y documentación de ediciones físicas retro."
    seo_hub_links = "\n".join(
        f'<a class="taxonomy-item" href="{h(p["filename"])}"><strong>{h(p["label"])}</strong><small>{h(p["h1"])}</small></a>'
        for p in SEO_LANDING_PAGES
    )
    body = f'''<main>
<section class="hero-section">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Preservación · Coleccionismo · PC clásico</p>
      <h1>Archivo físico de videojuegos de PC</h1>
      <p class="lead">Catálogo documental de ediciones físicas para PC, con especial atención a Big Box, MS-DOS, Windows clásicos, distribución española y preservación del soporte original.</p>
      <form class="search-hero catalog-search" action="index.html" method="get">
        <input name="titulo" placeholder="Buscar por título…" aria-label="Buscar por título">
        <select name="formato" aria-label="Filtrar por formato">
          <option value="">Todos los formatos</option>
          <option value="Big Box">Big Box</option>
          <option value="DVD Case">CD/DVD</option>
          <option value="Jewel Case">Jewel Case</option>
        </select>
        <select name="serie" aria-label="Filtrar por serie">
          <option value="">Todas las series</option>
          {series_options}
        </select>
        <button>Buscar</button>
      </form>
    </div>
    <aside class="stats-card" aria-label="Resumen del catálogo por formato">
      <strong>{bigbox}</strong><span>ediciones Big Box</span>
      <strong>{dvd_case}</strong><span>formato CD/DVD</span>
      <strong>{jewel_case}</strong><span>formato Jewel Case</span>
    </aside>
  </div>
</section>
<section class="wrap seo-hub" id="explorar-archivo">
  <div class="section-head"><h2>Explorar el archivo</h2><a href="series.html">Ver series</a></div>
  <p class="count">Rutas temáticas para encontrar el catálogo por búsquedas en español: PC clásico, Big Box, MS-DOS, Windows 95/98, ediciones españolas y aventuras gráficas.</p>
  <div class="taxonomy-grid">{seo_hub_links}</div>
</section>
<section class="wrap">
  <div class="section-head"><h2>Catálogo de juegos</h2><a href="bigbox.html">Ver Big Box</a></div>
  <p class="count">{len(games)} juegos encontrados.</p>
  <div class="grid cards" data-catalog-list>{cards}</div>
  <div class="load-sentinel" data-load-sentinel aria-hidden="true"></div>
</section>
<section class="wrap text-section">
  <h2>PC Game Archive como archivo documental</h2>
  <p>El objetivo del proyecto es documentar ediciones físicas de videojuegos de PC con valor histórico, técnico y coleccionista: cajas, manuales, discos, disquetes, plataformas compatibles, distribuidoras, sistemas de protección y contexto editorial.</p>
</section>
<script src="assets/js/search-index.js"></script>
<script src="assets/js/catalogo.js" defer></script>
</main>'''
    jsonld = [organization_jsonld(base_url), {"@context":"https://schema.org","@type":"WebSite","name":SITE_NAME,"url":base_url.rstrip("/") + "/","inLanguage":"es","description":desc,"potentialAction":{"@type":"SearchAction","target":base_url.rstrip("/") + "/index.html?q={search_term_string}","query-input":"required name=search_term_string"}}, collection_jsonld(base_url, "", "Archivo de videojuegos clásicos de PC", desc, games)]
    (out / "index.html").write_text(layout("PC Game Archive · Videojuegos clásicos de PC · Big Box · MS-DOS · Windows", desc, abs_url(base_url, ""), "index.html", body, jsonld=jsonld), encoding="utf-8")



def organization_jsonld(base_url: str) -> dict[str, Any]:
    return {"@context":"https://schema.org","@type":"Organization","name":SITE_NAME,"url":base_url.rstrip("/") + "/","logo":abs_url(base_url,"logo.png"),"sameAs":["https://www.instagram.com/pc_game_archive/"]}


def collection_jsonld(base_url: str, path: str, name: str, description: str, games: list[dict[str, Any]]) -> dict[str, Any]:
    return {"@context":"https://schema.org","@type":"CollectionPage","name":name,"url":abs_url(base_url,path),"description":description,"inLanguage":"es","isPartOf":{"@type":"WebSite","name":SITE_NAME,"url":base_url.rstrip("/") + "/"},"mainEntity":{"@type":"ItemList","numberOfItems":len(games),"itemListElement":[{"@type":"ListItem","position":i+1,"url":abs_url(base_url,g.get("url","")),"name":text(g.get("titulo"))} for i,g in enumerate(games[:50])]}}


def matches_landing(game: dict[str, Any], flt: dict[str, Any]) -> bool:
    if not flt:
        return True
    if flt.get("formato") and game.get("formato") != flt["formato"]:
        return False
    if flt.get("plataforma") and flt["plataforma"] not in (game.get("plataforma") or []):
        return False
    if flt.get("plataforma_any") and not any(p in (game.get("plataforma") or []) for p in flt["plataforma_any"]):
        return False
    if flt.get("genero_terms"):
        blob = " ".join(game.get("genero") or []).lower()
        if not any(t.lower() in blob for t in flt["genero_terms"]):
            return False
    if flt.get("text_terms"):
        blob = " ".join([text(game.get("titulo"),""), text(game.get("descripcion"),""), text(game.get("formato"),""), text(game.get("genero"),""), text(game.get("desarrollador"),""), text(game.get("distribuidor"),""), text(game.get("tags"),""), text(game.get("incluye"),"")]).lower()
        if not any(t.lower() in blob for t in flt["text_terms"]):
            return False
    return True


def default_filter_attr(flt: dict[str, Any]) -> str:
    if flt.get("formato"):
        return f' data-default-formato="{h(flt["formato"])}"'
    if flt.get("plataforma"):
        return f' data-default-plataforma="{h(flt["plataforma"])}"'
    if flt.get("plataforma_any"):
        return f' data-default-plataforma-any="{h("|".join(flt["plataforma_any"]))}"'
    if flt.get("genero_terms"):
        return f' data-default-genero-any="{h("|".join(flt["genero_terms"]))}"'
    if flt.get("text_terms"):
        return f' data-default-text-any="{h("|".join(flt["text_terms"]))}"'
    return ""


def generate_seo_landing_pages(games: list[dict[str, Any]], out: Path, base_url: str) -> None:
    for p in SEO_LANDING_PAGES:
        flt = p.get("filter", {})
        selected = [g for g in games if matches_landing(g, flt)]
        cards = "\n".join(card(g) for g in selected[:24])
        related = "\n".join(f'<a class="taxonomy-item" href="{h(x["filename"])}"><strong>{h(x["label"])}</strong><small>{h(x["h1"])}</small></a>' for x in SEO_LANDING_PAGES if x["filename"] != p["filename"])
        data_attr = default_filter_attr(flt)
        body = f'''<main class="wrap">
  <div class="page-head">
    <p class="eyebrow">SEO · Archivo documental</p>
    <h1>{h(p["h1"])}</h1>
    <p class="lead">{h(p["lead"])}</p>
  </div>
  <section class="content-card">
    <h2>Catálogo orientado a preservación</h2>
    <p>Esta sección refuerza la búsqueda en español y agrupa fichas por intención: formato físico, plataforma, género, distribución, idioma, soporte original y valor documental.</p>
    <p>Además de títulos concretos, el archivo quiere ser localizable por búsquedas como videojuegos clásicos de PC, juegos Big Box, juegos MS-DOS, ediciones españolas, aventuras gráficas clásicas y preservación de software físico.</p>
  </section>
  <section>
    <div class="section-head"><h2>Juegos documentados</h2><a href="index.html">Ver catálogo completo</a></div>
    <form class="toolbar" action="index.html" method="get"><input name="q" placeholder="Filtrar catálogo…"><button>Buscar</button></form>
    <p class="count">{len(selected)} juegos encontrados.</p>
    <div class="grid cards" data-catalog-list{data_attr}>{cards}</div>
    <div class="load-sentinel" data-load-sentinel aria-hidden="true"></div>
  </section>
  <section class="text-section"><h2>Explorar también</h2><div class="taxonomy-grid">{related}</div></section>
  <script src="assets/js/search-index.js"></script>
  <script src="assets/js/catalogo.js" defer></script>
</main>'''
        jsonld = [organization_jsonld(base_url), collection_jsonld(base_url, p["filename"], p["h1"], p["description"], selected)]
        (out / p["filename"]).write_text(layout(p["title"], p["description"], abs_url(base_url, p["filename"]), p["filename"], body, jsonld=jsonld), encoding="utf-8")

def generate_listing(games: list[dict[str, Any]], out: Path, base_url: str, filename: str, title: str, description: str, predicate) -> None:
    selected = [g for g in games if predicate(g)]
    cards = "\n".join(card(g) for g in selected[:24])
    body = f'''<main class="wrap">
  <div class="page-head">
    <p class="eyebrow">Catálogo</p>
    <h1>{h(title)}</h1>
    <p>{h(description)}</p>
  </div>
  <form class="toolbar" action="index.html" method="get"><input name="q" placeholder="Filtrar catálogo…"><button>Buscar</button></form>
  <p class="count">{len(selected)} juegos encontrados.</p>
  <div class="grid cards" data-catalog-list data-default-formato="{h('Big Box') if filename == 'bigbox.html' else ''}">{cards}</div>
  <div class="load-sentinel" data-load-sentinel aria-hidden="true"></div>
  <script src="assets/js/search-index.js"></script>
  <script src="assets/js/catalogo.js" defer></script>
</main>'''
    jsonld = [organization_jsonld(base_url), collection_jsonld(base_url, filename, title, description, selected)]
    (out / filename).write_text(layout(title, description, abs_url(base_url, filename), filename, body, jsonld=jsonld), encoding="utf-8")


def generate_series(games: list[dict[str, Any]], out: Path, base_url: str) -> None:
    counter = Counter()
    for g in games:
        for s in g.get("serie") or []:
            counter[s] += 1
    items = "\n".join(
        f'<a class="taxonomy-item" href="index.html?serie={quote(name)}"><strong>{h(name)}</strong><small>{count} juegos</small></a>'
        for name, count in sorted(counter.items(), key=lambda x: (-x[1], x[0].lower()))
    )
    title = "Series y colecciones · PC Game Archive"
    desc = "Explora las series, formatos y colecciones documentadas en PC Game Archive."
    body = f'''<main class="wrap">
  <div class="page-head"><p class="eyebrow">Exploración temática</p><h1>Series y colecciones</h1><p>{h(desc)}</p></div>
  <div class="taxonomy-grid">{items}</div>
</main>'''
    (out / "series.html").write_text(layout(title, desc, abs_url(base_url, "series.html"), "series.html", body), encoding="utf-8")


def generate_contact(out: Path, base_url: str) -> None:
    title = "Contacto · PC Game Archive"
    desc = "Contacto de PC Game Archive para correcciones, aportaciones documentales y propuestas sobre videojuegos físicos de PC."
    body = '''<main class="wrap">
  <article class="content-card">
    <h1>Contacto</h1>
    <p><strong>PC Game Archive</strong> es un proyecto dedicado a la preservación y documentación de videojuegos de PC en formato físico, con especial atención a ediciones clásicas de MS-DOS y Windows, Big Box, manuales, discos, disquetes y distribución española.</p>
    <p>Para proponer correcciones del catálogo, aportar información adicional sobre una edición concreta o compartir documentación relacionada con algún título, puedes usar estos canales.</p>
    <dl class="kv"><dt>Email</dt><dd><a href="mailto:contacto@pcgamearchive.org">contacto@pcgamearchive.org</a></dd><dt>Instagram</dt><dd><a href="https://www.instagram.com/pc_game_archive/" target="_blank" rel="noopener">@pc_game_archive</a></dd></dl>
  </article>
</main>'''
    (out / "contacto.html").write_text(layout(title, desc, abs_url(base_url, "contacto.html"), "contacto.html", body), encoding="utf-8")


def game_jsonld(game: dict[str, Any], base_url: str) -> dict[str, Any]:
    url = abs_url(base_url, game.get("url", ""))
    obj = {
        "@context": "https://schema.org",
        "@type": "VideoGame",
        "name": text(game.get("titulo")),
        "url": url,
        "description": truncate(text(game.get("descripcion"), ""), 500),
        "gamePlatform": game.get("plataforma") or [],
        "genre": game.get("genero") or [],
        "author": [{"@type":"Organization","name": v} for v in game.get("desarrollador") or []],
        "publisher": [{"@type":"Organization","name": v} for v in game.get("distribuidor") or []],
        "image": abs_url(base_url, img_path(game)),
    }
    if game.get("ean"):
        obj["gtin"] = game.get("ean")
    return obj


def breadcrumb_jsonld(game: dict[str, Any], base_url: str) -> dict[str, Any]:
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Inicio","item":abs_url(base_url,"")},
        {"@type":"ListItem","position":2,"name":text(game.get("formato")),"item":abs_url(base_url,"bigbox.html" if game.get("formato")=="Big Box" else "index.html")},
        {"@type":"ListItem","position":3,"name":text(game.get("titulo")),"item":abs_url(base_url,game.get("url",""))},
    ]}


def generate_game_pages(games: list[dict[str, Any]], out: Path, project_root: Path, base_url: str) -> None:
    url_counts = Counter(g.get("url") for g in games)
    for idx, game in enumerate(games, start=1):
        url = str(game.get("url", "")).strip()
        if not url or not re.match(r"^juegos/[a-z0-9\-]+/$", url):
            continue
        if url_counts[url] > 1:
            # Aun así generamos la primera aparición y saltamos duplicadas posteriores para no sobrescribir.
            if any(g is not game and g.get("url") == url for g in games[:idx-1]):
                continue
        prefix = rel_prefix_for(url + "index.html")
        title = text(game.get("titulo"))
        page_title = f"{title} · {text(game.get('formato'))} · PC Game Archive"
        desc = truncate(text(game.get("descripcion")), 155)
        gallery = existing_gallery(project_root, game)
        if not gallery:
            gallery = [img_path(game)]
        hero = prefix + gallery[0]
        chips = [game.get("formato")] + (game.get("plataforma") or []) + (game.get("serie") or [])[:3]
        chip_html = "".join(f'<a class="chip" href="{h(taxonomy_link("q", c, prefix))}">{h(c)}</a>' for c in chips if c)
        gallery_html = "\n".join(f'<img src="{h(prefix + src)}" alt="{h(title)}" loading="lazy" width="480" height="360" onerror="this.remove()">' for src in gallery)
        platform_links = " ".join(f'<a class="tag" href="{h(taxonomy_link("plataforma", p, prefix))}">{h(p)}</a>' for p in game.get("plataforma") or [])
        genre_links = " ".join(f'<a class="tag" href="{h(taxonomy_link("genero", g, prefix))}">{h(g)}</a>' for g in game.get("genero") or [])
        serie_links = " ".join(f'<a class="tag" href="{h(taxonomy_link("serie", s, prefix))}">{h(s)}</a>' for s in game.get("serie") or [])
        ig = game.get("ig") or ""
        ig_btn = f'<a class="button" href="{h(ig)}" target="_blank" rel="noopener">Ver publicación en Instagram</a>' if ig else ""
        prot = game.get("proteccion") if isinstance(game.get("proteccion"), dict) else {}
        body = f'''<main class="wrap game-detail">
  <nav class="breadcrumbs"><a href="{prefix}index.html">Inicio</a> / <a href="{prefix}bigbox.html">Catálogo</a> / <span>{h(title)}</span></nav>
  <article class="detail-grid">
    <section class="media-card">
      <img class="hero-img" src="{h(hero)}" alt="{h('Edición física de ' + title)}" width="760" height="570" onerror="this.classList.add('missing');this.removeAttribute('src')">
      <div class="chips">{chip_html}</div>
      <div class="actions"><a class="button" href="{prefix}index.html">Volver al catálogo</a>{ig_btn}</div>
    </section>
    <section class="content-card">
      <p class="eyebrow">Ficha #{h(game.get('num') or '000000')}</p>
      <h1>{h(title)}</h1>
      <p class="lead">{h(text(game.get('descripcion')))}</p>
      <dl class="kv">
        <dt>Formato</dt><dd>{h(text(game.get('formato')))}</dd>
        <dt>Plataforma</dt><dd class="tagrow">{platform_links}</dd>
        <dt>Género</dt><dd class="tagrow">{genre_links}</dd>
        <dt>Serie</dt><dd class="tagrow">{serie_links}</dd>
        <dt>Desarrollador</dt><dd>{h(text(game.get('desarrollador')))}</dd>
        <dt>Distribuidor</dt><dd>{h(text(game.get('distribuidor')))}</dd>
        <dt>EAN</dt><dd>{h(text(game.get('ean')))}</dd>
      </dl>
      <h2>Contenido de la edición</h2>
      <ul>{''.join(f'<li>{h(x)}</li>' for x in (game.get('incluye') or [])) or '<li>Pendiente de documentación.</li>'}</ul>
      <h2>Preservación</h2>
      <dl class="kv compact"><dt>Protección</dt><dd>{h(text(prot.get('tipo')))}</dd><dt>Formato recomendado</dt><dd>{h(text(prot.get('formato')))}</dd><dt>Jugable en virtualización</dt><dd>{'Sí' if prot.get('jugable_virtual') else 'No determinado'}</dd></dl>
      <p>{h(text(prot.get('preservacion'), 'Pendiente de documentación.'))}</p>
    </section>
  </article>
  <section class="content-card"><h2>Galería documental</h2><div class="gallery">{gallery_html}</div></section>
</main>'''
        page = layout(page_title, desc, abs_url(base_url, url), "", body, prefix=prefix, subtitle="Ficha documental", image=abs_url(base_url, img_path(game)), jsonld=[game_jsonld(game, base_url), breadcrumb_jsonld(game, base_url)])
        target = out / url / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page, encoding="utf-8")


def generate_sitemap(games: list[dict[str, Any]], out: Path, base_url: str) -> None:
    today = dt.date.today().isoformat()
    urls = ["", "index.html", "bigbox.html", "series.html", "contacto.html"] + [p["filename"] for p in SEO_LANDING_PAGES]
    seen = set(urls)
    for g in games:
        url = g.get("url")
        if isinstance(url, str) and re.match(r"^juegos/[a-z0-9\-]+/$", url) and url not in seen:
            urls.append(url)
            seen.add(url)
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = abs_url(base_url, u)
        prio = "1.0" if u in {"", "index.html"} else ("0.9" if not u.startswith("juegos/") else "0.7")
        lines.append(f"  <url><loc>{h(loc)}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>{prio}</priority></url>")
    lines.append("</urlset>")
    (out / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate_robots(out: Path, base_url: str) -> None:
    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {base_url.rstrip('/')}/sitemap.xml\n", encoding="utf-8")



def generate_favicons(project_root: Path, out: Path) -> None:
    logo = project_root / "logo.png"
    if not logo.exists():
        return
    try:
        from PIL import Image
        img = Image.open(logo).convert("RGBA")
        side = max(img.size)
        canvas = Image.new("RGBA", (side, side), (255, 255, 255, 0))
        canvas.paste(img, ((side - img.size[0]) // 2, (side - img.size[1]) // 2), img)
        for name, size in {"favicon-48x48.png":(48,48), "favicon-96x96.png":(96,96), "apple-touch-icon.png":(180,180)}.items():
            canvas.resize(size, Image.LANCZOS).save(out / name, "PNG", optimize=True)
        canvas.save(out / "favicon.ico", sizes=[(16,16), (32,32), (48,48)])
        manifest = {"name":SITE_NAME,"short_name":"PCGA","icons":[{"src":"/favicon-48x48.png","sizes":"48x48","type":"image/png"},{"src":"/favicon-96x96.png","sizes":"96x96","type":"image/png"},{"src":"/apple-touch-icon.png","sizes":"180x180","type":"image/png"}],"theme_color":"#111111","background_color":"#ffffff","display":"standalone","start_url":"/"}
        (out / "site.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except Exception:
        return

def copy_support_files(project_root: Path, out: Path) -> None:
    """
    Copia únicamente ficheros de soporte pequeños cuando se genera en una carpeta
    distinta al proyecto. No copia nunca juegos/, img/ ni contenido documental.

    En modo por defecto, out == project_root, por lo que no hace nada: el script
    trabaja directamente sobre el repositorio y solo sobrescribe los ficheros
    generados por sus propias funciones.
    """
    if out.resolve() == project_root.resolve():
        return

    for name in ["CNAME", "juegos.json", "json_schema.json", "favicon.ico", "favicon.svg", "apple-touch-icon.png", "site.webmanifest"]:
        src = project_root / name
        dst = out / name
        if src.exists() and src.is_file():
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(src.read_bytes())


def build_report(games: list[dict[str, Any]], out: Path) -> None:
    urls = [g.get("url") for g in games if g.get("url")]
    dup = [u for u,c in Counter(urls).items() if c > 1]
    invalid = [g for g in games if not isinstance(g.get("url"), str) or not re.match(r"^juegos/[a-z0-9\-]+/$", g.get("url", ""))]
    lines = [
        "# Informe de generación SEO",
        "",
        f"- Fecha: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"- Juegos en catálogo: {len(games)}",
        f"- URLs duplicadas detectadas: {len(dup)}",
        f"- URLs inválidas omitidas: {len(invalid)}",
        "",
        "## Observaciones",
        "",
        "- Las páginas de juego se generan como HTML estático en la ruta `juegos/<slug>/index.html`.",
        "- El sitemap usa `https://pcgamearchive.org` y elimina las rutas antiguas con hash.",
        "- Los duplicados no se sobrescriben: se conserva la primera aparición en el catálogo.",
        "- Se generan landing pages SEO en español para búsquedas genéricas.",
        "- Se generan favicon PNG/ICO y manifest desde logo.png para favorecer el icono en resultados de Google.",
    ]
    if dup:
        lines += ["", "## URLs duplicadas", ""] + [f"- `{u}`" for u in dup[:100]]
    if invalid:
        lines += ["", "## URLs inválidas omitidas", ""] + [f"- {g.get('num')} · {g.get('titulo')} · `{g.get('url')}`" for g in invalid[:100]]
    (out / "informe_generacion_seo.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalogo", default="juegos.json")
    parser.add_argument("--out", default=".", help="Directorio de salida. Por defecto: directorio actual, sin copiar imágenes.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    args = parser.parse_args()

    project_root = Path.cwd()
    catalog_path = (project_root / args.catalogo).resolve()
    out = (project_root / args.out).resolve()
    games = load_json(catalog_path)

    out.mkdir(parents=True, exist_ok=True)
    write_assets(out, games)
    copy_support_files(project_root, out)
    generate_favicons(project_root, out)
    generate_index(games, out, args.base_url)
    generate_listing(games, out, args.base_url, "bigbox.html", "Juegos PC Big Box · PC Game Archive", "Videojuegos de PC en formato Big Box: cajas grandes, manuales, disquetes, CD-ROM y ediciones físicas clásicas documentadas por PC Game Archive.", lambda g: g.get("formato") == "Big Box")
    generate_seo_landing_pages(games, out, args.base_url)
    generate_series(games, out, args.base_url)
    generate_contact(out, args.base_url)
    generate_game_pages(games, out, project_root, args.base_url)
    generate_sitemap(games, out, args.base_url)
    generate_robots(out, args.base_url)
    build_report(games, out)
    print("Versión generador: seo-hub-home-2026-05-27")
    print("Bloque SEO home: Explorar el archivo antes de Catálogo de juegos")
    print(f"Generación completada: {out}")
    print(f"Juegos procesados: {len(games)}")
    print("Modo de assets: no se copian imágenes ni carpetas img; solo se sobrescriben ficheros generados.")
    return 0


CSS = r'''
:root{--b:#111;--g:#666;--bd:#e6e6e6;--bg:#f7f7f5;--w:#fff;--soft:#f0eee9;--accent:#111;--max:1200px}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:var(--b);background:var(--bg);line-height:1.55}a{color:inherit}.wrap{max-width:var(--max);margin:0 auto;padding:0 18px}header{background:rgba(255,255,255,.95);border-bottom:1px solid var(--bd);position:sticky;top:0;z-index:10;backdrop-filter:blur(10px)}.header-row{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:14px 18px}.brand{display:flex;align-items:center;gap:12px;text-decoration:none}.brand strong{display:block;font-size:18px;letter-spacing:.2px}.brand small{display:block;color:var(--g);font-size:12px}.logo{width:64px;height:64px;object-fit:contain;display:block}.nav{display:flex;flex-wrap:wrap;gap:6px;justify-content:flex-end}.nav a{text-decoration:none;font-weight:800;font-size:14px;padding:8px 10px;border-radius:999px;border:1px solid transparent}.nav a:hover,.nav a.active{background:#f7f7f7;border-color:var(--bd)}main{padding-bottom:42px}.hero-section{background:linear-gradient(180deg,#fff,var(--soft));border-bottom:1px solid var(--bd)}.hero-grid{display:grid;grid-template-columns:1fr 280px;gap:28px;align-items:center;padding-top:48px;padding-bottom:48px}.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:12px;color:var(--g);font-weight:900;margin:0 0 10px}h1{font-size:clamp(32px,5vw,58px);line-height:1.02;margin:0 0 18px;letter-spacing:-.04em}h2{font-size:26px;line-height:1.15;margin:0 0 14px}.lead{font-size:18px;color:#333;max-width:760px}.search-hero,.toolbar{display:flex;gap:10px;margin-top:20px}.search-hero input,.toolbar input,.search-hero select,.toolbar select{flex:1;min-width:0;padding:14px 16px;border:1px solid var(--bd);border-radius:14px;background:#fff;font-size:16px}.search-hero select,.toolbar select{min-width:180px}.catalog-search{align-items:stretch}.search-hero button,.toolbar button,.button{border:1px solid var(--accent);background:var(--accent);color:#fff;text-decoration:none;border-radius:14px;padding:12px 16px;font-weight:900;cursor:pointer;display:inline-flex;align-items:center;justify-content:center}.stats-card{background:#111;color:#fff;border-radius:24px;padding:22px;display:grid;grid-template-columns:auto 1fr;gap:8px 14px}.stats-card strong{font-size:34px;line-height:1}.stats-card span{align-self:center;color:#ddd}.section-head,.meta{display:flex;align-items:end;justify-content:space-between;gap:14px;margin:30px 0 14px}.section-head a{font-weight:900}.grid.cards{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}.game-card{display:flex;flex-direction:column;background:#fff;border:1px solid var(--bd);border-radius:18px;overflow:hidden;text-decoration:none;min-height:245px;transition:transform .15s ease,box-shadow .15s ease}.game-card:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.08)}.game-card img{width:100%;aspect-ratio:4/3;object-fit:contain;background:#eee;padding:6px}.game-card img.missing,.hero-img.missing{background:repeating-linear-gradient(45deg,#eee,#eee 10px,#f8f8f8 10px,#f8f8f8 20px)}.game-card-body{display:flex;flex-direction:column;gap:6px;padding:12px}.game-card strong{font-size:14px;line-height:1.2}.game-card small,.count{color:var(--g);font-size:12px}.tagrow,.chips,.actions{display:flex;flex-wrap:wrap;gap:8px}.media-card .chips{margin-top:14px;margin-bottom:18px}.media-card .actions{margin-top:8px;padding-top:16px;border-top:1px solid var(--bd)}.tag,.chip{font-size:12px;padding:5px 9px;border:1px solid var(--bd);border-radius:999px;background:#fff;text-decoration:none}.page-head{padding:34px 0 20px}.page-head h1{font-size:42px}.taxonomy-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.taxonomy-item,.content-card,.media-card{background:#fff;border:1px solid var(--bd);border-radius:20px;padding:18px}.taxonomy-item{text-decoration:none;display:flex;justify-content:space-between;gap:16px}.taxonomy-item small{color:var(--g)}.text-section,.content-card{margin-top:28px}.breadcrumbs{font-size:13px;color:var(--g);padding:18px 0}.detail-grid{display:grid;grid-template-columns:minmax(300px,420px) 1fr;gap:20px;align-items:start}.hero-img{width:100%;height:auto;max-height:620px;object-fit:contain;border:1px solid var(--bd);border-radius:16px;background:#f3f3f1;display:block}.kv{display:grid;grid-template-columns:160px 1fr;gap:10px 14px;border-top:1px solid var(--bd);padding-top:14px;margin-top:18px}.kv dt{color:var(--g);font-weight:700}.kv dd{margin:0}.kv.compact{grid-template-columns:180px 1fr}.gallery{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.gallery img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:14px;border:1px solid var(--bd);background:#eee}footer{background:#fff;border-top:1px solid var(--bd);padding:22px 0}.footrow{display:flex;justify-content:space-between;gap:16px;align-items:center;color:var(--g);font-size:13px}.to-top{padding:8px 10px;border:1px solid var(--bd);border-radius:12px;text-decoration:none;font-weight:800;color:#111;background:#fff;cursor:pointer;font:inherit}.to-top:hover{background:#f7f7f7}@media(max-width:1100px){.grid.cards{grid-template-columns:repeat(4,1fr)}.taxonomy-grid{grid-template-columns:repeat(3,1fr)}}@media(max-width:800px){header{position:static}.header-row,.hero-grid,.detail-grid{grid-template-columns:1fr;display:grid}.nav{justify-content:flex-start}.grid.cards{grid-template-columns:repeat(2,1fr)}.taxonomy-grid,.gallery{grid-template-columns:repeat(2,1fr)}.search-hero,.toolbar{flex-direction:column}.kv{grid-template-columns:1fr}.page-head h1{font-size:34px}}@media(max-width:480px){.grid.cards,.taxonomy-grid,.gallery{grid-template-columns:1fr}.hero-grid{padding-top:30px;padding-bottom:30px}}
'''

JS = r'''
(function(){
  const PAGE_SIZE = 24;
  const params = new URLSearchParams(location.search);
  const grid = document.querySelector('[data-catalog-list], .grid.cards');
  const forms = document.querySelectorAll('form.catalog-search, form.search-hero, form.toolbar');
  const sentinel = document.querySelector('[data-load-sentinel]');

  restoreFormValues();
  if(!grid) return;

  const games = Array.isArray(window.PCGA_SEARCH_INDEX) ? window.PCGA_SEARCH_INDEX : [];
  if(!games.length) return;

  const titulo = normalize(params.get('titulo') || params.get('q') || '');
  const defaultFormato = normalize(grid.dataset.defaultFormato || '');
  const defaultPlataforma = normalize(grid.dataset.defaultPlataforma || '');
  const defaultPlataformaAny = splitTerms(grid.dataset.defaultPlataformaAny || '');
  const defaultGenero = normalize(grid.dataset.defaultGenero || '');
  const defaultGeneroAny = splitTerms(grid.dataset.defaultGeneroAny || '');
  const defaultTextAny = splitTerms(grid.dataset.defaultTextAny || '');
  const formato = normalize(params.get('formato') || '') || defaultFormato;
  const serie = normalize(params.get('serie') || '');
  const genero = normalize(params.get('genero') || '') || defaultGenero;
  const plataforma = normalize(params.get('plataforma') || '') || defaultPlataforma;

  const selected = games.filter(g => {
    const titleBlob = normalize(g.titulo);
    const genreBlob = normalize((g.genero || []).join(' '));
    const platformValues = (g.plataforma || []).map(normalize);
    const fullBlob = normalize([g.titulo, g.formato, (g.serie||[]).join(' '), (g.genero||[]).join(' '), (g.plataforma||[]).join(' ')].join(' '));
    if(titulo && !titleBlob.includes(titulo)) return false;
    if(formato && normalize(g.formato) !== formato) return false;
    if(serie && !(g.serie || []).some(s => normalize(s) === serie)) return false;
    if(genero && !genreBlob.includes(genero)) return false;
    if(defaultGeneroAny.length && !defaultGeneroAny.some(t => genreBlob.includes(t))) return false;
    if(plataforma && !platformValues.some(s => s === plataforma)) return false;
    if(defaultPlataformaAny.length && !defaultPlataformaAny.some(t => platformValues.includes(t))) return false;
    if(defaultTextAny.length && !defaultTextAny.some(t => fullBlob.includes(t))) return false;
    return true;
  });

  let rendered = 0;
  grid.innerHTML = '';
  renderNextPage();

  const count = document.querySelector('.count');
  if(count) count.textContent = selected.length + ' juegos encontrados.';

  if(!selected.length){
    grid.innerHTML = '<p class="content-card">No se han encontrado juegos con esos filtros.</p>';
    if(sentinel) sentinel.remove();
    return;
  }

  if(sentinel && 'IntersectionObserver' in window){
    const observer = new IntersectionObserver(entries => {
      if(entries.some(entry => entry.isIntersecting)) renderNextPage();
      if(rendered >= selected.length) observer.disconnect();
    }, {rootMargin: '700px 0px'});
    observer.observe(sentinel);
  } else {
    window.addEventListener('scroll', () => {
      if(rendered >= selected.length) return;
      if(window.innerHeight + window.scrollY >= document.body.offsetHeight - 900) renderNextPage();
    }, {passive:true});
  }

  function renderNextPage(){
    const next = selected.slice(rendered, rendered + PAGE_SIZE);
    if(!next.length) return;
    grid.insertAdjacentHTML('beforeend', next.map(g => card(g)).join(''));
    rendered += next.length;
    if(sentinel) sentinel.hidden = rendered >= selected.length;
  }

  function splitTerms(value){
    return String(value || '').split('|').map(normalize).filter(Boolean);
  }

  function normalize(value){
    return String(value || '')
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .trim();
  }

  function esc(s){
    return String(s || '').replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
  }

  function restoreFormValues(){
    forms.forEach(form => {
      ['titulo','q','formato','serie','genero','plataforma'].forEach(name => {
        const el = form.querySelector(`[name="${name}"]`);
        if(el && params.has(name)) el.value = params.get(name) || '';
      });
    });
  }

  function card(g){
    const tags = [g.formato].concat(g.plataforma || []).filter(Boolean).slice(0, 3).map(t => `<span class="tag">${esc(t)}</span>`).join('');
    const rawUrl = String(g.url || '#');
    const url = esc(rawUrl.endsWith('/') ? rawUrl + 'index.html' : rawUrl);
    const img = esc(rawUrl.replace(/\/$/, '') + '/img/001.jpg');
    return `<a class="game-card" href="${url}"><img src="${img}" alt="${esc('Portada de ' + (g.titulo || ''))}" loading="lazy" width="420" height="315" onerror="this.classList.add('missing');this.removeAttribute('src')"><span class="game-card-body"><strong>${esc(g.titulo)}</strong><small>${esc((g.genero || []).join(', '))}</small><span class="tagrow">${tags}</span></span></a>`;
  }
})();
'''

if __name__ == "__main__":
    raise SystemExit(main())