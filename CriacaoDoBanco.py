import sqlite3
import pandas as pd
from datetime import date

 
conn = sqlite3.connect('/content/e_commerce.db')
cursor = conn.cursor()

 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT UNIQUE,
        data_cadastro DATE
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        categoria TEXT,
        preco REAL,
        estoque INTEGER
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT UNIQUE,
        data_cadastro DATE
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        id_produto INTEGER,
        id_vendedor INTEGER,
        quantidade INTEGER,
        data_venda DATE,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
        FOREIGN KEY (id_produto) REFERENCES produtos(id),
        FOREIGN KEY (id_vendedor) REFERENCES vendedores(id)
    );
''')


conn.commit()

cursor.close()
conn.close()

print("Banco de dados SQLite criado com sucesso!")
