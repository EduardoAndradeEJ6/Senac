import pandas as pd 


precos = pd.series ([3500, 2500, 1200 , 900 ,1500], index = produtos )

print('\N Valor total do estoque por produto (preco * quantidade): ')
print(precos * estoque)