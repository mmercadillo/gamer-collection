# PC Game Archive

Archivo digital dedicado a la preservación, documentación y catalogación de videojuegos clásicos de PC en formato físico.

El proyecto está centrado especialmente en:

- Big Box
- CD/DVD Case
- Jewel Case
- ediciones españolas y europeas
- software clásico MS-DOS y Windows
- preservación documental y física

Sitio web oficial:

https://www.pcgamearchive.org

Instagram:

https://www.instagram.com/pc_game_archive/

---

# Objetivos del proyecto

PC Game Archive nace con el objetivo de:

- preservar ediciones físicas históricas de videojuegos para PC,
- documentar contenidos y variantes físicas,
- registrar distribuciones españolas y europeas,
- conservar información técnica y documental,
- facilitar catalogación estructurada,
- y crear un archivo digital accesible y navegable.

El proyecto NO está orientado a ROM sharing ni distribución de software protegido.

---

# Tecnologías utilizadas

El sitio está construido como una web estática generada automáticamente a partir de un catálogo JSON centralizado.

Stack actual:

- HTML5
- CSS3
- JavaScript
- Python
- GitHub Pages

Características:

- generación estática SEO-friendly,
- páginas individuales por juego,
- página institucional `/proyecto/` con propósito, conservación y roadmap,
- landing de compra/donación con explicación del tratamiento del material,
- sitemap automático,
- robots.txt automático,
- buscador integrado,
- navegación por series y formatos,
- responsive/mobile-friendly,
- preparado para futura evolución a PWA.

---

# Estructura del proyecto

```text
/
├── juegos.json
├── json_schema.json
├── generar_web.py
├── validar_catalogo.py
├── sitemap.xml
├── robots.txt
├── logo.png
├── proyecto/
│   └── index.html
├── vender-videojuegos-pc-antiguos/
│   └── index.html
├── incorporaciones/              # Se genera cuando existen fechas documentadas
│   └── index.html
├── assets/
│   ├── css/
│   └── js/
├── desarrolladores/
├── distribuidores/
├── generos/
├── plataformas/
├── formatos/
└── juegos/
    ├── doom-bigbox/
    │   ├── index.html
    │   └── img/
    ├── diablo-bigbox/
    │   ├── index.html
    │   └── img/
    └── ...
```

---

# Cómo añadir un nuevo juego

## 1. Añadir entrada en `juegos.json`

Cada juego se define mediante un objeto JSON validado contra el schema oficial del proyecto.

`fecha_incorporacion` registra cuándo la edición se incorpora documentalmente a PC Game Archive y utiliza formato ISO `YYYY-MM-DD`. Para fichas históricas cuya fecha real no está documentada se mantiene como cadena vacía (`""`); no debe inferirse a partir de `num`, Instagram ni del orden del JSON.

Ejemplo:

```json
{
  "num": "000999",
  "ig": "",
  "fecha_incorporacion": "2026-09-19",
  "titulo": "Example Game",
  "url": "juegos/example-game-bigbox/",
  "formato": "Big Box"
}
```

---

## 2. Crear carpeta del juego

```text
juegos/example-game-bigbox/
└── img/
    ├── 001.jpg
    ├── 002.jpg
    └── 003.jpg
```

---

## 3. Validar catálogo

```bash
python validar_catalogo.py
```

---

## 4. Regenerar la web

```bash
python generar_web.py
```

El generador:

- NO copia imágenes,
- NO duplica assets,
- únicamente sobrescribe:
  - HTML generado,
  - sitemap,
  - robots,
  - índices,
  - buscador,
  - vista de últimas incorporaciones cuando procede,
  - páginas de desarrolladores, distribuidores, géneros, plataformas y formatos.

---

# SEO y arquitectura

La web utiliza:

- páginas HTML individuales por juego,
- URLs amigables,
- Open Graph,
- metadata específica,
- sitemap XML,
- robots.txt,
- navegación enlazada,
- páginas de entidad generadas automáticamente,
- estructura optimizada para indexación.

Ejemplo de URL:

```text
https://www.pcgamearchive.org/juegos/diablo-bigbox/
```

---

# Buscador

El buscador integrado permite localizar juegos por:

- título,
- formato,
- serie,
- género,
- plataforma,
- desarrollador,
- distribuidor,
- EAN,
- tags,
- descripción,
- contenido de la edición,
- protección.

Google Analytics registra además búsquedas internas, filtros utilizados,
selección de fichas y clics de contacto. Las páginas se miden usando su URL
canónica para evitar separar métricas entre `/` y `/index.html` o entre
`/juegos/slug/` y `/juegos/slug/index.html`.

---

# URLs y SEO técnico

