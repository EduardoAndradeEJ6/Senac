import os

os.system('cls')


listaprevisoes = ['Nublado','Chuvoso','Tempestade','Ensolarados','Ensolarados']

listadias = ['Segunda','Terça','Quarta','Quinta','Sexta']

dias_ensolarados = []

dias_semsol = []

for i, v in enumerate(listaprevisoes):
    print(f'\n {listaprevisoes}')
    if listaprevisoes[i] == 'Ensolarados':
     dias_ensolarados.append(listadias[i])
    else:
       dias_semsol.append(listadias[i])

print(f'\n Dias ensolarados {dias_ensolarados}')

print(f'\n Dias sem sol {dias_semsol}')


#     if p == 'Ensolarados':
#         listadias.append(p)
#     else:
#         dias_semsol.append(p)

# print(f'Dias ensolarados: {dias_ensolarados}')

# print(f'Dias sem sol: {dias_semsol}')