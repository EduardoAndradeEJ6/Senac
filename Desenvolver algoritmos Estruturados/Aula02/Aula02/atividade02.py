import pandas as pd 
import numpy as np
import os 

os.system('cls')

df = pd.read_excel('vendas_roupas1.xlsx')

categoria = df['Categoria']

quantidade_vendida = df['Quantidade Vendida']

quantidade_vendida_org = df.sort_values(by='Quantidade Vendida')
quantidade_vendida = quantidade_vendida_org['Quantidade Vendida']
print(quantidade_vendida.values)



 # print(df)
# print('')
# print(categoria.unique())
# print('')
# # print(quantidade_vendida)

# print('')
# q1 = np.quantile(quantidade_vendida, 0.25)
# print(f'q1:  {q1}')

# print('')
# q2 = np.quantile(quantidade_vendida, 0.50)
# print(f'q2:  {q2}')

# print('')
# q3 = np.quantile(quantidade_vendida, 0.75)
# print(f'q3:  {q3}')
# print('')

# print('Media')
# media = np.mean(quantidade_vendida)
# print(media)

# print('Mediana')
# mediana = np.median(quantidade_vendida)
# print(mediana)