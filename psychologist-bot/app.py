import os
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chat():
    user_input = request.form.get('msg', '')

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {sk-5678mnopqrstuvwx5678mnopqrstuvwx5678mnop}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a calm and empathetic psychologist."},
                    {"role": "user", "content": user_input}
                ]
            },
            timeout=10
        )
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
    except Exception as e:
        reply = f"Error: {str(e)}"

    return reply

if __name__ == "__main__":
    app.run(debug=True)
