import os

os.system('cls')

# print('--- Atividade 01 - Aula 3 ---')

# n = int(input('Informe um número: '))

# if n >= 1:
#     print(f'O número é positivo {n}')

# elif n == 0:

#     print(f'Número inválido {n}')

# else:
#     print (f'O número é negativo {n}')

n = int(input('Informe um número: '))

if n != 0:
    if n > 0:
        print(f'Positivo {n}')
    else:
        print(f'Negativo {n}')
else:
    print(f'Não digite zero')

