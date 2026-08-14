#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador estático SEO/SEM para PC Game Archive.

Lee juegos.json como fuente maestra y genera una web estática indexable:
  - index.html
  - bigbox.html (compatibilidad/redirección)
  - series.html
  - contacto.html
  - vender-videojuegos-pc-antiguos/index.html
  - robots.txt
  - sitemap.xml
  - assets/css/styles.css
  - assets/js/catalogo.js
  - assets/js/search-index.js
  - índices y páginas de desarrolladores, distribuidores, géneros, plataformas y formatos
  - taxonomías editoriales por año, mercado, idioma, soporte y tipo de edición cuando existe cobertura suficiente
  - catálogo HTML paginado y rastreable en /catalogo/
  - una página HTML por juego en la ruta definida por juego["url"]

Uso recomendado:
  python generar_web.py

Uso alternativo generando en otra carpeta:
  python generar_web.py --catalogo juegos.json --out dist
  python generar_web.py --base-url https://pcgamearchive.org

Notas:
  - Por defecto genera in-place, en el directorio actual.
  - No modifica juegos.json.
  - No copia ni sobrescribe imágenes, carpetas img ni otros assets documentales de los juegos.
  - Solo sobrescribe ficheros generados: HTML, sitemap.xml, robots.txt, assets/css/styles.css, assets/js/catalogo.js, assets/js/search-index.js, directorios de taxonomías e informe_generacion_seo.md.
  - Buscador global por metadatos del catálogo, combinado con filtros de formato, serie, género y plataforma.
  - Los enlaces internos usan siempre URLs canónicas limpias, sin `index.html`.
  - El scroll infinito de la portada se complementa con paginación HTML estática para rastreo.
  - Las fotografías existentes en /juegos/<slug>/img/ se incorporan automáticamente al sitemap mediante la extensión de imágenes de Google.
  - Las fichas generan alt/captions descriptivos, ImageObject/primaryImageOfPage y prioridad alta para la imagen principal sin renombrar los originales.
  - Para probar localmente las URLs limpias se recomienda servir el directorio por HTTP (por ejemplo, `python -m http.server`).
  - En detalle de juego, la imagen principal se muestra completa sin recorte y los botones tienen separación respecto a las series/chips.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import math
import os
import re
import shutil
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import quote

SITE_NAME = "PC Game Archive"
DEFAULT_BASE_URL = "https://pcgamearchive.org"
GA_ID = "G-SQN0WTMVP3"
OG_IMAGE = "/no_disponible.png"
PENDING_NUM = "000000"
CATALOG_PAGE_SIZE = 24

SEO_LANDING_PAGES = [
    {"filename":"videojuegos-clasicos-pc.html","label":"PC clásico","title":"Videojuegos clásicos de PC · MS-DOS, Windows y Big Box","h1":"Videojuegos clásicos de PC","description":"Archivo documental de videojuegos clásicos de PC: MS-DOS, Windows 95/98, Big Box, CD-ROM, disquetes y ediciones físicas históricas.","lead":"PC Game Archive documenta videojuegos clásicos de PC en formato físico, con especial atención a cajas grandes, CD-ROM, disquetes, manuales, ediciones españolas y compatibilidad histórica con MS-DOS y Windows.","filter":{}},
    {"filename":"juegos-pc-big-box.html","label":"Big Box PC","title":"Juegos PC Big Box · Colección y archivo de cajas grandes","h1":"Juegos PC Big Box","description":"Catálogo de juegos de PC en formato Big Box: cajas grandes, manuales, disquetes, CD-ROM y ediciones físicas clásicas de los años 80, 90 y 2000.","lead":"Selección de ediciones Big Box de PC documentadas como piezas físicas: caja exterior, soporte original, manuales, material promocional y contexto histórico.","filter":{"formato":"Big Box"}},
    {"filename":"juegos-msdos.html","label":"MS-DOS","title":"Juegos MS-DOS de PC · Archivo físico y preservación","h1":"Juegos MS-DOS de PC","description":"Archivo de juegos MS-DOS en formato físico para PC: aventuras gráficas, estrategia, rol, simuladores, disquetes, CD-ROM y ediciones españolas.","lead":"Recorrido por juegos de PC para MS-DOS documentados desde su edición física original, incluyendo soporte, género, distribuidoras y contexto de preservación.","filter":{"plataforma":"MsDos"}},
    {"filename":"juegos-windows-95-98.html","label":"Windows 95/98","title":"Juegos Windows 95 y Windows 98 · PC clásico en CD-ROM","h1":"Juegos Windows 95 y Windows 98","description":"Catálogo de juegos clásicos de PC para Windows 95 y Windows 98: CD-ROM, Big Box, ediciones españolas, aventuras, estrategia, rol y simulación.","lead":"Documentación de juegos para Windows 95 y Windows 98, una etapa central del CD-ROM, la aceleración 3D, las localizaciones al castellano y el auge de las grandes cajas de PC.","filter":{"plataforma_any":["Win95","Win98"]}},
    {"filename":"ediciones-espanolas-pc.html","label":"Ediciones españolas","title":"Ediciones españolas de juegos de PC · Archivo documental","h1":"Ediciones españolas de juegos de PC","description":"Documentación de ediciones españolas y europeas de videojuegos clásicos de PC: cajas, manuales en castellano, distribuidoras, localizaciones y material físico.","lead":"PC Game Archive presta especial atención a las ediciones españolas y europeas: localización, distribuidoras, manuales en castellano, variantes físicas y materiales incluidos.","filter":{"text_terms":["españ","castellano","erbe","proein","dinamic","fx interactive","dro soft","virgin interactive españa","havas interactive españa"]}},
    {"filename":"aventuras-graficas-pc.html","label":"Aventuras gráficas","title":"Aventuras gráficas clásicas de PC · Point and click y MS-DOS","h1":"Aventuras gráficas clásicas de PC","description":"Catálogo de aventuras gráficas clásicas de PC: point and click, LucasArts, Sierra, MS-DOS, Windows, Big Box y ediciones físicas en castellano.","lead":"Selección de aventuras gráficas y point and click documentadas en formato físico, desde MS-DOS hasta Windows 95/98, con especial atención a ediciones Big Box y material impreso.","filter":{"genero_terms":["aventura gráfica","point and click"]}},

]

# Contenido editorial específico de las landings principales. Se mantiene separado de
# los filtros para poder evolucionar el texto sin alterar la lógica del catálogo.
LANDING_EDITORIAL = {
    "videojuegos-clasicos-pc.html": {
        "eyebrow": "Archivo de PC clásico",
        "intro_title": "Un archivo centrado en la edición física",
        "paragraphs": [
            "El videojuego clásico de PC no se conserva solo como software. Cada edición física documenta una forma concreta de publicar, distribuir y utilizar un juego: cajas, manuales, soportes ópticos o magnéticos, requisitos de sistema, material promocional y variantes de mercado.",
            "Esta selección reúne el núcleo histórico del archivo y permite recorrer distintas generaciones del PC, desde MS-DOS y Windows 3.x hasta Windows 95/98 y sistemas posteriores, manteniendo el foco en la pieza física y en la información asociada a cada edición."
        ],
        "secondary_title": "Cómo recorrer esta colección",
        "secondary_paragraphs": [
            "Puedes explorar el archivo por formato, plataforma, género, desarrollador o distribuidor. Las relaciones entre fichas permiten pasar de un juego concreto a otras ediciones que comparten contexto técnico o editorial.",
            "El catálogo se amplía de forma continua. Cuando se incorpora una nueva edición, esta página y sus relaciones se actualizan automáticamente a partir de los datos documentados en el archivo."
        ],
        "explore_taxonomies": ["formatos", "plataformas", "generos", "desarrolladores"]
    },
    "juegos-pc-big-box.html": {
        "eyebrow": "Formato físico · Big Box",
        "intro_title": "La gran caja como parte de la historia del PC",
        "paragraphs": [
            "Las ediciones Big Box fueron uno de los formatos más reconocibles del videojuego de PC. Su tamaño permitía reunir no solo el soporte del juego, sino también manuales extensos, mapas, referencias rápidas, catálogos, tarjetas de registro y otros materiales que hoy ayudan a reconstruir cómo se comercializaba y utilizaba el software.",
            "PC Game Archive documenta estas ediciones como conjuntos físicos. La caja, el contenido y las variantes de distribución forman parte de la ficha, porque dos publicaciones del mismo juego pueden ser documentalmente distintas aunque ejecuten el mismo software."
        ],
        "secondary_title": "Qué buscamos preservar en una Big Box",
        "secondary_paragraphs": [
            "La conservación no se limita al disco o al CD-ROM: también interesa identificar manuales, inserts, mapas, guías, referencias de distribuidor y cualquier elemento original que permita describir la edición con precisión.",
            "Desde esta página puedes comparar Big Box de distintas plataformas, géneros, desarrolladores y distribuidores y acceder a las fotografías y datos disponibles de cada ejemplar."
        ],
        "explore_taxonomies": ["plataformas", "generos", "desarrolladores", "distribuidores"]
    },
    "juegos-msdos.html": {
        "eyebrow": "Plataforma · MS-DOS",
        "intro_title": "El PC antes de la estandarización de Windows",
        "paragraphs": [
            "MS-DOS concentra una parte esencial de la historia del videojuego para compatibles IBM PC. En sus ediciones físicas conviven disquetes, CD-ROM, manuales técnicos, tablas de referencia y requisitos de hardware que reflejan una época en la que instalar y configurar un juego podía formar parte de la propia experiencia.",
            "El archivo reúne ediciones identificadas como compatibles con MS-DOS y las conecta con sus géneros, desarrolladores, distribuidores y formatos físicos. Esto permite estudiar no solo los títulos, sino también cómo fueron publicados y adaptados a diferentes mercados."
        ],
        "secondary_title": "Disquetes, CD-ROM y documentación técnica",
        "secondary_paragraphs": [
            "Las fichas pueden recoger el soporte original, el contenido de la caja y datos de compatibilidad cuando están documentados. Esa información resulta especialmente valiosa en software de MS-DOS, donde versiones, memoria disponible, tarjetas de sonido o métodos de instalación podían condicionar el funcionamiento.",
            "La colección incluye desde aventuras y juegos de rol hasta estrategia, simulación y acción, ofreciendo un recorrido transversal por varias etapas del PC clásico."
        ],
        "explore_taxonomies": ["generos", "desarrolladores", "distribuidores", "formatos"]
    },
    "juegos-windows-95-98.html": {
        "eyebrow": "Plataforma · Windows 95/98",
        "intro_title": "La consolidación del PC multimedia",
        "paragraphs": [
            "Windows 95 y Windows 98 marcaron una etapa de transición decisiva para el videojuego de PC. El CD-ROM se generalizó, crecieron las instalaciones en disco duro, la aceleración 3D ganó protagonismo y las ediciones físicas comenzaron a combinar grandes cajas con formatos más compactos.",
            "Esta página reúne las ediciones del archivo compatibles con Windows 95 o Windows 98 y permite relacionarlas con sus desarrolladores, distribuidores, géneros y formatos. Una misma obra puede aparecer en más de una plataforma o edición, y el catálogo conserva esas diferencias cuando están documentadas."
        ],
        "secondary_title": "Una época de cambios en la edición física",
        "secondary_paragraphs": [
            "Durante estos años convivieron Big Box, cajas de CD, manuales impresos de distinto tamaño y numerosas reediciones. Esa variedad hace especialmente útil documentar cada publicación como una edición concreta y no únicamente como un título de software.",
            "Las fichas del archivo permiten recorrer esa evolución desde el punto de vista físico y editorial, además de consultar los datos técnicos disponibles de cada juego."
        ],
        "explore_taxonomies": ["generos", "desarrolladores", "distribuidores", "formatos"]
    },
    "ediciones-espanolas-pc.html": {
        "eyebrow": "Mercado español · Archivo documental",
        "intro_title": "Documentar cómo llegaron los juegos de PC a España",
        "paragraphs": [
            "Las ediciones distribuidas en España son especialmente útiles para reconstruir la historia local del PC: traducciones y manuales en castellano, cambios de carátula, referencias comerciales, sellos de distribuidor, reediciones económicas y materiales creados específicamente para nuestro mercado.",
            "PC Game Archive intenta conservar esas diferencias editoriales porque una edición española puede aportar información que no aparece en la publicación internacional del mismo juego. La distribuidora, el idioma, el contenido físico y las referencias impresas forman parte de esa identidad documental."
        ],
        "secondary_title": "Una clasificación que seguirá ganando precisión",
        "secondary_paragraphs": [
            "La selección actual se construye a partir de los datos disponibles en las fichas —referencias a idioma, distribución y edición—. A medida que el catálogo incorpore campos más específicos de mercado e idioma, esta agrupación podrá afinarse todavía más.",
            "Mientras tanto, esta página funciona como punto de entrada a las ediciones con señales documentales vinculadas al mercado español y a los principales distribuidores representados en el archivo."
        ],
        "explore_taxonomies": ["distribuidores", "desarrolladores", "generos", "plataformas"]
    },
    "aventuras-graficas-pc.html": {
        "eyebrow": "Género · Aventura gráfica",
        "intro_title": "La aventura gráfica como patrimonio del PC",
        "paragraphs": [
            "La aventura gráfica está estrechamente ligada a varias generaciones del PC doméstico. Desde interfaces basadas en verbos hasta el point and click y las aventuras en 3D, el género dejó algunas de las ediciones físicas más reconocibles por sus ilustraciones, manuales, pistas, mapas y materiales narrativos.",
            "Esta selección reúne las fichas catalogadas como aventura gráfica o point and click y permite recorrerlas por plataforma, desarrollador, distribuidor y formato. El objetivo es conservar tanto el juego como el contexto editorial de cada publicación."
        ],
        "secondary_title": "Más allá del título del juego",
        "secondary_paragraphs": [
            "En este género, la edición física suele aportar elementos que amplían la experiencia: documentación de ambientación, manuales integrados en la ficción, guías de referencia o presentaciones especialmente cuidadas. Registrar esos componentes ayuda a diferenciar reediciones y variantes.",
            "El archivo conecta las aventuras de MS-DOS y Windows con las compañías y formatos presentes en la colección para facilitar una exploración histórica más amplia."
        ],
        "explore_taxonomies": ["desarrolladores", "distribuidores", "plataformas", "formatos"]
    }
}

TAXONOMIES = {
    "desarrolladores": {
        "field": "desarrollador",
        "singular": "desarrollador",
        "label": "Desarrolladores",
        "eyebrow": "Desarrollo",
        "min_count": 3,
        "min_documented": 0,
    },
    "distribuidores": {
        "field": "distribuidor",
        "singular": "distribuidor",
        "label": "Distribuidores",
        "eyebrow": "Distribución",
        "min_count": 3,
        "min_documented": 0,
    },
    "generos": {
        "field": "genero",
        "singular": "género",
        "label": "Géneros",
        "eyebrow": "Género",
        "min_count": 3,
        "min_documented": 0,
    },
    "plataformas": {
        "field": "plataforma",
        "singular": "plataforma",
        "label": "Plataformas",
        "eyebrow": "Plataforma",
        "min_count": 3,
        "min_documented": 0,
    },
    "formatos": {
        "field": "formato",
        "singular": "formato",
        "label": "Formatos",
        "eyebrow": "Formato físico",
        "min_count": 3,
        "min_documented": 0,
    },
    # Fase 10D: nuevas taxonomías editoriales. Además del mínimo por entidad,
    # exigen una masa crítica absoluta de fichas documentadas. Un umbral absoluto
    # evita que un hub ya publicado desaparezca al crecer el catálogo con campos vacíos.
    "anos": {
        "field": "anio",
        "singular": "año",
        "label": "Años",
        "eyebrow": "Año de la edición",
        "min_count": 3,
        "min_documented": 150,
    },
    "mercados": {
        "field": "mercado",
        "singular": "mercado",
        "label": "Mercados",
        "eyebrow": "Mercado editorial",
        "min_count": 3,
        "min_documented": 150,
    },
    "idiomas": {
        "field": "idioma",
        "singular": "idioma",
        "label": "Idiomas",
        "eyebrow": "Idioma de la edición",
        "min_count": 3,
        "min_documented": 150,
    },
    "soportes": {
        "field": "soporte",
        "singular": "soporte",
        "label": "Soportes",
        "eyebrow": "Soporte de distribución",
        "min_count": 3,
        "min_documented": 150,
    },
    "tipos-edicion": {
        "field": "tipo_edicion",
        "singular": "tipo de edición",
        "label": "Tipos de edición",
        "eyebrow": "Clasificación editorial",
        "min_count": 3,
        "min_documented": 150,
    },
}

