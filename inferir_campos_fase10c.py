#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inferencia conservadora de campos documentales de Fase 10C.

Rellena únicamente campos vacíos de juegos.json usando evidencia explícita ya
presente en la propia ficha. Nunca consulta fuentes externas y nunca inventa
valores cuando no existe evidencia suficiente.

Los valores candidatos se obtienen dinámicamente de json_schema.json y se
validan antes de escribirse. Tras la inferencia se compara la validación JSON
Schema completa antes/después: si aparecen errores nuevos, no se guarda nada.

Uso:
    python inferir_campos_fase10c.py --dry-run
    python inferir_campos_fase10c.py --output juegos_inferidos.json
    python inferir_campos_fase10c.py
    python inferir_campos_fase10c.py --juegos otro.json --schema json_schema.json
"""

from __future__ import annotations

import argparse
import copy
import csv
import datetime as dt
import json
import re
import shutil
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

from jsonschema import Draft202012Validator

FIELDS = ("anio", "mercado", "idioma", "soporte", "tipo_edicion")


def norm(text: object) -> str:
    s = str(text or "").casefold()
    s = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in s if not unicodedata.combining(ch))


def as_strings(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(v) for v in value if isinstance(v, (str, int, float))]
    if isinstance(value, str):
        return [value]
    return []


def evidence_sources(game: dict) -> dict[str, list[str]]:
    return {
        "titulo": as_strings(game.get("titulo")),
        "descripcion": as_strings(game.get("descripcion")),
        "incluye": as_strings(game.get("incluye")),
        "serie": as_strings(game.get("serie")),
        "tags": as_strings(game.get("tags")),
    }


def schema_allowed(schema: dict) -> dict[str, object]:
    props = schema["properties"]
    return {
        "anio_pattern": re.compile(props["anio"]["pattern"]),
        "mercado": set(props["mercado"]["items"]["enum"]),
        "idioma": set(props["idioma"]["items"]["enum"]),
        "soporte": set(props["soporte"]["items"]["enum"]),
        "tipo_edicion": set(props["tipo_edicion"]["items"]["enum"]),
    }


def add_candidate(out: dict[str, list[tuple[str, str]]], field: str, value: str, evidence: str, allowed: dict) -> None:
    if field == "anio":
        if not allowed["anio_pattern"].fullmatch(value):
            return
    elif value not in allowed[field]:
        return
    pair = (value, evidence.strip())
    if pair not in out[field]:
        out[field].append(pair)


# --- AÑO -----------------------------------------------------------------
# Solo expresiones que vinculan explícitamente una edición/publicación local
# con el año. Se excluye deliberadamente "publicado originalmente en ...".
YEAR_PATTERNS = [
    # "Edición ... lanzada/publicada en 2006" o con fecha completa.
    re.compile(r"(?i)\bedici[oó]n\b[^.!?]{0,90}?\b(?:lanzada|publicada|editada)\b(?!\s+originalmente)\s+(?:el\s+\d{1,2}\s+de\s+[a-záéíóúñ]+\s+de\s+|en\s+(?:el\s+año\s+)?|en\s+[a-záéíóúñ]+\s+de\s+)?((?:19|20)\d{2})\b"),
    # "distribuida en España el 23 de septiembre de 2010".
    re.compile(r"(?i)\bedici[oó]n\b[^.!?]{0,70}?\bdistribuida\s+en\s+(?:espa[ñn]a|portugal|europa)\s+(?:el\s+\d{1,2}\s+de\s+[a-záéíóúñ]+\s+de\s+|en\s+(?:el\s+año\s+)?)((?:19|20)\d{2})\b"),
    # Publicación local explícita: "publicada en España por X en 1998".
    re.compile(r"(?i)\b(?:publicada|lanzada|editada)\s+en\s+(?:espa[ñn]a|portugal)\b[^.!?]{0,55}?\ben\s+((?:19|20)\d{2})\b"),
    # "distribuida en el año 2000" cuando la frase habla de la edición.
    re.compile(r"(?i)\bedici[oó]n\b[^.!?]{0,80}?\bdistribuida\s+en\s+el\s+año\s+((?:19|20)\d{2})\b"),
]


def infer_year(game: dict, out: dict, allowed: dict) -> None:
    # El año se infiere solo desde descripción; título/tags contienen muchos años
    # temáticos, temporadas o nombres de producto que no son fecha de edición.
    desc = game.get("descripcion") or ""
    candidates = []
    for pat in YEAR_PATTERNS:
        for m in pat.finditer(desc):
            candidates.append((m.group(1), m.group(0)))
    years = {y for y, _ in candidates}
    # Si la propia evidencia apunta a más de un año, no elegimos ninguno.
    if len(years) == 1:
        y = next(iter(years))
        ev = next(e for yy, e in candidates if yy == y)
        add_candidate(out, "anio", y, f"descripcion: {ev}", allowed)


# --- MERCADO --------------------------------------------------------------
MARKET_ADJ = {
    "España": ("espanola", "espanol", "hispana", "hispano"),
    "Portugal": ("portuguesa", "portugues"),
    "Francia": ("francesa",),
    "Alemania": ("alemana",),
    "Italia": ("italiana",),
    "Reino Unido": ("britanica", "britanico"),
    "Irlanda": ("irlandesa", "irlandes"),
    "Países Bajos": ("neerlandesa", "holandesa"),
    "Bélgica": ("belga",),
    "Austria": ("austriaca", "austriaco"),
    "Suiza": ("suiza", "suizo"),
    "Polonia": ("polaca", "polaco"),
    "República Checa": ("checa", "checo"),
    "Hungría": ("hungara", "hungaro"),
    "Grecia": ("griega", "griego"),
    "Europa": ("europea", "europeo"),
    "Estados Unidos": ("estadounidense", "americana", "americano"),
    "Canadá": ("canadiense",),
    "México": ("mexicana", "mexicano"),
    "Brasil": ("brasilena", "brasileno"),
    "Argentina": ("argentina", "argentino"),
    "Latinoamérica": ("latinoamericana", "latinoamericano"),
    "Australia": ("australiana", "australiano"),
    "Nueva Zelanda": ("neozelandesa", "neozelandes"),
    "Japón": ("japonesa", "japones"),
    "Corea del Sur": ("surcoreana", "surcoreano"),
    "China": ("china", "chino"),
    "Asia": ("asiatica", "asiatico"),
    "Internacional": ("internacional",),
}
MARKET_COUNTRY = {
    "España": ("espana",), "Portugal": ("portugal",), "Francia": ("francia",),
    "Alemania": ("alemania",), "Italia": ("italia",), "Reino Unido": ("reino unido", "uk"),
    "Irlanda": ("irlanda",), "Países Bajos": ("paises bajos", "holanda"), "Bélgica": ("belgica",),
    "Austria": ("austria",), "Suiza": ("suiza",), "Polonia": ("polonia",),
    "República Checa": ("republica checa",), "Hungría": ("hungria",), "Grecia": ("grecia",),
    "Europa": ("europa",), "Estados Unidos": ("estados unidos", "usa"), "Canadá": ("canada",),
    "México": ("mexico",), "Brasil": ("brasil",), "Argentina": ("argentina",),
    "Latinoamérica": ("latinoamerica",), "Australia": ("australia",), "Nueva Zelanda": ("nueva zelanda",),
    "Japón": ("japon",), "Corea del Sur": ("corea del sur",), "China": ("china",), "Asia": ("asia",),
}


def infer_market(game: dict, out: dict, allowed: dict) -> None:
    src = evidence_sources(game)
    # Solo cláusulas cortas que describen explícitamente la edición/versión,
    # distribución o mercado. Así "aventura europea" o países del argumento
    # no se convierten en mercado de la copia catalogada.
    for field in ("titulo", "descripcion", "tags"):
        for raw in src[field]:
            for clause_raw in re.split(r"[.!?;,]", raw):
                clause = norm(clause_raw)
                if not clause.strip():
                    continue

                # Adjetivos: deben estar ligados a edición/versión/distribución.
                for market, adjectives in MARKET_ADJ.items():
                    for adjective in adjectives:
                        linked = False
                        # El adjetivo debe aparecer muy cerca de "edición/versión".
                        # Esto admite "edición física española/portuguesa" pero no
                        # "edición representativa de la aventura gráfica europea".
                        for cue in ("edicion", "version"):
                            for m in re.finditer(rf"\b{cue}\b", clause):
                                tail = clause[m.end():m.end() + 34]
                                if re.search(rf"\b{re.escape(adjective)}\b", tail):
                                    linked = True
                                    break
                            if linked:
                                break
                        if (linked or
                            re.search(rf"\bdistribucion\s+{re.escape(adjective)}\b", clause) or
                            re.search(rf"\bmercado\s+{re.escape(adjective)}\b", clause)):
                            add_candidate(out, "mercado", market, f"{field}: {clause_raw.strip()}", allowed)

                # Nombres de país/región solo con verbos o construcciones comerciales.
                for market, names in MARKET_COUNTRY.items():
                    for name in names:
                        patterns = [
                            rf"\b(?:distribuida|publicada|lanzada|editada)\s+en\s+(?:el\s+|la\s+)?{re.escape(name)}\b",
                            rf"\bdestinada\s+(?:al?|para)\s+(?:el\s+|la\s+)?{re.escape(name)}\b",
                            rf"\bmercado\s+(?:de\s+)?{re.escape(name)}\b",
                        ]
                        if any(re.search(p, clause) for p in patterns):
                            add_candidate(out, "mercado", market, f"{field}: {clause_raw.strip()}", allowed)



# --- IDIOMA ---------------------------------------------------------------
LANG_WORDS = {
    "Español": ("espanol", "castellano"),
    "Catalán": ("catalan",), "Gallego": ("gallego",), "Euskera": ("euskera", "vasco"),
    "Portugués": ("portugues",), "Inglés": ("ingles",), "Francés": ("frances",),
    "Alemán": ("aleman",), "Italiano": ("italiano",), "Neerlandés": ("neerlandes", "holandes"),
    "Danés": ("danes",), "Sueco": ("sueco",), "Noruego": ("noruego",), "Finés": ("fines",),
    "Polaco": ("polaco",), "Checo": ("checo",), "Húngaro": ("hungaro",), "Rumano": ("rumano",),
    "Ruso": ("ruso",), "Turco": ("turco",), "Japonés": ("japones",), "Coreano": ("coreano",),
    "Multilingüe": ("multilingue",),
}
LANG_MEDIA = r"(?:manual(?:es)?|documentacion|software|juego|textos?|subtitulos?|voces?|voz|interfaz|audio)"


def infer_language(game: dict, out: dict, allowed: dict) -> None:
    src = evidence_sources(game)
    pieces: list[tuple[str, str]] = []
    pieces.extend(("incluye", raw) for raw in src["incluye"])
    pieces.extend(("tags", raw) for raw in src["tags"])
    for raw in src["descripcion"]:
        pieces.extend(("descripcion", sentence) for sentence in re.split(r"[.!?;]", raw))

    for field, raw in pieces:
        n = norm(raw)
        if not n.strip():
            continue

        # Multilingüe es una afirmación inequívoca si describe edición,
        # documentación, manual, software o presentación.
        if re.search(r"\bmultilingue\b", n) and re.search(r"\b(edicion|documentacion|manual|software|presentacion|embalaje)\b", n):
            add_candidate(out, "idioma", "Multilingüe", f"{field}: {raw.strip()}", allowed)

        for lang, words in LANG_WORDS.items():
            if lang == "Multilingüe":
                continue
            for word in words:
                # Construcciones inequívocas: "manual en castellano",
                # "voces originales en inglés", "traducido al castellano", etc.
                explicit = [
                    rf"\b{LANG_MEDIA}\b[^.!?]{{0,40}}?\b(?:en|al|a)\s+{re.escape(word)}\b",
                    rf"\b(?:traducid[oa]|doblad[oa]|localizad[oa])\b[^.!?]{{0,25}}?\b(?:al|a|en)\s+{re.escape(word)}\b",
                    rf"\bidioma(?:s)?\b[^.!?]{{0,15}}?\b{re.escape(word)}\b",
                    rf"\bversion\s+en\s+{re.escape(word)}\b",
                ]
                matched = any(re.search(p, n) for p in explicit)

                # En elementos cortos de "incluye", una construcción como
                # "Manual en español/portugués" permite extraer ambos idiomas.
                if field == "incluye" and re.search(rf"\b{LANG_MEDIA}\b", n) and " en " in n and re.search(rf"\b{re.escape(word)}\b", n):
                    matched = True

                # Tags documentales concretos: "software en inglés",
                # "manual en español", "voces en inglés", etc.
                if field == "tags" and re.search(rf"\b{LANG_MEDIA}\b", n) and re.search(rf"\b(?:en|al)\s+{re.escape(word)}\b", n):
                    matched = True

                if matched:
                    add_candidate(out, "idioma", lang, f"{field}: {raw.strip()}", allowed)



# --- SOPORTE --------------------------------------------------------------
def _infer_support_piece(field: str, raw: str, out: dict, allowed: dict, extras: bool) -> None:
    n = norm(raw).replace("½", ".5").replace("¼", ".25")
    if re.search(r"\bdvd[\s-]?rom\b", n):
        add_candidate(out, "soporte", "DVD-ROM", f"{field}: {raw}", allowed)
    if re.search(r"\bcd[\s-]?rom\b", n):
        add_candidate(out, "soporte", "CD-ROM", f"{field}: {raw}", allowed)
    if re.search(r"\bblu[\s-]?ray\b", n):
        add_candidate(out, "soporte", "Blu-ray Disc", f"{field}: {raw}", allowed)
    if re.search(r"\b(?:disquete|disquetes|floppy|floppies)\b[^\n]{0,30}\b3\s*[,.]\s*5\b", n) or re.search(r"\b3\s*[,.]\s*5\b[^\n]{0,20}\b(?:disquete|disquetes)\b", n):
        add_candidate(out, "soporte", 'Disquete 3,5"', f"{field}: {raw}", allowed)
    if re.search(r"\b(?:disquete|disquetes|floppy|floppies)\b[^\n]{0,30}\b5\s*[,.]\s*25\b", n) or re.search(r"\b5\s*[,.]\s*25\b[^\n]{0,20}\b(?:disquete|disquetes)\b", n):
        add_candidate(out, "soporte", 'Disquete 5,25"', f"{field}: {raw}", allowed)

    # Extras físicos solo se infieren desde "incluye", nunca desde tags o
    # descripción, para no confundir audio Red Book o una mención histórica.
    if extras:
        if re.search(r"\b(?:cd|compact disc)\b[^\n]{0,45}\b(?:banda sonora|soundtrack|audio)\b", n) or re.search(r"\b(?:banda sonora|soundtrack)\b[^\n]{0,45}\bcd\b", n):
            add_candidate(out, "soporte", "CD de audio", f"{field}: {raw}", allowed)
        if not re.search(r"\bdvd[\s-]?rom\b", n) and re.search(r"\bdvd\b[^\n]{0,60}\b(?:video|documental|entre bastidores|making of|extras?)\b", n):
            add_candidate(out, "soporte", "DVD de vídeo", f"{field}: {raw}", allowed)
        if re.search(r"\b(?:usb|pendrive|memory stick usb|memoria usb)\b", n):
            add_candidate(out, "soporte", "USB", f"{field}: {raw}", allowed)
        if re.search(r"\bcodigo\s+de\s+descarga\b|\bdownload\s+code\b", n):
            add_candidate(out, "soporte", "Código de descarga", f"{field}: {raw}", allowed)
        if re.search(r"\bsin\s+soporte\s+fisico\b", n):
            add_candidate(out, "soporte", "Sin soporte físico", f"{field}: {raw}", allowed)


def infer_support(game: dict, out: dict, allowed: dict) -> None:
    src = evidence_sources(game)
    incluye = src["incluye"]
    if incluye:
        for raw in incluye:
            _infer_support_piece("incluye", raw, out, allowed, extras=True)
    else:
        # Cuando no hay inventario en "incluye", admitimos tags explícitos como
        # segunda mejor evidencia. Nunca usamos descripción general del juego.
        for raw in src["tags"]:
            _infer_support_piece("tags", raw, out, allowed, extras=False)



# --- TIPO DE EDICIÓN ------------------------------------------------------
EDITION_RULES: list[tuple[str, re.Pattern]] = [
    ("Edición coleccionista", re.compile(r"\bedicion(?:\s+de)?\s+coleccionistas?\b|\bcollector'?s?\s+edition\b")),
    ("Edición limitada", re.compile(r"\bedicion\s+limitada\b|\blimited\s+edition\b")),
    ("Edición especial", re.compile(r"\bedicion\s+especial\b|\bspecial\s+edition\b")),
    ("Budget", re.compile(r"\bbudget\b|\bprecio\s+reducido\b|\bgama\s+economica\b|\breedicion\s+economica\b")),
    ("Reedición", re.compile(
        r"\besta\s+(?:edicion|version)\b[^.!?]{0,100}?\b(?:reedicion|reeditad[oa])\b|"
        r"\breedicion\s+de\b|\bidentifica\s+esta\s+reedicion\b|\bcomo\s+reedicion\b"
    )),
    ("Compilación", re.compile(
        r"\bedicion\s+(?:de\s+oro\s+)?recopilatoria\b|"
        r"\b(?:recopilacion|compilacion)\s+(?:fisica\s+)?(?:que\s+)?(?:incluye|reune)\b|"
        r"\b(?:recopilacion|compilacion)\s+de\s+(?:juegos|clasicos|titulos|la\s+saga)\b|"
        r"\bes\s+una\s+(?:recopilacion|compilacion)\b|"
        r"\banthology\b"
    )),
    ("Colección", re.compile(r"\b(?:forma\s+parte\s+de\s+la|pertenece\s+a\s+la|dentro\s+de\s+la|reeditad[oa]\s+dentro\s+de\s+la)\s+coleccion\b|\bcoleccion\s+editorial\b")),
    ("Bundle/Pack", re.compile(r"\bbundle\b|\bpack\s+(?:que\s+reune|de\s+\d+\s+juegos|recopilatorio)\b")),
    ("OEM", re.compile(r"\bedicion\s+oem\b|\bversion\s+oem\b")),
    ("Promocional", re.compile(r"\bedicion\s+promocional\b|\bversion\s+promocional\b|\bpromotional\s+edition\b")),
    ("Prensa", re.compile(r"\bpress\s+kit\b|\bedicion\s+de\s+prensa\b|\bversion\s+de\s+prensa\b")),
    ("Demo", re.compile(r"\bedicion\s+demo\b|\bversion\s+demo\b|\bdemo\s+disc\b")),
    ("Shareware", re.compile(r"\bedicion\s+shareware\b|\bversion\s+shareware\b")),
]
UNCERTAINTY_RE = re.compile(r"\b(?:potencialmente|posiblemente|probablemente|quizas|tal\s+vez|podria)\b")


def infer_edition_type(game: dict, out: dict, allowed: dict) -> None:
    src = evidence_sources(game)
    pieces: list[tuple[str, str]] = []
    pieces.extend(("titulo", raw) for raw in src["titulo"])
    pieces.extend(("tags", raw) for raw in src["tags"])
    pieces.extend(("serie", raw) for raw in src["serie"])
    for raw in src["descripcion"]:
        pieces.extend(("descripcion", sentence) for sentence in re.split(r"[.!?;]", raw))

    for field, raw in pieces:
        n = norm(raw)
        if UNCERTAINTY_RE.search(n):
            continue
        for value, pat in EDITION_RULES:
            if pat.search(n):
                add_candidate(out, "tipo_edicion", value, f"{field}: {raw.strip()}", allowed)



def infer_game(game: dict, allowed: dict) -> dict[str, list[tuple[str, str]]]:
    out = {f: [] for f in FIELDS}
    infer_year(game, out, allowed)
    infer_market(game, out, allowed)
    infer_language(game, out, allowed)
    infer_support(game, out, allowed)
    infer_edition_type(game, out, allowed)
    return out


def error_signature(err) -> tuple:
    return (tuple(err.absolute_path), err.validator, json.dumps(err.validator_value, ensure_ascii=False, sort_keys=True, default=str))


def validate_games(games: list[dict], schema: dict) -> list:
    v = Draft202012Validator(schema)
    errors = []
    for i, game in enumerate(games):
        for err in v.iter_errors(game):
            # Prefijamos el índice de juego a la ruta para comparar exactamente.
            err._pcga_index = i  # atributo auxiliar solo en memoria
            errors.append(err)
    return errors


def validation_signatures(errors: list) -> set[tuple]:
    return {(getattr(e, "_pcga_index", -1),) + error_signature(e) for e in errors}


def main() -> int:
    ap = argparse.ArgumentParser(description="Inferencia conservadora de campos Fase 10C")
    ap.add_argument("--juegos", default="juegos.json")
    ap.add_argument("--schema", default="json_schema.json")
    ap.add_argument("--dry-run", action="store_true", help="No modifica juegos.json")
    ap.add_argument("--output", help="Escribe el catálogo inferido en otro fichero sin modificar juegos.json")
    ap.add_argument("--report-prefix", default="informe_inferencia_fase10c")
    args = ap.parse_args()

    juegos_path = Path(args.juegos)
    schema_path = Path(args.schema)
    games = json.loads(juegos_path.read_text(encoding="utf-8"))
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    if not isinstance(games, list):
        raise SystemExit("ERROR: juegos.json debe contener un array")

    allowed = schema_allowed(schema)
    before = copy.deepcopy(games)
    before_errors = validate_games(before, schema)
    before_sig = validation_signatures(before_errors)

    changes = []
    counts = Counter()
    value_counts = defaultdict(Counter)

    for idx, game in enumerate(games):
        inferred = infer_game(game, allowed)
        for field in FIELDS:
            current = game.get(field)
            # Nunca sobrescribir datos ya documentados.
            if field == "anio":
                empty = current == "" or current is None
            else:
                empty = current == [] or current is None
            if not empty:
                continue

            pairs = inferred[field]
            if not pairs:
                continue
            if field == "anio":
                values = sorted({v for v, _ in pairs})
                if len(values) != 1:
                    continue
                new_value = values[0]
            else:
                # Orden según el enum del schema, no alfabético, para mantener
                # una salida estable y semánticamente coherente.
                enum_order = list(schema["properties"][field]["items"]["enum"])
                inferred_values = {v for v, _ in pairs}
                new_value = [v for v in enum_order if v in inferred_values]
                if not new_value:
                    continue

            # Validación local del candidato contra la definición exacta del campo.
            field_validator = Draft202012Validator(schema["properties"][field])
            local_errors = list(field_validator.iter_errors(new_value))
            if local_errors:
                continue

            game[field] = new_value
            counts[field] += 1
            if isinstance(new_value, list):
                value_counts[field].update(new_value)
            else:
                value_counts[field][new_value] += 1
            changes.append({
                "index": idx,
                "num": game.get("num", ""),
                "titulo": game.get("titulo", ""),
                "url": game.get("url", ""),
                "campo": field,
                "antes": current,
                "despues": new_value,
                "evidencia": " || ".join(dict.fromkeys(e for _, e in pairs)),
            })

    after_errors = validate_games(games, schema)
    after_sig = validation_signatures(after_errors)
    new_errors = after_sig - before_sig
    if new_errors:
        print(f"ERROR: la inferencia introduciría {len(new_errors)} errores JSON Schema nuevos. No se guarda nada.", file=sys.stderr)
        return 2

    # Informes siempre, también en dry-run.
    prefix = Path(args.report_prefix)
    json_report = prefix.with_suffix(".json")
    csv_report = prefix.with_suffix(".csv")
    summary = {
        "fecha": dt.datetime.now().isoformat(timespec="seconds"),
        "dry_run": args.dry_run,
        "total_juegos": len(games),
        "cambios_por_campo": dict(counts),
        "valores_por_campo": {k: dict(v) for k, v in value_counts.items()},
        "errores_schema_antes": len(before_errors),
        "errores_schema_despues": len(after_errors),
        "errores_schema_nuevos": 0,
        "cambios": changes,
    }
    json_report.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with csv_report.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["index", "num", "titulo", "url", "campo", "antes", "despues", "evidencia"])
        w.writeheader()
        for row in changes:
            row = dict(row)
            row["antes"] = json.dumps(row["antes"], ensure_ascii=False)
            row["despues"] = json.dumps(row["despues"], ensure_ascii=False)
            w.writerow(row)

    if args.dry_run and args.output:
        print("ERROR: --dry-run y --output son excluyentes.", file=sys.stderr)
        return 3

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(json.dumps(games, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Catálogo inferido escrito en: {output_path}")
        print(f"Original sin modificar: {juegos_path}")
    elif not args.dry_run:
        stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup = juegos_path.with_name(juegos_path.name + f".bak_fase10c_{stamp}")
        shutil.copy2(juegos_path, backup)
        juegos_path.write_text(json.dumps(games, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Backup: {backup}")
        print(f"Actualizado: {juegos_path}")
    else:
        print("DRY-RUN: juegos.json no ha sido modificado.")

    print(f"Juegos: {len(games)}")
    for field in FIELDS:
        print(f"  {field}: {counts[field]} fichas inferidas")
        if value_counts[field]:
            top = ", ".join(f"{k}={v}" for k, v in value_counts[field].most_common(12))
            print(f"    {top}")
    print(f"Errores JSON Schema: {len(before_errors)} -> {len(after_errors)} (nuevos: 0)")
    print(f"Informe JSON: {json_report}")
    print(f"Informe CSV: {csv_report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
