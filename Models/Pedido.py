class Pedido():

    """Objeto de pedido do Cliente"""

    def __init__(self, id_pedido, fornecedor, data_pedido, itens_pedido):
        self._id_pedido = id_pedido
        self._fornecedor = fornecedor
        self._data_pedido = data_pedido
        self._itens_pedido = itens_pedido # lista de objetos do tipo pedido
    def calcular_valor_pedido(self, itens):
        """"""
        pass
    def adicionar_item_pedido(self, item):
        pass
    def finalizar_pedido(self): # Atualiza o Estoque
        pass
