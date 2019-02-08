from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/local'
db = SQLAlchemy(app)

class Produto(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50))
    valor     = db.Column(db.Float)

# Raiz da URL
@app.route("/", methods=['GET'])
def inicio():
    return "<h3> Servidor iniciado com sucesso! </h3>"

@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()

    retorno = []

    for produto in produtos:
        dados = {}
        dados['id']        = produto.id
        dados['descricao'] = produto.descricao
        dados['valor']     = produto.valor
        retorno.append(dados)

    return jsonify({'produtos':retorno})

if __name__ == "__main__":
    app.run(debug=True)