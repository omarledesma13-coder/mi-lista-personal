import requests
import os

# Traemos tus datos seguros de la "caja fuerte" de GitHub
USERNAME = os.environ.get('USER')
PASSWORD = os.environ.get('PASS')

def login_flow():
    # Aquí el script simula que sos vos entrando a la app de Flow
    # Se loguea y obtiene el Token Maestro
    print("Iniciando sesión en Flow...")
    # (Este es un ejemplo de la lógica, ya que la API real requiere headers específicos)
    return "TU_TOKEN_DE_SESION"

def generar_m3u():
    token = login_flow()
    
    # Creamos el archivo final que leerá tu Android
    with open('lista.m3u', 'w') as f:
        f.write("#EXTM3U\n")
        
        # Aquí el script recorre los canales y les pega el token nuevo
        # Ejemplo con un canal (esto se repite para todos los que tengas)
        f.write("#EXTINF:-1, Canal de Prueba\n")
        f.write(f"https://live.flow.com.ar{token}\n")

if __name__ == "__main__":
    if USERNAME and PASSWORD:
        generar_m3u()
        print("¡Lista m3u actualizada con éxito!")
    else:
        print("Error: No se encontraron las credenciales en los Secrets.")
