import sqlite3

class BancodeDados:
    _instance = None  # Singleton para garantir uma única conexão
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.conn = sqlite3.connect('meu_banco.db')
            cls._instance.cursor = cls._instance.conn.cursor()
        return cls._instance

    def fechar_conexao(self):
        self.conn.close()
        BancodeDados._instance = None