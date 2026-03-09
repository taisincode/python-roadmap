from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/dobro/<int:numero>") #Outros parâmetros possíveis:<float:preco>, <path:arquivo>.
def dobro(numero):

    dados = {
        "numero": numero,
        "dobro": numero * 2
    }

    return jsonify(dados)

app.run()