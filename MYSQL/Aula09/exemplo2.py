import pandas as pd 
import numpy as np 

import os

os.system('cls')

dados = pd.Series([2, 4, 6, 8, 10])

# Transforma os dados em array numpy

conjunto_dados = np.array(dados)
variancia = np.var(conjunto_dados)
media = conjunto_dados.mean()
desvio_padrao = np.sqrt(conjunto_dados.var())

print(f'O Conjunto de dados: {conjunto_dados}')

# calcula a media
print(f"Média: {conjunto_dados.mean()}")

# calcula a variancia
print(f"Variancia da série de dados: {np.var(conjunto_dados)}")

# cacular o desvio padrão
# o desvio padrão é a raiz quadrada da variancia

print(f'Desvio padrão da série de dados: {np.sqrt(conjunto_dados.var())}')

# forma mais direta de calcular o desvio padrão
# calcula diretamente o desvio padrão do conjunto de dados
# METODO MAIS UTILIZADO
print(f'Desvio padrão da série de dados: {np.std(conjunto_dados)}')


#distancia entre a variancia e a media
distancia_var_media = variancia / (media ** 2 )
print(f'Distância entre a Variância e a média: {distancia_var_media}')

#coeficiente de variação
coef_variacao = (desvio_padrao / media * 100)
print(f'Coeficiente de variação: {coef_variacao} %')

# variancia de calculo de amostra
varianca_amostra1 = np.var(dados, ddof=1)
print(f'Variância amostral: {varianca_amostra1}')

#desvio padrão
desvio_padrao_amostra1 = np.std(dados,ddof=1)
print(f'Desvio padrão entre as idades {desvio_padrao_amostra1}')