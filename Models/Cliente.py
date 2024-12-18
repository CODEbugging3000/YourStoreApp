from Models.BancodeDados import BancodeDados

class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        db = BancodeDados()  # Obtém a instância do banco de dados
        self.conn = db.conn
        self.cursor = db.cursor

    def adicionar_compra(self, venda):    # Adicionar uma nova venda
        self.historico_compras.append(venda)

    def cadastrar_cliente(self, nome, telefone, email):
        self.cursor.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
        self.conn.commit()
        print("Cadastro realizado com sucesso!")
        self.cursor.execute("SELECT id FROM clientes WHERE email = ?", (email,))
        retorno = self.cursor.fetchone()
        return retorno[0]
    