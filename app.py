from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar_cep():
    cep = request.form.get('cep', '').strip().replace('-', '')
    if len(cep) != 8 or not cep.isdigit():
        return jsonify({'erro': 'CEP inválido!'})

    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if response.status_code != 200:
        return jsonify({'erro': 'Erro ao consultar API!'})

    data = response.json()
    if 'erro' in data:
        return jsonify({'erro': 'CEP não encontrado!'})

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
