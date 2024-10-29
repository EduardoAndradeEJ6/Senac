import os

os.system('cls')

# tuplas_vazia = ()

# # Tupla de um elemento
# tupla_um_elemento = (10,)
# # print(tupla_um_elemento)
# # print(type(tupla_um_elemento))

# tupla_varios_elementos = (5, 4, 10, 15, 12)
# # print(tupla_varios_elementos)

# # tupla_um_elemento = tupla_um_elemento + tupla_varios_elementos

# # print(sorted{tupla_um_elemento})


nome = input('Informe o nome: ')
nota1 = input('Informe a nota 1: ')
nota2 = input('Informe a nota 2: ')

tupla_notas = (nome, nota1, nota2)

print(f'Dados do usuário: {tupla_notas}')