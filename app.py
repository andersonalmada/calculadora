from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita o CORS para todas as rotas

def parse_params(param1, param2):
    try:
        num1 = float(param1)
        num2 = float(param2)
        return num1, num2, None
    except ValueError:
        return None, None, "Invalid input. Please ensure both parameters are numbers."

@app.route('/operation/soma/<param1>/<param2>', methods=['POST'])
def add(param1, param2):
    num1, num2, error = parse_params(param1, param2)
    if error:
        return jsonify({"error": error}), 400
    result = num1 + num2
    return jsonify({"result": result})

@app.route('/operation/subtracao/<param1>/<param2>', methods=['POST'])
def subtract(param1, param2):
    num1, num2, error = parse_params(param1, param2)
    if error:
        return jsonify({"error": error}), 400
    result = num1 - num2
    return jsonify({"result": result})

@app.route('/operation/multiplicacao/<param1>/<param2>', methods=['POST'])
def multiply(param1, param2):
    num1, num2, error = parse_params(param1, param2)
    if error:
        return jsonify({"error": error}), 400
    result = num1 * num2
    return jsonify({"result": result})

@app.route('/operation/divisao/<param1>/<param2>', methods=['POST'])
def divide(param1, param2):
    num1, num2, error = parse_params(param1, param2)
    if error:
        return jsonify({"error": error}), 400
    if num2 == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    result = num1 / num2
    return jsonify({"result": result})

@app.route('/operations', methods=['GET'])
def list_operations():
    operations = {
        "operations": [
            {"name": "Soma", "path": "/operation/soma/param1/param2", "method": "POST"},
            {"name": "Subtracao", "path": "/operation/subtracao/param1/param2", "method": "POST"},
            {"name": "Multiplicacao", "path": "/operation/multiplicacao/param1/param2", "method": "POST"},
            {"name": "Divisao", "path": "/operation/divisao/param1/param2", "method": "POST"},
        ]
    }
    return jsonify(operations)

if __name__ == '__main__':
    app.run(debug=True)
