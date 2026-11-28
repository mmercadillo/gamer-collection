/* PCGA: buscador documental estático; sin peticiones externas ni HTML de datos. */
(function () {
  'use strict';
  const host = document.getElementById('doc-browser');
  const data = window.PCGA_DOCUMENTATION;
  if (!host || !data || !Array.isArray(data.rows)) return;
  const root = new URL(host.dataset.root || './', location.href);
  const base = new URL(host.dataset.baseRoute, root);
  const scope = host.dataset.category;
  const staticPage = Number(host.dataset.page) || 1;
  const size = data.pageSize;
  const form = document.getElementById('doc-filter-form');
  const query = document.getElementById('doc-query');
  const sort = document.getElementById('doc-sort');
  const result = document.getElementById('doc-results');
  const counter = document.getElementById('doc-count');
  const pages = document.getElementById('doc-pages');
  const facetBox = document.getElementById('doc-facets');
  const config = {
    categoria: 'Área documental', plataforma: 'Plataforma de la edición', soporte: 'Soporte original',
    anio: 'Año documentado del juego', tecnologias: 'Tecnología de ejecución', formatos_imagen: 'Formato de imagen',
    herramientas: 'Herramienta', estado: 'Resultado de preservación', temas: 'Tema'
  };
  const fields = {
    global: ['categoria','plataforma','soporte','tecnologias','formatos_imagen','herramientas','temas','anio'],
    guias: ['plataforma','tecnologias','soporte','anio'],
    preservacion: ['soporte','formatos_imagen','herramientas','estado','anio'],
    tecnica: ['temas','tecnologias','herramientas'], laboratorio: ['temas'], formatos: ['temas','soporte'], historia: ['temas','anio']
  };
  const collator = new Intl.Collator('es', {sensitivity:'base', numeric:true});
  const norm = s => String(s || '').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
  const label = (field, value) => field === 'categoria' ? (data.categories[value]?.label || value) : value;
  const records = data.rows.map(row => ({...row, search: norm([row.titulo,row.descripcion,row.label,...row.juegos,...Object.entries(row.facetas).flatMap(([k,v])=>v.map(x=>label(k,x)))].join(' '))}));
  const selects = {};
  function el(tag, text, className) {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  }
  for (const field of fields[scope] || []) {
    const values = [...new Set(records.flatMap(r => r.facetas[field] || []))].sort((a,b)=>collator.compare(label(field,a),label(field,b)));
    if (!values.length) continue;
    const wrapper = el('div');
    const id = 'doc-facet-' + field;
    const title = el('label', config[field]); title.htmlFor = id;
    const select = el('select'); select.id = id; select.name = field;
    const all = el('option','Todos'); all.value = ''; select.append(all);
    for (const value of values) { const option = el('option', label(field,value)); option.value = value; select.append(option); }
    wrapper.append(title,select); facetBox.append(wrapper); selects[field] = select;
    select.addEventListener('change',()=>apply(1));
  }
  // El año de catálogo no está informado en todas las fichas. No se infiere.
  if (!records.some(r => r.facetas.anio?.length)) sort.querySelector('[value="anio"]').remove();
  const validSort = () => [...sort.options].map(o=>o.value);
  function readState() {
    const p = new URLSearchParams(location.search);
    query.value = p.get('q') || '';
    sort.value = validSort().includes(p.get('orden')) ? p.get('orden') : 'recientes';
    for (const [k,s] of Object.entries(selects)) {
      s.value = [...s.options].some(o=>o.value===p.get(k)) ? p.get(k) : '';
    }
    return /^\d+$/.test(p.get('pagina') || '') ? Math.max(1, Number(p.get('pagina'))) : staticPage;
  }
  function params() {
    const p = new URLSearchParams();
    if (query.value.trim()) p.set('q',query.value.trim());
    if (sort.value !== 'recientes') p.set('orden',sort.value);
    for (const [k,s] of Object.entries(selects)) if (s.value) p.set(k,s.value);
    return p;
  }
  function getResults() {
    const tokens = norm(query.value).trim().split(/\s+/).filter(Boolean);
    const active = Object.entries(selects).filter(([,s])=>s.value);
    const rows = records.filter(r=>tokens.every(t=>r.search.includes(t)) && active.every(([k,s])=>(r.facetas[k]||[]).includes(s.value)));
    const titleCompare = (a,b)=>collator.compare(a.titulo,b.titulo) || collator.compare(a.id,b.id);
    const year = r=>Math.max(0,...(r.facetas.anio || []).map(x=>Number(x)||0));
    if (sort.value === 'az') rows.sort(titleCompare);
    else if (sort.value === 'antiguos') rows.sort((a,b)=>a.fecha.localeCompare(b.fecha)||titleCompare(a,b));
    else if (sort.value === 'anio') rows.sort((a,b)=>year(b)-year(a)||titleCompare(a,b));
    // El orden reciente coincide con el HTML paginado generado en Python.
    return rows;
  }
  function pageUrl(n) {
    const p = params();
    if (scope !== 'global' && !p.size) return new URL(n===1 ? base.href : `pagina/${n}/`,base);
    const url = new URL(base.href);
    if (n>1) p.set('pagina',String(n));
    url.search = p.toString();
    return url;
  }
  function item(r) {
    const card = el('article',undefined,'documentation-entry');
    const meta = el('p',r.label+' · '+r.fecha_texto,'eyebrow');
    const heading = el('h3'); const a = el('a',r.titulo); a.href = new URL(r.url,root); heading.append(a);
    card.append(meta,heading,el('p',r.descripcion));
    return card;
  }
  function render(requested) {
    const rows = getResults();
    const total = Math.max(1,Math.ceil(rows.length/size));
    const n = Math.min(total,Math.max(1,Number.isFinite(requested)?requested:1));
    const start=(n-1)*size;
    counter.textContent = rows.length ? `${rows.length} ${rows.length===1?'documento':'documentos'} · ${start+1}–${Math.min(start+size,rows.length)} · página ${n} de ${total}` : '0 documentos encontrados';
    result.replaceChildren(...rows.slice(start,start+size).map(item));
    if (!rows.length) result.append(el('p','No se encontraron documentos. Prueba otra búsqueda o limpia los filtros.','doc-empty'));
    pages.replaceChildren();
    if (total>1) {
      const nav=el('nav',undefined,'doc-pagination'); nav.setAttribute('aria-label','Páginas de documentos');
      const add=(page,text)=>{
        const a=el('a',text); const url=pageUrl(page); a.href=url;
        if(page===n) a.setAttribute('aria-current','page');
        a.addEventListener('click',e=>{
          if(e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey) return;
          if(url.pathname!==location.pathname) return; // navegación HTML estática o retorno al índice base
          e.preventDefault(); apply(page,true);
        });
        nav.append(a);
      };
      if(n>1) add(n-1,'Anterior');
      const shown=[...new Set([1,total,...Array.from({length:Math.min(total,n+2)-Math.max(1,n-2)+1},(_,i)=>Math.max(1,n-2)+i)])].sort((a,b)=>a-b);
      shown.forEach((p,i)=>{if(i&&p>shown[i-1]+1){const dots=el('span','…');dots.setAttribute('aria-hidden','true');nav.append(dots);} add(p,String(p));});
      if(n<total) add(n+1,'Siguiente');
      pages.append(nav);
    }
    return n;
  }
  function apply(n, focus=false) {
    const actual=render(n);
    const url=pageUrl(actual);
    if(url.pathname!==location.pathname) { location.assign(url.href); return; }
    if(url.href!==location.href) history.pushState(null,'',url);
    if(focus){counter.tabIndex=-1;counter.focus();counter.scrollIntoView({block:'center'});}
  }
  form.addEventListener('submit',e=>{e.preventDefault();apply(1);});
  sort.addEventListener('change',()=>apply(1));
  document.getElementById('doc-reset').addEventListener('click',()=>{query.value='';sort.value='recientes';for(const s of Object.values(selects))s.value='';apply(1);query.focus();});
  window.addEventListener('popstate',()=>render(readState()));
  form.hidden=false;
  render(readState());
})();
