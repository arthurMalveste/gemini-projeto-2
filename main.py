from flask import Flask, render_template, request, jsonify
import os
from gemini import responder_com_limpinha

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/responder", methods=["POST"])
def responder():
    dados = request.get_json()
    mensagem = dados.get("mensagem", "")
    resposta = responder_com_limpinha(mensagem)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))(debug=True)
