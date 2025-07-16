
# Gamer Collection 📦🎮

Este proyecto es una colección digital organizada de videojuegos para PC, especialmente en formato físico (Big Box, FX Games, etc.), publicada a través de **GitHub Pages**.

## 🧱 Estructura del proyecto

```
/
├── index.html                  # Página de inicio con categorías
├── categorias.json             # Lista de categorías con nombre, slug y URL
├── listado.html                # Página reutilizable para mostrar los juegos por categoría
├── detalle.html                # Página reutilizable con detalles de cada juego
├── bigbox/
│   ├── juegos.json             # Lista de juegos de esta categoría
│   └── juegos/
│       └── age-of-empires/
│           ├── img/            # Imágenes del juego
│           └── game.json       # Información detallada del juego
└── ...
```

---

## 📄 Archivos clave

### `categorias.json`

Lista de categorías disponibles:

```json
[
  {
    "nombre": "BigBox",
    "slug": "bigbox",
    "url": "listado.html?categoria=bigbox"
  },
  ...
]
```

### `juegos.json` (por categoría)

Contiene un array de juegos para esa categoría. Ejemplo:

```json
[
  {
    "titulo": "Age of Empires",
    "url": "juegos/age-of-empires/",
    "plataforma": "Windows 95/98",
    "estado": "Sin-verificar",
    "desarrollador": "Ensemble Studios",
    "distribuidor": "Microsoft"
  }
]
```

### `game.json` (por juego)

Cada juego tiene su propio archivo con los siguientes campos:

```json
{
  "titulo": "Age of Empires",
  "plataforma": "Windows 95/98",
  "estado": "Sin-verificar",
  "genero": "Estrategia en tiempo real",
  "desarrollador": "Ensemble Studios",
  "distribuidor": "Microsoft",
  "ean": "0882224084390",
  "descripcion": "Age of Empires es un juego de estrategia en tiempo real que abarca la historia desde la Edad de Piedra hasta la Edad del Hierro.",
  "incluye": [
    "Caja original",
    "CD",
    "Manual de instrucciones"
  ]
}
```

---

## ⚙️ Generación automática de estructura

Puedes usar el script `generar_estructura.py` para:

- Crear carpetas por categoría y por juego
- Crear subcarpetas `img/` para las imágenes
- Crear `game.json` con campos por defecto si no existe
- Crear `juegos.json` vacío si no existe

### ▶️ Ejecutar el script

Guárdalo en el raíz del proyecto y ejecútalo con:

```bash
python generar_estructura.py
```

---

## ✅ Funcionalidades destacadas

- Vista de catálogo por categoría
- Página de detalle con galería de imágenes
- Responsive para móviles
- Orden alfabético
- Buscador por título

---

## 🚀 Publicación

El sitio funciona directamente desde GitHub Pages. Solo asegúrate de que:

- Los ficheros estén en la rama `main` o `gh-pages`
- `index.html` esté en la raíz
- Las rutas estén bien formateadas (`/categoria/juegos/...`)

---

¡Gracias por visitar la colección! 🎮✨
