
import subprocess

def descargar_video(url):
    comando = [
        'yt-dlp',
        '-f', 'best',
        '-o', '%(title).100s.%(ext)s',  # Título limpio, limitado a 100 caracteres
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
        print("Video descargado correctamente.")
    else:
        print("Hubo un error durante la descarga.")

if __name__ == "__main__":
    url = input("Introduce el enlace del video de YouTube: ")
    descargar_video(url)
