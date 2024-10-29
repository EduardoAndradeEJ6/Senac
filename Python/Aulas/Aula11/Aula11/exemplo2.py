import os

os.system('cls')

import pandas as pd

try:
    
    df = pd.read_csv('ClassicDisco.csv' , sep=',', encoding='utf-8')
    # print(df)
    # print(df.to_string())
    # print(df.head(50))
    # print(df.tail())
    # print(df.info())
    # print(df.describe())
    # pd.set_option('display.min_rows', 20)
    # popularidade = df[df['Popularity'] > 20]
    # print(popularidade[['Track','Popularity']])
    # michael_jackson = df[df['Artist'] == 'Michael Jackson']
    # print(michael_jackson[['Album','Artist','Track']])
    # pd.set_option('display.max_columns', None)
    # df.to_csv('Base_modificada.csv', index = False, sep=',' , encoding = 'utf-8')

    df.to_excel('Classic_disco_modificado.xlsx', index=False, engine='openpyxl')

    print(df)


except Exception as e:
    print(f'Erro{e}')