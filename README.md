# 🎮 Colección de Videojuegos en Formato Físico

Este proyecto es una página estática en HTML, CSS y JavaScript que muestra una colección personal de videojuegos físicos (BigBox, FX Games, Bestseller Series, etc.).

La web está diseñada para funcionar directamente desde GitHub Pages.

---

## 📁 Estructura del proyecto

```
📂 raiz/
├── index.html                ← Página principal con categorías
├── bigbox/
│   ├── index.html           ← Listado de juegos BigBox
│   └── juegos/
│       └── nombre-del-juego/
│           ├── index.html   ← Plantilla genérica (no se edita más)
│           ├── game.json    ← Datos dinámicos del juego
│           └── img/         ← Imágenes (000.jpg, 001.jpg, ...)
├── fx-games/
│   └── ...
```

---

## ✍️ Cómo añadir un nuevo juego

1. 📂 Ir a la carpeta correspondiente a la categoría (`bigbox`, `fx-games`, etc.)
2. 📁 Crear una nueva carpeta dentro de `juegos/` con el nombre del juego (sin espacios ni acentos)
3. 📝 Copiar dentro el archivo `index.html` plantilla (es el mismo para todos los juegos)
4. 📸 Añadir imágenes a la subcarpeta `img/` con nombre `000.jpg`, `001.jpg`, `002.jpg`, ...
5. ✏️ Crear el archivo `game.json` con el siguiente formato:

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

✅ ¡No es necesario tocar el HTML! El contenido se carga automáticamente desde `game.json`.

6. 🔗 Editar el `index.html` de la categoría y añadir una nueva fila a la tabla con:
   - Título
   - Plataforma
   - Estado
   - Enlace al juego

---

## ✅ Características

- Sitio responsive (funciona en móvil y escritorio)
- Galería de imágenes con scroll horizontal y Lightbox2
- Datos de cada juego cargados desde un JSON (`game.json`)
- Solo es necesario mantener imágenes y JSON — el HTML queda fijo
- Código plano, sin frameworks ni build

---

## 🚀 Publicar en GitHub Pages

1. Subir todo este contenido a un nuevo repositorio de GitHub
2. Activar GitHub Pages desde "Settings" > "Pages"
3. Seleccionar la rama `main` y la carpeta `/ (root)`
4. Tu sitio estará online en:  
   `https://<tu-usuario>.github.io/<nombre-del-repositorio>/`

---

## 🛠️ Ideas futuras

- Filtro por género o plataforma
- Buscador por título
- Sistema de reserva/contacto
- Generador automático de fichas desde CSV

---

## 📬 Contacto

Este proyecto es personal. Si tienes sugerencias o quieres colaborar, ¡escribime!