# Reutiliza landings editoriales existentes cuando ya cubren claramente la misma intención.
# Así evitamos crear una segunda URL SEO para Big Box, MS-DOS, Windows 95/98 o aventura gráfica.
TAXONOMY_ROUTE_OVERRIDES = {
    ("formatos", "big box"): "juegos-pc-big-box.html",
    ("plataformas", "msdos"): "juegos-msdos.html",
    ("plataformas", "win95"): "juegos-windows-95-98.html",
    ("plataformas", "win98"): "juegos-windows-95-98.html",
    ("generos", "aventura grafica"): "aventuras-graficas-pc.html",
    ("generos", "point and click"): "aventuras-graficas-pc.html",
    # Mercado España reutiliza la landing editorial histórica para evitar dos
    # URLs compitiendo por la misma intención de búsqueda.
    ("mercados", "espana"): "ediciones-espanolas-pc.html",
}

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


def site_path(path: str) -> str:
    """Convierte una ruta del catálogo en ruta absoluta desde la raíz del sitio."""
    raw = str(path or "").strip()
    if not raw:
        return "/"
    return "/" + raw.lstrip("/")


def img_path(game: dict[str, Any], filename: str = "001.jpg") -> str:
    return site_path(f"{game.get('url', '').rstrip('/')}/img/{filename}")


def game_href(game: dict[str, Any], prefix: str = "") -> str:
    """Devuelve siempre la URL canónica limpia de una ficha desde la raíz del sitio."""
    return site_path(str(game.get("url", "")))


def home_href(prefix: str = "") -> str:
    """Enlace a la raíz del sitio compatible con páginas en subdirectorios."""
    return prefix or "./"


def existing_gallery(project_root: Path, game: dict[str, Any]) -> list[str]:
    url = str(game.get("url", ""))
    img_dir = project_root / url / "img"
    if not img_dir.exists():
        return []
    files = sorted(
        f.name for f in img_dir.iterdir()
        if f.is_file() and f.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    )
    return [site_path(f"{url.rstrip('/')}/img/{name}") for name in files]


def build_gallery_index(project_root: Path, games: list[dict[str, Any]]) -> dict[str, list[str]]:
    """Inventario único de imágenes documentales existentes por ficha.

    Solo se incluyen ficheros que existen físicamente en /juegos/<slug>/img/.
    El índice se reutiliza para las fichas y para el sitemap de imágenes.
    """
    index: dict[str, list[str]] = {}
    for game in games:
        url = str(game.get("url", "")).strip()
        if not url or not re.match(r"^juegos/[a-z0-9\-]+/$", url):
            continue
        index[url] = existing_gallery(project_root, game)
    return index


def image_platform_text(game: dict[str, Any]) -> str:
    labels = {
        "msdos": "MS-DOS",
        "win3x": "Windows 3.x",
        "win95": "Windows 95",
        "win98": "Windows 98",
        "winme": "Windows Me",
        "winnt": "Windows NT",
        "win2k": "Windows 2000",
        "winxp": "Windows XP",
        "winvista": "Windows Vista",
        "win7": "Windows 7",
        "win8": "Windows 8",
        "win10": "Windows 10",
        "win11": "Windows 11",
    }
    values = list_values(game.get("plataforma"))
    result: list[str] = []
    for value in values[:3]:
        key = entity_key(value).replace(" ", "").replace("-", "")
        result.append(labels.get(key, value))
    return ", ".join(result)


def edition_image_label(game: dict[str, Any], *, kind: str = "principal", position: int | None = None) -> str:
    """Alt descriptivo de una fotografía documental, sin keyword stuffing."""
    title = text(game.get("titulo"), "videojuego")
    fmt = text(game.get("formato"), "")
    platform = image_platform_text(game)
    if kind == "cover":
        lead = f"Portada de {title}"
    elif kind == "gallery" and position is not None:
        lead = f"Imagen documental {position} de {title}"
    else:
        lead = f"Edición física de {title}"
    details: list[str] = []
    if fmt:
        details.append(f"formato {fmt}")
    if platform:
        details.append(f"para {platform}")
    return lead + (", " + ", ".join(details) if details else "")


def edition_image_caption(game: dict[str, Any]) -> str:
    parts = [text(game.get("titulo"), "Videojuego")]
    fmt = text(game.get("formato"), "")
    platform = image_platform_text(game)
    if fmt:
        parts.append(fmt)
    if platform:
        parts.append(platform)
    return " · ".join(parts)


def image_object_jsonld(game: dict[str, Any], base_url: str, image_path: str) -> dict[str, Any]:
    image_url = abs_url(base_url, image_path)
    return {
        "@type": "ImageObject",
        "@id": image_url + "#image",
        "url": image_url,
        "contentUrl": image_url,
        "name": edition_image_label(game),
        "caption": edition_image_caption(game),
        "representativeOfPage": True,
    }


RELATED_GENERIC_SERIES = {"todos", "big box", "dvd case", "jewel case"}


def value_keys(game: dict[str, Any], field: str) -> set[str]:
    return {entity_key(v) for v in list_values(game.get(field)) if entity_key(v)}


def meaningful_series(game: dict[str, Any]) -> list[str]:
    """Series/colecciones útiles para relacionar fichas, excluyendo valores estructurales."""
    return [v for v in list_values(game.get("serie")) if entity_key(v) not in RELATED_GENERIC_SERIES]


def build_related_indexes(games: list[dict[str, Any]]) -> dict[str, Any]:
    """Índices invertidos y firmas normalizadas para construir relacionados con bajo coste."""
    by_url: dict[str, dict[str, Any]] = {}
    signatures: dict[str, dict[str, set[str]]] = {}
    indexes: dict[str, dict[str, list[str]]] = {
        name: defaultdict(list) for name in (
            "titulo", "serie", "desarrollador", "genero", "plataforma",
            "distribuidor", "tags", "formato"
        )
    }
    for game in games:
        url = str(game.get("url", "")).strip()
        if not url or url in by_url:
            continue
        by_url[url] = game
        title_key = entity_key(text(game.get("titulo"), ""))
        if title_key:
            indexes["titulo"][title_key].append(url)

        signature = {
            "serie": {entity_key(v) for v in meaningful_series(game) if entity_key(v)},
            "desarrollador": {entity_key(v) for v in list_values(game.get("desarrollador")) if entity_key(v)},
            "genero": {entity_key(v) for v in list_values(game.get("genero")) if entity_key(v)},
            "plataforma": {entity_key(v) for v in list_values(game.get("plataforma")) if entity_key(v)},
            "distribuidor": {entity_key(v) for v in list_values(game.get("distribuidor")) if entity_key(v)},
            "tags": {entity_key(v) for v in list_values(game.get("tags")) if entity_key(v)},
            "formato": {entity_key(text(game.get("formato"), ""))} if entity_key(text(game.get("formato"), "")) else set(),
        }
        signatures[url] = signature
        for field, keys in signature.items():
            for key in keys:
                indexes[field][key].append(url)
    return {"by_url": by_url, "indexes": indexes, "signatures": signatures}


def indexed_candidates(related_index: dict[str, Any], field: str, keys: set[str]) -> list[dict[str, Any]]:
    urls: set[str] = set()
    field_index = related_index["indexes"][field]
    for key in keys:
        urls.update(field_index.get(key, []))
    by_url = related_index["by_url"]
    return [by_url[url] for url in urls if url in by_url]


def unique_title_games(candidates: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    """Prioriza variedad de títulos dentro de un bloque relacionado."""
    result: list[dict[str, Any]] = []
    seen_titles: set[str] = set()
    for candidate in candidates:
        title_key = entity_key(text(candidate.get("titulo"), ""))
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)
        result.append(candidate)
        if len(result) >= limit:
            break
    return result


def build_related_game_groups(game: dict[str, Any], related_index: dict[str, Any], limit: int = 4) -> list[dict[str, Any]]:
    """Construye bloques deterministas de navegación contextual para una ficha."""
    current_url = str(game.get("url", ""))
    used_urls = {current_url}
    groups: list[dict[str, Any]] = []
    indexes = related_index["indexes"]
    by_url = related_index["by_url"]
    signatures = related_index["signatures"]
    current_sig = signatures.get(current_url, {})

    # 1) Otras ediciones del mismo título: aquí sí interesa conservar variantes físicas.
    current_title = entity_key(text(game.get("titulo"), ""))
    editions = [
        by_url[url] for url in indexes["titulo"].get(current_title, [])
        if url not in used_urls and url in by_url
    ]
    editions.sort(key=lambda g: (entity_key(text(g.get("formato"), "")), entity_key(text(g.get("plataforma"), "")), str(g.get("url", ""))))
    if editions:
        selected = editions[:limit]
        groups.append({"kind":"editions", "title":"Otras ediciones de este juego", "games":selected})
        used_urls.update(str(g.get("url", "")) for g in selected)

    # 2) Serie o colección significativa.
    series_values = meaningful_series(game)
    if series_values:
        series_keys = current_sig.get("serie", set())
        ranked: list[tuple[int, str, dict[str, Any]]] = []
        for other in indexed_candidates(related_index, "serie", series_keys):
            other_url = str(other.get("url", ""))
            if other_url in used_urls:
                continue
            shared = series_keys & signatures.get(other_url, {}).get("serie", set())
            if shared:
                ranked.append((len(shared), entity_key(text(other.get("titulo"), "")), other))
        ranked.sort(key=lambda row: (-row[0], row[1], str(row[2].get("url", ""))))
        selected = unique_title_games([row[2] for row in ranked], limit)
        if selected:
            label = series_values[0] if len(series_values) == 1 else "la misma serie o colección"
            title = f"Más de {label}" if len(series_values) == 1 else "Misma serie o colección"
            groups.append({"kind":"series", "title":title, "games":selected})
            used_urls.update(str(g.get("url", "")) for g in selected)

    # 3) Mismo desarrollador, priorizando además géneros compartidos.
    developer_values = list_values(game.get("desarrollador"))
    developer_keys = current_sig.get("desarrollador", set())
    if developer_keys:
        genre_keys = current_sig.get("genero", set())
        ranked_dev: list[tuple[int, int, str, dict[str, Any]]] = []
        for other in indexed_candidates(related_index, "desarrollador", developer_keys):
            other_url = str(other.get("url", ""))
            if other_url in used_urls:
                continue
            other_sig = signatures.get(other_url, {})
            shared_dev = developer_keys & other_sig.get("desarrollador", set())
            if not shared_dev:
                continue
            shared_genres = genre_keys & other_sig.get("genero", set())
            ranked_dev.append((len(shared_dev), len(shared_genres), entity_key(text(other.get("titulo"), "")), other))
        ranked_dev.sort(key=lambda row: (-row[0], -row[1], row[2], str(row[3].get("url", ""))))
        selected = unique_title_games([row[3] for row in ranked_dev], limit)
        if selected:
            if len(developer_values) == 1:
                title = f"Otros juegos de {developer_values[0]}"
            else:
                title = "Otros juegos de los mismos desarrolladores"
            groups.append({"kind":"developer", "title":title, "games":selected})
            used_urls.update(str(g.get("url", "")) for g in selected)

    # 4) Relación semántica básica basada exclusivamente en datos catalogados.
    genre_keys = current_sig.get("genero", set())
    platform_keys = current_sig.get("plataforma", set())
    distributor_keys = current_sig.get("distribuidor", set())
    tag_keys = current_sig.get("tags", set())
    format_keys = current_sig.get("formato", set())
    format_key = next(iter(format_keys), "")

    candidate_urls: set[str] = set()
    for field, keys in (
        ("genero", genre_keys),
        ("plataforma", platform_keys),
        ("distribuidor", distributor_keys),
        ("tags", tag_keys),
        ("formato", {format_key} if format_key else set()),
    ):
        for key in keys:
            candidate_urls.update(indexes[field].get(key, []))

    ranked_similar: list[tuple[int, int, str, dict[str, Any]]] = []
    for other_url in candidate_urls:
        if other_url in used_urls or other_url not in by_url:
            continue
        other = by_url[other_url]
        other_sig = signatures.get(other_url, {})
        shared_genres = genre_keys & other_sig.get("genero", set())
        shared_platforms = platform_keys & other_sig.get("plataforma", set())
        shared_distributors = distributor_keys & other_sig.get("distribuidor", set())
        shared_tags = tag_keys & other_sig.get("tags", set())
        same_format = bool(format_key) and format_key in other_sig.get("formato", set())
        score = (5 * len(shared_genres)) + (2 * len(shared_platforms)) + (2 if same_format else 0) + (2 * len(shared_distributors)) + min(3, len(shared_tags))
        if score >= 5:
            ranked_similar.append((score, len(shared_genres), entity_key(text(other.get("titulo"), "")), other))
    ranked_similar.sort(key=lambda row: (-row[0], -row[1], row[2], str(row[3].get("url", ""))))
    selected = unique_title_games([row[3] for row in ranked_similar], limit)
    if selected:
        groups.append({"kind":"similar", "title":"Juegos relacionados", "games":selected})

    return groups


def related_groups_html(game: dict[str, Any], related_index: dict[str, Any], prefix: str = "") -> str:
    sections: list[str] = []
    for group in build_related_game_groups(game, related_index):
        cards = "\n".join(card(item, prefix) for item in group["games"])
        sections.append(
            f'<section class="related-section" data-related-kind="{h(group["kind"])}">'
            f'<div class="section-head"><h2>{h(group["title"])}</h2></div>'
            f'<div class="related-grid">{cards}</div>'
            f'</section>'
        )
    if not sections:
        return ""
    return '<section class="related-area" aria-label="Explorar juegos relacionados">' + "\n".join(sections) + '</section>'


def nav(active: str, prefix: str = "") -> str:
    items = [
        ("", "Inicio"),
        ("catalogo/", "Catálogo"),
        ("videojuegos-clasicos-pc.html", "PC clásico"),
        ("juegos-pc-big-box.html", "Big Box PC"),
        ("juegos-msdos.html", "MS-DOS"),
        ("series.html", "Series"),
        ("vender-videojuegos-pc-antiguos/", "Ofrecer juegos"),
        ("contacto.html", "Contacto"),
    ]
    links = []
    for href, label in items:
        is_active = (not href and active == "index.html") or href == active
        cls = ' class="active"' if is_active else ""
        target = home_href(prefix) if not href else prefix + href
        links.append(f'<a{cls} href="{target}">{label}</a>')
    links.append('<a href="https://www.instagram.com/pc_game_archive/" target="_blank" rel="noopener">Instagram</a>')
    return "\n".join(links)


def head(title: str, description: str, canonical: str, prefix: str = "", image: str | None = None, extra_jsonld: list[dict[str, Any]] | None = None, image_alt: str | None = None) -> str:
    image_url = image or abs_url(DEFAULT_BASE_URL, OG_IMAGE)
    canonical_js = json.dumps(canonical, ensure_ascii=False)
    jsonld = ""
    for obj in extra_jsonld or []:
        jsonld += f'\n<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False, separators=(",", ":"))}</script>'
    image_alt_meta = ""
    if image_alt:
        image_alt_meta = f'\n<meta property="og:image:alt" content="{h(image_alt)}" />\n<meta name="twitter:image:alt" content="{h(image_alt)}" />'
    return f'''<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{h(title)}</title>
<meta name="description" content="{h(description)}" />
<meta name="robots" content="index,follow,max-image-preview:large" />
<meta name="theme-color" content="#111111" />
<link rel="canonical" href="{h(canonical)}" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="{SITE_NAME}" />
<meta property="og:title" content="{h(title)}" />
<meta property="og:description" content="{h(description)}" />
<meta property="og:url" content="{h(canonical)}" />
<meta property="og:image" content="{h(image_url)}" />{image_alt_meta}
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
<script>
(function(){{
  if(!/^https?:$/.test(location.protocol)) return;
  if(location.pathname.endsWith('/index.html')){{
    var cleanPath=location.pathname.slice(0,-'index.html'.length);
    location.replace(cleanPath+location.search+location.hash);
  }}
}})();
</script>
<script>
window.dataLayer=window.dataLayer||[];
function gtag(){{dataLayer.push(arguments);}}
window.PCGA_ANALYTICS_ENABLED=!['localhost','127.0.0.1','[::1]','::1'].includes(String(location.hostname||'').toLowerCase());
if(window.PCGA_ANALYTICS_ENABLED){{
  var gaScript=document.createElement('script');
  gaScript.async=true;
  gaScript.src='https://www.googletagmanager.com/gtag/js?id={GA_ID}';
  document.head.appendChild(gaScript);
}}
(function(){{
  var campaignKeys=['utm_source','utm_medium','utm_campaign','utm_term','utm_content','utm_id','gclid','gbraid','wbraid','dclid'];
  var current=new URLSearchParams(location.search);
  var tracking=new URLSearchParams();
  var attribution={{}};
  campaignKeys.forEach(function(key){{
    var value=current.get(key);
    if(value){{
      tracking.set(key,value);
      attribution[key]=value;
    }}
  }});
  try{{
    if(Object.keys(attribution).length){{
      sessionStorage.setItem('pcga_campaign_attribution',JSON.stringify(attribution));
    }}
    window.pcgaCampaignAttribution=function(){{
      try{{return JSON.parse(sessionStorage.getItem('pcga_campaign_attribution')||'{{}}');}}catch(e){{return {{}};}}
    }};
  }}catch(e){{
    window.pcgaCampaignAttribution=function(){{return attribution;}};
  }}
  var canonical={canonical_js};
  window.PCGA_TRACKING_LOCATION=canonical+(tracking.toString()?'?'+tracking.toString():'');
}})();
if(window.PCGA_ANALYTICS_ENABLED){{
  gtag('js',new Date());
  gtag('config','{GA_ID}',{{page_location:window.PCGA_TRACKING_LOCATION}});
}}
</script>{jsonld}'''


