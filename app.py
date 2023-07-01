from flask import Flask, render_template, request
import requests
from werkzeug.serving import WSGIRequestHandler
from gunicorn.app.base import BaseApplication
from api import app as fastapi_app
from judini.agent import Agent

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    text = request.form['text']
    print("Texto ingresado:", text)  # Muestra el texto por consola
    # Realiza la llamada a la API con el texto ingresado
    # Usa el módulo requests para enviar una solicitud POST a la API
    # Procesa la respuesta de la API según tus necesidades
    # Puedes usar la librería requests para enviar la solicitud a la API
    # Ejemplo:
    #response = requests.post('http://localhost:8000/send', json={'text': text})
    # Procesa la respuesta de la API según tus necesidades
    # Retorna la respuesta o realiza cualquier otra acción que desees
    api_key = "ac3d74a1-3577-4552-96d1-60ee0c9196fc"
    agent_id = "c6f9c8dd-90ad-4553-8523-e8234e61de1f"

    # Inicializa la clase de Judini
    agent_instance = Agent(api_key, agent_id)

    # Bucle infinito para recibir consultas
    # Recibe la consulta del usuario
    query = input("Ingresa tu consulta (o escribe 'salir' para terminar): ")


    # Realiza la solicitud de completado al modelo
    response = agent_instance.completion(query, stream=False)

    # Maneja la respuesta según sea necesario
    print(response)

    return response.text

class FlaskApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key, value)

    def load(self):
        return self.application

if __name__ == '__main__':
    # Iniciar el servidor de Gunicorn con la aplicación Flask
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    options = {
        'bind': 'localhost:5000',
        'workers': 4
    }
    FlaskApplication(app, options).run()

