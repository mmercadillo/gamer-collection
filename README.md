# 🎮 Colección de Videojuegos en Formato Físico

Este proyecto es una página estática desarrollada en HTML, CSS y JavaScript para mostrar una colección personal de videojuegos físicos (BigBox, FX Games, Bestseller Series, etc.).

Toda la información se carga dinámicamente desde archivos JSON, y solo se utilizan tres HTMLs reutilizables:

- `index.html` → Página principal (categorías)
- `listado.html` → Listado dinámico de juegos por categoría
- `detalle.html` → Ficha de juego individual

---

## 📁 Estructura del proyecto

```
📂 raiz/
├── index.html              ← Página principal
├── listado.html            ← Lista de juegos dinámica
├── detalle.html            ← Detalle de juego dinámica
├── categorias.json         ← Lista de categorías

📂 bigbox/
├── juegos.json             ← Lista de juegos de BigBox
└── juegos/
    └── age-of-empires/
        ├── game.json       ← Datos del juego
        └── img/            ← Imágenes (000.jpg, 001.jpg, ...)
```

---

## 🧭 Navegación

- Página principal:  
  `index.html`

- Listado de una categoría:  
  `listado.html?categoria=bigbox`

- Ficha de un juego:  
  `detalle.html?categoria=bigbox&juego=age-of-empires`

---

## ✍️ Cómo añadir una nueva categoría

1. Crear una carpeta con el nombre de la categoría, por ejemplo: `fx-games/`
2. Crear el archivo `juegos.json` con contenido como este:

```json
[
  {
    "titulo": "Nombre del juego",
    "url": "juegos/nombre-del-juego/",
    "plataforma": "Plataforma",
    "estado": "Estado"
  }
]
```

3. Añadir esa categoría en `categorias.json` de la raíz:

```json
[
  {
    "nombre": "FX Games",
    "url": "fx-games"
  }
]
```

---

## 🕹️ Cómo añadir un nuevo juego

1. Crear carpeta del juego en la ruta: `categoria/juegos/nombre-del-juego/`
2. Crear `game.json` con este formato:

```json
{
  "titulo": "Nombre del juego",
  "plataforma": "Plataforma",
  "estado": "Estado del juego",
  "genero": "Género",
  "descripcion": "Descripción del juego.",
  "incluye": [
    "Caja original",
    "Manual",
    "CD sin rayones"
  ]
}
```

3. Añadir imágenes en la carpeta `img/` con nombres `000.jpg`, `001.jpg`, etc.
4. Añadir entrada del juego en el `juegos.json` de la categoría correspondiente.

✅ No es necesario modificar ningún HTML.

---

## ✅ Ventajas

- Sitio responsive (funciona en móvil y escritorio)
- Galería con Lightbox2 y scroll horizontal
- Fichas de juegos cargadas con JSON
- Navegación 100% dinámica
- Mantenimiento muy simple

---

## 🚀 Probar en local

Para desarrollo, puedes usar un servidor local con Python:

```bash
python3 -m http.server 8000
```

Y acceder a:

- `http://localhost:8000/`
- `http://localhost:8000/listado.html?categoria=bigbox`
- `http://localhost:8000/detalle.html?categoria=bigbox&juego=age-of-empires`

---

## 🌐 Publicar en GitHub Pages

1. Subir todo a un repositorio en GitHub
2. Activar GitHub Pages desde Settings > Pages
3. Seleccionar la rama `main` y carpeta `/ (root)`
4. Acceder al sitio en:  
   `https://<tu-usuario>.github.io/<repo>/`

---

## 📬 Contacto

Este proyecto es personal. Si quieres sugerir mejoras o colaborar, ¡bienvenido!
