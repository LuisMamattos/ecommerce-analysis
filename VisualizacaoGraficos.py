import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('e_commerce.db')  
cursor = conn.cursor()

cursor.execute('''
    SELECT v.data_venda, v.quantidade, p.nome AS produto, u.nome AS usuario, ve.nome AS vendedor
    FROM vendas v
    JOIN produtos p ON v.id_produto = p.id
    JOIN usuarios u ON v.id_usuario = u.id
    JOIN vendedores ve ON v.id_vendedor = ve.id
''')

data_vendas = cursor.fetchall()
df_vendas = pd.DataFrame(data_vendas, columns=['data_venda', 'quantidade', 'produto', 'usuario', 'vendedor'])

cursor.close()
conn.close()

vendas_produto = df_vendas.groupby('produto')['quantidade'].sum().reset_index()
vendas_produto = vendas_produto.sort_values(by='quantidade', ascending=False)

plt.figure(figsize=(10, 5))
plt.barh(vendas_produto['produto'], vendas_produto['quantidade'], color='skyblue')
plt.xlabel("Quantidade Vendida")
plt.ylabel("Produto")
plt.title("Vendas por Produto")
plt.gca().invert_yaxis()  # Inverter a ordem para mostrar o mais vendido primeiro
plt.show()

print("Dados de Vendas:")
print(df_vendas)
