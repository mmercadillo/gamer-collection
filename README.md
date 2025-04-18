# 🎮 Colección de Videojuegos en Formato Físico

Este proyecto es una página estática en HTML, CSS y JavaScript que muestra una colección personal de videojuegos físicos (BigBox, FX Games, Bestseller Series, etc.).

Toda la información se carga dinámicamente desde archivos JSON, por lo que no es necesario editar los archivos HTML manualmente.

---

## 📁 Estructura del proyecto

```
📂 raiz/
├── index.html              ← Página principal con lista de categorías
├── categorias.json         ← Lista de categorías (nombre + URL)
├── bigbox/
│   ├── index.html          ← Plantilla de categoría (no se edita)
│   ├── juegos.json         ← Lista de juegos (título, plataforma, etc.)
│   └── juegos/
│       └── age-of-empires/
│           ├── index.html  ← Plantilla de ficha individual (no se edita)
│           ├── game.json   ← Información del juego
│           └── img/        ← Imágenes (000.jpg, 001.jpg, ...)
├── fx-games/
│   └── ...
```

---

## ✍️ Cómo añadir una nueva categoría

1. 📁 Crear una carpeta para la categoría, por ejemplo: `fx-games/`
2. Copiar dentro el `index.html` de categoría (es una plantilla que carga datos dinámicos)
3. Crear un archivo `juegos.json` con la lista de juegos, por ejemplo:

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

4. Añadir la categoría al archivo raíz `categorias.json`:

```json
[
  {
    "nombre": "FX Games",
    "url": "fx-games/index.html"
  }
]
```

---

## 🕹️ Cómo añadir un nuevo juego a una categoría

1. 📁 Crear una carpeta para el juego dentro de `juegos/`
2. Copiar dentro:
   - `index.html` (plantilla que no se edita)
   - `game.json` con la información del juego
   - Carpeta `img/` con imágenes numeradas (`000.jpg`, `001.jpg`, etc.)

Ejemplo de `game.json`:

```json
{
  "titulo": "Nombre del juego",
  "plataforma": "Plataforma",
  "estado": "Estado del juego",
  "genero": "Género",
  "descripcion": "Descripción detallada del juego.",
  "incluye": [
    "Caja original",
    "Manual",
    "CD/DVD sin rayones"
  ]
}
```

3. Añadir el juego al `juegos.json` de la categoría correspondiente.

✅ ¡No es necesario modificar ningún archivo HTML!

---

## ✅ Características

- Sitio responsive (funciona en móvil y escritorio)
- Galería de imágenes con scroll horizontal y Lightbox2
- Datos de juegos y categorías cargados desde archivos JSON
- Plantillas HTML reutilizables
- Mantenimiento simple y escalable

---

## 🚀 Publicar en GitHub Pages

1. Subí todo el contenido a un repositorio de GitHub
2. Activá GitHub Pages desde "Settings" > "Pages"
3. Seleccioná la rama `main` y la carpeta `/ (root)`
4. Accedé al sitio en:  
   `https://<tu-usuario>.github.io/<nombre-del-repositorio>/`

---

## 🛠️ Ideas futuras

- Filtros por género o plataforma
- Buscador por título
- Contacto o formulario para interesados
- Generador automático desde hoja de cálculo

---

## 📬 Contacto

Este proyecto es personal. Si tenés sugerencias o querés colaborar, ¡escribime!
