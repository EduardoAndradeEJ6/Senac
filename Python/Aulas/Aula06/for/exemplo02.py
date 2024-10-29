import os

os.system('cls')


lista_previsao = [ 'Ensolarado', 'Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado']


PREVISAO_BOA = 'Ensolarado'

for e in lista_previsao:
    
    
    if e == PREVISAO_BOA:
        print(f'{e}: Aproveite o dia pra passear')
    else:
        print(f"{e}: Não esqueça o guarda-chuva")
   