from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chat():
    user_input = request.form.get('msg', '')

    try:
        response = requests.post(
            "https://api.chatanywhere.com.cn/v1/chat/completions",
            headers={"Authorization": "Bearer pk-freemium"},
            json={
                "model": "pai-001",
                "messages": [
                    {"role": "system", "content": "You are a calm and empathetic rogerian psychologist bot. You support users emotionally, suggest healthy habits, and never give medical advice."},
                    {"role": "user", "content": user_input}
                ]
            },
            timeout=10
        )
        data = response.json()

        if 'choices' in data and data['choices']:
            reply = data['choices'][0]['message']['content']
        else:
            reply = "Sorry, I couldn't understand that. Please try again."

    except Exception as e:
        reply = f"Oops! Error: {str(e)}"

    return reply

if __name__ == "__main__":
    app.run(debug=True)
