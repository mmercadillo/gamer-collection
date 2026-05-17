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

https://pcgamearchive.org

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
├── generar_web_v8.py
├── validar_catalogo.py
├── sitemap.xml
├── robots.txt
├── logo.png
├── assets/
│   ├── css/
│   └── js/
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

Ejemplo:

```json
{
  "num": "000999",
  "ig": "",
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
python generar_web_v8.py
```

El generador:

- NO copia imágenes,
- NO duplica assets,
- únicamente sobrescribe:
  - HTML generado,
  - sitemap,
  - robots,
  - índices,
  - buscador.

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
- estructura optimizada para indexación.

Ejemplo de URL:

```text
https://pcgamearchive.org/juegos/diablo-bigbox/index.html
```

---

# Buscador

El buscador integrado permite localizar juegos por:

- título,
- formato,
- serie.

El índice de búsqueda se genera automáticamente desde `juegos.json`.

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

## Próximamente

- PWA instalable
- APK Android ligera
- filtros avanzados
- navegación por plataforma
- timeline histórico
- fichas relacionadas
- estadísticas del archivo
- mejoras mobile-first
- búsqueda avanzada
- soporte multilenguaje

---

# Licencia

El código y estructura del proyecto pertenecen a PC Game Archive.

Las imágenes, logotipos y materiales físicos documentados pertenecen a sus respectivos propietarios y se utilizan únicamente con fines documentales, históricos y de preservación.

---

# Contacto

Web:

https://pcgamearchive.org

Instagram:

https://www.instagram.com/pc_game_archive/
