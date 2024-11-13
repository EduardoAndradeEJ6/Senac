import pandas as pd 

import numpy as np 


try:
    print('Obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    df_estelionato = df_ocorrencias[['munic', 'estelionato']]

    df_estelionato = df_estelionato.groupby(['munic']).sum(['estelionato']).reset_index()

    

    print(f'Total de estelionato nos top 10  municipios {df_estelionato.head(10)}')

    array_estelionato = np.array(df_ocorrencias['estelionato'])

    media = np.mean(array_estelionato)

    mediana= np.median(array_estelionato)

    distancia_media_mediana = abs ((media - mediana) / mediana * 100)

    # df_estelionato = df_estelionato.groupby(['munic']).sum(['estelionato']).reset_index()


    print(f"\n Média de estelionatos: {media}")

    print(f"\n Mediana de estelionatos: {mediana}")

    print(f'Distancia entre media e mediana {distancia_media_mediana}')

    # print(df_total)




except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()