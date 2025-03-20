from flask import Flask, request, jsonify

app = Flask(__name__)

# Token de verificação do Facebook
VERIFY_TOKEN = "sec-123-@1"

@app.route("/", methods=["GET"])
def home():
    """Rota principal para evitar erro 404 no Render"""
    return "Webhook ativo!", 200

@app.route('/webhook', methods=['GET'])
def verify():
    """Validação do Webhook pelo Facebook"""
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    
    if token == VERIFY_TOKEN:
        return challenge  # O Facebook espera esse retorno para validar o webhook
    return "Token inválido", 403

@app.route('/webhook', methods=['POST'])
def receive_data():
    """Recebendo dados do Webhook"""
    data = request.get_json()

    # Verifica se há dados recebidos
    if data:
        print(f"🔹 Dados recebidos: {data}")
    else:
        print("⚠️ Nenhum dado recebido!")

    return jsonify({"status": "Recebido"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
