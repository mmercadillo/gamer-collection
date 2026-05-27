
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
