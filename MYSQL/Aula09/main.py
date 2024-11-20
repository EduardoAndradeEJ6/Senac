dados = {1, 2, 3, 4, 5}

# calcula a media

media = sum(dados) / len(dados)
print(f'Média : {media}')
print(30*'.')
# calcular as diferenças entre cada valor e a média
diferencas = [x - media for x in dados]
print(f'Diferenças: {diferencas}')
print(30*'.')
# elevar diferenças ao quadrado
quadrados_diferencas = [x**2 for x in diferencas]
print(f'Quadrado das diferenças: {quadrados_diferencas}')


#calcular a média dos quadrados da diferença
media_quadrados_diferenca = sum(quadrados_diferencas) / len(quadrados_diferencas)

# calcular a raiz quadrada da média dos quadrados das diferenças
desvio_padrao = media_quadrados_diferenca ** 0.5
print(f'Desvio padrão é a raiz quadrada da variância: {desvio_padrao}')