- La portada canónica es `https://www.pcgamearchive.org/`.
- Las fichas usan como URL canónica `https://www.pcgamearchive.org/juegos/<slug>/`.
- Los enlaces internos no incluyen `index.html`.
- `bigbox.html` se mantiene solo como compatibilidad y redirige a `juegos-pc-big-box.html`.
- `detalle.html?juego=<slug>` redirige las antiguas fichas dinámicas a la ficha estática actual.
- El sitemap publica únicamente URLs canónicas.
- No se generan fechas `lastmod` si no existe una fecha real de modificación de la ficha.
- `no_disponible.png` se usa como imagen de respaldo visual y Open Graph cuando una ficha no dispone de imágenes.

Para probar la web generada localmente con las mismas rutas que producción:

```bash
python -m http.server 8000
```

y abrir `http://localhost:8000/`.

El índice de búsqueda se genera automáticamente desde `juegos.json`.

## Entidades del catálogo

`generar_web.py` crea automáticamente índices y páginas SEO para:

- desarrolladores,
- distribuidores,
- géneros,
- plataformas,
- formatos.

Solo se crea una página indexable cuando la entidad aparece en al menos 3
fichas. Variantes puramente tipográficas (por ejemplo, diferencias de
mayúsculas o acentos) se agrupan en una única entidad. Las landings existentes
de Big Box, MS-DOS, Windows 95/98 y aventura gráfica se reutilizan para evitar
crear URLs competidoras para la misma intención.

---

# Filosofía del archivo

PC Game Archive intenta documentar:

- cajas,
- manuales,
- discos,
- variantes,
- distribuciones,
- sistemas anticopia,
- tecnologías,
- contexto histórico,
- y materiales físicos asociados.

La intención es tratar el videojuego de PC como patrimonio tecnológico y cultural.

---

# Roadmap

El roadmap público del proyecto de preservación se publica en:

```text
https://www.pcgamearchive.org/proyecto/#roadmap
```

La página diferencia de forma explícita los hitos **en funcionamiento**, **en desarrollo** y **objetivos futuros**.

## Roadmap técnico de la web

Las evoluciones técnicas se priorizan según necesidades reales del archivo. Entre las líneas posibles se mantienen:

- mejoras de búsqueda y filtros,
- estadísticas del archivo,
- evolución mobile-first,
- capacidades PWA,
- soporte multilenguaje,
- mejoras de accesibilidad y rendimiento.

---

# Fase 13 — Identidad, conservación y donaciones

La Fase 13 incorpora una nueva página pública **El proyecto** (`/proyecto/`) con:

- propósito del archivo,
- actividad actual,
- principios de conservación,
- proceso de incorporación y preservación de piezas,
- roadmap público,
- situación actual de la exposición física,
- presentación breve de las personas impulsoras del proyecto.

La landing `/vender-videojuegos-pc-antiguos/` se amplía además con información específica para donantes: procedencia, catalogación, conservación física, preservación digital y situación actual de la colección.

La navegación principal, el sitemap, las páginas generadas y los datos estructurados se actualizan automáticamente desde `generar_web.py`.

---


# Fase 14 — Últimas incorporaciones

La Fase 14 incorpora una fecha documental de entrada al archivo mediante el campo obligatorio `fecha_incorporacion`, utilizada para construir una vista de novedades sin duplicar el catálogo.

- `fecha_incorporacion` admite `YYYY-MM-DD` o cadena vacía para fichas históricas sin fecha documentada.
- El dato es independiente de `num` y de la publicación en Instagram/redes sociales.
- La portada muestra hasta 6 **Últimas incorporaciones al archivo** cuando existen fechas reales.
- `/incorporaciones/` muestra únicamente las 24 incorporaciones más recientes, sin paginación ni histórico acumulativo.
- Las incorporaciones se ordenan estrictamente por `fecha_incorporacion`, de más reciente a más antigua; a igualdad de fecha se conserva el orden de `juegos.json`.
- Las fechas futuras se excluyen de las vistas de novedades y quedan señaladas por el validador para su corrección.
- Las fichas individuales muestran **Incorporado al archivo** cuando la fecha está documentada.
- El sitemap incluye únicamente la ruta canónica `/incorporaciones/` cuando existen registros fechados.
- El validador comprueba formato ISO, fechas calendáricamente válidas y avisa si se registra una fecha futura.

Las 1.562 fichas existentes se migran con `fecha_incorporacion: ""` para no fabricar fechas históricas que el archivo no puede acreditar. A partir de esta fase, la fecha debe documentarse en las nuevas incorporaciones reales.

---

# Licencia

El código y estructura del proyecto pertenecen a PC Game Archive.

Las imágenes, logotipos y materiales físicos documentados pertenecen a sus respectivos propietarios y se utilizan únicamente con fines documentales, históricos y de preservación.

---

# Contacto

Web:

https://www.pcgamearchive.org

Instagram:

https://www.instagram.com/pc_game_archive/
