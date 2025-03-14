import sqlite3
import pandas as pd
from datetime import date

conn = sqlite3.connect('e_commerce.db')
cursor = conn.cursor()

def inserir_usuario():
    nome = input("Nome do usuário: ")
    email = input("E-mail do usuário: ")
    data_cadastro = date.today()
    
    cursor.execute('''
        INSERT INTO usuarios (nome, email, data_cadastro)
        VALUES (?, ?, ?);
    ''', (nome, email, data_cadastro))
    conn.commit()
    print("Usuário cadastrado com sucesso!\n")

def inserir_produto():
    nome = input("Nome do produto: ")
    categoria = input("Categoria do produto: ")
    preco = float(input("Preço do produto: "))
    estoque = int(input("Quantidade em estoque: "))

    cursor.execute('''
        INSERT INTO produtos (nome, categoria, preco, estoque)
        VALUES (?, ?, ?, ?);
    ''', (nome, categoria, preco, estoque))
    conn.commit()
    print("Produto cadastrado com sucesso!\n")

def inserir_vendedor():
    nome = input("Nome do vendedor: ")
    email = input("E-mail do vendedor: ")
    data_cadastro = date.today()

    cursor.execute('''
        INSERT INTO vendedores (nome, email, data_cadastro)
        VALUES (?, ?, ?);
    ''', (nome, email, data_cadastro))
    conn.commit()
    print("Vendedor cadastrado com sucesso!\n")

def inserir_venda():
    id_usuario = int(input("ID do usuário: "))
    id_produto = int(input("ID do produto: "))
    id_vendedor = int(input("ID do vendedor: "))
    quantidade = int(input("Quantidade vendida: "))
    data_venda = date.today()

    cursor.execute('''
        INSERT INTO vendas (id_usuario, id_produto, id_vendedor, quantidade, data_venda)
        VALUES (?, ?, ?, ?, ?);
    ''', (id_usuario, id_produto, id_vendedor, quantidade, data_venda))
    conn.commit()
    print("Venda registrada com sucesso!\n")

while True:
    print("1 - Inserir Usuário")
    print("2 - Inserir Produto")
    print("3 - Inserir Vendedor")
    print("4 - Inserir Venda")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        inserir_usuario()
    elif escolha == '2':
        inserir_produto()
    elif escolha == '3':
        inserir_vendedor()
    elif escolha == '4':
        inserir_venda()
    elif escolha == '5':
        break
    else:
        print("Opção inválida. Tente novamente.\n")

cursor.close()
conn.close()

print("Programa encerrado.")
