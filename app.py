from flask import Flask, jsonify, request
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

# Retorna todos os produtos
@app.route('/produto', methods=['GET'])
def get_produto():
    produtos = Produto.query.all()

    retorno = []

    for produto in produtos:
        dados = {}
        dados['id']        = produto.id
        dados['descricao'] = produto.descricao
        dados['valor']     = produto.valor
        retorno.append(dados)

    return jsonify({'retorno':retorno})

# Retorna os produtos pelo ID
@app.route('/produto/<int:id>', methods=['GET'])
def get_produto_por_id(id):
    produto = Produto.query.filter_by(id=id).first()

    if not produto:
        return jsonify({'retorno':'Nenhum produto foi encontrado'})
        
    dados = {}
    dados['id']        = produto.id
    dados['descricao'] = produto.descricao
    dados['valor']     = produto.valor    

    return jsonify({'produtos':dados})    

# Inserindo um novo produto
@app.route('/produto', methods=['POST'])
def post_produto():    
    dados = request.get_json()

    novo_produto = Produto(id=dados['id'], descricao=dados['descricao'], valor=dados['valor'])
    db.session.add(novo_produto)
    db.session.commit()

    return jsonify({'retorno':'Produto inserido.'})

# Editando um produto
@app.route('/produto/<int:id>', methods=['PUT'])
def put_produto(id):            
    produto = Produto.query.filter_by(id=id).first()

    if not produto:
        return jsonify({'retorno':'Nenhum produto foi encontrado'})

    dados = request.get_json()        

    produto.id        = dados['id']
    produto.descricao = dados['descricao']
    produto.valor     = dados['valor']

    db.session.commit()

    return jsonify({'retorno':'Produto alterado.'})

# Deletando um produto
@app.route('/produto/<int:id>', methods=['DELETE'])
def delete_produto(id):      
    produto = Produto.query.filter_by(id=id).first()

    if not produto:
        return jsonify({'retorno':'Nenhum produto foi encontrado'})

    db.session.delete(produto)
    db.session.commit()

    return jsonify({'retorno':'Produto deletado.'})

if __name__ == "__main__":
    app.run(debug=True)