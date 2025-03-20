from flask import Flask, request, jsonify

app = Flask(__name__)

# Token de verificação do Facebook
VERIFY_TOKEN = "MEU_TOKEN_SECRETO"

@app.route('/webhook', methods=['GET'])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == VERIFY_TOKEN:
        return challenge
    return "Token inválido", 403

@app.route('/webhook', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Dados recebidos: {data}")
    return jsonify({"status": "Recebido"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
