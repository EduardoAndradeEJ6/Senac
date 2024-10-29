import os

os.system('cls')

senha = '54321'
login = 'Eduardo'
leitura = ''

while leitura != senha:
    leitura = input('Digite senha: ')
    if leitura == senha:
        print('Acesso liberado')
    else:
        print('Acesso negado. Tente novamente.')