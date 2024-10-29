import os 

def limpa_tela():
    os.system('cls')


def decoracao():
    print(20* '=')


# ATIVIDADE [1]
# FUNÇÕES SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO E DIVISÃO.


limpa_tela()
decoracao()
print('Calculadora')
print('')

import random


def gerar_numeros():
    x = random.randint(1, 10)
    y = random.randint(1,10)
    return x, y


def soma(x, y):
    total = x + y
    return total


def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y



n1, n2 = gerar_numeros()

x1 = soma(n1, n2)
print(f'{n1} + {n2}, A soma é igual {x1}')


x2 = subtracao(n1, n2)
print(f'{n1} - {n2}, A subtração é igual {x2}')


x3 = multiplicacao(n1, n2)
print(f'{n1} x {n2}, A multiplicação é igual {x3}')


x4 = divisao(n1, n2)
print(f'{n1} / {n2}, A divisão é igual {x4}')