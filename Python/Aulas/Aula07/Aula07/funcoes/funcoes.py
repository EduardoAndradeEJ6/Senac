import os

os.system('cls')


def decoracao():
    print()
    print(30 * '=')


def saudacao(txt):
    print(f'Olá {txt}')


def somar_valores(a,b):
    total = a + b 
    med = (a + b ) / 2
    return total , med
    
    # print(F"A soma dos números é {total:.2f}")

# decoracao()
# print('Iniciando programa')
# print('Nome: ')
# print('Idade: ')
# print('Cidade: ')

# decoracao()
# print('Dados Pessoais')
# print('CPF: ')
# print('RG: ')


# decoracao()
# print('Redes Sociais')
# print('Linkedin: ')
# print('GitHub: ')

# print('Iniciando o programa')
# nome = input('Informe o seu nome: ')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

valor = somar_valores(n1,n2)

print(f'A soma dos números e divisão : {valor}')
