import pandas as pd 

produtos = ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Camera']
quantidade_estoque = [15, 30 ,20 ,10 ,25 ]

estoque = pd.Series (quantidade_estoque, index=produtos)

print(estoque)

print('\n Quantidade de notebooks em estoque: ')
print(estoque['Notebook'])

print('\n Estoque de notebook e Camera: ')
print(estoque[['Notebook', 'Camera']].values)


print(estoque + 5)

precos = pd.series ([3500, 2500, 1200 , 900 ,1500], index = produtos )

print('\N Valor total do estoque por produto (preco * quantidade):')
print(precos * estoque)


