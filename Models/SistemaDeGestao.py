#Imports necessários
from time import sleep
from hamcrest import empty
from Models.Cliente import Cliente
from Models.Estoque import Estoque
from Models.Produto import Produto
from Models.Venda import Venda
from Models.Usuario import Usurario
from Views.TerminalStyle import TerminalStyle
from Models.BancodeDados import BancodeDados

class SistemaDeGestao:
    """Objeto geral do programa"""
    def __init__(self):
        # Obtém a instância única do banco de dados
        db = BancodeDados()
        self.conn = db.conn
        self.cursor = db.cursor
        self.cursor.execute("PRAGMA foreign_keys = ON") # Habilita as chaves estrangeiras
        self.clientes = [] # lista de objetos
        # Criar tabelas
        self._criar_tabelas()
    # Criar um objeto terminal
    terminal = TerminalStyle()

    def _criar_tabelas(self):
        """Cria as tabelas necessárias no banco de dados."""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            senha TEXT NOT NULL, 
            nome TEXT NOT NULL,
            cnpj TEXT NOT NULL
        )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL, 
            historico_compras TEXT NOT NULL
        )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL, 
            quantidade INTEGER NOT NULL
        )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL REFERENCES clientes(id),
            cliente TEXT NOT NULL,
            data TEXT NOT NULL,
            item TEXT NOT NULL,
            total REAL NOT NULL
        )''')
        self.conn.commit()  # Salva alterações no banco
    
    def fechar(self):
        """Fecha a conexão com o banco de dados."""
        db = BancodeDados()  # Obtém a instância existente do banco de dados
        db.fechar_conexao()  # Chama o método fechar_conexao na instância

    def loginverify(self, email_e_senha=None):
        logado = False
        while not logado:
            if email_e_senha is None:
                email_e_senha = self.terminal.loginPage()
            usuario = Usurario(email_e_senha[0], email_e_senha[1])
            self.cursor.execute("SELECT * FROM usuarios WHERE email = ?", (usuario.email,))
            resultado = self.cursor.fetchall()
            if resultado == []:
                print("Email nao cadastrado tente novamente")
                sleep(1)
                email_e_senha = None
            elif resultado is not empty and usuario.senha != resultado[0][2]:
                print("Senha incorreta tente novamente")
                sleep(1)
                email_e_senha = None
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
            self.cursor.execute("SELECT * FROM usuarios WHERE email = ?", (user.email,))
            resultado = self.cursor.fetchall() # retorna uma lista de tuplas do SELECT
            if resultado == []:
                self.cursor.execute("INSERT INTO usuarios (email, senha, nome, cnpj) VALUES (?, ?, ?, ?)", 
                                    (user.email, user.senha, user.nome, user.cnpj))
                self.conn.commit()  # Salvar alterações
                print("Cadastro realizado com sucesso!")
                sleep(1)
                cadastrou = True
            else:
                print("Email ja cadastrado! tente novamente!")
                dados = None
                sleep(1)
    
    def adicionar_cliente(self, cliente): # adiciona um cliente no sistema
        dados_do_cliente = self.terminal.cadastro_de_cliente()
        return dados_do_cliente
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
                        dados_da_venda = self.terminal.venda()
                        estoque = Estoque()
                        tem_no_estoque = estoque.verificar_estoque(dados_da_venda[1])
                        if tem_no_estoque:
                            tem_o_suficiente = estoque.atualizar_estoque(dados_da_venda[1], dados_da_venda[2])
                            if tem_o_suficiente:
                                venda = Venda(dados_da_venda[0], dados_da_venda[1], dados_da_venda[2])
                                venda.realizar_venda()
                                self.terminal.pos_venda(venda.calcular_valor_total())
                    elif op_logado == "3": # Gerenciar estoque
                        estoque = Estoque()
                        while True: # loop estoque
                            op_estoque = self.terminal.estoque()
                            if op_estoque == "1": # Listar produtos
                                estoque.listar_produtos()
                            elif op_estoque == "2": # Adicionar produtos
                                post = self.terminal.cadastro_produto()
                                estoque.adicionar_produto(Produto(post[0], post[1], post[2], post[3], post[4]))
                            elif op_estoque == "3": # Remover produtos
                                codigo = self.terminal.remover_produto()
                                estoque.remover_produto(codigo)

                            elif op_estoque == "4": # Consultar produtos
                                codigo = self.terminal.consultar_produto()
                                estoque.consultar_produto(codigo)
                            elif op_estoque == "5": # Voltar
                                break
                    elif op_logado == "4": # Logout
                        break
            elif op == "2": # Cadastro
                self.cadastro()
            elif op == "3": # Sair
                self.fechar() # Fecha Banco de Dados
                break
            else:
                print("Opcao invalida")
                sleep(1)
                pass
    
