import pandas as pd
import polars as pl
import gc
from datetime import datetime



try:
    
    ENDERECO_DADOS = r'./Dados/'

    hora_import = datetime.now()

    df_janeiro = pl.read_csv(ENDERECO_DADOS + '202401_NovoBolsaFamilia.csv', separator = ';', encoding='iso-8859-1')

    print(df_janeiro)

    hora_impressao = datetime.now()

    print('Obtendo Dados')

    inicio = datetime.now()

    lista_arquivos = ['202401_NovoBolsaFamilia.csv', '202402_NovoBolsaFamilia.csv', '']

    print(f'Tempo de execução: {hora_impressao - hora_import}')

    for arquivo in lista_arquivos:
        print(f'Processando arquivo {arquivo}')

        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator = ';', encoding='iso-8859-1')

        if 'df_bolsa_familia' in locals ():
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        else:
            df_bolsa_familia = df
        
        hora_impressao = datetime.now()

        print(df.head())

        print(f'Tempo de execução: {hora_impressao - hora_import}')

        del df
        gc.collect()


except ImportError as e:   
    print('Erro ao obter dados', e)