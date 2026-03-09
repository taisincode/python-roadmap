from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calculadora')
def soma():
    
    numero1 = int (request.args.get('numero1'))
    numero2 = int (request.args.get('numero2'))
    
    dados ={
        'numero1': numero1,
        'numero2': numero2, 
        'soma': numero1 + numero2
    }
    
    return jsonify(dados)

app.run()