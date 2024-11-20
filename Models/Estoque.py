class Estoque():
    """Objeto para o Estoque"""
    def __init__(self, produto):
        #Produto deve ser um dictionary com chave = codigo_do_produto e valor = obj do tipo produto
        self._produto = produto

    def adicionar_produto(self, produto): # adiciona um produto ao Estoque
        pass

    def remover_produto(self, codigo):  # remove um produto pelo seu código
        pass

    def consultar_produto(self, codigo): #consulta um produto pelo seu código
        pass

    def listar_produtos(self): # Printa todos os produtos no Estoque
        pass

        
