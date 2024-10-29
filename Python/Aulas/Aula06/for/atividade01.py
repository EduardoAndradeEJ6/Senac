import os

os.system('cls')


# for e in range (10,0, -1 ):
#     print(f'Contagem regressiva {e}')


n = int(input("Insira o número desejado: "))

for e in range (1, n + 1):
   if n % e == 0:
    print(e)


