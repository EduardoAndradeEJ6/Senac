import pandas as pd 


data = {
    'Cod':[1, 2 , 3],
    'Produto': ['Notebook', 'Smartphone', 'Tablet'],
    'Vendidas': [120, 340, 210 ],
    'Cor': ['Preto', 'Prata', 'Azul'],
    'Categoria': ['Eletrônicos', 'Eletrônicos' , 'Eletrônicos'],
    'Preço': [3500, 2500, 1200],
    'Faturamento': [42000, 85000, 252105],
    'Satisfação': ['Alto', 'Muito Alto', 'Médio']
}

df = pd.DataFrame(data)
print(df)


print('\n Variaveis Quantitativas')
print(30*'=')
print(df['Cod'])
print(df['Vendidas'])
print(df['Preço'])
print(df['Faturamento'])

print('\n Variaveis Não Quantitativas')
print(30*'=')
print(df['Produto'])
print(df['Cor'])
print(df['Categoria'])
print(df['Satisfação'])
