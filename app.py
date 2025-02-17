from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = {"response": f"Hello! You said: {user_input}"}
    return jsonify(response)

@app.route('/')
def home():
    return "Chatbot App is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
