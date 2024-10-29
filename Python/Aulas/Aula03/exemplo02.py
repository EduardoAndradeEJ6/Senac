import os

os.system('cls')

print('--- Exemplo 02 - Aula 3 ---')

resposta = input('Quer desconto Sim / Não? ')[0].upper()

if resposta == 'S':
    print('Desconto aplicado')
else:
    print('Desconto não aplicado')

