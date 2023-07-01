from flask import Flask, render_template, request, jsonify
from judini.agent import Agent

app = Flask(__name__)

# Replace with your actual API key and URL ID
api_key = "ac3d74a1-3577-4552-96d1-60ee0c9196fc"
agent_id = "c6f9c8dd-90ad-4553-8523-e8234e61de1f"

# Initialize the Judini agent
agent_instance = Agent(api_key, agent_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    try:
        prompt = request.get_json()['prompt']

        # Make a completion request
        response = agent_instance.completion(prompt, stream=False)

        # If the response is a dict or list, it can be directly passed to jsonify
        # If it's an instance of a custom class, you may need to convert it to a dict first
        # This part may need to be modified based on the actual type of the `response`
        return jsonify(response)
    except Exception as e:
        print("Error: " + str(e))
        error_message = str(e)
        error_response = {
            'error': error_message
        }
        return jsonify(error_response), 400


if __name__ == '__main__':
    app.run()
