
import os
import json

# Leer categorias.json desde raíz
with open("categorias.json", encoding="utf-8") as f:
    categorias = json.load(f)

for categoria in categorias:
    nombre = categoria.get("nombre", "Sin nombre")
    slug = categoria.get("slug")

    if not slug:
        print(f"⚠️  La categoría '{nombre}' no tiene slug. Se omite.")
        continue

    print(f"\n📂 Procesando categoría: {nombre} ({slug})")

    categoria_path = os.path.join(slug)
    juegos_json_path = os.path.join(categoria_path, "juegos.json")

    # Crear carpeta de categoría si no existe
    os.makedirs(categoria_path, exist_ok=True)

    # Si juegos.json no existe, crear uno vacío
    if not os.path.exists(juegos_json_path):
        with open(juegos_json_path, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)
        print(f"📄 Se creó {juegos_json_path} vacío (sin juegos).")
        continue

    # Cargar juegos existentes y generar estructura de cada uno
    with open(juegos_json_path, encoding="utf-8") as f:
        juegos = json.load(f)

    for juego in juegos:
        ruta_juego = os.path.join(categoria_path, juego["url"].rstrip("/"))
        ruta_img = os.path.join(ruta_juego, "img")
        ruta_game_json = os.path.join(ruta_juego, "game.json")

        os.makedirs(ruta_img, exist_ok=True)

        if not os.path.exists(ruta_game_json):
            juego_completo = {
                "titulo": juego.get("titulo", ""),
                "plataforma": juego.get("plataforma", ""),
                "estado": juego.get("estado", "Sin-verificar"),
                "genero": juego.get("genero", ""),
                "desarrollador": juego.get("desarrollador", ""),
                "distribuidor": juego.get("distribuidor", ""),
                "ean": juego.get("ean", ""),
                "descripcion": "",
                "incluye": []
            }

            with open(ruta_game_json, "w", encoding="utf-8") as f:
                json.dump(juego_completo, f, indent=2, ensure_ascii=False)
            print(f"✅ game.json creado en: {ruta_game_json}")
        else:
            print(f"🔒 ya existe: {ruta_game_json}")

print("\n🎉 Todas las estructuras han sido creadas o completadas.")
