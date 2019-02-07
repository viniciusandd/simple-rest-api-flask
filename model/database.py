import psycopg2

class Database():
    def __init__(self, banco, usuario, senha):
        try:
            self.connection = psycopg2.connect(
                "dbname='%s' user='%s' host='localhost' password='%s' port='5432'" % (banco, usuario, senha))
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Conexão com o banco de dados efetuada com sucesso!")
        except Exception as e:
            print("Erro ao conectar no database: %s" % e)

    def query(self, sql):
        self.cursor.execute(sql)
        registros = self.cursor.fetchall()
        return registros

    def execute(self, sql):
        self.cursor.execute(sql)

# Deixar sem aspas (simples/dupla) se for ler essas informações de um arquivo
banco   = input('informe o nome do banco de dados: ')
usuario = input('informe o usuario: ')
senha   = input('informe a senha: ')

db = Database(banco, usuario, senha)

produtos = db.query("SELECT * FROM PRODUTOS")

for i in produtos:
    print(i)

