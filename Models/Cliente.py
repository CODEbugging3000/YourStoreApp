class Cliente:
    def __init__(self, id_cliente, nome, telefone, email, historico_compras):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.historico_compras = historico_compras
    def adicionar_compra(self, venda):    # Adicionar uma nova venda
        self.historico_compras.append(venda)

    def visualizar_historico(self):    # Printar a lista de historico_compras:
        for venda in self.historico_compras:
            print(venda)
