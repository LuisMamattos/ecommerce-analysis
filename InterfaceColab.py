import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output
from datetime import date


conn = sqlite3.connect('e_commerce.db')# Conectar ao banco
cursor = conn.cursor()


def inserir_usuario(nome, email):
    clear_output()
    try:
        cursor.execute('''
            INSERT INTO usuarios (nome, email, data_cadastro)
            VALUES (?, ?, ?);
        ''', (nome, email, date.today()))
        conn.commit()
        print("Usuário cadastrado com sucesso!")
    except Exception as e:
        print("Erro:", e)


def inserir_produto(nome, categoria, preco, estoque):
    clear_output()
    try:
        cursor.execute('''
            INSERT INTO produtos (nome, categoria, preco, estoque)
            VALUES (?, ?, ?, ?);
        ''', (nome, categoria, preco, estoque))
        conn.commit()
        print("Produto cadastrado com sucesso!")
    except Exception as e:
        print("Erro:", e)


def inserir_vendedor(nome, email):
    clear_output()
    try:
        cursor.execute('''
            INSERT INTO vendedores (nome, email, data_cadastro)
            VALUES (?, ?, ?);
        ''', (nome, email, date.today()))
        conn.commit()
        print("Vendedor cadastrado com sucesso!")
    except Exception as e:
        print("Erro:", e)


def inserir_venda(id_usuario, id_produto, id_vendedor, quantidade):
    clear_output()
    try:
        cursor.execute('''
            INSERT INTO vendas (id_usuario, id_produto, id_vendedor, quantidade, data_venda)
            VALUES (?, ?, ?, ?, ?);
        ''', (id_usuario, id_produto, id_vendedor, quantidade, date.today()))
        conn.commit()
        print("Venda registrada com sucesso!")
    except Exception as e:
        print("Erro:", e)


def visualizar_vendas():
    clear_output()
    query = '''
        SELECT v.data_venda, v.quantidade, p.nome AS produto, u.nome AS usuario, ve.nome AS vendedor
        FROM vendas v
        JOIN produtos p ON v.id_produto = p.id
        JOIN usuarios u ON v.id_usuario = u.id
        JOIN vendedores ve ON v.id_vendedor = ve.id
    '''
    cursor.execute(query)
    data_vendas = cursor.fetchall()
    
    if not data_vendas:
        print("Nenhuma venda registrada.")
        return
    
    df_vendas = pd.DataFrame(data_vendas, columns=['Data', 'Quantidade', 'Produto', 'Usuário', 'Vendedor'])
    display(df_vendas)

    
    vendas_produto = df_vendas.groupby('Produto')['Quantidade'].sum().reset_index()
    vendas_produto = vendas_produto.sort_values(by='Quantidade', ascending=False)

    plt.figure(figsize=(8, 4))
    plt.barh(vendas_produto['Produto'], vendas_produto['Quantidade'], color='skyblue')
    plt.xlabel("Quantidade Vendida")
    plt.ylabel("Produto")
    plt.title("Vendas por Produto")
    plt.gca().invert_yaxis()
    plt.show()


# Usuário
input_nome_usuario = widgets.Text(placeholder="Nome")
input_email_usuario = widgets.Text(placeholder="E-mail")
btn_usuario = widgets.Button(description="Cadastrar Usuário", button_style='primary')
btn_usuario.on_click(lambda b: inserir_usuario(input_nome_usuario.value, input_email_usuario.value))

# Produto
input_nome_produto = widgets.Text(placeholder="Nome do Produto")
input_categoria = widgets.Text(placeholder="Categoria")
input_preco = widgets.FloatText(value=None, description="Preço")
input_estoque = widgets.IntText(value=None, description="Estoque")
btn_produto = widgets.Button(description="Cadastrar Produto", button_style='primary')
btn_produto.on_click(lambda b: inserir_produto(input_nome_produto.value, input_categoria.value, input_preco.value, input_estoque.value))

# Vendedor
input_nome_vendedor = widgets.Text(placeholder="Nome")
input_email_vendedor = widgets.Text(placeholder="E-mail")
btn_vendedor = widgets.Button(description="Cadastrar Vendedor", button_style='primary')
btn_vendedor.on_click(lambda b: inserir_vendedor(input_nome_vendedor.value, input_email_vendedor.value))

# Venda
input_id_usuario = widgets.IntText(value=None, description="Usuário")
input_id_produto = widgets.IntText(value=None, description="Produto")
input_id_vendedor = widgets.IntText(value=None, description="Vendedor")
input_quantidade = widgets.IntText(value=None, description="Qtd")
btn_venda = widgets.Button(description="Registrar Venda", button_style='primary')
btn_venda.on_click(lambda b: inserir_venda(input_id_usuario.value, input_id_produto.value, input_id_vendedor.value, input_quantidade.value))


btn_visualizar = widgets.Button(description="Visualizar Vendas", button_style='info')
btn_visualizar.on_click(lambda b: visualizar_vendas())


display(
    widgets.VBox([
        widgets.Label("Cadastro de Usuários"),
        input_nome_usuario, input_email_usuario, btn_usuario,
        widgets.Label(""),

        widgets.Label("Cadastro de Produtos"),
        input_nome_produto, input_categoria, input_preco, input_estoque, btn_produto,
        widgets.Label(""),
        
        widgets.Label("Cadastro de Vendedores"),
        input_nome_vendedor, input_email_vendedor, btn_vendedor,
        widgets.Label(""),

        widgets.Label("Registrar Venda"),
        input_id_usuario, input_id_produto, input_id_vendedor, input_quantidade, btn_venda,
        widgets.Label(""),

        widgets.Label("Visualizar Vendas"),
        btn_visualizar
    ])
)
