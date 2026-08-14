
(function(){
  const PAGE_SIZE = 24;
  const params = new URLSearchParams(location.search);
  const grid = document.querySelector('[data-catalog-list], .grid.cards');
  const forms = document.querySelectorAll('form.catalog-search, form.search-hero, form.toolbar');
  const sentinel = document.querySelector('[data-load-sentinel]');

  restoreFormValues();
  prepareCleanSubmissions();
  if(!grid) return;

  const games = Array.isArray(window.PCGA_SEARCH_INDEX) ? window.PCGA_SEARCH_INDEX : [];
  if(!games.length) return;

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
  const formato = normalize(params.get('formato') || '') || defaultFormato;
  const serie = normalize(params.get('serie') || '');
  const genero = normalize(params.get('genero') || '') || defaultGenero;
  const plataforma = normalize(params.get('plataforma') || '') || defaultPlataforma;

  const selected = games.filter(g => {
    const genreBlob = normalize((g.genero || []).join(' '));
    const platformValues = (g.plataforma || []).map(normalize);
    const searchBlob = normalize(g.search_text || [g.titulo, g.formato, (g.serie||[]).join(' '), (g.genero||[]).join(' '), (g.plataforma||[]).join(' ')].join(' '));
    if(searchTerms.length && !searchTerms.every(term => searchBlob.includes(term))) return false;
    if(formato && normalize(g.formato) !== formato) return false;
    if(serie && !(g.serie || []).some(s => normalize(s) === serie)) return false;
    if(genero && !genreBlob.includes(genero)) return false;
    if(defaultGeneroAny.length && !defaultGeneroAny.some(t => genreBlob.includes(t))) return false;
    if(plataforma && !platformValues.some(s => s === plataforma)) return false;
    if(defaultPlataformaAny.length && !defaultPlataformaAny.some(t => platformValues.includes(t))) return false;
    if(defaultTextAny.length && !defaultTextAny.some(t => searchBlob.includes(t))) return false;
    if(defaultTaxonomy && defaultTaxonomyValues.length){
      const rawValues = Array.isArray(g[defaultTaxonomy]) ? g[defaultTaxonomy] : [g[defaultTaxonomy]];
      const entityValues = rawValues.map(normalize).filter(Boolean);
      if(!defaultTaxonomyValues.some(t => entityValues.includes(t))) return false;
    }
    return true;
  });

  if(rawSearchTerm && typeof gtag === 'function'){
    gtag('event','search',{
      search_term: rawSearchTerm,
      results_count: selected.length
    });
    if(!selected.length){
      gtag('event','search_no_results',{search_term: rawSearchTerm});
    }
  }

  if(typeof gtag === 'function'){
    ['formato','serie','genero','plataforma'].forEach(name => {
      const value = params.get(name);
      if(value){
        gtag('event','filter_used',{filter_name:name,filter_value:value});
      }
    });
  }

  let rendered = 0;
  grid.innerHTML = '';
  renderNextPage();

  const count = (grid.closest('section') || document).querySelector('.count');
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

  function tokenize(value){
    return normalize(value).split(/\s+/).filter(Boolean);
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
      const q = form.querySelector('[name="q"]');
      if(q && !params.has('q') && params.has('titulo')) q.value = params.get('titulo') || '';
    });
  }

  function prepareCleanSubmissions(){
    forms.forEach(form => {
      form.addEventListener('submit', () => {
        form.querySelectorAll('input[name], select[name]').forEach(el => {
          if(!String(el.value || '').trim()) el.disabled = true;
        });
      });
    });
  }

  function card(g){
    const tags = [g.formato].concat(g.plataforma || []).filter(Boolean).slice(0, 3).map(t => `<span class="tag">${esc(t)}</span>`).join('');
    const rawUrl = String(g.url || '#');
    const siteUrl = rawUrl === '#' ? '#' : '/' + rawUrl.replace(/^\/+/, '');
    const url = esc(siteUrl);
    const img = esc(siteUrl === '#' ? '/no_disponible.png' : siteUrl.replace(/\/$/, '') + '/img/001.jpg');
    const gameId = esc(rawUrl.replace(/^\/+|\/+$/g, '').split('/').pop() || 'game_unknown');
    const platforms = (g.plataforma || []).filter(Boolean).slice(0, 3).join(', ');
    let imageAlt = 'Portada de ' + (g.titulo || 'videojuego');
    if(g.formato) imageAlt += ', formato ' + g.formato;
    if(platforms) imageAlt += ', para ' + platforms;
    return `<a class="game-card" href="${url}" data-game-link data-game-id="${gameId}"><img src="${img}" alt="${esc(imageAlt)}" loading="lazy" decoding="async" width="420" height="315" onerror="this.onerror=null;this.src='/no_disponible.png';this.alt='Imagen no disponible';this.classList.add('missing')"><span class="game-card-body"><strong>${esc(g.titulo)}</strong><small>${esc((g.genero || []).join(', '))}</small><span class="tagrow">${tags}</span></span></a>`;
  }
})();
