# 🎮 Colección de Videojuegos en Formato Físico

Este proyecto es una página estática creada con HTML, CSS y JavaScript para mostrar una colección personal de videojuegos físicos (BigBox, FX Games, Bestseller Series, etc.).

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
│           ├── index.html   ← Ficha del juego
│           └── img/         ← Imágenes (000.jpg, 001.jpg, ...)
├── fx-games/
│   └── ...
```

---

## ✍️ Cómo añadir un nuevo juego

1. 📂 Ir a la carpeta correspondiente a la categoría (`bigbox`, `fx-games`, etc.)
2. 📁 Crear una nueva carpeta dentro de `juegos/` con el nombre del juego (sin espacios ni acentos)
3. 📝 Copiar dentro la plantilla `index.html` de ficha de juego
4. 📸 Añadir imágenes a la subcarpeta `img/` con nombre `000.jpg`, `001.jpg`, `002.jpg`, ...
5. ✏️ Editar el `index.html` del juego y completar:
   - Título
   - Plataforma
   - Estado
   - Género
   - Descripción
   - Lista de elementos incluidos
6. 🔗 Editar el `index.html` de la categoría y añadir una nueva fila a la tabla con:
   - Título
   - Plataforma
   - Estado
   - Enlace al juego

---

## ✅ Características

- Sitio responsive (funciona en móvil y escritorio)
- Galería de imágenes con scroll horizontal y Lightbox2
- Estructura clara por categorías
- Código plano, sin dependencias complejas
- Fácil de mantener y ampliar

---

## 🚀 Publicar en GitHub Pages

1. Subí todo este contenido a un nuevo repositorio de GitHub
2. Activá GitHub Pages desde "Settings" > "Pages"
3. Seleccioná la rama `main` y la carpeta `/ (root)`
4. Tu sitio estará online en:  
   `https://<tu-usuario>.github.io/<nombre-del-repositorio>/`

---

## 🛠️ Pendiente o ideas futuras

- Filtro por género o plataforma
- Buscador por título
- Sistema de reserva/contacto
- Generador automático de fichas

---

## 📬 Contacto

Este proyecto es personal. Si tenés sugerencias o querés colaborar, ¡escribime!
