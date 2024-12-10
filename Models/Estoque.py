from Models.BancodeDados import BancodeDados
class Estoque:
    def __init__(self):
        get_produtos = BancodeDados.conn.execute("SELECT * FROM estoque")
        self.produtos = get_produtos

    def adicionar_produto(self, produto): # adiciona um produto ao Estoque
        BancodeDados.cursor.execute("INSERT INTO estoque (codigo, nome, categoria, preco, quantidade) VALUES (?, ?, ?, ?, ?)",(
            produto.codigo, produto.nome, produto.categoria, int(produto.preco), int(produto.quantidade_estoque)))

    def remover_produto(self, codigo):  # remove um produto pelo seu código
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.pop(codigo)

    def consultar_produto(self, codigo): #consulta um produto pelo seu código
        pass

    def listar_produtos(self): # Printa todos os produtos no Estoque
        op = ''
        while op not in "yYyesYes":
            for i in self.produtos:
                print(i)
                print("\n")
            op = input("sair?(y/n): ")

