(()=>{'use strict';
const feature=document.getElementById('pcga-feature');if(!feature)return;
const start=feature.dataset.start;if(!/^\d{4}-\d{2}-\d{2}$/.test(start))return;
const today=new Intl.DateTimeFormat('en-CA',{timeZone:'Europe/Madrid',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
const day=(s)=>Date.parse(s+'T00:00:00Z')/86400000;
const elapsed=day(today)-day(start);const active=elapsed>=0&&elapsed<14;
feature.hidden=!active;
const cards=[...document.querySelectorAll('.pcga-news-card')];
if(active){const duplicate=cards.find(c=>c.dataset.newsUrl===feature.dataset.newsUrl);if(duplicate)duplicate.hidden=true;}
let shown=0;for(const card of cards){if(card.hidden)continue;card.hidden=shown++>=4;}
})();
