import pandas as pd 

import numpy as np 

#obter dados

try:
    print('Obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()

    print(df_roubo_veiculo.head())

    print('\n Dados obtidos com sucesso!')



except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()


try:

    print('\n Calculando infomrações sobre padrão de roubo de veículos....')

    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    media_roubo_veiculo = np.mean(array_roubo_veiculo)

    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    distancia_media_mediana = abs ((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo * 100)

    print(f"Média de roubo de veiculos: {media_roubo_veiculo}")
    print(f"Mediana de roubo de veiculos: {mediana_roubo_veiculo}")
    print(f"Distancia da media e mediana de roubo de veiculos: {distancia_media_mediana} %")

    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude = maximo - minimo
    print('')
    print('Máximo: ', maximo)
    print('Minimo: ', minimo)
    print('Amplitude maxima: ', amplitude)


    q1 = np.quantile(
        array_roubo_veiculo, 0.25, method="weibull")
    
    q2 = np.quantile(
        array_roubo_veiculo, 0.50, method="weibull")
    
    q3 = np.quantile(
        array_roubo_veiculo, 0.75, method="weibull")
    
    print(30 *'-')
    print("Q1: ", q1)
    print(30 *'-')
    print("Q2: ", q2)
    print(30 *'-')
    print("Q3: ", q3)

    IQR = q3 - q1
    print(30 *'-')
    print(30 *'-')
    print(F'O IQR é: {IQR}')

    print(30 *'-')
    limite_superior = q3 + (1.5 * IQR)
    print(f' O limite superior é: {limite_superior}')

    print(30 *'-')
    limite_inferior = abs (q1 - (1.5 * IQR))
    print(f' O limite inferior é: {limite_inferior}')



except ImportError as e:
    print(f'Erro ao obter informações sobre padrão de roubo de  veículos: {e}')
    exit()

    