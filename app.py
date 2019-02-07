from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Raiz da URL
@app.route("/", methods=['GET'])
def inicio():
    return "Servidor iniciado com sucesso."

produtos = [
    {
        'codigo': '01',
        'descricao': 'Mouse'
    },
    {
        'codigo': '02',
        'descricao': 'Monitor'
    },
    {
        'codigo': '03',
        'descricao': 'Notebook'
    } ,
    {
        'codigo': '04',
        'descricao': 'Cooler'
    }             
]

@app.route("/produtos", methods=['GET'])
def get_produtos():
    return jsonify(produtos)

if __name__ == "__main__":
    app.run(debug=True)