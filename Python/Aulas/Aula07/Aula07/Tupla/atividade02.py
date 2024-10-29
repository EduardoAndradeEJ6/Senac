import os

os.system('cls')


n1 = int(input('Informe o primeiro número '))
n2 = int(input('Informe o segundo número '))
n3 = int(input('Informe o terceiro número '))
n4 = int(input('Informe o quarto número '))
n5 = int(input('Informe o quinto número  '))


tupla_numeros = (n1,n2,n3,n4,n5)

soma = (sum(tupla_numeros))
maior = (max(tupla_numeros))
menor = (min(tupla_numeros))

print(f'\n O maior número é: {maior} \n O menor número é: {menor} \n A soma dos números é: {soma:.2f}')
print(sorted(tupla_numeros))

