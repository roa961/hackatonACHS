from flask import Flask, render_template, request
import requests
app = Flask(__name__)
@app.route('/', methods=['GET'])
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
    print("xdd")
    response = requests.post('http://localhost:5000/send', json={'text': text})
    # Procesa la respuesta de la API según tus necesidades
    # Retorna la respuesta o realiza cualquier otra acción que desees
    return response.text


if __name__ == '__main__':
    app.run(debug=True)
