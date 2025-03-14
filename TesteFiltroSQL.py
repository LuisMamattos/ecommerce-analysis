conn = sqlite3.connect('/content/e_commerce.db')
cursor = conn.cursor()

query = '''
    SELECT vendas.id, vendas.data_venda, vendas.quantidade,
           produtos.nome AS produto, usuarios.nome AS usuario, vendedores.nome AS vendedor
    FROM vendas
    JOIN produtos ON vendas.id_produto = produtos.id
    JOIN usuarios ON vendas.id_usuario = usuarios.id
    JOIN vendedores ON vendas.id_vendedor = vendedores.id
'''

cursor.execute(query)

resultados = cursor.fetchall()

df_vendas = pd.DataFrame(resultados, columns=['id', 'data_venda', 'quantidade', 'produto', 'usuario', 'vendedor'])

print(df_vendas)

cursor.close()
conn.close()
