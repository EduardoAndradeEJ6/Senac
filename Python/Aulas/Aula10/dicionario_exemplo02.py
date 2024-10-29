import os 
os.system('cls')


pessoas = {}


for i in range(1):
    os.system('cls')
    nome = input('Digite o nome: ')
    email = input( 'Digite o email: ')
    idade = input('Digite a idade: ')
    cpf = input('Digite o CPF: ')

    pessoas [nome] = {
        'EMAIL' : email,
        'IDADE' : idade,
        'CPF'   : cpf
    }

    print(pessoas[nome]['EMAIL'])
  