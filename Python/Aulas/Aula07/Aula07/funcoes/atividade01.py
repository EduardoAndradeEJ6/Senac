import os

os.system('cls')


def divisao(n):
    resposta = ''
    num = n % 2
    if num == 0:
        resposta ='Par'
    else:
         resposta ='ímpar'
    return resposta
    


n = float(input('Digite um número: '))

resp = divisao(n)

print(f'{n} é {resp}')




