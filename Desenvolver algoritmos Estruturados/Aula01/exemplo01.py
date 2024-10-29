import pandas as pd 

data = {
    'nome':['Ana', 'João', 'Maria'],
    'Idade': [23, 35, 29],
    'Gênero': ['F', 'M', 'F'],
    'Altura': [1.70, 1.80, 1.65]
}

df = pd.DataFrame(data)

print(f'\n {df}')

print('\n Variaveis Quantitativas')
print(30*'=')

print(df['Idade'])
print('')
print(30*'=')
print(df['Altura'])