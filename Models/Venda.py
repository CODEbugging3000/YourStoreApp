class Venda:
    def __init__(self, id_venda, cliente, data, itens, valor_total, funcionario_responsavel):
        self.id_venda = id_venda 
        self.Cliente = cliente # Objeto Cliente
        self.data = data
        self.itens = itens # lista de objetos de ItemVenda
        self.valor_total = valor_total
        self.funcionario_responsavel = funcionario_responsavel # Objeto Funcionario
    def calcular_valor_total(self): # deve calcular o valor_total e armazenar em valor_total
        return 0

    def adicionar_item(self, item): # adiciona novo item a compra
        self.itens.append(item)
