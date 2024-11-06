
import os

os.system ('cls')

import numpy as np

dados_salario = [2000 , 2500 , 3000 , 3500 , 4000 , 30000]

mediana = np.median(dados_salario)

print('')
print(f'A mediana dos salarios é de  {mediana}')