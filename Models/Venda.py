class Venda():
    def __init__(self, id_venda, Cliente, data, itens, valor_total, funcionario_responsavel):
        self._id_venda = id_venda
        self._Cliente = Cliente
        self._data = data
        self._itens = itens
        self._valor_total = valor_total
        self._funcionario_responsavel = funcionario_responsavel
    def calcular_valor_total(self): #deve calcular o valor_total e armazenar em valor_total
        pass

    def adicionar_item(self, item): #adiciona novo item a compra
        pass
