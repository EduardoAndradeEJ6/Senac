import os

os.system('cls')

# ------------------ exemplo 03-----------------------

# contador = 500

# while contador !=0:
#     print(contador)
#     contador -= 1



# ------------------ exemplo 03.1-----------------------

# s = 0
# c = 1 

# while c < 4:
#     n = int(input('Informe um número: '))
#     s += n
#     c +=1
# print('O total é ', s)


# ------------------ exemplo 03.2-----------------------

# n = ''
# resposta = 's'

# while resposta != 'N':
#     n = input('Informe um texto: ')
#     resposta = input('Quer continuar S/N ')[0].upper()
#     print(f'O Texto informado foi: {n}')


# ------------------ exemplo 03.3-----------------------

n = s = 0 
while True:
    n = int(input("Número: "))
    if n == 999:
        break
    s = s + n
    print (s)   

