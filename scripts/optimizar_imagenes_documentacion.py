#!/usr/bin/env python3
"""Optimización sin pérdida de las imágenes PNG públicas de PC Game Archive.
Requiere Pillow. Ejecutar desde la raíz del proyecto; --simular no escribe.
"""
import argparse
import os
import stat
import tempfile
from pathlib import Path
from PIL import Image, PngImagePlugin, ImageChops


def optimizar(path, simular=False):
    original = path.stat().st_size
    tmp = None
    try:
        with Image.open(path) as im:
            if im.format != 'PNG' or getattr(im, 'n_frames', 1) != 1:
                return original, original, 'omitida (formato/animación)'
            im.load()
            # No eliminar metadatos desconocidos ni alterar colorimetría.
            allowed = {'srgb', 'gamma', 'dpi', 'icc_profile', 'transparency', 'chromaticity', 'exif'}
            if set(im.info) - allowed or im.text:
                return original, original, 'omitida (metadatos especiales)'
            pnginfo = PngImagePlugin.PngInfo()
            import struct
            if 'srgb' in im.info:
                pnginfo.add(b'sRGB', bytes([im.info['srgb']]))
            if 'gamma' in im.info:
                pnginfo.add(b'gAMA', struct.pack('>I', round(im.info['gamma'] * 100000)))
            if 'chromaticity' in im.info:
                pnginfo.add(b'cHRM', struct.pack('>8I', *(round(x * 100000) for x in im.info['chromaticity'])))
            options = {k: im.info[k] for k in ('dpi', 'icc_profile', 'transparency', 'exif') if k in im.info}
            options.update(optimize=True, compress_level=9, pnginfo=pnginfo)
            fd, name = tempfile.mkstemp(suffix='.png', dir=path.parent)
            os.close(fd)
            tmp = Path(name)
            im.save(tmp, format='PNG', **options)
            # Comparación de todos los canales, incluidos RGB bajo alfa cero.
            with Image.open(tmp) as check:
                check.load()
                if (im.size != check.size or im.mode != check.mode or
                    im.tobytes() != check.tobytes() or
                    im.convert('RGBA').tobytes() != check.convert('RGBA').tobytes() or
                    im.info != check.info):
                    return original, original, 'omitida (verificación no coincidente)'
        new = tmp.stat().st_size
        if new >= original:
            return original, original, 'sin cambios'
        if not simular:
            os.chmod(tmp, stat.S_IMODE(path.stat().st_mode))
            os.replace(tmp, path)
        return original, new, 'optimizable' if simular else 'optimizada'
    finally:
        if tmp is not None:
            tmp.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--simular', action='store_true', help='Calcular ahorro sin sustituir imágenes')
    parser.add_argument('--base', type=Path, default=Path(__file__).resolve().parent, help='Raíz del proyecto')
    args = parser.parse_args()
    root = args.base.resolve() / 'documentacion'
    if not root.is_dir() or not (root.parent / 'documentacion.json').is_file():
        parser.error('No se encuentra documentacion/ y documentacion.json en la raíz indicada')
    total = final = count = changed = errors = 0
    # Exclusivamente carpetas img de las áreas públicas, no fuentes ni evidencias internas.
    areas = ('guias', 'preservacion', 'tecnica', 'entornos', 'formatos', 'historia')
    for area in areas:
        base = root / area
        if not base.is_dir() or base.is_symlink():
            continue
        for folder, dirs, files in os.walk(base, followlinks=False):
            dirs[:] = sorted(d for d in dirs if not d.startswith('.') and d != '__pycache__' and not (Path(folder)/d).is_symlink())
            if Path(folder).name.lower() != 'img':
                continue
            for name in sorted(files):
                p = Path(folder) / name
                if p.suffix.lower() != '.png' or p.is_symlink() or not p.is_file():
                    continue
                count += 1
                try:
                    a,b,status = optimizar(p,args.simular)
                    total += a; final += b; changed += int(b < a)
                    print(f'{status}: {p.relative_to(root)} ({a:,} -> {b:,} bytes)')
                except Exception as exc:
                    errors += 1
                    print(f'ERROR: {p.relative_to(root)}: {exc}')
    print(f'\n{"SIMULACIÓN" if args.simular else "RESULTADO"}: {count} PNG, {changed} con ahorro, {errors} errores')
    print(f'Bytes procesados correctamente: {total:,} -> {final:,}; ahorro: {total-final:,} ({(100*(total-final)/total if total else 0):.2f}%)')
    return int(errors > 0)

if __name__ == '__main__':
    raise SystemExit(main())
