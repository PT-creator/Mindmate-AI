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
        # API call
        response = requests.post(
            "https://api.chatanywhere.com.cn/v1/chat/completions",
            headers={"Authorization": "Bearer sk-antipaid"},
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a kind and calm AI psychologist. Your job is to listen, support, and gently guide the user through their thoughts. You do not diagnose or prescribe."},
                    {"role": "user", "content": user_input}
                ]
            },
            timeout=10
        )

        # Log the entire response
        print("API Response:", response.text)

        # Convert JSON
        data = response.json()

        # Validate and extract content
        if data and "choices" in data and len(data["choices"]) > 0:
            reply = data["choices"][0]["message"]["content"]
        else:
            reply = "I received an unexpected response. Please try again."

    except Exception as e:
        reply = f"An error occurred: {str(e)}"

    return reply

if __name__ == "__main__":
    app.run(debug=True)
