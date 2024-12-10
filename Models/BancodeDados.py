import sqlite3
class BancodeDados:
    # Conectar ao banco de dados
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()
    