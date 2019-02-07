from flask import Flask

app = Flask(__name__)

# Raiz da URL
@app.route("/")
def hello():
    return "Servidor iniciado com sucesso."

if __name__ == "__main__":
    app.run(debug=True)