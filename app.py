from flask import Flask, render_template, request, jsonify
from judini.agent import Agent
import json

app = Flask(__name__)

# Replace with your actual API key and URL ID
api_key = "ac3d74a1-3577-4552-96d1-60ee0c9196fc"
agent_id_default = "c6f9c8dd-90ad-4553-8523-e8234e61de1f"
agent_derivador_id= "b2f0e979-fd3c-4d8f-a7b7-a8eba6b54f76"
agent_instance_default = Agent(api_key, agent_id_default)
# Initialize the Judini agent
agent_derivador_instance = Agent(api_key,agent_derivador_id)
#agent_instance = Agent(api_key, agent_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    try:
        prompt = request.get_json()['prompt']
        prompt += ". Responde y explica de la forma mas completa posible.\n"
        try:
            response = agent_derivador_instance.completion(prompt, stream=False)
            print(response)
            response_json = json.loads(response)

            # Obtener los valores del JSON de respuesta
            
            id_temporal = response_json["id"]
            topico = response_json["topico"]
            print(id_temporal)
            print(topico)
            
            agent_aux_id = id_temporal
            agent_aux_instance = Agent(api_key,agent_aux_id)
            response2= agent_aux_instance.completion(prompt,stream=False)
        except Exception as e:
            print("Error: " + str(e))
            print("agente por defecto")
            response2 = agent_instance_default.completion(prompt, stream=False)

        # If the response is a dict or list, it can be directly passed to jsonify
        # If it's an instance of a custom class, you may need to convert it to a dict first
        # This part may need to be modified based on the actual type of the `response`
        return jsonify(response2)
    except Exception as e:
        print("Error: " + str(e))
        error_message = str(e)
        error_response = {
            'error': error_message
        }
        return jsonify(error_response), 400


if __name__ == '__main__':
    app.run(port=8000 ,debug=True)