def layout(title: str, description: str, canonical: str, active: str, body: str, prefix: str = "", subtitle: str = "Archivo físico de videojuegos de PC · Big Box · MS-DOS · Windows", image: str | None = None, jsonld: list[dict[str, Any]] | None = None, image_alt: str | None = None) -> str:
    return f'''<!doctype html>
<html lang="es">
<head>
{head(title, description, canonical, prefix, image, jsonld, image_alt)}
</head>
<body>
<header id="top">
  <div class="wrap header-row">
    <a class="brand" href="{home_href(prefix)}" aria-label="PC Game Archive">
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
  if(btn){{
    e.preventDefault();
    window.scrollTo({{top:0,behavior:'smooth'}});
    if(history.replaceState){{history.replaceState(null,'',location.pathname+location.search);}}
    return;
  }}

  var link=e.target.closest('a');
  if(!link || typeof gtag!=='function') return;

  if(link.matches('[data-game-link]')){{
    gtag('event','select_content',{{
      content_type:'game',
      content_id:link.getAttribute('data-game-id')||'game_unknown'
    }});
  }}

  var href=link.getAttribute('href')||'';
  var acquisition=link.getAttribute('data-acquisition-intent');
  if(acquisition){{
    var offerEvent={{
      intent:acquisition,
      channel:link.getAttribute('data-acquisition-channel')||'unknown',
      link_url:href,
      source_page:location.pathname
    }};

    // En enlaces mailto damos un margen breve al Google tag para procesar el
    // evento antes de abrir el cliente de correo. No duplicamos además el
    // evento como contact_click: offer_games_click es la acción de captación.
    if(href.indexOf('mailto:')===0){{
      e.preventDefault();
      var followed=false;
      var follow=function(){{
        if(followed) return;
        followed=true;
        location.href=href;
      }};
      offerEvent.event_callback=follow;
      offerEvent.event_timeout=900;
      gtag('event','offer_games_click',offerEvent);
      window.setTimeout(follow,1000);
      return;
    }}

    gtag('event','offer_games_click',offerEvent);
    return;
  }}

  if(href.indexOf('mailto:')===0){{
    gtag('event','contact_click',{{method:'email',link_url:href,source_page:location.pathname}});
  }} else if(href.indexOf('instagram.com/')!==-1){{
    gtag('event','outbound_social_click',{{platform:'instagram',link_url:href,source_page:location.pathname}});
  }}
}});
</script>
</body>
</html>
'''


def card(game: dict[str, Any], prefix: str = "") -> str:
    url = game_href(game, prefix)
    img = img_path(game)
    title = text(game.get("titulo"))
    game_id = str(game.get("url", "")).strip("/").split("/")[-1] or "game_unknown"
    fallback = "/no_disponible.png"
    tags = [game.get("formato", "")] + (game.get("plataforma") or [])[:2]
    tag_html = "".join(f'<span class="tag">{h(t)}</span>' for t in tags if t)
    image_alt = edition_image_label(game, kind="cover")
    return f'''<a class="game-card" href="{h(url)}" data-game-link data-game-id="{h(game_id)}">
  <img src="{h(img)}" alt="{h(image_alt)}" loading="lazy" decoding="async" width="420" height="315" onerror="this.onerror=null;this.src='{h(fallback)}';this.alt='Imagen no disponible';this.classList.add('missing')" />
  <span class="game-card-body">
    <strong>{h(title)}</strong>
    <small>{h(text(game.get('genero')))}</small>
    <span class="tagrow">{tag_html}</span>
  </span>
</a>'''


def taxonomy_link(kind: str, value: str, prefix: str = "") -> str:
    return f'{home_href(prefix)}?{kind}={quote(value)}'


def list_values(value: Any) -> list[str]:
    """Normaliza campos que históricamente pueden aparecer como string o lista."""
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return [str(v).strip() for v in value if str(v).strip()]
    raw = str(value).strip()
    return [raw] if raw else []


def entity_key(value: str) -> str:
    """Clave estable para agrupar diferencias solo tipográficas (acentos/caja)."""
    normalized = unicodedata.normalize("NFKD", str(value))
    normalized = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", normalized).strip().casefold()


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", str(value))
    normalized = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    normalized = normalized.casefold().replace("&", " y ")
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")
    return normalized or "sin-nombre"


def build_taxonomy_entities(games: list[dict[str, Any]], taxonomy: str) -> list[dict[str, Any]]:
    """Agrupa entidades del catálogo y fusiona variantes solo tipográficas."""
    cfg = TAXONOMIES[taxonomy]
    field = cfg["field"]
    grouped: dict[str, dict[str, Any]] = {}
    for game in games:
        # Evita contar dos veces una misma entidad dentro de una misma ficha.
        seen_in_game: set[str] = set()
        for value in list_values(game.get(field)):
            key = entity_key(value)
            if not key or key in seen_in_game:
                continue
            seen_in_game.add(key)
            entry = grouped.setdefault(key, {"variants": Counter(), "games": []})
            entry["variants"][value] += 1
            entry["games"].append(game)

    entities: list[dict[str, Any]] = []
    used_slugs: dict[str, str] = {}
    for key, data in grouped.items():
        # Preferimos la grafía más frecuente en el catálogo; empate: más descriptiva y estable.
        variants = data["variants"]
        name = sorted(variants, key=lambda v: (-variants[v], -len(v), v.casefold()))[0]
        route_slug = slugify(name)
        if route_slug in used_slugs and used_slugs[route_slug] != key:
            # Colisión real entre nombres distintos tras slugificar: sufijo determinista corto.
            suffix = hashlib.sha1(key.encode("utf-8")).hexdigest()[:6]
            route_slug = f"{route_slug}-{suffix}"
        used_slugs[route_slug] = key
        entities.append({
            "key": key,
            "name": name,
            "slug": route_slug,
            "count": len(data["games"]),
            "games": data["games"],
            "variants": sorted(variants),
        })
    return sorted(entities, key=lambda e: (-e["count"], e["name"].casefold()))


def taxonomy_coverage(games: list[dict[str, Any]], taxonomy: str) -> tuple[int, float]:
    """Devuelve fichas con dato y cobertura global del campo de una taxonomía."""
    if not games:
        return 0, 0.0
    field = TAXONOMIES[taxonomy]["field"]
    documented = sum(1 for game in games if list_values(game.get(field)))
    return documented, documented / len(games)


def taxonomy_is_publishable(games: list[dict[str, Any]], taxonomy: str, entities: list[dict[str, Any]] | None = None) -> bool:
    """Publica un hub solo cuando el campo tiene cobertura y alguna entidad útil."""
    cfg = TAXONOMIES[taxonomy]
    documented, _ = taxonomy_coverage(games, taxonomy)
    if documented < int(cfg.get("min_documented", 0)):
        return False
    entities = entities if entities is not None else build_taxonomy_entities(games, taxonomy)
    return any(entity["count"] >= cfg["min_count"] for entity in entities)


def build_taxonomy_lookup(games: list[dict[str, Any]]) -> dict[str, dict[str, dict[str, Any]]]:
    lookup: dict[str, dict[str, dict[str, Any]]] = {}
    for taxonomy, cfg in TAXONOMIES.items():
        entities = build_taxonomy_entities(games, taxonomy)
        if not taxonomy_is_publishable(games, taxonomy, entities):
            lookup[taxonomy] = {}
            continue
        lookup[taxonomy] = {
            e["key"]: e
            for e in entities
            if e["count"] >= cfg["min_count"]
        }
    return lookup


def entity_route(taxonomy: str, entity: dict[str, Any]) -> str:
    return TAXONOMY_ROUTE_OVERRIDES.get((taxonomy, entity["key"]), f'{taxonomy}/{entity["slug"]}/')


def entity_href(taxonomy: str, value: str, lookup: dict[str, dict[str, dict[str, Any]]], prefix: str = "") -> str | None:
    entity = lookup.get(taxonomy, {}).get(entity_key(value))
    if not entity:
        return None
    return prefix + entity_route(taxonomy, entity)


def entity_tag(taxonomy: str, value: str, lookup: dict[str, dict[str, dict[str, Any]]], prefix: str = "", css_class: str = "tag") -> str:
    href = entity_href(taxonomy, value, lookup, prefix)
    if href:
        return f'<a class="{h(css_class)}" href="{h(href)}">{h(value)}</a>'
    return f'<span class="{h(css_class)}">{h(value)}</span>'


def flatten_search_values(value: Any) -> list[str]:
    """Aplana valores JSON para construir el texto de búsqueda sin perder metadatos."""
    if value is None:
        return []
    if isinstance(value, dict):
        values: list[str] = []
        for item in value.values():
            values.extend(flatten_search_values(item))
        return values
    if isinstance(value, (list, tuple, set)):
        values: list[str] = []
        for item in value:
            values.extend(flatten_search_values(item))
        return values
    raw = str(value).strip()
    return [raw] if raw else []


