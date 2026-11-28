#!/usr/bin/env python3
import os
import tempfile
from shutil import move
from PIL import Image

# ============================================
# CONFIGURACIÓN
# ============================================

CALIDAD = 82          # Calidad recomendada (80–85)
MAX_RES = None        # Ejemplo: (1600, 1600) para reescalar. None = sin cambio
EXTS = [".jpg", ".jpeg"]

IGNORAR = {".git", "__pycache__"}


# ============================================
# FUNCIÓN: Optimizar imagen si mejora el tamaño
# ============================================

def optimizar_imagen(path):
    try:
        img = Image.open(path)

        # Archivo temporal donde guardamos la versión comprimida
        tmp_fd, tmp_path = tempfile.mkstemp(suffix=".jpg")
        os.close(tmp_fd)

        # Reescalar si se desea
        if MAX_RES is not None:
            img.thumbnail(MAX_RES)

        # Guardar versión optimizada provisional
        img.save(tmp_path, "JPEG", quality=CALIDAD, optimize=True)

        # Comparar tamaños
        orig_size = os.path.getsize(path)
        new_size = os.path.getsize(tmp_path)

        if new_size < orig_size:
            move(tmp_path, path)
            print(f"    Optimizada ({orig_size} → {new_size} bytes): {os.path.basename(path)}")
        else:
            os.remove(tmp_path)
            print(f"    Sin cambios (ya era óptima): {os.path.basename(path)}")

    except Exception as e:
        print(f"    ERROR en {path}: {e}")


# ============================================
# FUNCIÓN: Recorrer directorios y procesar carpetas /img/
# ============================================

def recorrer_directorios(base):
    for root, dirs, files in os.walk(base):
        # Ignorar carpetas de sistema
        if any(skip in root for skip in IGNORAR):
            continue

        # Detectar carpetas 'img'
        if os.path.basename(root).lower() == "img":
            juego = os.path.basename(os.path.dirname(root))
            print(f"\nProcesando imágenes del juego: {juego}")

            for f in files:
                ext = os.path.splitext(f)[1].lower()
                if ext in EXTS:
                    optimizar_imagen(os.path.join(root, f))


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(f"Iniciando optimización en: {BASE_DIR}")

    recorrer_directorios(BASE_DIR)

    print("\nOptimización completada.")
