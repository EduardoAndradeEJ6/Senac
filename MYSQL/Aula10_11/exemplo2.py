import pandas as pd 

import numpy as np 

#obter dados

try:
    print('Obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    df_estelionato = df_ocorrencias[['mes_ano', 'estelionato']]

    df_roubo_veiculo = df_estelionato.groupby(['mes_ano']).sum(['estelionato']).reset_index()

    print(df_estelionato.head())

    print('\n Dados obtidos com sucesso!')



except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()


try:

    print('\n Calculando infomrações sobre padrão de roubo de veículos....')

    array_estelionato = np.array(df_estelionato['estelionato'])

    media_estelionato = np.mean(array_estelionato)

    mediana_estelionato = np.median(array_estelionato)

    distancia_media_mediana = abs ((media_estelionato - mediana_estelionato) / mediana_estelionato * 100)

    print(f"Média de estelionatos: {media_estelionato}")
    print(f"Mediana de estelionatos: {mediana_estelionato}")
    print(f"Distancia da media e mediana de estelionatos: {distancia_media_mediana} %")


    q1 = np.quantile(array_estelionato, 0.25, method='weibull')
    q2 = np.quantile(array_estelionato, 0.50, method='weibull')
    q3 = np.quantile(array_estelionato, 0.75, method='weibull')

    print(q1)
    print(q2)
    print(q3)

    df_mes_ano_acima_q3 = [df_estelionato['estelionato'] > q3]

    df_mes_ano_abaixo_q1 = [df_estelionato['estelionato'] < q1]

    print(df_mes_ano_acima_q3)
    print(df_mes_ano_abaixo_q1)




except ImportError as e:
    print(f'Erro ao obter informações sobre padrão de roubo de  veículos: {e}')
    exit()

    