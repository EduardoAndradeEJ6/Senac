import pandas as pd

filmes = {
    'ano': [2003, 2000, 1985,],
    'genero': ['Ação', 'Terror', 'Ficção Cientifica'],
    'filme': ['BadBoys 2', 'Premonição', 'De volta para o futuro']
}


print(30*'=')
print('filmes')
df = pd.DataFrame(filmes)
print(df)

print('')

print(30*'=')
print('Localizando por indice')
print(df.iloc[2]['ano'])

print(df.iloc[2]['genero'])

print(df.iloc[2]['filme'])

print('')

print(30*'=')
df.index = ['A','B','C']
serie_colunas = df.loc['A']
print(serie_colunas, '\n')