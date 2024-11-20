class Fornecedor():
    def __init__(self, id_fornecedor, nome, contato, produtos_fornecidos):
        """ produtos_fornecidos deve ser um dictionary com objetos do tipo Produto"""
        self._id_fornecedor = id_fornecedor
        self._nome = nome
        self._contato = contato
        self._produtos_fornecidos = produtos_fornecidos

    def adicionar_produto(self, produto): #adiciona um produto fornecido ao dicionario de produtos
        pass

    def remover_produto(self, codigo): # remove um produto fornecido do dicionario de produtos
        pass

