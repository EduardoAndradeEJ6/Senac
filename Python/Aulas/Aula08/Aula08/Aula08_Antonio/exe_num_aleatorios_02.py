import os

os.system('cls')

# BIBLIOTECA PARA NÚMEROS ALEATÓRIOS
# EXEMPLO [1]

# import random

# num = random.randint(1, 10)

# print(num)

# =======================================================
# EXEMPLO [2]

import random


def gera_numeros(inicio, final, quantidade):
    
    return [random.randint(inicio, final) for _ in range(quantidade)]



inicio = int(input('Informe o primeiro valor: '))
final = int(input('Informe o final: '))
quantidade = int(input('Quantos números você quer gerar? '))

numeros = gera_numeros(inicio, final, quantidade)

print(numeros)


# =======================================================
# EXEMPLO [3]
