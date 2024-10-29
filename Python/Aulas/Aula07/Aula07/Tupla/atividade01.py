import os

os.system('cls')



nome = input('Informe o nome: ')
cargo = input('Informe o seu cargo: ')
salario = input('Informe o seu Salário: ')
idade = input('Informe a sua idade: ')

tupla_dados = (nome, cargo, salario, idade)

print(f'Os dados do usuario são: \n {tupla_dados}')