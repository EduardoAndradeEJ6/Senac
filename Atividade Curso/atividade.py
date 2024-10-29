import os

os.system('cls')

import pandas as pd

try:
    
    df = pd.read_csv('Dados.csv' , sep=';', encoding='utf-8')
   

    print(df.head(20))
    
    


except Exception as e:
    print(f'Erro{e}')