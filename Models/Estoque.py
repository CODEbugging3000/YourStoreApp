from time import sleep
from Models.BancodeDados import BancodeDados

class Estoque:
    def __init__(self):
        db = BancodeDados()  # Obtém a instância do banco de dados
        self.conn = db.conn
        self.cursor = db.cursor

    def adicionar_produto(self, produto): # adiciona um produto ao Estoque
        self.cursor.execute("INSERT INTO estoque (codigo, nome, categoria, preco, quantidade) VALUES (?, ?, ?, ?, ?)",(
            produto.codigo, produto.nome, produto.categoria, int(produto.preco), int(produto.quantidade_estoque)))
        self.conn.commit()

    def remover_produto(self, codigo):  # remove um produto pelo seu código
        self.cursor.execute("DELETE FROM estoque WHERE codigo = ?", (codigo,))
        self.conn.commit()  # Confirma a transação no banco de dados

    def consultar_produto(self, codigo): #consulta um produto pelo seu código
        self.cursor.execute("SELECT * FROM estoque WHERE codigo = ?", (codigo,))
        produto = self.cursor.fetchone()
        if produto:
            print(f"- Código: {produto[1]}, Nome: {produto[2]}, Categoria: {produto[3]}, Preço: {produto[4]}, Quantidade: {produto[5]}")
            input("Pressione ENTER para voltar: ")
        else:
            print("Produto não encontrado.")
            input("Pressione ENTER para voltar: ")

    def listar_produtos(self): # Printa todos os produtos no Estoque
        """Lista todos os produtos do estoque."""
        self.cursor.execute("SELECT * FROM estoque")
        produtos = self.cursor.fetchall()
        if produtos:
            for produto in produtos:
                print(f"- Código: {produto[1]}, Nome: {produto[2]}, Categoria: {produto[3]}, Preço: {produto[4]}, Quantidade: {produto[5]}")
                sleep(0.2)
            input("Pressione ENTER para voltar: ")
        else:
            print("O estoque está vazio.")

