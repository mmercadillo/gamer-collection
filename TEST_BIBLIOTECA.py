"""Pruebas de escala aisladas; no modifica el catálogo real."""
import tempfile, json, time, math
from pathlib import Path
from html.parser import HTMLParser
import generar_web as w
ROOT=Path(__file__).parent
BASE='https://www.pcgamearchive.org'
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__(); self.entries=0; self.links=[]; self.canonical=None; self.feed(path.read_text(encoding='utf-8'))
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='article' and 'documentation-entry' in a.get('class','').split(): self.entries+=1
  if tag=='a': self.links.append(a.get('href',''))
  if tag=='link' and a.get('rel')=='canonical': self.canonical=a.get('href')
def main():
 docs=w.load_documentation(ROOT/'documentacion.json'); games=w.load_json(ROOT/'juegos.json')
 hub=Page(ROOT/'documentacion/index.html'); assert hub.entries==5
 for route in w.documentation_area_routes(docs):
  p=Page(ROOT/route/'index.html'); assert 0<p.entries<=24; assert p.canonical==BASE+'/'+route
 for n in (1000,3500,10000):
  start=time.perf_counter(); rows=[dict(docs[i%len(docs)],id=f'test-{i}',titulo=f'Prueba {i:05}',url=f'documentacion/{docs[i%len(docs)]["categoria"]}/test-{i}/') for i in range(n)]
  with tempfile.TemporaryDirectory() as tmp:
   out=Path(tmp); w.generate_documentation_hub(rows,out,BASE); w.generate_documentation_library(rows,games,out,BASE)
   routes=w.documentation_area_routes(rows); total=0
   for route in routes:
    p=Page(out/route/'index.html'); assert 0<p.entries<=24; total+=p.entries; assert p.canonical==BASE+'/'+route
    for href in p.links:
     if '/pagina/' in href and not href.startswith('http'): assert (out/route/href/'index.html').resolve().is_file(), (route,href)
   assert total==n; assert Page(out/'documentacion/index.html').entries==5
   raw=(out/'assets/js/documentacion-global.js').read_text(); payload=json.loads(raw.removeprefix('window.PCGA_DOCUMENTATION=').strip().removesuffix(';')); assert len(payload['rows'])==n
   # Regenerar con menos registros elimina páginas sobrantes.
   w.generate_documentation_library(docs,games,out,BASE)
   for route in set(routes)-set(w.documentation_area_routes(docs)): assert not (out/route/'index.html').exists()
   print(f'{n}: {len(routes)} páginas, {len(raw.encode())} bytes índice global, {time.perf_counter()-start:.2f}s; OK')
if __name__=='__main__': main()
