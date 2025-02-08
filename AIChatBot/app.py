from flask import Flask, request, render_template, jsonify
import subprocess
import ollama

app = Flask(__name__)

# Ensure the model is pulled using the CLI
subprocess.run(["ollama", "pull", "deepseek-r1"], check=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    input_text = request.form['input_text']
    
    try:
        response = ollama.chat(
            model="deepseek-r1",
            messages=[
                {"role": "user", "content": input_text},
            ],
        )
        
        if "message" in response and "content" in response["message"]:
            return jsonify({"response": response["message"]["content"]})
        else:
            return jsonify({"response": "No content found in the response"})
    except Exception as e:
        return jsonify({"response": f"An error occurred: {e}"})

if __name__ == '__main__':
    app.run(debug=True)