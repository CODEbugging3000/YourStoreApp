import os
from time import sleep
class TerminalStyle:
    def __init__(self):
        self.frufru1 = "-=" * 20
        pass

    def clear(self):
        os.system('clear')

    def apresentacao_inicial(self):
        self.clear()
        print(self.frufru1, "Bem-vindo ao Sistema de Gestão de Vendas YourStoreApp", self.frufru1)
        print("Escolha uma opcao: ")
        print("1 - Fazer login")
        print("2 - Criar uma nova conta")
        print("3 - Sair")
        op = input("Opcao: ")
        self.clear()
        return op

    def loginPage(self):        
        self.clear()
        print(self.frufru1,"Login", self.frufru1)
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        self.clear()
        return [email, senha]

    def RegisterPage(self):
        self.clear()
        print(self.frufru1,"Cadastro", self.frufru1)
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        nome = input("Digite seu nome: ")
        cnpj = input("Digite seu CNPJ: ")
        self.clear()
        return [email, senha, nome, cnpj]
    
    def loggedinPage(self):
        self.clear()
        print(self.frufru1,"Bem-vindo ao Sistema de Gestão de Vendas YourStoreApp", self.frufru1)
        print("Escolha uma opcao: ")
        print("1 - Realizar uma venda")
        print("2 - gerenciar estoque")
        print("3 - Logout")
        op = input("Opcao: ")
        self.clear()
        return op
    
    def estoque(self):
        self.clear()
        print(self.frufru1,"Estoque", self.frufru1)
        print("1 - Listar todos osprodutos")
        print("2 - Adicionar produtos")
        print("3 - Remover produtos")
        print("4 - Consultar produto")
        print("5 - Voltar")
        op = input("Opcao: ")
        self.clear()
        return op
    
    def cadastro_produto(self):
        self.clear()
        print(self.frufru1,"Cadastro de produtos", self.frufru1)
        codigo = input("Digite o codigo do produto: ")
        nome = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria do produto: ")
        preco = input("Digite o preco do produto: ")
        estoque = input("Digite a quantidade em estoque: ")
        self.clear()
        return [codigo, nome, categoria, preco, estoque]
    def remover_produto(self):
        """ Recebe do terminal o codigo do produto a ser removido do estoque"""
        self.clear()
        print(self.frufru1,"Remover produto", self.frufru1)
        codigo = input("Digite o codigo do produto: ")
        self.clear()
        return codigo
    
    def consultar_produto(self):
        self.clear()
        print(self.frufru1,"Consultar produto", self.frufru1)
        codigo = input("Digite o codigo do produto: ")
        self.clear()
        return codigo
    
    def venda(self):
        self.clear()
        print(self.frufru1,"Realizar venda", self.frufru1)
        id_cliente = input("digite o id do cliente: ")
        codigo = input("digite o codigo do produto vendido: ")
        quantidade = input("digite a quantidade vendida: ")
        self.clear()
        return [id_cliente, codigo, quantidade]
    
    def pos_venda(self, total):
        self.clear()
        print(f"Venda de {total} realizada com sucesso!")
        sleep(2.5)
        self.clear()

    def cadastro_de_cliente(self):
        self.clear()
        print(self.frufru1,"Cadastro de clientes", self.frufru1)
        nome = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite o email do cliente: ")
        self.clear()
        return [nome, telefone, email]