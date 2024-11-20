class SistemaDeGestao():
    """Objeto geral"""
    def __init__(self, clientes, funcionarios, estoque, vendas, pedidos):
        self._clientes = clientes
        self._funcionarios = funcionarios
        self._estoque = estoque
        self._vendas = vendas
        self._pedidos = pedidos
    def adicionar_cliente(self, cliente): #adiciona um cliente no sistema
        pass 
    
    def adicionar_funcionario(self, funcionario):
        pass

    def realizar_venda(self, venda): #processa uma venda
        pass

    def gerar_relatorio_vendas(self): # printa no terminal os objetos de vendas realizados
        pass
