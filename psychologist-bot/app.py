from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chat():
    user_input = request.form['msg']

    # Free API call to pawan.krd
    response = requests.post(
        "https://api.pawan.krd/v1/chat/completions",
        headers={"Authorization": "Bearer pk-freemium"},
        json={
            "model": "pai-001",
            "messages": [
                {"role": "system", "content": "You are a calm and empathetic psychologist bot. You support users emotionally, suggest healthy habits, and never give medical advice."},
                {"role": "user", "content": user_input}
            ]
        }
    )
    data = response.json()
    reply = data['choices'][0]['message']['content']
    return reply

if __name__ == "__main__":
    app.run(debug=True)
