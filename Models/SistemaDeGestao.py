#imports necessários
from Cliente import *
from Estoque import *
from Fornecedor import *
from Funcionario import *
from ItemVenda import *
from Pedido import *
from Produto import *
from Venda import *

class SistemaDeGestao():
    """Objeto geral"""
    def __init__(self, clientes, funcionarios, estoque, vendas, pedidos):
        self._clientes = clientes # lista de objetos
        self._funcionarios = funcionarios # lista de objetos
        self._estoque = estoque # Objeto
        self._vendas = vendas # lista de objetos
        self._pedidos = pedidos # lista de objetos
    def adicionar_cliente(self, cliente): # adiciona um cliente no sistema
        pass 
    
    def adicionar_funcionario(self, funcionario):
        pass

    def realizar_venda(self, venda): #processa uma venda
        pass

    def gerar_relatorio_vendas(self): # printa no terminal os objetos de vendas realizados
        pass
