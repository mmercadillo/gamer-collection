"""Regresión del modelo de documentación técnica. Ejecutar desde la raíz:
    python TEST_DOCUMENTACION_TECNICA.py
No modifica el proyecto ni requiere dependencias de terceros.
"""
import json
import re
import tempfile
import unittest
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
import generar_web as web

ROOT = Path(__file__).resolve().parent
TECH_ID = 'tecnica-windows-31-dosbox-staging-portable'
TECH_ROUTE = 'documentacion/tecnica/windows-31-dosbox-staging-portable/'
HUB = 'documentacion/tecnica/'
BASE = 'https://www.pcgamearchive.org/'
GAME_DOCS = (
    'guia-in-the-1st-degree-asesinato-en-primer-grado-bigbox-portable',
    'guia-lode-runner-the-legend-returns-bigbox-portable',
)

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(); self.hrefs = []; self.images = []; self.canonical = None
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == 'a' and d.get('href'): self.hrefs.append(d['href'])
        if tag == 'img' and 'doc-inline-image' in d.get('class', '').split(): self.images.append(d['src'])
        if tag == 'link' and d.get('rel') == 'canonical': self.canonical = d.get('href')

class TestDocumentacionTecnica(unittest.TestCase):
    def setUp(self):
        self.raw = json.loads((ROOT/'documentacion.json').read_text(encoding='utf-8'))
        self.documents = web.load_documentation(ROOT/'documentacion.json')
        self.byid = {d['id']: d for d in self.documents}
    def invalid(self, change):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/'index.json'; change(self.raw); p.write_text(json.dumps(self.raw), encoding='utf-8')
            with self.assertRaises(ValueError): web.load_documentation(p)
    def entry(self, key): return next(d for d in self.raw if d['id'] == key)
    def test_reference_model(self):
        self.assertEqual(self.byid[TECH_ID]['juegos'], [])
        self.assertEqual(self.byid[TECH_ID]['url'], TECH_ROUTE)
        for key in GAME_DOCS: self.assertIn(TECH_ID, self.byid[key]['referencias_documentales'])
        web.validate_documentation_sources(self.documents, ROOT)
        index = web.build_documentation_game_index(self.documents)
        self.assertFalse(any(d['id'] == TECH_ID for ds in index.values() for d in ds))
    def test_unknown_reference(self):
        self.invalid(lambda _: self.entry(GAME_DOCS[0]).update(referencias_documentales=['no-existe']))
    def test_duplicate_reference(self):
        self.invalid(lambda _: self.entry(GAME_DOCS[0]).update(referencias_documentales=[TECH_ID, TECH_ID]))
    def test_self_reference(self):
        self.invalid(lambda _: self.entry(TECH_ID).update(referencias_documentales=[TECH_ID]))
    def test_invalid_reference_type(self):
        self.invalid(lambda _: self.entry(GAME_DOCS[0]).update(referencias_documentales=TECH_ID))
    def test_reserved_route(self):
        self.invalid(lambda _: self.entry(TECH_ID).update(url=HUB))
    def test_technical_not_bound_to_game(self):
        self.invalid(lambda _: self.entry(TECH_ID).update(juegos=self.entry(GAME_DOCS[0])['juegos']))
    def test_routes_and_sitemap(self):
        ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls=[e.text for e in ET.parse(ROOT/'sitemap.xml').findall('s:url/s:loc',ns)]
        for route in (HUB, TECH_ROUTE, *[self.byid[k]['url'] for k in GAME_DOCS]):
            self.assertEqual(urls.count(BASE+route),1)
            self.assertEqual(Page(ROOT/route/'index.html').canonical,BASE+route)
        self.assertTrue(any(HUB in x for x in Page(ROOT/'documentacion/index.html').hrefs))
        self.assertTrue(any(TECH_ROUTE in x for x in Page(ROOT/HUB/'index.html').hrefs))
    def test_generated_links_and_images(self):
        for key in GAME_DOCS:
            d=self.byid[key]; page=Page(ROOT/d['url']/'index.html')
            self.assertTrue(any('tecnica/windows-31-dosbox-staging-portable/' in x for x in page.hrefs))
            if key==GAME_DOCS[0]:
                self.assertFalse(any('lode-runner-the-legend-returns' in x for x in page.hrefs))
                self.assertGreaterEqual(len(page.images),18)
        path=ROOT/TECH_ROUTE/'index.html'; page=Page(path)
        self.assertGreaterEqual(len(page.images),10)
        for key in GAME_DOCS: self.assertTrue(any(self.byid[key]['url'] in x for x in page.hrefs))
        self.assertNotIn('Piezas relacionadas',path.read_text(encoding='utf-8'))
        for src in page.images: self.assertTrue((path.parent/src).is_file())
    def test_configuration_transcription(self):
        d=self.byid[GAME_DOCS[0]]; source=(ROOT/d['contenido']).read_text(encoding='utf-8')
        original=(ROOT/'registros_compatibilidad/in-the-1st-degree-asesinato-en-primer-grado-bigbox/dosbox.conf').read_text(encoding='utf-8').strip()
        self.assertIn(original, re.findall(r'```ini\n(.*?)\n```',source,re.S))
        self.assertNotIn('AUTOEXEC.@echo',source)
    def test_nonempty_areas_and_permanent_access(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            web.generate_documentation_hub(self.documents, out, BASE.rstrip('/'))
            web.generate_documentation_library(self.documents, web.load_json(ROOT/'juegos.json'), out, BASE.rstrip('/'))
            path = out/'documentacion/index.html'
            html = path.read_text(encoding='utf-8')
            page = Page(path)
            for key in ('historia', 'formatos'):
                self.assertNotIn(web.DOCUMENTATION_CATEGORIES[key]['label'], html)
                self.assertFalse((out/web.DOCUMENTATION_AREA_ROUTES[key]/'index.html').exists())
            for key in ('laboratorio', 'preservacion', 'guias', 'tecnica'):
                route = web.DOCUMENTATION_AREA_ROUTES[key]
                self.assertTrue(any(href.endswith(route) for href in page.hrefs))
                index = Page(out/route/'index.html')
                for d in self.documents:
                    if d['categoria'] == key:
                        self.assertTrue(any(href.endswith(d['url']) for href in index.hrefs), d['id'])
            self.assertEqual(html.count('class="documentation-entry"'),5)
            sample = dict(self.documents[0], categoria='historia', id='test-historia', url='documentacion/historia/test/')
            web.generate_documentation_hub(self.documents + [sample], out, BASE.rstrip('/'))
            web.generate_documentation_library(self.documents + [sample], [], out, BASE.rstrip('/'))
            self.assertTrue(any(href.endswith('documentacion/historia/') for href in Page(path).hrefs))
            self.assertTrue((out/'documentacion/historia/index.html').is_file())

    def test_independent_output_images(self):
        games=web.load_json(ROOT/'juegos.json')
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)
            web.generate_documentation_hub(self.documents,out,BASE.rstrip('/'))
            web.generate_documentation_library(self.documents,games,out,BASE.rstrip('/'))
            web.generate_documentation_pages(self.documents,games,out,ROOT,BASE.rstrip('/'))
            p=out/TECH_ROUTE/'index.html'; page=Page(p)
            self.assertGreaterEqual(len(page.images),10)
            for src in page.images: self.assertTrue((p.parent/src).is_file())
            self.assertTrue((out/HUB/'index.html').is_file())

if __name__=='__main__': unittest.main(verbosity=2)
