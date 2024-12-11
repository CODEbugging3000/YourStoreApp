class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    def adicionar_compra(self, venda):    # Adicionar uma nova venda
        self.historico_compras.append(venda)

    def visualizar_historico(self):    # Printar a lista de historico_compras:
        pass
    def cadastrar_cliente(self, nome, telefone, email):
        self.cursor.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
        self.conn.commit()
        print("Cadastro realizado com sucesso!")
        input()
