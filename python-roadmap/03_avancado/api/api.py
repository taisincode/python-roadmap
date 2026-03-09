from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return "API de estudos funcionando."

@app.route("/perfil")
def usuario():
    return jsonify({
        "nome": "Tais",
        "area":"Backend",
        "linguagem": "Python"})

@app.route("/cidade")
def endereco():
    return jsonify({"cidade": "Lagoa Real", 
                    "estado": "BA", 
                    "pais": "Brasil"})

app.run()