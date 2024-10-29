import os

os.system ('cls')

import numpy as np

dados = np.array([12,15,17,20,22,25,28,30,35,40])

q1 = np.quantile(dados, 0.25)
print(f'q1 25% {q1}')

q2 = np.quantile(dados, 0.50)
print(f'q2 50% {q2}')

q3 = np.quantile(dados, 0.75)
print(f'q3 75% {q3}')

