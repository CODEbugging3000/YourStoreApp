import datetime
from Models import Cliente, SistemaDeGestao
from Models.BancodeDados import BancodeDados
from time import sleep
class Venda(SistemaDeGestao):
    def __init__(self, cliente, codigo_do_item, quantidade_do_item):
        self.cliente = cliente # Objeto Cliente
        self.codigo_do_item = codigo_do_item # lista de objetos de ItemVenda
        self.qnt_do_item = quantidade_do_item
        self.data = datetime.datetime.now()
        db = BancodeDados()  # Obtém a instância do banco de dados
        self.conn = db.conn
        self.cursor = db.cursor

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
            dados_do_cliente = super.adicionar_cliente()
            novo_cliente = Cliente(dados_do_cliente[0], dados_do_cliente[1], dados_do_cliente[2])
            novo_cliente.cadastrar_cliente(dados_do_cliente[0], dados_do_cliente[1], dados_do_cliente[2])
        else:
            self.cursor.execute("SELECT nome FROM clientes WHERE id = ?", (self.cliente,))
            nome_cliente = self.cursor.fetchone()[0]
            self.cursor.execute("INSERT INTO vendas (id_cliente, cliente, data, total) VALUES (?, ?, ?, ?)", (self.cliente, nome_cliente, self.data, self.calcular_valor_total()))

## TODO: Atualizar bd de clientes se não houver o cliente inserido na hora da venda, se tiver
## apenas associá-lo