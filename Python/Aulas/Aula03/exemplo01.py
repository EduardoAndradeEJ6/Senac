import os

os.system('cls')

print('--- Exemplo 01 - Aula 3 ---')

profissao =  (input('Informe sua profissão: ')).upper()
localidade = (input('Informe seu estado por extenso: ')).upper()

if profissao == 'PROFESSOR' and localidade == 'RIO DE JANEIRO':
    print ('Válido para desconto')
else:
    print ('Inválido para desconto')