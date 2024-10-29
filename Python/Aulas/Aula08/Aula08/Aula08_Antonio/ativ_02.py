import os 

os.system('cls')

# ATIVIDADE [2]
# 

# def multa():
#     # m1 = peso_peixe - PESO_LIMITE
#     if peso_peixe > PESO_LIMITE:
#         m2 = peso_peixe - PESO_LIMITE
#         m3 = m2 * 4
#         print(f'Kg {2} x R$ {4.00}')
#         print(f'A multa ficou no valor de R$ {m3}')
#         return m3
#     else:
#         print('O peixe não excedeu o limite.')
    

# PESO_LIMITE = 100
# peso_peixe = float(input('Informe o peso do peixe: '))


# resultado = multa()

def multa(peso_peixe, PESO_LIMITE):
    if peso_peixe > PESO_LIMITE:
        m2 = peso_peixe - PESO_LIMITE
        m3 = m2 * 4
        print(f'Kg {m2} x R$ {4.00}')
        return m3
    

PESO_LIMITE = 100
peso_peixe = float(input('Informe o peso do peixe: '))

 
x3 = multa(peso_peixe, PESO_LIMITE)

if peso_peixe > PESO_LIMITE:
    print(f'A multa é no valor de {x3}')
else:
     print('O peixe não excedeu o limite.')