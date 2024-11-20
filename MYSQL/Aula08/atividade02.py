import os

os.system('cls')

import numpy as np 

import pandas as pd



df_dados_vendas = pd.read_csv ('tb_Vendas2017_Miranda.csv', sep=';', encoding='iso-8859-1')

df_vendas = df_dados_vendas [['Numero da Venda', 'ID Produto','ID Cliente', 'Quantidade Vendida']]

df_dados_produtos = pd.read_csv ('tb_CadastroProdutos2017_Miranda.csv', sep=';', encoding='utf-8')

df_produtos = df_dados_produtos [['Nome da Marca', 'Categoria','Preco Unitario', 'ID Produto']]

df_produtos.loc[:, 'Preco Unitario'] = df_produtos['Preco Unitario'].str.replace(',','.').astype(float)

print('Dados obtidos com sucesso!')



try:

    df_produtos_vendidos = pd.merge (df_vendas, df_produtos, on = "ID Produto")
    

    df_produtos_vendidos['Valor Total'] = df_produtos_vendidos['Quantidade Vendida']
    df_produtos_vendidos['Preco Unitario']

    df_produtos_vendidos = df_produtos_vendidos.groupby('Preco Unitario').agg({
        'Quantidade Vendida':'sum', 
        'Valor Total': 'sum'
        }).reset_index()

    print(df_produtos_vendidos)
    print(30*'/')
except SystemError as e:
    print(f'Erro ao obter dados: {e}')
    exit()


try:

    array_produtos_vendidos = np.array(df_produtos_vendidos['Valor Total'])

    media_produtos_vendidos = np.mean(array_produtos_vendidos)

    mediana_produtos_vendidos = np.median(array_produtos_vendidos)

    distancia = abs(
        (media_produtos_vendidos - mediana_produtos_vendidos) / mediana_produtos_vendidos
    ) * 100


    print(f'Média de produtos vendidos: {media_produtos_vendidos}')
    print(30*'-')
    print(f'Mediana de produtos vendidos: {mediana_produtos_vendidos}')
    print(30*'-')
    print(f'Distancia entre media e mediana {distancia} %')

    maximo = np.max(array_produtos_vendidos)
    minimo = np.min(array_produtos_vendidos)
    amplitude = maximo - minimo
    print(30*'-')
    print(f'Maximo: {maximo}')
    print(30*'-')
    print(f'Minimo: {minimo}')
    print(30*'-')
    print(f'Amplitude: {amplitude}')
    print(30*'/')
    q1 = np.quantile(array_produtos_vendidos, 0.25, method='weibull')
    q2 = np.quantile(array_produtos_vendidos, 0.50, method='weibull')
    q3 = np.quantile(array_produtos_vendidos, 0.75, method='weibull')

    iqr = q3 - q1
    limite_superior = q3 + (1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)

    print(limite_superior)
    print(30*'-')
    print(limite_inferior)
    print(30*'/')

    df_produtos_vendidos_outliers_inferiores = df_produtos_vendidos[df_produtos_vendidos['Valor Total'] < limite_inferior]

    df_produtos_vendidos_outliers_superiores = df_produtos_vendidos[df_produtos_vendidos['Valor Total'] > limite_superior]

    print('Outliers inferiores: ')
    if len(df_produtos_vendidos_outliers_inferiores) ==0:
        print( 'Não existem outliers inferiores!')
    else:
        print(df_produtos_vendidos_outliers_inferiores.sort_values(by='Valor Total', ascending=True))
    
    print(30*'/')

    print('Outliers Superiores: ')
    if len(df_produtos_vendidos_outliers_superiores) ==0:
        print( 'Não existem outliers superiores!')
    else:
        print(df_produtos_vendidos_outliers_superiores.sort_values(by='Valor Total', ascending=True))


    variancia = np.var(df_produtos_vendidos)
    desvio_padrao = np.sqrt(df_produtos_vendidos.var())
    desvio_padrao = np.sqrt(df_produtos_vendidos.var())

    distancia_var_media = variancia / (media_produtos_vendidos ** 2 )
    print(f'Distância entre a Variância e a média: {distancia_var_media}')

    
    coef_variacao = (desvio_padrao / media_produtos_vendidos * 100)
    print(f'Coeficiente de variação: {coef_variacao} %')

    print(f'Desvio padrão da série de idade: {np.std(df_produtos_vendidos)}')


except SyntaxError as e:
    print(f'Erro ao obter dados: {e}')
    exit()






