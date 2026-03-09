from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return('API funcionando')


@app.route('/ola/<nome>')
def usuario(nome):
    
    dados = {
        "usuario": nome
    }
    
    return jsonify(dados)

@app.route('/triplo/<int:numero>')
def triplo(numero):

    dados = {
        "numero": numero,
        "triplo": numero * 3
    }
    
    return jsonify(dados)

app.run()