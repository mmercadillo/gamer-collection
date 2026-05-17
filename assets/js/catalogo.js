
(function(){
  const params = new URLSearchParams(location.search);
  const grid = document.querySelector('.grid.cards');
  const forms = document.querySelectorAll('form.catalog-search, form.search-hero');

  restoreFormValues();
  if(!params.toString() || !grid) return;

  const titulo = normalize(params.get('titulo') || params.get('q') || '');
  const formato = normalize(params.get('formato') || '');
  const serie = normalize(params.get('serie') || '');
  const genero = normalize(params.get('genero') || '');
  const plataforma = normalize(params.get('plataforma') || '');

  const games = Array.isArray(window.PCGA_SEARCH_INDEX) ? window.PCGA_SEARCH_INDEX : [];
  if(!games.length){
    grid.innerHTML = '<p class="content-card">No se pudo cargar el índice de búsqueda generado.</p>';
    return;
  }

  const selected = games.filter(g => {
    if(titulo && !normalize(g.titulo).includes(titulo)) return false;
    if(formato && normalize(g.formato) !== formato) return false;
    if(serie && !(g.serie || []).some(s => normalize(s) === serie)) return false;
    if(genero && !(g.genero || []).some(s => normalize(s).includes(genero))) return false;
    if(plataforma && !(g.plataforma || []).some(s => normalize(s) === plataforma)) return false;
    return true;
  }).slice(0, 240);

  grid.innerHTML = selected.length ? selected.map(g => card(g)).join('') : '<p class="content-card">No se han encontrado juegos con esos filtros.</p>';
  const count = document.querySelector('.count');
  if(count) count.textContent = selected.length + ' juegos encontrados.';

  function normalize(value){
    return String(value || '')
      .toLowerCase()
      .normalize('NFD')
      .replace(/[̀-ͯ]/g, '')
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
    return `<a class="game-card" href="${url}"><img src="${img}" alt="${esc(g.titulo)}" loading="lazy" width="420" height="315" onerror="this.classList.add('missing');this.removeAttribute('src')"><span class="game-card-body"><strong>${esc(g.titulo)}</strong><small>${esc((g.genero || []).join(', '))}</small><span class="tagrow">${tags}</span></span></a>`;
  }
})();
