from flask import Flask, render_template, request
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
    prompt = request.form['prompt']
    
    # Make a completion request
    response = agent_instance.completion(prompt, stream=False)
    
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run()