def build_search_index(games: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Genera el índice de búsqueda global en cliente."""
    index: list[dict[str, Any]] = []
    searchable_fields = (
        "num", "titulo", "plataforma", "formato", "genero", "desarrollador",
        "distribuidor", "ean", "descripcion", "incluye", "serie", "tags", "proteccion",
        # Fase 10B: nuevos metadatos. Mientras estén vacíos no alteran el índice
        # generado; cuando se documenten pasan a formar parte de la búsqueda global.
        "anio", "mercado", "idioma", "soporte", "tipo_edicion",
    )
    for g in games:
        search_values: list[str] = []
        for field in searchable_fields:
            search_values.extend(flatten_search_values(g.get(field)))
        item = {
            "titulo": g.get("titulo", ""),
            "url": site_path(str(g.get("url", ""))),
            "formato": g.get("formato", ""),
            "serie": list_values(g.get("serie")),
            "genero": list_values(g.get("genero")),
            "plataforma": list_values(g.get("plataforma")),
            "desarrollador": list_values(g.get("desarrollador")),
            "distribuidor": list_values(g.get("distribuidor")),
            "search_text": " ".join(search_values),
        }
        # Mantiene compatibilidad byte a byte cuando los nuevos campos están
        # vacíos, pero expone sus valores al filtro de taxonomía cuando existen.
        anio = str(g.get("anio") or "").strip()
        if anio:
            item["anio"] = anio
        for field in ("mercado", "idioma", "soporte", "tipo_edicion"):
            values = list_values(g.get(field))
            if values:
                item[field] = values
        index.append(item)
    return index


def write_assets(out: Path, games: list[dict[str, Any]]) -> None:
    (out / "assets/css").mkdir(parents=True, exist_ok=True)
    (out / "assets/js").mkdir(parents=True, exist_ok=True)
    (out / "assets/css/styles.css").write_text(CSS, encoding="utf-8")
    search_index_js = "window.PCGA_SEARCH_INDEX=" + json.dumps(build_search_index(games), ensure_ascii=False, separators=(",", ":")) + ";\n"
    (out / "assets/js/search-index.js").write_text(search_index_js, encoding="utf-8")
    (out / "assets/js/catalogo.js").write_text(JS, encoding="utf-8")



def catalog_page_route(page_number: int) -> str:
    # URL canónica de una página del catálogo estático.
    return "catalogo/" if page_number <= 1 else f"catalogo/pagina/{page_number}/"


def pagination_numbers(current: int, total: int) -> list[int | None]:
    # Ventana compacta de páginas. None representa un separador visual.
    if total <= 9:
        return list(range(1, total + 1))
    keep = {1, 2, total - 1, total, current - 2, current - 1, current, current + 1, current + 2}
    values = sorted(n for n in keep if 1 <= n <= total)
    result: list[int | None] = []
    previous = 0
    for number in values:
        if previous and number - previous > 1:
            result.append(None)
        result.append(number)
        previous = number
    return result


def pagination_html(current: int, total: int) -> str:
    # Navegación mediante enlaces HTML reales, independiente de JavaScript.
    if total <= 1:
        return ""
    parts: list[str] = []
    if current > 1:
        parts.append(f'<a class="pagination-prev" href="{h(site_path(catalog_page_route(current - 1)))}" rel="prev">← Anterior</a>')
    for number in pagination_numbers(current, total):
        if number is None:
            parts.append('<span class="pagination-gap" aria-hidden="true">…</span>')
        elif number == current:
            parts.append(f'<span class="pagination-current" aria-current="page">{number}</span>')
        else:
            parts.append(f'<a href="{h(site_path(catalog_page_route(number)))}" aria-label="Página {number}">{number}</a>')
    if current < total:
        parts.append(f'<a class="pagination-next" href="{h(site_path(catalog_page_route(current + 1)))}" rel="next">Siguiente →</a>')
    return '<nav class="pagination" aria-label="Paginación del catálogo">' + "".join(parts) + '</nav>'


def catalog_breadcrumb_jsonld(base_url: str, page_number: int) -> dict[str, Any]:
    items = [
        {"@type":"ListItem","position":1,"name":"Inicio","item":abs_url(base_url, "")},
        {"@type":"ListItem","position":2,"name":"Catálogo","item":abs_url(base_url, "catalogo/")},
    ]
    if page_number > 1:
        items.append({"@type":"ListItem","position":3,"name":f"Página {page_number}","item":abs_url(base_url, catalog_page_route(page_number))})
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items}


def generate_catalog_pages(games: list[dict[str, Any]], out: Path, base_url: str) -> None:
    # Genera una serie paginada rastreable que complementa el scroll infinito de la portada.
    root = out / "catalogo"
    if root.exists():
        shutil.rmtree(root)
    total_games = len(games)
    total_pages = max(1, math.ceil(total_games / CATALOG_PAGE_SIZE))
    for page_number in range(1, total_pages + 1):
        start = (page_number - 1) * CATALOG_PAGE_SIZE
        end = min(start + CATALOG_PAGE_SIZE, total_games)
        page_games = games[start:end]
        route = catalog_page_route(page_number)
        prefix = rel_prefix_for(route + "index.html")
        cards = "\n".join(card(game, prefix) for game in page_games)
        page_suffix = "" if page_number == 1 else f" · Página {page_number}"
        title = f"Catálogo de videojuegos de PC{page_suffix} · {SITE_NAME}"
        description = truncate(
            f"Catálogo físico de videojuegos de PC de {SITE_NAME}{page_suffix.lower()}: Big Box, CD/DVD, Jewel Case, MS-DOS y Windows clásicos.",
            155,
        )
        breadcrumb_tail = "" if page_number == 1 else f" / <span>Página {page_number}</span>"
        pagination = pagination_html(page_number, total_pages)
        body = f'''<main class="wrap">
  <nav class="breadcrumbs"><a href="{home_href(prefix)}">Inicio</a> / <a href="{h(site_path('catalogo/'))}">Catálogo</a>{breadcrumb_tail}</nav>
  <div class="page-head">
    <p class="eyebrow">Catálogo completo · Página {page_number} de {total_pages}</p>
    <h1>Catálogo de videojuegos de PC{h(page_suffix)}</h1>
    <p class="lead">Explora el archivo mediante páginas HTML rastreables. Cada edición enlaza directamente con su ficha documental y esta navegación complementa el scroll infinito de la portada.</p>
  </div>
  <section>
    <div class="section-head"><h2>Ediciones documentadas</h2><a href="{home_href(prefix)}">Buscar y filtrar</a></div>
    <p class="count">Mostrando {start + 1}–{end} de {total_games} juegos.</p>
    <div class="grid cards">{cards}</div>
    {pagination}
  </section>
</main>'''
        jsonld = [
            organization_jsonld(base_url),
            collection_jsonld(base_url, route, f"Catálogo de videojuegos de PC{page_suffix}", description, page_games),
            catalog_breadcrumb_jsonld(base_url, page_number),
        ]
        target = out / route / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            layout(title, description, abs_url(base_url, route), "catalogo/", body, prefix=prefix, subtitle="Catálogo físico de videojuegos de PC", jsonld=jsonld),
            encoding="utf-8",
        )


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
    entity_hub_links = "\n".join(
        f'<a class="taxonomy-item" href="{h(taxonomy)}/"><strong>{h(cfg["label"])}</strong><small>Explorar por {h(cfg["singular"])}</small></a>'
        for taxonomy, cfg in TAXONOMIES.items()
        if taxonomy_is_publishable(games, taxonomy)
    )
    editorial_taxonomies = {"anos", "mercados", "idiomas", "soportes", "tipos-edicion"}
    has_editorial_taxonomies = any(taxonomy_is_publishable(games, taxonomy) for taxonomy in editorial_taxonomies)
    entity_hub_description = (
        "Explora desarrolladores, distribuidores, géneros, plataformas, formatos y, cuando existe cobertura suficiente, metadatos editoriales como mercado, idioma o soporte."
        if has_editorial_taxonomies
        else "Desarrolladores, distribuidores, géneros, plataformas y formatos enlazados directamente con las fichas documentales."
    )
    body = f'''<main>
<section class="hero-section">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Preservación · Coleccionismo · PC clásico</p>
      <h1>Archivo físico de videojuegos de PC</h1>
      <p class="lead">Catálogo documental de ediciones físicas para PC, con especial atención a Big Box, MS-DOS, Windows clásicos, distribución española y preservación del soporte original.</p>
      <form class="search-hero catalog-search catalog-search-advanced" action="./" method="get">
        <div class="search-query-row">
          <input name="q" placeholder="Buscar en todo el archivo…" aria-label="Buscar en todo el archivo">
        </div>
        <div class="search-filter-row">
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
        </div>
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
<section class="wrap seo-hub" id="explorar-entidades">
  <div class="section-head"><h2>Explorar por datos del catálogo</h2></div>
  <p class="count">{h(entity_hub_description)}</p>
  <div class="taxonomy-grid">{entity_hub_links}</div>
</section>
<section class="wrap acquisition-strip" aria-labelledby="acquisition-home-title">
  <div>
    <p class="eyebrow">Ayuda a ampliar el archivo</p>
    <h2 id="acquisition-home-title">¿Tienes videojuegos físicos de PC?</h2>
    <p>Compramos colecciones, lotes y juegos individuales y también aceptamos donaciones de material con interés documental.</p>
  </div>
  <a class="button" href="vender-videojuegos-pc-antiguos/">Vender o donar juegos</a>
</section>
<section class="wrap">
  <div class="section-head"><h2>Catálogo de juegos</h2><a href="catalogo/">Ver catálogo completo</a></div>
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
    jsonld = [organization_jsonld(base_url), {"@context":"https://schema.org","@type":"WebSite","name":SITE_NAME,"url":base_url.rstrip("/") + "/","inLanguage":"es","description":desc,"potentialAction":{"@type":"SearchAction","target":base_url.rstrip("/") + "/?q={search_term_string}","query-input":"required name=search_term_string"}}, collection_jsonld(base_url, "", "Archivo de videojuegos clásicos de PC", desc, games)]
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


def landing_distinct_count(games: list[dict[str, Any]], field: str) -> int:
    keys: set[str] = set()
    for game in games:
        for value in list_values(game.get(field)):
            key = entity_key(value)
            if key:
                keys.add(key)
    return len(keys)


def landing_top_entity_links(selected: list[dict[str, Any]], taxonomy: str, lookup: dict[str, dict[str, dict[str, Any]]], limit: int = 3) -> list[tuple[str, int, str]]:
    cfg = TAXONOMIES[taxonomy]
    field = cfg["field"]
    counts: Counter[str] = Counter()
    for game in selected:
        seen: set[str] = set()
        for value in list_values(game.get(field)):
            key = entity_key(value)
            if not key or key in seen:
                continue
            seen.add(key)
            if key in lookup.get(taxonomy, {}):
                counts[key] += 1

    result: list[tuple[str, int, str]] = []
    for key, count in counts.most_common():
        entity = lookup[taxonomy][key]
        result.append((entity["name"], count, "/" + entity_route(taxonomy, entity).lstrip("/")))
        if len(result) >= limit:
            break
    return result


def landing_explore_html(selected: list[dict[str, Any]], editorial: dict[str, Any], lookup: dict[str, dict[str, dict[str, Any]]]) -> str:
    items: list[str] = []
    seen_hrefs: set[str] = set()
    for taxonomy in editorial.get("explore_taxonomies", []):
        cfg = TAXONOMIES[taxonomy]
        for name, count, href in landing_top_entity_links(selected, taxonomy, lookup):
            if href in seen_hrefs:
                continue
            seen_hrefs.add(href)
            items.append(
                f'<a class="taxonomy-item" href="{h(href)}"><strong>{h(name)}</strong>'
                f'<small>{h(cfg["label"])} · {count} ediciones</small></a>'
            )
    return "\n".join(items)


def landing_breadcrumb_jsonld(base_url: str, page: dict[str, Any]) -> dict[str, Any]:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": abs_url(base_url, "")},
            {"@type": "ListItem", "position": 2, "name": page["h1"], "item": abs_url(base_url, page["filename"])},
        ],
    }


def generate_seo_landing_pages(games: list[dict[str, Any]], out: Path, base_url: str) -> None:
    taxonomy_lookup = build_taxonomy_lookup(games)
    for p in SEO_LANDING_PAGES:
        flt = p.get("filter", {})
        selected = [g for g in games if matches_landing(g, flt)]
        cards = "\n".join(card(g) for g in selected[:24])
        editorial = LANDING_EDITORIAL.get(p["filename"], {})
        related = "\n".join(
            f'<a class="taxonomy-item" href="/{h(x["filename"])}"><strong>{h(x["label"])}</strong><small>{h(x["h1"])}</small></a>'
            for x in SEO_LANDING_PAGES if x["filename"] != p["filename"]
        )
        explore = landing_explore_html(selected, editorial, taxonomy_lookup)
        data_attr = default_filter_attr(flt)

        paragraphs = "\n".join(f'<p>{h(paragraph)}</p>' for paragraph in editorial.get("paragraphs", []))
        secondary_paragraphs = "\n".join(f'<p>{h(paragraph)}</p>' for paragraph in editorial.get("secondary_paragraphs", []))
        intro_title = editorial.get("intro_title", "Archivo documental")
        secondary_title = editorial.get("secondary_title", "Explorar la colección")
        eyebrow = editorial.get("eyebrow", "Archivo documental")

        dev_count = landing_distinct_count(selected, "desarrollador")
        dist_count = landing_distinct_count(selected, "distribuidor")
        genre_count = landing_distinct_count(selected, "genero")

        body = f"""<main class="wrap">
  <nav class="breadcrumbs" aria-label="Migas de pan"><a href="/">Inicio</a> / <span>{h(p["h1"])}</span></nav>
  <div class="page-head">
    <p class="eyebrow">{h(eyebrow)}</p>
    <h1>{h(p["h1"])}</h1>
    <p class="lead">{h(p["lead"])}</p>
  </div>
  <section class="landing-stats" aria-label="Resumen del catálogo">
    <div class="landing-stat"><strong>{len(selected)}</strong><span>ediciones documentadas</span></div>
    <div class="landing-stat"><strong>{dev_count}</strong><span>desarrolladores</span></div>
    <div class="landing-stat"><strong>{dist_count}</strong><span>distribuidores</span></div>
    <div class="landing-stat"><strong>{genre_count}</strong><span>géneros y subgéneros</span></div>
  </section>
  <section class="content-card landing-editorial">
    <h2>{h(intro_title)}</h2>
    {paragraphs}
  </section>
  <section>
    <div class="section-head"><h2>Juegos documentados</h2><a href="/catalogo/">Ver catálogo completo</a></div>
    <form class="toolbar" action="/" method="get"><input name="q" placeholder="Buscar dentro del archivo…"><button>Buscar</button></form>
    <p class="count">{len(selected)} juegos encontrados.</p>
    <div class="grid cards" data-catalog-list{data_attr}>{cards}</div>
    <div class="load-sentinel" data-load-sentinel aria-hidden="true"></div>
  </section>
  <section class="content-card landing-editorial">
    <h2>{h(secondary_title)}</h2>
    {secondary_paragraphs}
  </section>
  <section class="text-section">
    <h2>Explorar esta colección</h2>
    <p>Algunas de las entidades con mayor presencia dentro de esta selección.</p>
    <div class="taxonomy-grid">{explore}</div>
  </section>
  <section class="text-section"><h2>Otras rutas del archivo</h2><div class="taxonomy-grid">{related}</div></section>
  <script src="assets/js/search-index.js"></script>
  <script src="assets/js/catalogo.js" defer></script>
</main>"""
        jsonld = [organization_jsonld(base_url), landing_breadcrumb_jsonld(base_url, p), collection_jsonld(base_url, p["filename"], p["h1"], p["description"], selected)]
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
  <form class="toolbar" action="./" method="get"><input name="q" placeholder="Filtrar catálogo…"><button>Buscar</button></form>
  <p class="count">{len(selected)} juegos encontrados.</p>
  <div class="grid cards" data-catalog-list data-default-formato="{h('Big Box') if filename == 'bigbox.html' else ''}">{cards}</div>
  <div class="load-sentinel" data-load-sentinel aria-hidden="true"></div>
  <script src="assets/js/search-index.js"></script>
  <script src="assets/js/catalogo.js" defer></script>
</main>'''
    jsonld = [organization_jsonld(base_url), collection_jsonld(base_url, filename, title, description, selected)]
    (out / filename).write_text(layout(title, description, abs_url(base_url, filename), filename, body, jsonld=jsonld), encoding="utf-8")


def taxonomy_breadcrumb_jsonld(base_url: str, taxonomy: str, entity: dict[str, Any] | None = None) -> dict[str, Any]:
    cfg = TAXONOMIES[taxonomy]
    items = [
        {"@type":"ListItem","position":1,"name":"Inicio","item":abs_url(base_url, "")},
        {"@type":"ListItem","position":2,"name":cfg["label"],"item":abs_url(base_url, f"{taxonomy}/")},
    ]
    if entity is not None:
        items.append({"@type":"ListItem","position":3,"name":entity["name"],"item":abs_url(base_url, entity_route(taxonomy, entity))})
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items}


def top_values(games: list[dict[str, Any]], field: str, limit: int = 4) -> list[str]:
    counter: Counter[str] = Counter()
    for game in games:
        seen: set[str] = set()
        for value in list_values(game.get(field)):
            key = entity_key(value)
            if key in seen:
                continue
            seen.add(key)
            counter[value] += 1
    return [name for name, _ in counter.most_common(limit)]


def readable_list(values: list[str]) -> str:
    if not values:
        return ""
    if len(values) == 1:
        return values[0]
    return ", ".join(values[:-1]) + " y " + values[-1]


def entity_context_text(entity: dict[str, Any]) -> str:
    games = entity["games"]
    formats = readable_list(top_values(games, "formato", 3))
    platforms = readable_list(top_values(games, "plataforma", 4))
    genres = readable_list(top_values(games, "genero", 4))
    parts = []
    if formats:
        parts.append(f"Los formatos físicos más representados en estas fichas son {formats}.")
    if platforms:
        parts.append(f"Entre las plataformas documentadas aparecen {platforms}.")
    if genres:
        parts.append(f"Entre los géneros con presencia en este conjunto figuran {genres}.")
    return " ".join(parts)


def taxonomy_entity_copy(taxonomy: str, entity: dict[str, Any]) -> tuple[str, str, str, str]:
    """Copy específico para que las nuevas taxonomías sean naturales y útiles."""
    name = entity["name"]
    count = entity["count"]
    cfg = TAXONOMIES[taxonomy]

    if taxonomy == "idiomas":
        if entity_key(name) == entity_key("Multilingüe"):
            h1 = "Juegos de PC multilingües"
        else:
            h1 = f"Juegos de PC en {name.casefold()}"
        title = f"{h1} · {SITE_NAME}"
        description = truncate(f"{count} ediciones físicas de juegos de PC con contenido documentado en {name}, catalogadas en {SITE_NAME}.", 155)
        lead = f"PC Game Archive reúne {count} ediciones físicas con {name} documentado como idioma de la edición."
        return title, h1, description, lead

    if taxonomy == "soportes":
        h1 = f"Juegos de PC en {name}"
        title = f"{h1} · {SITE_NAME}"
        description = truncate(f"{count} ediciones físicas de juegos de PC distribuidas en {name}, documentadas en {SITE_NAME}.", 155)
        lead = f"PC Game Archive reúne {count} ediciones físicas que incluyen {name} como soporte de distribución documentado."
        return title, h1, description, lead

    if taxonomy == "mercados":
        h1 = f"Ediciones de PC para {name}"
        title = f"{h1} · {SITE_NAME}"
        description = truncate(f"{count} ediciones físicas de videojuegos de PC destinadas al mercado de {name}, documentadas en {SITE_NAME}.", 155)
        lead = f"PC Game Archive reúne {count} ediciones físicas con {name} documentado como mercado o territorio comercial."
        return title, h1, description, lead

    if taxonomy == "anos":
        h1 = f"Juegos de PC de {name}"
        title = f"{h1} · {SITE_NAME}"
        description = truncate(f"{count} ediciones físicas de juegos de PC publicadas en {name}, documentadas en {SITE_NAME}.", 155)
        lead = f"PC Game Archive reúne {count} ediciones físicas cuyo año de publicación documentado es {name}."
        return title, h1, description, lead

    if taxonomy == "tipos-edicion":
        h1 = f"{name}: ediciones de juegos de PC"
        title = f"{h1} · {SITE_NAME}"
        description = truncate(f"{count} ediciones físicas de juegos de PC clasificadas como {name}, documentadas en {SITE_NAME}.", 155)
        lead = f"PC Game Archive reúne {count} ediciones físicas clasificadas como {name}."
        return title, h1, description, lead

    h1 = f"{name}: juegos de PC"
    title = f"{h1} · {SITE_NAME}"
    description = truncate(f"{count} ediciones físicas de videojuegos de PC relacionadas con {name}, documentadas en {SITE_NAME}.", 155)
    lead = f"PC Game Archive reúne {count} ediciones físicas del catálogo asociadas a {name} como {cfg['singular']}."
    return title, h1, description, lead


def taxonomy_hub_jsonld(base_url: str, taxonomy: str, entities: list[dict[str, Any]]) -> dict[str, Any]:
    cfg = TAXONOMIES[taxonomy]
    return {
        "@context":"https://schema.org",
        "@type":"CollectionPage",
        "name":f'{cfg["label"]} · {SITE_NAME}',
        "url":abs_url(base_url, f"{taxonomy}/"),
        "inLanguage":"es",
        "isPartOf":{"@type":"WebSite","name":SITE_NAME,"url":base_url.rstrip("/") + "/"},
        "mainEntity":{
            "@type":"ItemList",
            "numberOfItems":len(entities),
            "itemListElement":[
                {"@type":"ListItem","position":i+1,"name":entity["name"],"url":abs_url(base_url, entity_route(taxonomy, entity))}
                for i, entity in enumerate(entities)
            ],
        },
    }


def generate_taxonomy_pages(games: list[dict[str, Any]], out: Path, base_url: str) -> dict[str, list[dict[str, Any]]]:
    """Genera hubs y páginas SEO de entidades con suficiente representación en el catálogo."""
    generated: dict[str, list[dict[str, Any]]] = {}
    for taxonomy, cfg in TAXONOMIES.items():
        root = out / taxonomy
        if root.exists():
            shutil.rmtree(root)

        all_entities = build_taxonomy_entities(games, taxonomy)
        if not taxonomy_is_publishable(games, taxonomy, all_entities):
            generated[taxonomy] = []
            continue

        root.mkdir(parents=True, exist_ok=True)
        entities = [e for e in all_entities if e["count"] >= cfg["min_count"]]
        generated[taxonomy] = entities
        hub_prefix = "../"
        hub_items = "\n".join(
            f'<a class="taxonomy-item" href="{h(hub_prefix + entity_route(taxonomy, entity))}"><strong>{h(entity["name"])}</strong><small>{entity["count"]} juegos</small></a>'
            for entity in entities
        )
        hub_title = f'{cfg["label"]} de videojuegos de PC · {SITE_NAME}'
        hub_desc = truncate(f'Explora {cfg["label"].lower()} presentes en las ediciones físicas documentadas por {SITE_NAME}. Índice conectado con las fichas del archivo.', 155)
        hub_body = f'''<main class="wrap">
  <nav class="breadcrumbs"><a href="{hub_prefix}">Inicio</a> / <span>{h(cfg["label"])}</span></nav>
  <div class="page-head">
    <p class="eyebrow">Explorar el catálogo</p>
    <h1>{h(cfg["label"])}</h1>
    <p class="lead">Índice de {h(cfg["label"].lower())} presentes en PC Game Archive. Se muestran entidades con al menos {cfg["min_count"]} fichas documentadas y solo se publica el índice cuando el campo dispone de masa crítica suficiente.</p>
  </div>
  <p class="count">{len(entities)} entidades disponibles.</p>
  <div class="taxonomy-grid">{hub_items}</div>
</main>'''
        hub_page = layout(
            hub_title,
            hub_desc,
            abs_url(base_url, f"{taxonomy}/"),
            "",
            hub_body,
            prefix=hub_prefix,
            subtitle=f'Índice de {cfg["label"].lower()}',
            jsonld=[organization_jsonld(base_url), taxonomy_hub_jsonld(base_url, taxonomy, entities), taxonomy_breadcrumb_jsonld(base_url, taxonomy)],
        )
        (root / "index.html").write_text(hub_page, encoding="utf-8")

        for entity in entities:
            # Las landings editoriales existentes son el destino canónico de estas entidades.
            if (taxonomy, entity["key"]) in TAXONOMY_ROUTE_OVERRIDES:
                continue
            selected = entity["games"]
            entity_prefix = "../../"
            cards = "\n".join(card(game, entity_prefix) for game in selected[:24])
            context = entity_context_text(entity)
            values_attr = "|".join(entity["variants"])
            title, entity_h1, description, lead = taxonomy_entity_copy(taxonomy, entity)
            related = [e for e in entities if e["key"] != entity["key"]][:8]
            related_html = "\n".join(
                f'<a class="taxonomy-item" href="{h(entity_prefix + entity_route(taxonomy, other))}"><strong>{h(other["name"])}</strong><small>{other["count"]} juegos</small></a>'
                for other in related
            )
            entity_body = f'''<main class="wrap">
  <nav class="breadcrumbs"><a href="{entity_prefix}">Inicio</a> / <a href="{entity_prefix}{taxonomy}/">{h(cfg["label"])}</a> / <span>{h(entity["name"])}</span></nav>
  <div class="page-head">
    <p class="eyebrow">{h(cfg["eyebrow"])}</p>
    <h1>{h(entity_h1)}</h1>
    <p class="lead">{h(lead)}</p>
  </div>
  <section class="content-card">
    <h2>Presencia en el archivo</h2>
    <p>{h(context or 'Esta página agrupa las ediciones físicas relacionadas con esta entidad dentro del catálogo documental.')}</p>
  </section>
  <section>
    <div class="section-head"><h2>Ediciones documentadas</h2><a href="{entity_prefix}{taxonomy}/">Ver {h(cfg["label"].lower())}</a></div>
    <form class="toolbar" action="./" method="get"><input name="q" placeholder="Filtrar dentro de {h(entity['name'])}…"><button>Buscar</button></form>
    <p class="count">{len(selected)} juegos encontrados.</p>
    <div class="grid cards" data-catalog-list data-default-taxonomy="{h(cfg['field'])}" data-default-taxonomy-values="{h(values_attr)}">{cards}</div>
    <div class="load-sentinel" data-load-sentinel aria-hidden="true"></div>
  </section>
  <section class="text-section"><h2>Explorar otros {h(cfg["label"].lower())}</h2><div class="taxonomy-grid">{related_html}</div></section>
  <script src="{entity_prefix}assets/js/search-index.js"></script>
  <script src="{entity_prefix}assets/js/catalogo.js" defer></script>
</main>'''
            page = layout(
                title,
                description,
                abs_url(base_url, entity_route(taxonomy, entity)),
                "",
                entity_body,
                prefix=entity_prefix,
                subtitle=f'{cfg["label"]} · Archivo documental',
                jsonld=[organization_jsonld(base_url), collection_jsonld(base_url, entity_route(taxonomy, entity), f'{entity["name"]}: juegos de PC', description, selected), taxonomy_breadcrumb_jsonld(base_url, taxonomy, entity)],
            )
            target = root / entity["slug"] / "index.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(page, encoding="utf-8")
    return generated


def generate_series(games: list[dict[str, Any]], out: Path, base_url: str) -> None:
    counter = Counter()
    for g in games:
        for s in g.get("serie") or []:
            counter[s] += 1
    items = "\n".join(
        f'<a class="taxonomy-item" href="./?serie={quote(name)}"><strong>{h(name)}</strong><small>{count} juegos</small></a>'
        for name, count in sorted(counter.items(), key=lambda x: (-x[1], x[0].lower()))
    )
    title = "Series y colecciones · PC Game Archive"
    desc = "Explora las series, formatos y colecciones documentadas en PC Game Archive."
    body = f'''<main class="wrap">
  <div class="page-head"><p class="eyebrow">Exploración temática</p><h1>Series y colecciones</h1><p>{h(desc)}</p></div>
  <div class="taxonomy-grid">{items}</div>
</main>'''
    (out / "series.html").write_text(layout(title, desc, abs_url(base_url, "series.html"), "series.html", body), encoding="utf-8")


def acquisition_breadcrumb_jsonld(base_url: str) -> dict[str, Any]:
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Inicio","item":abs_url(base_url, "")},
        {"@type":"ListItem","position":2,"name":"Vender o donar videojuegos de PC","item":abs_url(base_url, "vender-videojuegos-pc-antiguos/")},
    ]}


def generate_acquisition_landing(out: Path, base_url: str) -> None:
    route = "vender-videojuegos-pc-antiguos/"
    title = "Vender o donar videojuegos antiguos de PC · PC Game Archive"
    desc = "Compra y donación de videojuegos antiguos de PC: Big Box, CD-ROM, DVD, Jewel Case, disquetes, manuales y colecciones. Contacta con PC Game Archive."
    prefix = "../"
    sell_mail = "mailto:contacto@pcgamearchive.org?subject=Quiero%20vender%20videojuegos%20de%20PC"
    donate_mail = "mailto:contacto@pcgamearchive.org?subject=Quiero%20donar%20videojuegos%20de%20PC"
    general_mail = "mailto:contacto@pcgamearchive.org?subject=Consulta%20sobre%20videojuegos%20para%20PC%20Game%20Archive"
    body = f'''<main>
<section class="acquisition-hero">
  <div class="wrap acquisition-hero-grid">
    <div>
      <nav class="breadcrumbs" aria-label="Migas de pan"><a href="../">Inicio</a> / <span>Ofrecer juegos</span></nav>
      <p class="eyebrow">Compramos · Recibimos donaciones · Preservamos</p>
      <h1>¿Tienes videojuegos antiguos de PC?</h1>
      <p class="lead">PC Game Archive busca ediciones físicas para ampliar y documentar el archivo. Compramos colecciones, lotes y juegos individuales y también aceptamos donaciones.</p>
      <div class="actions acquisition-actions">
        <a class="button" href="{sell_mail}" data-acquisition-intent="sell" data-acquisition-channel="email">Quiero vender juegos</a>
        <a class="button button-secondary" href="{donate_mail}" data-acquisition-intent="donate" data-acquisition-channel="email">Quiero donar material</a>
      </div>
    </div>
    <figure class="acquisition-visual">
      <img src="/anuncio_with_bgc.png" alt="PC Game Archive busca videojuegos clásicos de PC para preservar y documentar" width="1080" height="1080" loading="eager" fetchpriority="high">
    </figure>
  </div>
</section>
<section class="wrap acquisition-section">
  <div class="section-head"><h2>Qué material buscamos</h2></div>
  <div class="acquisition-grid">
    <article class="content-card"><h3>Ediciones físicas</h3><p>Big Box, CD-ROM, DVD, Jewel Case y juegos distribuidos en disquete.</p></article>
    <article class="content-card"><h3>Documentación</h3><p>Manuales, mapas, guías, referencias rápidas, catálogos y otros elementos originales de la edición.</p></article>
    <article class="content-card"><h3>Material promocional</h3><p>Folletos, press kits, material de distribuidor y otros documentos relacionados con la publicación del juego.</p></article>
    <article class="content-card"><h3>Ediciones españolas y europeas</h3><p>Nos interesan especialmente las variantes distribuidas en España y Europa, aunque puedes consultarnos por cualquier edición física de PC.</p></article>
  </div>
  <p class="acquisition-note"><strong>No tiene que estar todo completo.</strong> Una caja, un manual, un disco o un lote parcial también puede tener interés documental para el archivo.</p>
</section>
<section class="acquisition-soft">
  <div class="wrap acquisition-section">
    <div class="section-head"><h2>Cómo funciona</h2></div>
    <ol class="acquisition-steps">
      <li><strong>Cuéntanos qué tienes.</strong><span>Puede ser una colección completa, un lote o unos pocos juegos.</span></li>
      <li><strong>Envíanos fotos o una lista.</strong><span>Con unas imágenes generales y los títulos podemos hacer una primera revisión.</span></li>
      <li><strong>Revisamos el material.</strong><span>Valoramos su interés para el archivo y te indicamos si podemos adquirirlo o incorporarlo como donación.</span></li>
      <li><strong>Acordamos los siguientes pasos.</strong><span>Si seguimos adelante, concretamos contigo la forma de entrega o envío.</span></li>
    </ol>
  </div>
</section>
<section class="wrap acquisition-section">
  <div class="acquisition-contact-card">
    <div>
      <p class="eyebrow">Contacto directo</p>
      <h2>¿Quieres ofrecernos una colección o un juego?</h2>
      <p>Escríbenos indicando, si puedes, qué títulos tienes y adjunta algunas fotografías. No hace falta preparar un inventario perfecto antes de contactar.</p>
    </div>
    <div class="actions acquisition-actions">
      <a class="button" href="{general_mail}" data-acquisition-intent="general" data-acquisition-channel="email">contacto@pcgamearchive.org</a>
      <a class="button button-secondary" href="https://www.instagram.com/pc_game_archive/" target="_blank" rel="noopener" data-acquisition-intent="general" data-acquisition-channel="instagram">@pc_game_archive</a>
    </div>
  </div>
</section>
<section class="wrap acquisition-section acquisition-faq" aria-labelledby="faq-title">
  <div class="section-head"><h2 id="faq-title">Preguntas habituales</h2></div>
  <details><summary>¿Solo os interesan colecciones grandes?</summary><p>No. Puedes contactar aunque tengas un único juego o unos pocos títulos.</p></details>
  <details><summary>¿Aceptáis material incompleto?</summary><p>Sí. Cajas, manuales, discos, disquetes y otros elementos sueltos pueden tener valor documental aunque la edición no esté completa.</p></details>
  <details><summary>¿Compráis y también aceptáis donaciones?</summary><p>Sí. Estudiamos ambas opciones en función del material y de lo que prefiera la persona que contacta.</p></details>
  <details><summary>¿Puedo contactar aunque no sepa exactamente qué edición tengo?</summary><p>Sí. Unas fotografías de la portada, trasera y contenido suelen ser suficientes para comenzar a identificarla.</p></details>
</section>
</main>'''
    jsonld = [
        organization_jsonld(base_url),
        acquisition_breadcrumb_jsonld(base_url),
        {"@context":"https://schema.org","@type":"WebPage","name":"Vender o donar videojuegos antiguos de PC","url":abs_url(base_url, route),"description":desc,"inLanguage":"es","about":{"@type":"Thing","name":"Videojuegos físicos de PC"}},
    ]
    target = out / route / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        layout(title, desc, abs_url(base_url, route), route, body, prefix=prefix, subtitle="Preservación de videojuegos físicos de PC", image=abs_url(base_url, "anuncio_with_bgc.png"), jsonld=jsonld, image_alt="PC Game Archive busca videojuegos clásicos de PC para preservar y documentar"),
        encoding="utf-8",
    )


def generate_contact(out: Path, base_url: str) -> None:
    title = "Contacto · PC Game Archive"
    desc = "Contacto de PC Game Archive para correcciones, aportaciones documentales y propuestas sobre videojuegos físicos de PC."
    body = '''<main class="wrap">
  <article class="content-card">
    <h1>Contacto</h1>
    <p><strong>PC Game Archive</strong> es un proyecto dedicado a la preservación y documentación de videojuegos de PC en formato físico, con especial atención a ediciones clásicas de MS-DOS y Windows, Big Box, manuales, discos, disquetes y distribución española.</p>
    <p>Para proponer correcciones del catálogo, aportar información adicional sobre una edición concreta o compartir documentación relacionada con algún título, puedes usar estos canales.</p>
    <p>Si quieres <strong>vender o donar videojuegos físicos de PC</strong>, consulta primero nuestra página de <a href="vender-videojuegos-pc-antiguos/">ofrecimiento de juegos y colecciones</a>.</p>
    <dl class="kv"><dt>Email</dt><dd><a href="mailto:contacto@pcgamearchive.org">contacto@pcgamearchive.org</a></dd><dt>Instagram</dt><dd><a href="https://www.instagram.com/pc_game_archive/" target="_blank" rel="noopener">@pc_game_archive</a></dd></dl>
  </article>
</main>'''
    (out / "contacto.html").write_text(layout(title, desc, abs_url(base_url, "contacto.html"), "contacto.html", body), encoding="utf-8")


def game_jsonld(game: dict[str, Any], base_url: str, image_path: str | None = None) -> dict[str, Any]:
    url = abs_url(base_url, game.get("url", ""))
    obj = {
        "@context": "https://schema.org",
        "@type": "VideoGame",
        "@id": url + "#videogame",
        "name": text(game.get("titulo")),
        "url": url,
        "mainEntityOfPage": url,
        "description": truncate(text(game.get("descripcion"), ""), 500),
        "gamePlatform": list_values(game.get("plataforma")),
        "genre": list_values(game.get("genero")),
        "author": [{"@type":"Organization","name": v} for v in list_values(game.get("desarrollador"))],
        "publisher": [{"@type":"Organization","name": v} for v in list_values(game.get("distribuidor"))],
    }
    if image_path:
        obj["image"] = image_object_jsonld(game, base_url, image_path)
    if game.get("ean"):
        obj["gtin"] = game.get("ean")

    # Fase 10B: los nuevos campos del modelo solo enriquecen el JSON-LD cuando
    # están documentados. Con valores vacíos la salida permanece idéntica.
    anio = str(game.get("anio") or "").strip()
    idiomas = list_values(game.get("idioma"))
    if anio:
        obj["datePublished"] = anio
    if idiomas:
        obj["inLanguage"] = idiomas
    return obj


def game_page_jsonld(game: dict[str, Any], base_url: str, image_path: str | None = None) -> dict[str, Any]:
    url = abs_url(base_url, game.get("url", ""))
    obj: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": text(game.get("titulo")),
        "inLanguage": "es",
        "mainEntity": {"@id": url + "#videogame"},
    }
    if image_path:
        obj["primaryImageOfPage"] = image_object_jsonld(game, base_url, image_path)
    return obj

def breadcrumb_jsonld(game: dict[str, Any], base_url: str, taxonomy_lookup: dict[str, dict[str, dict[str, Any]]]) -> dict[str, Any]:
    format_value = text(game.get("formato"), "Catálogo")
    format_entity = taxonomy_lookup.get("formatos", {}).get(entity_key(format_value))
    format_path = entity_route("formatos", format_entity) if format_entity else ""
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Inicio","item":abs_url(base_url,"")},
        {"@type":"ListItem","position":2,"name":format_value,"item":abs_url(base_url,format_path)},
        {"@type":"ListItem","position":3,"name":text(game.get("titulo")),"item":abs_url(base_url,game.get("url",""))},
    ]}


def generate_game_pages(games: list[dict[str, Any]], out: Path, project_root: Path, base_url: str, gallery_index: dict[str, list[str]] | None = None) -> None:
    url_counts = Counter(g.get("url") for g in games)
    taxonomy_lookup = build_taxonomy_lookup(games)
    related_index = build_related_indexes(games)
    gallery_index = gallery_index or build_gallery_index(project_root, games)
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
        gallery = gallery_index.get(url, [])
        primary_image_path = gallery[0] if gallery else None
        hero_path = primary_image_path or "/no_disponible.png"
        hero = hero_path
        hero_alt = edition_image_label(game) if primary_image_path else f"Imagen no disponible de {title}"
        hero_caption = edition_image_caption(game) if primary_image_path else f"{title} · imagen documental pendiente"
        chip_parts: list[str] = []
        if game.get("formato"):
            chip_parts.append(entity_tag("formatos", str(game.get("formato")), taxonomy_lookup, prefix, "chip"))
        chip_parts.extend(entity_tag("plataformas", p, taxonomy_lookup, prefix, "chip") for p in list_values(game.get("plataforma")))
        chip_parts.extend(f'<a class="chip" href="{h(taxonomy_link("serie", s, prefix))}">{h(s)}</a>' for s in list_values(game.get("serie"))[:3])
        chip_html = "".join(chip_parts)
        gallery_items: list[str] = []
        total_gallery = len(gallery)
        for image_number, src in enumerate(gallery, start=1):
            alt = edition_image_label(game, kind="gallery", position=image_number)
            caption = f"Imagen documental {image_number} de {total_gallery}"
            gallery_items.append(
                f'<figure class="gallery-item"><a class="gallery-link" href="{h(src)}" target="_blank" rel="noopener" aria-label="Abrir imagen documental {image_number} de {h(title)} a tamaño completo">'
                f'<img src="{h(src)}" alt="{h(alt)}" loading="lazy" decoding="async" width="480" height="360" onerror="this.closest(\'figure\').remove()"></a>'
                f'<figcaption>{h(caption)}</figcaption></figure>'
            )
        gallery_html = "\n".join(gallery_items)
        if not gallery_html:
            gallery_html = f'<figure class="gallery-item gallery-missing"><img src="/no_disponible.png" alt="{h("Imágenes no disponibles de " + title)}" loading="lazy" decoding="async" width="480" height="360"><figcaption>Galería pendiente de documentación</figcaption></figure>'
        format_link = entity_tag("formatos", text(game.get("formato"), ""), taxonomy_lookup, prefix) if text(game.get("formato"), "") else "—"
        platform_links = " ".join(entity_tag("plataformas", p, taxonomy_lookup, prefix) for p in list_values(game.get("plataforma")))
        genre_links = " ".join(entity_tag("generos", g, taxonomy_lookup, prefix) for g in list_values(game.get("genero")))
        serie_links = " ".join(f'<a class="tag" href="{h(taxonomy_link("serie", s, prefix))}">{h(s)}</a>' for s in list_values(game.get("serie")))
        developer_links = " ".join(entity_tag("desarrolladores", d, taxonomy_lookup, prefix) for d in list_values(game.get("desarrollador"))) or "—"
        distributor_links = " ".join(entity_tag("distribuidores", d, taxonomy_lookup, prefix) for d in list_values(game.get("distribuidor"))) or "—"
        format_value = text(game.get("formato"), "Catálogo")
        format_href = entity_href("formatos", format_value, taxonomy_lookup, prefix) or home_href(prefix)
        ig = game.get("ig") or ""
        ig_btn = f'<a class="button" href="{h(ig)}" target="_blank" rel="noopener">Ver publicación en Instagram</a>' if ig else ""
        prot = game.get("proteccion") if isinstance(game.get("proteccion"), dict) else {}

        # Fase 10B: metadatos editoriales nuevos. Todos son obligatorios en el
        # schema, pero se admiten vacíos. Por eso las filas solo aparecen cuando
        # hay información real y no cambian visualmente las fichas actuales.
        extra_metadata_rows: list[str] = []
        anio = str(game.get("anio") or "").strip()
        mercado_values = list_values(game.get("mercado"))
        idioma_values = list_values(game.get("idioma"))
        soporte_values = list_values(game.get("soporte"))
        tipo_edicion_values = list_values(game.get("tipo_edicion"))
        if anio:
            extra_metadata_rows.append(f'<dt>Año</dt><dd class="tagrow">{entity_tag("anos", anio, taxonomy_lookup, prefix)}</dd>')
        if mercado_values:
            extra_metadata_rows.append('<dt>Mercado</dt><dd class="tagrow">' + ''.join(entity_tag("mercados", v, taxonomy_lookup, prefix) for v in mercado_values) + '</dd>')
        if idioma_values:
            extra_metadata_rows.append('<dt>Idioma</dt><dd class="tagrow">' + ''.join(entity_tag("idiomas", v, taxonomy_lookup, prefix) for v in idioma_values) + '</dd>')
        if soporte_values:
            extra_metadata_rows.append('<dt>Soporte</dt><dd class="tagrow">' + ''.join(entity_tag("soportes", v, taxonomy_lookup, prefix) for v in soporte_values) + '</dd>')
        if tipo_edicion_values:
            extra_metadata_rows.append('<dt>Tipo de edición</dt><dd class="tagrow">' + ''.join(entity_tag("tipos-edicion", v, taxonomy_lookup, prefix) for v in tipo_edicion_values) + '</dd>')
        extra_metadata_html = ''.join(extra_metadata_rows)

        related_html = related_groups_html(game, related_index, prefix)
        body = f'''<main class="wrap game-detail">
  <nav class="breadcrumbs"><a href="{home_href(prefix)}">Inicio</a> / <a href="{h(format_href)}">{h(format_value)}</a> / <span>{h(title)}</span></nav>
  <article class="detail-grid">
    <section class="media-card">
      <figure class="hero-figure">
        <img class="hero-img" src="{h(hero)}" alt="{h(hero_alt)}" width="760" height="570" loading="eager" fetchpriority="high" onerror="this.onerror=null;this.src='/no_disponible.png';this.alt='Imagen no disponible';this.classList.add('missing')">
        <figcaption>{h(hero_caption)}</figcaption>
      </figure>
      <div class="chips">{chip_html}</div>
      <div class="actions"><a class="button" href="{home_href(prefix)}">Volver al catálogo</a>{ig_btn}</div>
    </section>
    <section class="content-card">
      <p class="eyebrow">Ficha #{h(game.get('num') or '000000')}</p>
      <h1>{h(title)}</h1>
      <p class="lead">{h(text(game.get('descripcion')))}</p>
      <dl class="kv">
        <dt>Formato</dt><dd class="tagrow">{format_link}</dd>
        <dt>Plataforma</dt><dd class="tagrow">{platform_links}</dd>
        <dt>Género</dt><dd class="tagrow">{genre_links}</dd>
        <dt>Serie</dt><dd class="tagrow">{serie_links}</dd>
        <dt>Desarrollador</dt><dd class="tagrow">{developer_links}</dd>
        <dt>Distribuidor</dt><dd class="tagrow">{distributor_links}</dd>
        <dt>EAN</dt><dd>{h(text(game.get('ean')))}</dd>{extra_metadata_html}
      </dl>
      <h2>Contenido de la edición</h2>
      <ul>{''.join(f'<li>{h(x)}</li>' for x in (game.get('incluye') or [])) or '<li>Pendiente de documentación.</li>'}</ul>
      <h2>Preservación</h2>
      <dl class="kv compact"><dt>Protección</dt><dd>{h(text(prot.get('tipo')))}</dd><dt>Formato recomendado</dt><dd>{h(text(prot.get('formato')))}</dd><dt>Jugable en virtualización</dt><dd>{'Sí' if prot.get('jugable_virtual') else 'No determinado'}</dd></dl>
      <p>{h(text(prot.get('preservacion'), 'Pendiente de documentación.'))}</p>
    </section>
  </article>
  <section class="content-card"><h2>Galería documental</h2><div class="gallery">{gallery_html}</div></section>
  {related_html}
</main>'''
        page = layout(
            page_title, desc, abs_url(base_url, url), "", body, prefix=prefix, subtitle="Ficha documental",
            image=abs_url(base_url, hero_path),
            jsonld=[game_page_jsonld(game, base_url, primary_image_path), game_jsonld(game, base_url, primary_image_path), breadcrumb_jsonld(game, base_url, taxonomy_lookup)],
            image_alt=hero_alt,
        )
        target = out / url / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page, encoding="utf-8")


def generate_sitemap(games: list[dict[str, Any]], out: Path, base_url: str, gallery_index: dict[str, list[str]] | None = None) -> None:
    urls = ["", "series.html", "contacto.html", "vender-videojuegos-pc-antiguos/"] + [p["filename"] for p in SEO_LANDING_PAGES]
    seen = set(urls)
    total_catalog_pages = max(1, math.ceil(len(games) / CATALOG_PAGE_SIZE))
    for page_number in range(1, total_catalog_pages + 1):
        route = catalog_page_route(page_number)
        if route not in seen:
            urls.append(route)
            seen.add(route)
    for taxonomy, cfg in TAXONOMIES.items():
        entities = build_taxonomy_entities(games, taxonomy)
        if not taxonomy_is_publishable(games, taxonomy, entities):
            continue
        hub = f"{taxonomy}/"
        if hub not in seen:
            urls.append(hub)
            seen.add(hub)
        for entity in entities:
            if entity["count"] < cfg["min_count"]:
                continue
            route = entity_route(taxonomy, entity)
            if route not in seen:
                urls.append(route)
                seen.add(route)
    for g in games:
        url = g.get("url")
        if isinstance(url, str) and re.match(r"^juegos/[a-z0-9\-]+/$", url) and url not in seen:
            urls.append(url)
            seen.add(url)
    gallery_index = gallery_index or {}
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
    ]
    for u in urls:
        loc = abs_url(base_url, u)
        images = gallery_index.get(u, []) if isinstance(u, str) and u.startswith("juegos/") else []
        if images:
            lines.append("  <url>")
            lines.append(f"    <loc>{h(loc)}</loc>")
            for image_path in images[:1000]:
                lines.append("    <image:image>")
                lines.append(f"      <image:loc>{h(abs_url(base_url, image_path))}</image:loc>")
                lines.append("    </image:image>")
            lines.append("  </url>")
        else:
            lines.append(f"  <url><loc>{h(loc)}</loc></url>")
    lines.append("</urlset>")
    (out / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate_robots(out: Path, base_url: str) -> None:
    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {base_url.rstrip('/')}/sitemap.xml\n", encoding="utf-8")


def generate_static_redirect(out: Path, base_url: str, filename: str, target: str, title: str) -> None:
    """Genera una redirección permanente compatible con hosting estático."""
    target_url = abs_url(base_url, target)
    page = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{h(title)}</title>
<meta name="robots" content="noindex,follow" />
<link rel="canonical" href="{h(target_url)}" />
<meta http-equiv="refresh" content="0; url={h(target_url)}" />
</head>
<body>
<p>Esta página se ha trasladado a <a href="{h(target_url)}">{h(target_url)}</a>.</p>
</body>
</html>
'''
    (out / filename).write_text(page, encoding="utf-8")


def generate_legacy_detail(out: Path, base_url: str) -> None:
    """Compatibilidad para antiguas URLs detalle.html?juego=<slug>."""
    home_url = abs_url(base_url, "")
    page = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Ficha trasladada · PC Game Archive</title>
<meta name="robots" content="noindex,follow" />
<script>
(function(){{
  var params=new URLSearchParams(location.search);
  var slug=(params.get('juego')||'').trim().toLowerCase();
  var target={json.dumps(home_url)};
  if(/^[a-z0-9-]+$/.test(slug)){{
    target={json.dumps(base_url.rstrip('/') + '/juegos/')}+slug+'/';
  }}
  location.replace(target);
}})();
</script>
</head>
<body>
<p>La ficha se ha trasladado. <a href="{h(home_url)}">Ir a PC Game Archive</a>.</p>
</body>
</html>
'''
    (out / "detalle.html").write_text(page, encoding="utf-8")



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

    for name in ["CNAME", "juegos.json", "json_schema.json", "logo.png", "no_disponible.png", "anuncio_with_bgc.png", "favicon.ico", "favicon.svg", "apple-touch-icon.png", "site.webmanifest"]:
        src = project_root / name
        dst = out / name
        if src.exists() and src.is_file():
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(src.read_bytes())


def build_report(games: list[dict[str, Any]], out: Path, gallery_index: dict[str, list[str]] | None = None) -> None:
    urls = [g.get("url") for g in games if g.get("url")]
    dup = [u for u,c in Counter(urls).items() if c > 1]
    invalid = [g for g in games if not isinstance(g.get("url"), str) or not re.match(r"^juegos/[a-z0-9\-]+/$", g.get("url", ""))]
    gallery_index = gallery_index or {}
    image_count = sum(len(images) for images in gallery_index.values())
    games_with_images = sum(1 for images in gallery_index.values() if images)
    lines = [
        "# Informe de generación SEO",
        "",
        f"- Fecha: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"- Juegos en catálogo: {len(games)}",
        f"- URLs duplicadas detectadas: {len(dup)}",
        f"- URLs inválidas omitidas: {len(invalid)}",
        f"- Desarrolladores con página/landing indexable: {sum(1 for e in build_taxonomy_entities(games, 'desarrolladores') if e['count'] >= TAXONOMIES['desarrolladores']['min_count'])}",
        f"- Distribuidores con página/landing indexable: {sum(1 for e in build_taxonomy_entities(games, 'distribuidores') if e['count'] >= TAXONOMIES['distribuidores']['min_count'])}",
        f"- Géneros con página/landing indexable: {sum(1 for e in build_taxonomy_entities(games, 'generos') if e['count'] >= TAXONOMIES['generos']['min_count'])}",
        f"- Plataformas con página/landing indexable: {sum(1 for e in build_taxonomy_entities(games, 'plataformas') if e['count'] >= TAXONOMIES['plataformas']['min_count'])}",
        f"- Formatos con página/landing indexable: {sum(1 for e in build_taxonomy_entities(games, 'formatos') if e['count'] >= TAXONOMIES['formatos']['min_count'])}",
        f"- Años documentados: {taxonomy_coverage(games, 'anos')[0]} fichas ({taxonomy_coverage(games, 'anos')[1]:.1%}); entidades indexables: {sum(1 for e in build_taxonomy_entities(games, 'anos') if taxonomy_is_publishable(games, 'anos') and e['count'] >= TAXONOMIES['anos']['min_count'])}",
        f"- Mercados documentados: {taxonomy_coverage(games, 'mercados')[0]} fichas ({taxonomy_coverage(games, 'mercados')[1]:.1%}); entidades indexables: {sum(1 for e in build_taxonomy_entities(games, 'mercados') if taxonomy_is_publishable(games, 'mercados') and e['count'] >= TAXONOMIES['mercados']['min_count'])}",
        f"- Idiomas documentados: {taxonomy_coverage(games, 'idiomas')[0]} fichas ({taxonomy_coverage(games, 'idiomas')[1]:.1%}); entidades indexables: {sum(1 for e in build_taxonomy_entities(games, 'idiomas') if taxonomy_is_publishable(games, 'idiomas') and e['count'] >= TAXONOMIES['idiomas']['min_count'])}",
        f"- Soportes documentados: {taxonomy_coverage(games, 'soportes')[0]} fichas ({taxonomy_coverage(games, 'soportes')[1]:.1%}); entidades indexables: {sum(1 for e in build_taxonomy_entities(games, 'soportes') if taxonomy_is_publishable(games, 'soportes') and e['count'] >= TAXONOMIES['soportes']['min_count'])}",
        f"- Tipos de edición documentados: {taxonomy_coverage(games, 'tipos-edicion')[0]} fichas ({taxonomy_coverage(games, 'tipos-edicion')[1]:.1%}); entidades indexables: {sum(1 for e in build_taxonomy_entities(games, 'tipos-edicion') if taxonomy_is_publishable(games, 'tipos-edicion') and e['count'] >= TAXONOMIES['tipos-edicion']['min_count'])}",
        f"- Páginas estáticas del catálogo: {max(1, math.ceil(len(games) / CATALOG_PAGE_SIZE))}",
        f"- Fichas con imágenes documentales detectadas: {games_with_images}",
        f"- Imágenes documentales incluidas en el sitemap: {image_count}",
        "",
        "## Observaciones",
        "",
        "- Las páginas de juego se generan físicamente como `juegos/<slug>/index.html`, pero todos los enlaces y canonical usan `/juegos/<slug>/`.",
        "- El sitemap contiene exclusivamente URLs canónicas y no publica fechas `lastmod` artificiales.",
        "- El sitemap usa la extensión oficial de imágenes y asocia a cada ficha únicamente las imágenes que existen físicamente en `/juegos/<slug>/img/`.",
        "- Las fichas añaden `primaryImageOfPage`/`ImageObject` solo cuando existe fotografía real; `no_disponible.png` se mantiene como fallback visual/social pero no se presenta como imagen documental en datos estructurados ni en el sitemap de imágenes.",
        "- Las imágenes documentales tienen alt descriptivo, captions visibles y la imagen principal usa `fetchpriority=high`; el resto mantiene carga diferida nativa.",
        "- Se permite `max-image-preview:large` para que Google pueda usar previsualizaciones grandes cuando corresponda.",
        "- Se conservan los nombres documentales originales (`001.jpg`, etc.); no se renombran ficheros ni se rompen rutas históricas del archivo.",
        "- `bigbox.html` se conserva únicamente como redirección a `juegos-pc-big-box.html`.",
        "- `detalle.html?juego=<slug>` se conserva únicamente como compatibilidad con URLs antiguas.",
        "- Google Analytics normaliza la ruta a la canonical, conserva parámetros de campaña (`utm_*`, `gclid`, `gbraid`, `wbraid`, `dclid`) para no perder atribución SEM y no se inicializa en localhost/127.0.0.1/::1.",
        "- Los duplicados no se sobrescriben: se conserva la primera aparición en el catálogo.",
        "- Se generan landing pages SEO en español para búsquedas genéricas.",
        "- Se generan automáticamente hubs y páginas SEO por desarrollador, distribuidor, género, plataforma y formato cuando una entidad aparece en 3 o más fichas.",
        "- Fase 10D añade año, mercado, idioma, soporte y tipo de edición como taxonomías potenciales; además del mínimo por entidad, cada campo nuevo exige al menos 150 fichas documentadas antes de publicar su hub para evitar páginas prematuras y despublicaciones por crecimiento del catálogo.",
        "- Variantes puramente tipográficas de una entidad (mayúsculas/acentos) se agrupan en una única página.",
        "- Big Box, MS-DOS, Windows 95/98 y aventura gráfica reutilizan sus landings editoriales existentes para evitar canibalización.",
        "- Las landings principales incorporan contenido editorial específico, métricas dinámicas, breadcrumbs y enlaces internos a entidades relevantes.",
        "- Se genera `/vender-videojuegos-pc-antiguos/` como landing de captación para compra/donación, con CTA medidos mediante `offer_games_click`; los mailto esperan brevemente al callback del Google tag antes de abrir el correo.",
        "- Las fichas enlazan directamente a las páginas de entidad cuando existe una landing indexable.",
        "- Las fichas incorporan bloques automáticos de otras ediciones, serie/colección, desarrollador y juegos relacionados, deduplicados entre sí para reforzar la navegación contextual.",
        "- Se generan favicon PNG/ICO y manifest desde logo.png para favorecer el icono en resultados de Google.",
        "- El scroll infinito de la portada se complementa con `/catalogo/` y una serie paginada de enlaces HTML rastreables, con canonical propio por página.",
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
    gallery_index = build_gallery_index(project_root, games)

    out.mkdir(parents=True, exist_ok=True)
    write_assets(out, games)
    copy_support_files(project_root, out)
    generate_favicons(project_root, out)
    generate_index(games, out, args.base_url)
    generate_catalog_pages(games, out, args.base_url)
    generate_seo_landing_pages(games, out, args.base_url)
    generate_taxonomy_pages(games, out, args.base_url)
    generate_series(games, out, args.base_url)
    generate_acquisition_landing(out, args.base_url)
    generate_contact(out, args.base_url)
    generate_game_pages(games, out, project_root, args.base_url, gallery_index)
    generate_static_redirect(out, args.base_url, "bigbox.html", "juegos-pc-big-box.html", "Big Box · PC Game Archive")
    generate_legacy_detail(out, args.base_url)
    generate_sitemap(games, out, args.base_url, gallery_index)
    generate_robots(out, args.base_url)
    build_report(games, out, gallery_index)
    print("Versión generador: fase12.1-layout-buscador-2026-08-14")
    print("Bloque SEO home: Explorar el archivo antes de Catálogo de juegos")
    print(f"Generación completada: {out}")
    print(f"Juegos procesados: {len(games)}")
    print("Modo de assets: no se copian imágenes ni carpetas img; solo se sobrescriben ficheros generados.")
    return 0


CSS = r'''
:root{--b:#111;--g:#666;--bd:#e6e6e6;--bg:#f7f7f5;--w:#fff;--soft:#f0eee9;--accent:#111;--max:1200px}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:var(--b);background:var(--bg);line-height:1.55}a{color:inherit}.wrap{max-width:var(--max);margin:0 auto;padding:0 18px}header{background:rgba(255,255,255,.95);border-bottom:1px solid var(--bd);position:sticky;top:0;z-index:10;backdrop-filter:blur(10px)}.header-row{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:14px 18px}.brand{display:flex;align-items:center;gap:12px;text-decoration:none}.brand strong{display:block;font-size:18px;letter-spacing:.2px}.brand small{display:block;color:var(--g);font-size:12px}.logo{width:64px;height:64px;object-fit:contain;display:block}.nav{display:flex;flex-wrap:wrap;gap:6px;justify-content:flex-end}.nav a{text-decoration:none;font-weight:800;font-size:14px;padding:8px 10px;border-radius:999px;border:1px solid transparent}.nav a:hover,.nav a.active{background:#f7f7f7;border-color:var(--bd)}main{padding-bottom:42px}.hero-section{background:linear-gradient(180deg,#fff,var(--soft));border-bottom:1px solid var(--bd)}.hero-grid{display:grid;grid-template-columns:1fr 280px;gap:28px;align-items:center;padding-top:48px;padding-bottom:48px}.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:12px;color:var(--g);font-weight:900;margin:0 0 10px}h1{font-size:clamp(32px,5vw,58px);line-height:1.02;margin:0 0 18px;letter-spacing:-.04em}h2{font-size:26px;line-height:1.15;margin:0 0 14px}.lead{font-size:18px;color:#333;max-width:760px}.search-hero,.toolbar{display:flex;gap:10px;margin-top:20px}.search-hero input,.toolbar input,.search-hero select,.toolbar select{flex:1;min-width:0;padding:14px 16px;border:1px solid var(--bd);border-radius:14px;background:#fff;font-size:16px}.search-hero select,.toolbar select{min-width:180px}.catalog-search{align-items:stretch}.search-hero button,.toolbar button,.button{border:1px solid var(--accent);background:var(--accent);color:#fff;text-decoration:none;border-radius:14px;padding:12px 16px;font-weight:900;cursor:pointer;display:inline-flex;align-items:center;justify-content:center}.stats-card{background:#111;color:#fff;border-radius:24px;padding:22px;display:grid;grid-template-columns:auto 1fr;gap:8px 14px}.stats-card strong{font-size:34px;line-height:1}.stats-card span{align-self:center;color:#ddd}.section-head,.meta{display:flex;align-items:end;justify-content:space-between;gap:14px;margin:30px 0 14px}.section-head a{font-weight:900}.grid.cards{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}.game-card{display:flex;flex-direction:column;background:#fff;border:1px solid var(--bd);border-radius:18px;overflow:hidden;text-decoration:none;min-height:245px;transition:transform .15s ease,box-shadow .15s ease}.game-card:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.08)}.game-card img{width:100%;aspect-ratio:4/3;object-fit:contain;background:#eee;padding:6px}.game-card img.missing,.hero-img.missing{background:repeating-linear-gradient(45deg,#eee,#eee 10px,#f8f8f8 10px,#f8f8f8 20px)}.game-card-body{display:flex;flex-direction:column;gap:6px;padding:12px}.game-card strong{font-size:14px;line-height:1.2}.game-card small,.count{color:var(--g);font-size:12px}.tagrow,.chips,.actions{display:flex;flex-wrap:wrap;gap:8px}.media-card .chips{margin-top:14px;margin-bottom:18px}.media-card .actions{margin-top:8px;padding-top:16px;border-top:1px solid var(--bd)}.tag,.chip{font-size:12px;padding:5px 9px;border:1px solid var(--bd);border-radius:999px;background:#fff;text-decoration:none}.page-head{padding:34px 0 20px}.page-head h1{font-size:42px}.taxonomy-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.taxonomy-item,.content-card,.media-card{background:#fff;border:1px solid var(--bd);border-radius:20px;padding:18px}.taxonomy-item{text-decoration:none;display:flex;justify-content:space-between;gap:16px}.taxonomy-item small{color:var(--g)}.text-section,.content-card{margin-top:28px}.landing-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:4px 0 28px}.landing-stat{background:#111;color:#fff;border-radius:18px;padding:18px;display:flex;flex-direction:column;gap:4px}.landing-stat strong{font-size:30px;line-height:1}.landing-stat span{color:#ddd;font-size:13px}.landing-editorial p{max-width:900px}.landing-editorial p:last-child{margin-bottom:0}.breadcrumbs{font-size:13px;color:var(--g);padding:18px 0}.detail-grid{display:grid;grid-template-columns:minmax(300px,420px) 1fr;gap:20px;align-items:start}.hero-figure{margin:0}.hero-figure figcaption{margin-top:9px;color:var(--g);font-size:12px;line-height:1.4}.hero-img{width:100%;height:auto;max-height:620px;object-fit:contain;border:1px solid var(--bd);border-radius:16px;background:#f3f3f1;display:block}.kv{display:grid;grid-template-columns:160px 1fr;gap:10px 14px;border-top:1px solid var(--bd);padding-top:14px;margin-top:18px}.kv dt{color:var(--g);font-weight:700}.kv dd{margin:0}.kv.compact{grid-template-columns:180px 1fr}.gallery{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.gallery-item{margin:0;min-width:0}.gallery-link{display:block;text-decoration:none}.gallery img{display:block;width:100%;aspect-ratio:4/3;object-fit:contain;border-radius:14px;border:1px solid var(--bd);background:#eee}.gallery-item figcaption{margin-top:6px;color:var(--g);font-size:12px;line-height:1.35}.gallery-missing img{object-fit:contain}.related-area{margin-top:34px}.related-section{margin-top:30px}.related-section:first-child{margin-top:0}.related-section .section-head{margin-bottom:14px}.related-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.related-grid .game-card{min-height:230px}.pagination{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px;margin:28px 0 10px}.pagination a,.pagination-current,.pagination-gap{min-width:38px;height:38px;padding:0 10px;border:1px solid var(--bd);border-radius:10px;background:#fff;display:inline-flex;align-items:center;justify-content:center;text-decoration:none;font-weight:800;font-size:13px}.pagination a:hover{background:#f2f2f0}.pagination-current{background:#111;color:#fff;border-color:#111}.pagination-gap{border-color:transparent;background:transparent;color:var(--g)}.pagination-prev,.pagination-next{min-width:auto!important}.button-secondary{background:#fff;color:#111;border-color:#111}.button-secondary:hover{background:#f2f2f0}.acquisition-strip{margin-top:32px;margin-bottom:12px;background:#111;color:#fff;border-radius:24px;padding:24px;display:flex;align-items:center;justify-content:space-between;gap:24px}.acquisition-strip h2{margin-bottom:8px}.acquisition-strip p:not(.eyebrow){margin:0;color:#ddd;max-width:760px}.acquisition-strip .eyebrow{color:#bbb}.acquisition-strip .button{background:#fff;color:#111;border-color:#fff;white-space:nowrap}.acquisition-hero{background:linear-gradient(180deg,#fff,var(--soft));border-bottom:1px solid var(--bd)}.acquisition-hero-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(280px,430px);gap:42px;align-items:center;padding-bottom:48px}.acquisition-hero .breadcrumbs{padding-top:22px}.acquisition-visual{margin:28px 0 0}.acquisition-visual img{display:block;width:100%;height:auto;border-radius:24px;border:1px solid var(--bd);box-shadow:0 16px 45px rgba(0,0,0,.08)}.acquisition-section{padding-top:36px;padding-bottom:36px}.acquisition-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.acquisition-grid .content-card{margin-top:0}.acquisition-grid h3{margin-top:0;margin-bottom:8px}.acquisition-grid p{margin:0;color:#444}.acquisition-note{margin:20px 0 0;padding:16px 18px;border-left:4px solid #111;background:#fff;border-radius:0 14px 14px 0}.acquisition-soft{background:var(--soft);border-top:1px solid var(--bd);border-bottom:1px solid var(--bd)}.acquisition-steps{list-style:none;counter-reset:acq;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.acquisition-steps li{counter-increment:acq;background:#fff;border:1px solid var(--bd);border-radius:20px;padding:18px;display:flex;flex-direction:column;gap:7px}.acquisition-steps li:before{content:counter(acq);width:34px;height:34px;border-radius:50%;background:#111;color:#fff;display:inline-flex;align-items:center;justify-content:center;font-weight:900;margin-bottom:5px}.acquisition-steps span{color:#555;font-size:14px}.acquisition-contact-card{background:#111;color:#fff;border-radius:24px;padding:26px;display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:30px}.acquisition-contact-card h2{margin-bottom:8px}.acquisition-contact-card p:not(.eyebrow){color:#ddd;max-width:760px;margin-bottom:0}.acquisition-contact-card .eyebrow{color:#bbb}.acquisition-contact-card .button{background:#fff;color:#111;border-color:#fff}.acquisition-contact-card .button-secondary{background:transparent;color:#fff;border-color:#fff}.acquisition-actions{margin-top:20px}.acquisition-faq details{background:#fff;border:1px solid var(--bd);border-radius:14px;margin:10px 0;padding:0 16px}.acquisition-faq summary{cursor:pointer;font-weight:800;padding:15px 0}.acquisition-faq details p{margin:0 0 16px;color:#444}footer{background:#fff;border-top:1px solid var(--bd);padding:22px 0}.footrow{display:flex;justify-content:space-between;gap:16px;align-items:center;color:var(--g);font-size:13px}.to-top{padding:8px 10px;border:1px solid var(--bd);border-radius:12px;text-decoration:none;font-weight:800;color:#111;background:#fff;cursor:pointer;font:inherit}.to-top:hover{background:#f7f7f7}@media(max-width:1100px){.grid.cards{grid-template-columns:repeat(4,1fr)}.related-grid{grid-template-columns:repeat(4,1fr)}.taxonomy-grid{grid-template-columns:repeat(3,1fr)}.acquisition-grid,.acquisition-steps{grid-template-columns:repeat(2,1fr)}}@media(max-width:800px){.landing-stats{grid-template-columns:repeat(2,1fr)}header{position:static}.header-row,.hero-grid,.detail-grid,.acquisition-hero-grid,.acquisition-contact-card{grid-template-columns:1fr;display:grid}.nav{justify-content:flex-start}.grid.cards{grid-template-columns:repeat(2,1fr)}.related-grid{grid-template-columns:repeat(2,1fr)}.taxonomy-grid,.gallery{grid-template-columns:repeat(2,1fr)}.search-hero,.toolbar{flex-direction:column}.kv{grid-template-columns:1fr}.page-head h1{font-size:34px}.acquisition-strip{align-items:flex-start;flex-direction:column}.acquisition-contact-card .actions{justify-content:flex-start}}@media(max-width:480px){.landing-stats{grid-template-columns:1fr}.grid.cards,.related-grid,.taxonomy-grid,.gallery,.acquisition-grid,.acquisition-steps{grid-template-columns:1fr}.hero-grid{padding-top:30px;padding-bottom:30px}.acquisition-actions{flex-direction:column}.acquisition-actions .button{width:100%}}
'''
CSS += r'''
.catalog-search-advanced{display:grid;grid-template-columns:1fr;gap:10px;margin-top:20px;align-items:stretch}.catalog-search-advanced .search-query-row{min-width:0}.catalog-search-advanced .search-filter-row{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr) auto;gap:10px;align-items:stretch}.catalog-search-advanced .search-query-row>input,.catalog-search-advanced .search-autocomplete{width:100%}.catalog-search-advanced .search-query-row input{font-size:18px;padding:16px 18px}.catalog-search-advanced .search-filter-row select{width:100%;min-width:0}.catalog-search-advanced .search-filter-row>button{min-width:126px}.search-autocomplete{position:relative;flex:1;min-width:0}.search-autocomplete>input{width:100%}.search-suggestions{position:absolute;left:0;right:0;top:calc(100% + 7px);z-index:40;background:#fff;border:1px solid var(--bd);border-radius:16px;box-shadow:0 16px 42px rgba(0,0,0,.14);padding:8px;max-height:430px;overflow:auto}.search-suggestions[hidden]{display:none}.search-hero button.search-suggestion{width:100%;display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:16px;text-align:left;border:1px solid transparent;background:#fff;color:#111;padding:13px 14px;border-radius:12px;cursor:pointer}.search-hero button.search-suggestion:hover,.search-hero button.search-suggestion.is-active{background:#f7f7f5;color:#111;border-color:var(--bd)}.search-suggestion-main{min-width:0;display:flex;flex-direction:column;gap:3px}.search-suggestion-main strong{white-space:normal;overflow:visible;text-overflow:clip;font-size:15px;line-height:1.28}.search-suggestion-main small,.search-suggestion-count{color:var(--g);font-size:12px;line-height:1.3}.search-suggestion-count{white-space:nowrap;font-weight:700}.search-facets{margin:16px 0 8px;padding:14px;background:#fff;border:1px solid var(--bd);border-radius:18px}.search-facets-head{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:10px}.search-facets-head strong{font-size:14px}.search-facets-head a{font-size:12px;color:var(--g);font-weight:800}.search-facet-groups{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}.search-facet-group{min-width:0}.search-facet-group>strong{display:block;font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--g);margin-bottom:7px}.search-facet-values{display:flex;flex-wrap:wrap;gap:6px}.facet-chip{display:inline-flex;gap:5px;align-items:center;padding:5px 8px;border:1px solid var(--bd);border-radius:999px;background:#fff;text-decoration:none;font-size:11px;line-height:1.2}.facet-chip:hover,.facet-chip.active{background:#111;color:#fff;border-color:#111}.facet-chip span{opacity:.7}.search-empty{grid-column:1/-1}.search-empty h3{margin-top:0}.search-empty-suggestions{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.search-empty-suggestions a{font-size:12px;padding:7px 10px;border:1px solid var(--bd);border-radius:999px;text-decoration:none;background:#fff}.search-empty-suggestions a:hover{background:var(--soft)}
@media(max-width:900px){.search-facet-groups{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:700px){.catalog-search-advanced .search-filter-row{grid-template-columns:1fr}.catalog-search-advanced .search-filter-row>button{width:100%}}@media(max-width:520px){.search-facet-groups{grid-template-columns:1fr}.search-suggestions{max-height:320px}.search-hero button.search-suggestion{padding:12px;gap:10px}.search-suggestion-main strong{font-size:14px}}
'''

JS = r'''(function(){
  const PAGE_SIZE = 24;
  const params = new URLSearchParams(location.search);
  const grid = document.querySelector('[data-catalog-list], .grid.cards');
  const forms = document.querySelectorAll('form.catalog-search, form.search-hero, form.toolbar');
  const sentinel = document.querySelector('[data-load-sentinel]');
  const games = Array.isArray(window.PCGA_SEARCH_INDEX) ? window.PCGA_SEARCH_INDEX : [];
  const FILTER_FIELDS = ['formato','serie','genero','plataforma','desarrollador','distribuidor','mercado','idioma','soporte','tipo_edicion','anio'];
  const FACET_FIELDS = [
    ['formato','Formato'],['plataforma','Plataforma'],['genero','Género'],['desarrollador','Desarrollador']
  ];

  restoreFormValues();
  prepareCleanSubmissions();
  setupAutocomplete();
  if(!grid || !games.length) return;

  const rawSearchTerm = String(params.get('titulo') || params.get('q') || '').trim();
  const searchTerms = tokenize(rawSearchTerm);
  const defaultFormato = normalize(grid.dataset.defaultFormato || '');
  const defaultPlataforma = normalize(grid.dataset.defaultPlataforma || '');
  const defaultPlataformaAny = splitTerms(grid.dataset.defaultPlataformaAny || '');
  const defaultGenero = normalize(grid.dataset.defaultGenero || '');
  const defaultGeneroAny = splitTerms(grid.dataset.defaultGeneroAny || '');
  const defaultTextAny = splitTerms(grid.dataset.defaultTextAny || '');
  const defaultTaxonomy = String(grid.dataset.defaultTaxonomy || '').trim();
  const defaultTaxonomyValues = splitTerms(grid.dataset.defaultTaxonomyValues || '');

  const filters = {};
  FILTER_FIELDS.forEach(name => filters[name] = normalize(params.get(name) || ''));
  if(!filters.formato) filters.formato = defaultFormato;
  if(!filters.genero) filters.genero = defaultGenero;
  if(!filters.plataforma) filters.plataforma = defaultPlataforma;

  const ranked = [];
  games.forEach((g, order) => {
    const searchScore = scoreSearch(g, searchTerms);
    if(searchTerms.length && searchScore < 0) return;
    if(!matchesDefaults(g)) return;
    if(!matchesFilters(g)) return;
    ranked.push({g, score: searchScore, order});
  });
  if(searchTerms.length){
    ranked.sort((a,b) => b.score - a.score || normalize(a.g.titulo).localeCompare(normalize(b.g.titulo)) || a.order-b.order);
  }
  const selected = ranked.map(x => x.g);

  if(rawSearchTerm && typeof gtag === 'function'){
    gtag('event','search',{search_term: rawSearchTerm,results_count: selected.length});
    if(!selected.length) gtag('event','search_no_results',{search_term: rawSearchTerm});
  }
  if(typeof gtag === 'function'){
    FILTER_FIELDS.forEach(name => {
      const value = params.get(name);
      if(value) gtag('event','filter_used',{filter_name:name,filter_value:value});
    });
  }

  renderFacets();
  let rendered = 0;
  grid.innerHTML = '';
  renderNextPage();

  const count = (grid.closest('section') || document).querySelector('.count');
  if(count) count.textContent = selected.length + ' juegos encontrados.';

  if(!selected.length){
    renderEmptyState();
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

  function matchesDefaults(g){
    const genreValues = valueList(g,'genero');
    const platformValues = valueList(g,'plataforma');
    const searchBlob = normalizedSearchBlob(g);
    if(defaultGeneroAny.length && !defaultGeneroAny.some(t => genreValues.includes(t))) return false;
    if(defaultPlataformaAny.length && !defaultPlataformaAny.some(t => platformValues.includes(t))) return false;
    if(defaultTextAny.length && !defaultTextAny.some(t => searchBlob.includes(t))) return false;
    if(defaultTaxonomy && defaultTaxonomyValues.length){
      const entityValues = valueList(g, defaultTaxonomy);
      if(!defaultTaxonomyValues.some(t => entityValues.includes(t))) return false;
    }
    return true;
  }

  function matchesFilters(g, ignoreField){
    for(const name of FILTER_FIELDS){
      if(name === ignoreField) continue;
      const wanted = filters[name];
      if(!wanted) continue;
      if(name === 'genero'){
        if(!valueList(g,name).some(v => v.includes(wanted))) return false;
      } else if(!valueList(g,name).includes(wanted)) return false;
    }
    return true;
  }

  function scoreSearch(g, terms){
    if(!terms.length) return 0;
    const title = normalize(g.titulo || '');
    const blob = normalizedSearchBlob(g);
    const words = uniqueWords(blob);
    let score = 0;
    for(const term of terms){
      if(title === term){ score += 130; continue; }
      if(title.startsWith(term)){ score += 95; continue; }
      if(title.includes(term)){ score += 72; continue; }
      if(blob.includes(term)){ score += 48; continue; }
      const fuzzy = bestFuzzy(term, words);
      if(fuzzy < 0) return -1;
      score += fuzzy;
    }
    if(terms.length > 1 && title.includes(terms.join(' '))) score += 70;
    return score;
  }

  function bestFuzzy(term, words){
    if(term.length < 4) return -1;
    const maxDistance = term.length >= 8 ? 2 : 1;
    let best = 99;
    for(const word of words){
      if(Math.abs(word.length-term.length) > maxDistance) continue;
      const d = levenshteinLimited(term, word, maxDistance);
      if(d < best) best = d;
      if(best === 1) break;
    }
    return best <= maxDistance ? (term.length >= 8 ? 28-best*5 : 24-best*5) : -1;
  }

  function levenshteinLimited(a,b,limit){
    if(a === b) return 0;
    if(Math.abs(a.length-b.length) > limit) return limit+1;
    let prev = Array.from({length:b.length+1},(_,i)=>i);
    for(let i=1;i<=a.length;i++){
      const cur=[i]; let rowMin=i;
      for(let j=1;j<=b.length;j++){
        const value=Math.min(cur[j-1]+1,prev[j]+1,prev[j-1]+(a[i-1]===b[j-1]?0:1));
        cur[j]=value; if(value<rowMin) rowMin=value;
      }
      if(rowMin>limit) return limit+1;
      prev=cur;
    }
    return prev[b.length];
  }

  function renderFacets(){
    const hasQueryOrFilter = rawSearchTerm || FILTER_FIELDS.some(name => params.get(name));
    if(!hasQueryOrFilter) return;
    const section = grid.closest('section') || grid.parentElement;
    if(!section || section.querySelector('.search-facets')) return;
    const groups=[];
    FACET_FIELDS.forEach(([field,label]) => {
      const counts=new Map();
      games.forEach(g => {
        if(searchTerms.length && scoreSearch(g,searchTerms)<0) return;
        if(!matchesDefaults(g) || !matchesFilters(g,field)) return;
        rawValues(g,field).forEach(raw => {
          if(!raw || (field==='serie' && normalize(raw)==='todos')) return;
          counts.set(raw,(counts.get(raw)||0)+1);
        });
      });
      const current=normalize(params.get(field)||'');
      const values=[...counts.entries()].sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0],'es')).slice(0,6);
      if(!values.length) return;
      const chips=values.map(([value,n]) => {
        const u=new URL(location.href); u.searchParams.set(field,value); u.searchParams.delete('titulo');
        if(rawSearchTerm && !u.searchParams.get('q')) u.searchParams.set('q',rawSearchTerm);
        const active=current===normalize(value)?' active':'';
        return `<a class="facet-chip${active}" href="${esc(u.pathname+u.search)}">${esc(value)} <span>${n}</span></a>`;
      }).join('');
      groups.push(`<div class="search-facet-group"><strong>${esc(label)}</strong><div class="search-facet-values">${chips}</div></div>`);
    });
    if(!groups.length) return;
    const clearUrl=new URL(location.href); FILTER_FIELDS.forEach(f=>clearUrl.searchParams.delete(f)); clearUrl.searchParams.delete('titulo'); if(rawSearchTerm) clearUrl.searchParams.set('q',rawSearchTerm);
    const box=document.createElement('div'); box.className='search-facets';
    box.innerHTML=`<div class="search-facets-head"><strong>Refinar resultados</strong><a href="${esc(clearUrl.pathname+clearUrl.search)}">Limpiar filtros</a></div><div class="search-facet-groups">${groups.join('')}</div>`;
    const countEl=section.querySelector('.count');
    if(countEl) countEl.insertAdjacentElement('afterend',box); else grid.insertAdjacentElement('beforebegin',box);
  }

  function renderEmptyState(){
    const suggestions = nearestSuggestions(rawSearchTerm,5);
    const suggestionHtml=suggestions.length?`<div class="search-empty-suggestions">${suggestions.map(s=>`<a href="${esc(s.href)}" data-search-suggestion="empty">${esc(s.label)}</a>`).join('')}</div>`:'';
    const clear=new URL(location.href); clear.search='';
    grid.innerHTML=`<div class="content-card search-empty"><h3>No hemos encontrado coincidencias</h3><p>Prueba con menos palabras, una variante del nombre o elimina alguno de los filtros.</p>${suggestionHtml}<p><a class="button button-secondary" href="${esc(clear.pathname)}">Ver todo el catálogo</a></p></div>`;
  }

  function setupAutocomplete(){
    if(!games.length) return;
    const suggestionsIndex=buildSuggestionsIndex();
    forms.forEach(form => {
      const input=form.querySelector('input[name="q"],input[name="titulo"]');
      if(!input || input.dataset.autocompleteReady) return;
      input.dataset.autocompleteReady='1'; input.setAttribute('autocomplete','off'); input.setAttribute('aria-autocomplete','list');
      const wrap=document.createElement('div'); wrap.className='search-autocomplete';
      input.parentNode.insertBefore(wrap,input); wrap.appendChild(input);
      const panel=document.createElement('div'); panel.className='search-suggestions'; panel.hidden=true; panel.setAttribute('role','listbox'); wrap.appendChild(panel);
      let active=-1, current=[];
      const update=()=>{
        const q=input.value.trim(); active=-1;
        if(q.length<2){panel.hidden=true; panel.innerHTML=''; return;}
        current=findSuggestions(q,suggestionsIndex,8);
        panel.innerHTML=current.map((s,i)=>`<button type="button" class="search-suggestion" role="option" data-i="${i}"><span class="search-suggestion-main"><strong>${esc(s.label)}</strong><small>${esc(s.type)}</small></span><span class="search-suggestion-count">${s.count>1?esc(s.count+' fichas'):''}</span></button>`).join('');
        panel.hidden=!current.length;
      };
      input.addEventListener('input',update);
      input.addEventListener('focus',update);
      input.addEventListener('keydown',e=>{
        if(panel.hidden || !current.length) return;
        if(e.key==='ArrowDown'){e.preventDefault();active=(active+1)%current.length;paintActive();}
        else if(e.key==='ArrowUp'){e.preventDefault();active=(active-1+current.length)%current.length;paintActive();}
        else if(e.key==='Escape'){panel.hidden=true;active=-1;}
        else if(e.key==='Enter' && active>=0){e.preventDefault();choose(current[active]);}
      });
      panel.addEventListener('mousedown',e=>{
        const btn=e.target.closest('[data-i]'); if(!btn) return; e.preventDefault(); choose(current[Number(btn.dataset.i)]);
      });
      document.addEventListener('click',e=>{if(!wrap.contains(e.target)) panel.hidden=true;});
      function paintActive(){panel.querySelectorAll('.search-suggestion').forEach((el,i)=>el.classList.toggle('is-active',i===active));}
      function choose(s){
        if(typeof gtag==='function') gtag('event','search_suggestion_click',{suggestion_type:s.type,suggestion_value:s.label});
        if(s.url){location.href=s.url;return;}
        if(s.field){const u=new URL('/',location.origin);u.searchParams.set(s.field,s.label);location.href=u.pathname+u.search;return;}
        input.value=s.label; panel.hidden=true; form.requestSubmit?form.requestSubmit():form.submit();
      }
    });
  }

  function buildSuggestionsIndex(){
    const map=new Map();
    const fields=[['desarrollador','Desarrollador'],['distribuidor','Distribuidor'],['serie','Serie'],['genero','Género'],['plataforma','Plataforma'],['formato','Formato'],['mercado','Mercado'],['idioma','Idioma'],['soporte','Soporte']];
    games.forEach(g=>{
      const title=String(g.titulo||'').trim();
      if(title){const key='j:'+normalize(title);const cur=map.get(key)||{label:title,type:'Juego',count:0,url:g.url};cur.count++;if(cur.count>1)cur.url=null;map.set(key,cur);}
      fields.forEach(([field,type])=>rawValues(g,field).forEach(value=>{if(!value||normalize(value)==='todos')return;const key=field+':'+normalize(value);const cur=map.get(key)||{label:value,type,count:0,url:null,field};cur.count++;map.set(key,cur);}));
    });
    return [...map.values()].map(s=>({...s,norm:normalize(s.label),words:uniqueWords(normalize(s.label))}));
  }

  function findSuggestions(query,index,limit){
    const q=normalize(query); const qTerms=tokenize(q); const ranked=[];
    index.forEach(s=>{
      let score=0;
      if(s.norm===q)score=150; else if(s.norm.startsWith(q))score=115; else if(s.norm.includes(q))score=85; else {
        let ok=true;
        for(const t of qTerms){const f=bestFuzzy(t,s.words);if(f<0){ok=false;break;}score+=f;}
        if(!ok)return;
      }
      if(s.type==='Juego')score+=12;
      score+=Math.min(s.count,20)/10;
      ranked.push({s,score});
    });
    return ranked.sort((a,b)=>b.score-a.score||a.s.label.localeCompare(b.s.label,'es')).slice(0,limit).map(x=>x.s);
  }

  function nearestSuggestions(query,limit){
    if(!query) return [];
    const idx=buildSuggestionsIndex();
    return findSuggestions(query,idx,limit).map(s=>({label:s.label,href:s.url||(s.field?buildFacetHref(s.field,s.label):buildQueryHref(s.label))}));
  }

  function buildQueryHref(q){const u=new URL(location.href);u.search='';u.searchParams.set('q',q);return u.pathname+u.search;}
  function buildFacetHref(field,value){const u=new URL('/',location.origin);u.searchParams.set(field,value);return u.pathname+u.search;}
  function rawValues(g,field){const v=g[field];return (Array.isArray(v)?v:[v]).map(x=>String(x||'').trim()).filter(Boolean);}
  function valueList(g,field){return rawValues(g,field).map(normalize);}
  function normalizedSearchBlob(g){return normalize(g.search_text||[g.titulo,g.formato,(g.serie||[]).join(' '),(g.genero||[]).join(' '),(g.plataforma||[]).join(' ')].join(' '));}
  function uniqueWords(value){return [...new Set(String(value||'').split(/[^a-z0-9]+/).filter(Boolean))];}
  function splitTerms(value){return String(value||'').split('|').map(normalize).filter(Boolean);}
  function tokenize(value){return normalize(value).split(/\s+/).filter(Boolean);}
  function normalize(value){return String(value||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').trim();}
  function esc(s){return String(s||'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));}

  function restoreFormValues(){
    forms.forEach(form=>{
      FILTER_FIELDS.concat(['titulo','q']).forEach(name=>{const el=form.querySelector(`[name="${name}"]`);if(el&&params.has(name))el.value=params.get(name)||'';});
      const q=form.querySelector('[name="q"]');if(q&&!params.has('q')&&params.has('titulo'))q.value=params.get('titulo')||'';
    });
  }
  function prepareCleanSubmissions(){forms.forEach(form=>form.addEventListener('submit',()=>form.querySelectorAll('input[name],select[name]').forEach(el=>{if(!String(el.value||'').trim())el.disabled=true;})));}

  function card(g){
    const tags=[g.formato].concat(g.plataforma||[]).filter(Boolean).slice(0,3).map(t=>`<span class="tag">${esc(t)}</span>`).join('');
    const rawUrl=String(g.url||'#');const siteUrl=rawUrl==='#'?'#':'/'+rawUrl.replace(/^\/+/, '');const url=esc(siteUrl);
    const img=esc(siteUrl==='#'?'/no_disponible.png':siteUrl.replace(/\/$/,'')+'/img/001.jpg');
    const gameId=esc(rawUrl.replace(/^\/+|\/+$/g,'').split('/').pop()||'game_unknown');
    const platforms=(g.plataforma||[]).filter(Boolean).slice(0,3).join(', ');let imageAlt='Portada de '+(g.titulo||'videojuego');if(g.formato)imageAlt+=', formato '+g.formato;if(platforms)imageAlt+=', para '+platforms;
    return `<a class="game-card" href="${url}" data-game-link data-game-id="${gameId}"><img src="${img}" alt="${esc(imageAlt)}" loading="lazy" decoding="async" width="420" height="315" onerror="this.onerror=null;this.src='/no_disponible.png';this.alt='Imagen no disponible';this.classList.add('missing')"><span class="game-card-body"><strong>${esc(g.titulo)}</strong><small>${esc((g.genero||[]).join(', '))}</small><span class="tagrow">${tags}</span></span></a>`;
  }
})();
'''

if __name__ == "__main__":
    raise SystemExit(main())