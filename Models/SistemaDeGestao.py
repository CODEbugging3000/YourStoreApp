#Imports necessários
from time import sleep
from hamcrest import empty
from Models.BancodeDados import BancodeDados
from Models.Cliente import Cliente
from Models.Estoque import Estoque
from Models.Produto import Produto
from Models.Venda import Venda
from Models.Usuario import Usurario
from Views.TerminalStyle import TerminalStyle

class SistemaDeGestao(BancodeDados):
    """Objeto geral do programa"""
    def __init__(self):
        self.clientes = [] # lista de objetos
        self.vendas = [] # lista de objetos
        
    # Criar tabela usuario
    BancodeDados.cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        senha TEXT NOT NULL, 
        nome TEXT NOT NULL,
        cnpj TEXT NOT NULL
    )''')

    #criar tabela clientes
    BancodeDados.cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL, 
        historico_compras TEXT NOT NULL
    )''')
    
    BancodeDados.cursor.execute('''
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco INTEGER NOT NULL, 
            quantidade INTEGER NOT NULL
        )''')
    
    # Criar um objeto terminal
    terminal = TerminalStyle()

    def adicionar_cliente(self, cliente): # adiciona um cliente no sistema
        self.clientes.append(cliente)

    def historico_de_vendas(self, venda): #processa uma venda
        self.vendas.append(venda)

    def loginverify(self, email_e_senha=None):
        logado = False
        while not logado:
            if email_e_senha is None:
                email_e_senha = self.terminal.loginPage()
            usuario = Usurario(email_e_senha[0], email_e_senha[1])
            BancodeDados.cursor.execute("SELECT * FROM usuarios WHERE email = ?", (usuario.email,))
            resultado = BancodeDados.cursor.fetchall()
            if resultado is empty:
                print("Email nao cadastrado tente novamente")
                email_e_senha = None
            elif resultado is not empty and usuario.senha != resultado[0][2]:
                print("Senha incorreta tente novamente")
            else:
                print("Usuario logado com sucesso!")
                sleep(1)
                logado = True

    def cadastro(self, dados=None):
        cadastrou = False
        while not cadastrou:
            if dados is None:
                dados = self.terminal.RegisterPage()
            user = Usurario(dados[0], dados[1], dados[2], dados[3])

            # Verificar se o email ja foi cadastrado
            BancodeDados.cursor.execute("SELECT * FROM usuarios WHERE email = ?", (user.email,))
            resultado = BancodeDados.cursor.fetchall() # retorna uma lista de tuplas do SELECT
            if resultado == []:
                BancodeDados.cursor.execute("INSERT INTO usuarios (email, senha, nome, cnpj) VALUES (?, ?, ?, ?)", 
                                    (user.email, user.senha, user.nome, user.cnpj))
                BancodeDados.conn.commit()  # Salvar alterações
                print("Cadastro realizado com sucesso!")
                sleep(1)
                cadastrou = True
            else:
                print("Email ja cadastrado! tente novamente!")
                dados = None
                sleep(1)
    

    def run(self): #loop do sistema
        while True:
            op = self.terminal.apresentacao_inicial()
            if op == "1": # Login
                self.loginverify()
                while True:
                    op_logado = self.terminal.loggedinPage()
                    if op_logado == "1": # Adicionar um novo cliente
                        pass
                    elif op_logado == "2": # Realizar uma venda
                        pass
                    elif op_logado == "3": # Gerenciar estoque
                        self.Estoque = Estoque()
                        while True: # loop estoque
                            op_estoque = self.terminal.estoque()
                            if op_estoque == "1": # Listar produtos
                                self.Estoque.listar_produtos()
                            elif op_estoque == "2": # Adicionar produtos
                                self.post = self.terminal.cadastro_produto()
                                self.Estoque.adicionar_produto(Produto(self.post[0], self.post[1], self.post[2], self.post[3], self.post[4]))
                            elif op_estoque == "3": # Remover produtos
                                pass
                            elif op_estoque == "4": # Consultar produtos
                                pass
                            elif op_estoque == "5": # Voltar
                                break
                    elif op_logado == "4": # Logout
                        break
            elif op == "2": # Cadastro
                self.cadastro()
            elif op == "3": # Sair
                BancodeDados.conn.close() # Fecha Banco de Dados
                break
            else:
                print("Opcao invalida")
                sleep(1)
                pass
