import os 
os.system('cls')


#dicionario basicamente para armazenar as informações de forma conjunta separados por campos

dicionario =  {
    'nome': 'João',
    'telefone': '9234-6789',
    'idade': 24,
    'cpf': '02345.486.257-25'
}

dicionario1 = {
    'nome': 'Maria'
}


# print(dicionario ['nome'])
# print(dicionario ['telefone'])
# print(dicionario ['idade'])
# print(dicionario ['cpf'])


# dicionario['nome'] = 'Paula'
# print(dicionario)

# Adicionando novos campos no dicionarios após o mesmo ser criado anteriormente
dicionario1['email'] = 'maria@gmail.com'
dicionario1['idade'] = 25

# remover/deletar chaves do dicionário ou o dicionario por completo
# del dicionario1['email']
# print(dicionario1)

# Método .pop retorna o valor da chave apagada
print(dicionario1.pop('idade','35'))
print(dicionario1)

