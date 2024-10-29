import os

os.system('cls')

resposta = input('Informe a M ou F: ').upper()

if resposta != '':
    letra = resposta [0]

    if letra == 'M' or letra == 'F':

        if letra == 'F' :
            print('Feminino')
        elif letra =='M':
            print('Masculino')
        else:
            print('Sexo Inválido')

else:
    print('Digite novamente!!! ')
