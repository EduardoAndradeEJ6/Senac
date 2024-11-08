from sqlalchemy import create_engine

import os

os.system('cls')

import pandas as pd 

import numpy as np

import os

os.system('cls')

host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_loja'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

df_estoque = pd.read_sql('tb_produtos', engine)

df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']
# print(df_estoque[['NomeProduto','TotalEstoque']])

# print('')
# print('')
# print('')
# print('')

# mediana = np.median(df_estoque['TotalEstoque'])
# print(f'A mediana do total do estoque: {mediana}')

# media = np.mean(df_estoque['TotalEstoque'])
# print(f'A media do total do estoque: {media}')

array_total_estoque = np.array(df_estoque['TotalEstoque'])

media = np.mean(array_total_estoque)
mediana = np.median(array_total_estoque)

# print(f'Média do valor total: R${media:.2f}')
# print(f'Mediana do valor total: R${mediana:.2f}')

distancia = (media - mediana)/ mediana

# print(distancia)

proporcao = distancia * 100
# print(proporcao)

# print(f'Distância entre a média e a mediana: {distancia:.2f}')


df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']

df_agrupado = df_estoque.groupby('NomeProduto').agg({
    'QuantidadeEstoque' : 'sum',
    'TotalEstoque' : 'sum'
}).reset_index()

print(df_agrupado)

df_ordenado = df_agrupado. sort_values(by ='TotalEstoque', ascending=False)

print(df_ordenado[['NomeProduto', 'TotalEstoque']])

print(f'\n Total geral em estoque: R${df_ordenado["TotalEstoque"].sum()}')