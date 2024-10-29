import pandas as pd 

dados = {
    'cargos' : ['Assistente', 'Auxiliar', 'Gerente'],
    'salários' : [2500, 1800, 750]
}

dados_bi = pd.DataFrame(dados)
# print(dados_bi)


dados_cargos = pd.Series(dados['cargos'])
# print(dados_cargos)


# print(dados_cargos.index)

# print(dados_cargos.values)

# imprime a linha do indice
df_linha = dados_bi.iloc[1]
# print(df_linha)

print(dados_bi.iloc[1]['cargos'])
print(dados_bi.iloc[1]['salários'])