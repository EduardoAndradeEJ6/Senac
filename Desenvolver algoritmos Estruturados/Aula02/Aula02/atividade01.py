import os

os.system ('cls')

import numpy as np

dados_venda = [150000 , 180000 , 200000 , 220000 , 250000 , 280000, 300000, 320000, 400000, 1500000]

mediana = np.median(dados_venda)
media = np.mean(dados_venda)



print('')
print(f'A media das vendas é de  {media}')
print('')
print(f'A mediana das vendas é de  {mediana}')
print('Devido a influencia do alto valor de venda unico, 1.500,000 a mediana traz um resultado mais preciso das vendas')