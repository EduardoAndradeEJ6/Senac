import os

os.system('cls')

print('--- Atividade 02 - Aula 3 ---')

p = float(input('Informe o seu peso em KG: '))
a = float(input('Informe a sua altura em metros: '))
imc = float

imc = p / a ** 2


if imc <= 18.5:
    print('Abaixo do peso')

# elif imc == 18.5:
#     print ('Peso normal')

elif imc <= 24.9:
    print ('Peso normal')

# elif imc == 25.0:
#     print('Sobrepeso')

elif imc <= 29.9:
    print('Sobrepeso')

elif imc >= 30:
    print('Obesidade')

print(f'Seu IMC é {imc}')
