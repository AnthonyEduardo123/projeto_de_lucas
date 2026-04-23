import sqlite3

def conectar():
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS itens 
                      (id INTEGER PRIMARY KEY, nome TEXT, categoria TEXT)''')
    conn.commit()
    conn.close()

def inserir_item(nome, categoria):
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO itens (nome, categoria) VALUES (?, ?)", (nome, categoria))
    conn.commit()
    conn.close()

def listar_itens():
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM itens")
    dados = cursor.fetchall()
    conn.close()
    return dados
