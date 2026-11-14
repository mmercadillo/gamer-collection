#!/usr/bin/env python3
"""PC Game Archive: adapta vídeos a Reels 9:16 sin recortar la imagen.

Requiere Python 3.9+ y FFmpeg/FFprobe disponibles en PATH.
Ejemplos:
  python convertir_reels_instagram.py "intro.mp4"
  python convertir_reels_instagram.py "carpeta_videos" --salida "reels"
  python convertir_reels_instagram.py "intro.mp4" --fondo desenfocado
  python convertir_reels_instagram.py "intro.mp4" --forzar
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

EXTENSIONES = {'.mp4', '.mov', '.mkv', '.avi', '.webm', '.m4v'}


def comprobar_herramientas():
    for herramienta in ('ffmpeg', 'ffprobe'):
        if not shutil.which(herramienta):
            sys.exit(f'ERROR: no se encuentra {herramienta}. Instala FFmpeg y añádelo al PATH.')


def obtener_info(ruta):
    proceso = subprocess.run(
        ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
         '-show_entries', 'stream=width,height,avg_frame_rate:format=duration',
         '-of', 'json', str(ruta)], capture_output=True, text=True, check=True
    )
    datos = json.loads(proceso.stdout)
    if not datos.get('streams'):
        raise ValueError('No contiene ninguna pista de vídeo')
    return datos['streams'][0], float(datos.get('format', {}).get('duration', 0))


def filtro_video(fondo):
    ajustar = 'scale=1080:1920:force_original_aspect_ratio=decrease:force_divisible_by=2,setsar=1'
    if fondo == 'negro':
        return f'[0:v:0]{ajustar},pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,format=yuv420p[v]'
    # El fondo se genera desde el mismo fotograma; la imagen central queda íntegra.
    return (
        '[0:v:0]split=2[bg][fg];'
        '[bg]scale=1080:1920:force_original_aspect_ratio=increase,'
        'crop=1080:1920,setsar=1,gblur=sigma=30[blur];'
        f'[fg]{ajustar}[front];'
        '[blur][front]overlay=(W-w)/2:(H-h)/2:shortest=1,format=yuv420p[v]'
    )


def convertir(origen, destino, fondo, crf, preset, forzar):
    if origen.resolve() == destino.resolve():
        raise ValueError('La ruta de salida coincide con el original')
    if destino.exists() and not forzar:
        print(f'OMITIDO (ya existe): {destino}')
        return
    info, duracion = obtener_info(origen)
    destino.parent.mkdir(parents=True, exist_ok=True)
    print(f'\nConvirtiendo: {origen.name}')
    print(f"  Original: {info['width']}x{info['height']} | "
          f"{info.get('avg_frame_rate', '?')} fps | {duracion:.2f} s")
    print(f'  Destino : {destino} (1080x1920, fondo {fondo})')
    comando = [
        'ffmpeg', '-hide_banner', '-nostdin', '-loglevel', 'error', '-stats',
        '-y' if forzar else '-n', '-i', str(origen),
        '-filter_complex', filtro_video(fondo),
        '-map', '[v]', '-map', '0:a:0?',
        '-c:v', 'libx264', '-preset', preset, '-crf', str(crf),
        '-pix_fmt', 'yuv420p', '-fps_mode', 'passthrough',
        '-c:a', 'aac', '-b:a', '192k',
        '-movflags', '+faststart', '-max_muxing_queue_size', '1024',
        str(destino),
    ]
    resultado = subprocess.run(comando)
    if resultado.returncode != 0:
        # No dejar archivos MP4 incompletos tras un error de FFmpeg.
        if destino.exists():
            destino.unlink()
        raise RuntimeError(f'FFmpeg terminó con código {resultado.returncode}')
    salida_info, salida_duracion = obtener_info(destino)
    if salida_info['width'] != 1080 or salida_info['height'] != 1920:
        raise RuntimeError('La resolución de salida no es 1080x1920')
    if duracion and abs(salida_duracion - duracion) > 0.25:
        print(f'  AVISO: diferencia de duración: {salida_duracion - duracion:+.3f} s')
    print(f'  OK: {salida_duracion:.2f} s | {destino.stat().st_size / 1024 / 1024:.1f} MiB')


def main():
    parser = argparse.ArgumentParser(description='PC Game Archive — conversor 9:16 para Instagram Reels sin recortes')
    parser.add_argument('entrada', type=Path, help='Archivo de vídeo o carpeta de vídeos')
    parser.add_argument('--salida', type=Path, help='Carpeta de salida (por defecto, junto a cada original)')
    parser.add_argument('--fondo', choices=('negro', 'desenfocado'), default='negro')
    parser.add_argument('--crf', type=int, choices=range(16, 29), metavar='16-28', default=20,
                        help='Calidad H.264: menor = más calidad/tamaño (20 por defecto)')
    parser.add_argument('--preset', choices=('fast', 'medium', 'slow'), default='medium')
    parser.add_argument('--forzar', action='store_true', help='Sobrescribir salidas existentes')
    args = parser.parse_args()
    comprobar_herramientas()
    if not args.entrada.exists():
        parser.error(f'No existe: {args.entrada}')
    if args.entrada.is_file():
        videos = [args.entrada]
    elif args.entrada.is_dir():
        videos = sorted(p for p in args.entrada.iterdir()
                        if p.is_file() and p.suffix.lower() in EXTENSIONES
                        and not p.stem.endswith('_instagram_reel'))
    else:
        parser.error('La entrada debe ser un archivo o una carpeta')
    if not videos:
        parser.error('No se encontraron vídeos compatibles')
    fallidos = 0
    for video in videos:
        carpeta = args.salida or video.parent
        destino = carpeta / f'{video.stem}_instagram_reel.mp4'
        try:
            convertir(video, destino, args.fondo, args.crf, args.preset, args.forzar)
        except (OSError, subprocess.CalledProcessError, ValueError, RuntimeError) as error:
            fallidos += 1
            print(f'ERROR con {video.name}: {error}', file=sys.stderr)
    print(f'\nProcesados: {len(videos)} | Errores: {fallidos}')
    return 1 if fallidos else 0


if __name__ == '__main__':
    sys.exit(main())
