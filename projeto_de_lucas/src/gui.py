import tkinter as tk
from tkinter import ttk
import database

root = tk.Tk()
root.title("Cadastro de Produtos")
root.geometry("400x400")

tk.Label(root, text="Nome do Produto:").pack(pady=(10, 0))
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Preço:").pack(pady=(10, 0))
entry_preco = tk.Entry(root)
entry_preco.pack()

def adicionar():
    if entry_nome.get() and entry_preco.get():
        database.inserir_item(entry_nome.get(), entry_preco.get())
        atualizar_lista()
        entry_nome.delete(0, tk.END)
        entry_preco.delete(0, tk.END)

def atualizar_lista():
    for i in tree.get_children():
        tree.delete(i)
    for row in database.listar_itens():
        tree.insert("", "end", values=row)

btn = tk.Button(root, text="Cadastrar", command=adicionar)
btn.pack(pady=15)

tree = ttk.Treeview(root, columns=("ID", "Nome", "Preço"), show='headings')
tree.heading("ID", text="ID"); tree.heading("Nome", text="Nome"); tree.heading("Preço", text="Preço")
tree.column("ID", width=30)
tree.pack(fill=tk.BOTH, expand=True)

database.conectar()
atualizar_lista()
root.mainloop()