import os

os.system('cls')

# EXEMPLO DE FUNÇÕES
# =======================================================
# EXEMPLO [1]

# def calcula_dobro(x):
#     dobro = x * 2
#     print(dobro)



# # PARTE PRINCIPAL
# num = float(input('Informe o número: '))

# calcula_dobro(num)

# =======================================================
# EXEMPLO [2]
# def calcula_dobro(x):
#     dobro = x * 2
#     return dobro



# # PARTE PRINCIPAL
# num = float(input('Informe o número: '))

# resultado = calcula_dobro(num)
# print(resultado)

# =======================================================
# EXEMPLO [3]

# def calcula_dobro(x):
#     return x * 2


# # PARTE PRINCIPAL
# num = float(input('Informe o número: '))

# print(calcula_dobro(num))

# =======================================================
# EXEMPLO [4]

def calcula_dobro(x):
    dobro = x * 2
    triplo = x * 3
    return dobro, triplo


num = float(input('Informe o número: '))

x2, x3 = calcula_dobro(num)

print(f'O dobro é {x2}, o triplo é {x3}.')
