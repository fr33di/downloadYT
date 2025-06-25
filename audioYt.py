import subprocess

def audio(url):
    comando = [
        'yt-dlp',
        '-f', 'bestaudio',                 # Solo la mejor calidad de audio
        '--extract-audio',                # Extraer solo el audio
        '--audio-format', 'mp3',          # Convertir audio a mp3
        '--audio-quality', '0',           # Mejor calidad de audio posible
        '-o', '%(title).100s.%(ext)s',   # Nombre de archivo limpio y limitado a 100 caracteres
        url
    ]

    proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    while True:
        linea = proceso.stdout.readline()
        if not linea:
            break
        print(linea.strip())

    proceso.wait()

    if proceso.returncode == 0:
        print("Audio descargado correctamente.")
    else:
        print("Hubo un error durante la descarga.")

if __name__ == "__main__":
    url = input("Introduce el enlace del video de YouTube: ")
    audio(url)
