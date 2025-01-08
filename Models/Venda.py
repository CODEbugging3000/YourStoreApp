import datetime
from Models.Cliente import Cliente
from Views.TerminalStyle import TerminalStyle
from Models.BancodeDados import BancodeDados
from time import sleep
class Venda:
    def __init__(self, cliente, codigo_do_item, quantidade_do_item):
        super().__init__()
        self.cliente = cliente
        self.codigo_do_item = codigo_do_item # lista de objetos de ItemVenda
        self.qnt_do_item = quantidade_do_item
        self.data = datetime.datetime.now()
        db = BancodeDados()  # Obtém a instância do banco de dados
        self.conn = db.conn
        self.cursor = db.cursor
    
    terminal = TerminalStyle()

    def calcular_valor_total(self): # deve calcular o valor_total e armazenar em valor_total
        self.cursor.execute("SELECT preco FROM estoque WHERE codigo = ?", (self.codigo_do_item,))
        resposta = self.cursor.fetchone()
        if resposta == ():
            print("Produto nao encontrado")
            sleep(1)
        else:
            preco = resposta[0]
        valor_total = preco * int(self.qnt_do_item)
        return valor_total

    def realizar_venda(self):
        self.cursor.execute("SELECT * FROM clientes WHERE id = ?", (self.cliente,))
        resultado = self.cursor.fetchall()
        if resultado == []:
            print("Cliente nao encontrado")
            print("Adicionando novo cliente...")
            sleep(1)
            dados_do_cliente = self.terminal.cadastro_de_cliente()
            novo_cliente = Cliente(dados_do_cliente[0], dados_do_cliente[1], dados_do_cliente[2])
            id_novo_cliente = novo_cliente.cadastrar_cliente(dados_do_cliente[0], dados_do_cliente[1], dados_do_cliente[2])
            self.conn.commit()

            # Adiciona a venda na tabela
            self.cursor.execute("SELECT nome FROM clientes WHERE id = ?", (id_novo_cliente,))
            nome_cliente = self.cursor.fetchone() # retorna uma tupla com 1 nome
            self.cursor.execute("SELECT nome FROM estoque WHERE codigo = ?", (self.codigo_do_item,))
            item = self.cursor.fetchone()
            self.cursor.execute("INSERT INTO vendas (id_cliente, cliente, data, item, total) VALUES (?, ?, ?, ?, ?)", (int(id_novo_cliente), nome_cliente[0], self.data, item[0], self.calcular_valor_total()))
            self.conn.commit()
            print("Venda realizada com sucesso!")
            input()
        else:
            print("Cliente encontrado")
            self.cursor.execute("SELECT nome FROM clientes WHERE id = ?", (self.cliente,))
            nome_cliente = self.cursor.fetchone()
            self.cursor.execute("SELECT nome FROM estoque WHERE codigo = ?", (self.codigo_do_item,))
            item = self.cursor.fetchone()
            self.cursor.execute("INSERT INTO vendas (id_cliente, cliente, data, item, total) VALUES (?, ?, ?, ?, ?)", (self.cliente, nome_cliente[0], self.data, item[0], self.calcular_valor_total()))
            self.conn.commit()
            print("Venda realizada com sucesso!")
            input()