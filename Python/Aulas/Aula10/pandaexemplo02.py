import pandas as pd


try:
    df_base_de_dados = pd.read_csv('ClassicDisco.csv', sep = ',', encoding='utf-8')

    print(df_base_de_dados.describe())
except Exception as e:
    print(f'Erro{e}')


    
