import os 
os.system('cls')


alunos = {}

for i in range(2):
    # os.system('cls')
    nome = input('\n Digite o seu nome: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    

    media = (nota1 + nota2 + nota3) / 3
    if media >= 6 :
        resultado = 'Aprovado'
        print('')
    else:
        resultado = 'Reprovado'
        print('')
   
    alunos [nome] = {
        'nome' : nome,
        'nota1' : nota1,
        'nota2' : nota2,
        'nota3' : nota3,
        'media' : media,
        'resultado': resultado
        } 

    print(alunos[nome])
    

