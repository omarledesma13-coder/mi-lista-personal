import requests
import os

# Sacamos tus datos de la "caja fuerte" de GitHub
user = os.environ.get('USER')
password = os.environ.get('PASS')

def obtener_lista():
    # Aquí el robot simula que sos vos entrando a la web de Flow
    # y genera el archivo lista.m3u con tokens nuevos
    with open('lista.m3u', 'w') as f:
        f.write("#EXTM3U\n")
        # Ejemplo: Aquí el script pediría la API real de Flow
        f.write("#EXTINF:-1, Canal Ejemplo\n")
        f.write("https://link-con-token-nuevo.m3u8\n")

if __name__ == "__main__":
    obtener_lista()
