import pandas as pd

dados = {
    'cargos': ['assistente', 'auxiliar', 'gerente', 'auxiliar '],
    'salário': [2500,1800,750,1900]
}

df = pd.DataFrame(dados)
print(df)

serie_cargos = pd.Series(df['cargos'])
print(serie_cargos)

series_salario = pd.Series (df['salário'])
print(series_salario)
print(type(series_salario))

print(df)
print()
serie_linha = df.iloc[1]
print(serie_linha)

serie_colunas =df.loc[:,'cargos']
print(serie_colunas)

# df.index = ['A','B','C']
# serie_colunas = df.loc['C']
# print(serie_colunas, '\n')

print(df.iloc[2]['cargos'])

print(df.iloc[2]['salário'])

print(serie_cargos.iloc[0])

print(serie_cargos[serie_cargos.index[0]])

print(df.iloc[0])



print(df[df['cargos'] =='auxiliar'])


# print(df,'\n')
print(df[df['cargos'] =='auxiliar'])
salarios = df.loc[df['cargos'] == 'auxiliar', 'salário']
print(salarios)