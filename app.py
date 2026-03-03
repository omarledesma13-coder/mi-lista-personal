from flask import Flask, Response
import os

app = Flask(__name__)

@app.route('/lista.m3u')
def generar_m3u():
    contenido = "#EXTM3U\n"
    try:
        with open('lLISTA FLOW.txt', 'r') as f:
            for i, line in enumerate(f, 1):
                url = line.strip()
                if url:
                    contenido += f"#EXTINF:-1, Canal {i}\n{url}\n"
    except FileNotFoundError:
        return "Archivo no encontrado", 404
    
    return Response(contenido, mimetype='text/plain')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
