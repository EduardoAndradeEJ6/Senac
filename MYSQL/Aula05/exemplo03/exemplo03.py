import os

os.system('cls')

from sqlalchemy import create_engine

import pandas as pd 

host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_vendas'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

query_clientes = "SELECT id_cliente, nome, email FROM tb_clientes"
df_clientes = pd.read_sql(query_clientes, engine)

df_pedidos = pd.read_excel('tb_pedidos.xlsx')

print(df_clientes)
print(df_pedidos)