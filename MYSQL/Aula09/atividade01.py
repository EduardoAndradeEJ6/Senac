import pandas as pd 
import numpy as np 

import os

os.system('cls')

idade = pd.Series([5, 10, 12, 35, 38])


conjunto_idade = np.array(idade)

media = conjunto_idade.mean()
variancia = np.var(conjunto_idade)
desvio_padrao = np.sqrt(conjunto_idade.var())

print(f"Média: {conjunto_idade.mean()}")

print(f"Variancia da série de idade: {np.var(conjunto_idade)}")

print(f'Desvio padrão da série de idade: {np.std(conjunto_idade)}')


#distancia entre a variancia e a media
distancia_var_media = variancia / (media ** 2 )
print(f'Distância entre a Variância e a média: {distancia_var_media}')

#coeficiente de variação
coef_variacao = (desvio_padrao / media * 100)
print(f'Coeficiente de variação: {coef_variacao} %')


# variancia de calculo de amostra
varianca_amostra1 = np.var(idade, ddof=1)
print(f'Variância amostral: {varianca_amostra1}')

#desvio padrão
desvio_padrao_amostra1 = np.std(idade,ddof=1)
print(f'Desvio padrão entre as idades {desvio_padrao_amostra1}')
