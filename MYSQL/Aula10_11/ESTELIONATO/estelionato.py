import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt
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

    iqr = q3 - q1


    limite_superior = q3 + (1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)


    maximo = np.max(array_estelionato)
    minimo = np.min(array_estelionato)
    amplitude = maximo - minimo

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


try:

    plt.boxplot(array_estelionato, vert=False, showmeans=True, showfliers=True)
    plt.show()

    plt.subplots(1, 2, figsize=(16, 7))
    plt.suptitle('Analise de roubo de veiculos no RJ')

    plt.subplot(1, 2, 1)
    plt.boxplot(array_estelionato, vert=False, showmeans=True)
    plt.title('Boxplot dos dados')

   
    plt.subplot(1, 2, 2)  
    plt.text(0.1, 0.9, f'Média: {media_estelionato}', fontsize=12)
    plt.text(0.1, 0.8, f'Mediana: {mediana_estelionato}', fontsize=12)
    plt.text(0.1, 0.7, f'Distância: {distancia_media_mediana}', fontsize=12)
    plt.text(0.1, 0.6, f'Menor valor: {minimo}', fontsize=12) 
    plt.text(0.1, 0.5, f'Limite inferior: {limite_inferior}', fontsize=12)
    plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=12)
    plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=12)
    plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=12)
    plt.text(0.1, 0.1, f'Maior valor: {maximo}', fontsize=12)
    plt.text(0.1, 0.0, f'Amplitude Total: {amplitude}', fontsize=12)
    plt.title('Medidas observadas')

    plt.axis('off')
    plt.tight_layout()
    plt.show()

    plt.show()

except SystemError as e:
    print(f'Erro ao obter informações sobre padrão de roubo de  veículos: {e}')
    exit()
    