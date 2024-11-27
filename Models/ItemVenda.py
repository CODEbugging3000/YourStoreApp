class ItemVenda():
    """Objeto do item da Venda"""
    def __init__(self, produto, quantidade, preco_unitario):
        self._produto = produto
        self._quantidade = quantidade
        self._preco_unitario = preco_unitario

    def calcular_total(self, quantidade, preco_unitario):
        return preco_unitario * quantidade

        
        
