import pandas as pd 
import numpy as np
import os 

os.system('cls')

df = pd.read_excel('vendas_eletos_eletronicos2.xlsx')

# print(df)

total = df['Total']

produtos = df['Nome do Produto']

vendas_unidades = df['Vendas (unidades)']

print('Mediana do total da quantidade de produtos vendidos')
mediana = np.median(vendas_unidades)
print(mediana)
print('------------------------------------')
print('Media do total da quantidade de produtos vendidos')
media = np.mean(vendas_unidades)
print(media)
print('------------------------------------')
print('25% do total das vendas')
q1 = np.quantile(vendas_unidades, 0.25)
print(f'q1:  {q1}')
print('')
print('50% do total das vendas')
q2 = np.quantile(vendas_unidades, 0.50)
print(f'q2:  {q2}')
print('')
print('75% do total das vendas')
q3 = np.quantile(vendas_unidades, 0.75)
print(f'q3:  {q3}')
print('')
# print(produtos.describe())

print('Produtos mais vendidos')
filtro = q3
top_vendas = df [df['Vendas (unidades)'] > filtro]
print(top_vendas[['Nome do Produto','Vendas (unidades)']])


