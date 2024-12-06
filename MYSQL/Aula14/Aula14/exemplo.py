import polars as pl
from datetime import datetime
import os
import gc
 
 
ENDERECO_DADOS = r'./Dados/'
 
 
try:
    print('Iniciando leituras dos arquivos parquet')
   
    inicio = datetime.now()
 
    df_bolsa_familia = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    df_bolsa_familia = df_bolsa_familia_plan.collect()

    print(df_bolsa_familia)
   
    fim = datetime.now()

    print(f'Tempo de execução: {fim - inicio}')
 
 
except ImportError as e:
    print('Erro ao obter dados', e)