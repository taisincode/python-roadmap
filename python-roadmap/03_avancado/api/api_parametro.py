from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/usuario/<nome>")
def usuario(nome):

    dados = {
        "usuario": nome
    }

    return jsonify(dados)

app.run()
