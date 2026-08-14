(function(){
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
    const resultsMeta=countEl ? countEl.closest('.search-results-meta') : null;
    if(resultsMeta) resultsMeta.insertAdjacentElement('afterend',box);
    else if(countEl) countEl.insertAdjacentElement('afterend',box);
    else grid.insertAdjacentElement('beforebegin',box);
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
