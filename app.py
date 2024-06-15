from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Initialize the OpenAI client
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)