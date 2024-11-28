import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sqlalchemy import create_engine
from dotenv import load_dotenv

import os 


try:
    print('Obtendo Dados...')
    load_dotenv

    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    engine = create_engine(f'mysql+pymysql:// {user}:{password}@{host}:{port}')
    df_base = pd.read_sql('basedp', engine)
    df_roubo_celular = pd.read_sql('basedp', engine)

except SystemError:
    print('Erro ao obter dados...')