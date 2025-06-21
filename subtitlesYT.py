import subprocess
import re
import os
import json

def obtener_titulo_video(url):
    resultado = subprocess.run(
        ['yt-dlp', '--dump-json', '--skip-download', url],
        capture_output=True, text=True
    )
    if resultado.returncode == 0:
        info = json.loads(resultado.stdout)
        return info['title']
    else:
        return None

def descargar_subtitulos_vtt(url, idioma='en'):
    titulo = obtener_titulo_video(url)
    if not titulo:
        print("No se pudo obtener el título del video.")
        return

    print(f"Título del video: {titulo}")

    comando = [
        'yt-dlp',
        '--write-auto-sub',
        f'--sub-lang={idioma}',
        '--skip-download',
        url
    ]

    proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    porcentaje_regex = re.compile(r'\b(\d{1,3}\.\d)%')

    while True:
        linea = proceso.stdout.readline()
        if not linea:
            break

        match = porcentaje_regex.search(linea)
        if match:
            print(f"Descargando subtítulos... {match.group(1)}%")
        else:
            print(linea.strip())

    proceso.wait()

    if proceso.returncode == 0:
        print("Subtítulos descargados correctamente.")

        # Buscar archivo original con .en.vtt
        for archivo in os.listdir('.'):
            if archivo.endswith('.en.vtt'):
                nuevo_nombre = f"{titulo}.vtt"
                os.rename(archivo, nuevo_nombre)
                print(f"Renombrado a: {nuevo_nombre}")
                break
        else:
            print("No se encontró archivo .vtt para renombrar.")
    else:
        print("Error durante la descarga.")

if __name__ == "__main__":
    url = input("Por favor, introduce el link del video de YouTube: ")
    descargar_subtitulos_vtt(url)
