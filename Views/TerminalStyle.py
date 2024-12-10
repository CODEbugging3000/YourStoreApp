import os
class TerminalStyle:
    def __init__(self):
        self.frufru1 = "-=" * 20
        pass
    def apresentacao_inicial(self):
        os.system('clear')
        print(self.frufru1, "Bem-vindo ao Sistema de Gestão de Vendas YourStoreApp", self.frufru1)
        print("Escolha uma opcao: ")
        print("1 - Fazer login")
        print("2 - Criar uma nova conta")
        print("3 - Sair")
        op = input("Opcao: ")
        os.system('clear')
        return op

    def loginPage(self):
        os.system('clear')
        print(self.frufru1,"Login", self.frufru1)
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        os.system('clear')
        return [email, senha]

    def RegisterPage(self):
        os.system('clear')
        print(self.frufru1,"Cadastro", self.frufru1)
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        nome = input("Digite seu nome: ")
        cnpj = input("Digite seu CNPJ: ")
        os.system('clear')
        return [email, senha, nome, cnpj]
    
    def loggedinPage(self):
        os.system('clear')
        print(self.frufru1,"Bem-vindo ao Sistema de Gestão de Vendas YourStoreApp", self.frufru1)
        print("Escolha uma opcao: ")
        print("1 - Adicionar um novo cliente")
        print("2 - Realizar uma venda")
        print("3 - gerenciar estoque")
        print("4 - Logout")
        op = input("Opcao: ")
        os.system('clear')
        return op
    
    def estoque(self):
        os.system('clear')
        print(self.frufru1,"Estoque", self.frufru1)
        print("1 - Listar todos osprodutos")
        print("2 - Adicionar produtos")
        print("3 - Remover produtos")
        print("4 - Consultar produto")
        print("5 - Voltar")
        op = input("Opcao: ")
        os.system('clear')
        return op
    
    def cadastro_produto(self):
        os.system('clear')
        print(self.frufru1,"Cadastro de produtos", self.frufru1)
        codigo = input("Digite o codigo do produto: ")
        nome = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria do produto: ")
        preco = input("Digite o preco do produto: ")
        estoque = input("Digite a quantidade em estoque: ")
        os.system('clear')
        return [codigo, nome, categoria, preco, estoque]
    def remover_produto(self):
        """ Recebe do terminal o codigo do produto a ser removido do estoque"""
        os.system('clear')
        print(self.frufru1,"Remover produto", self.frufru1)
        codigo = input("Digite o codigo do produto: ")
        os.system('clear')
        return codigo
    
    def consultar_produto(self):
        os.system('clear')
        print(self.frufru1,"Consultar produto", self.frufru1)
        codigo = input("Digite o codigo do produto: ")
        os.system('clear')
        return codigo