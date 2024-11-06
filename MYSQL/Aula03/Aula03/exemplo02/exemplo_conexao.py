from sqlalchemy import create_engine, text

host ='localhost'
user = 'root'
password = 'root'
database = 'bd_produtos'

#função para conectar no banco
def conecta_banco():
    try:
        # URL de conexão com o banco, usando o SQLALCHEMY E PYMYSQL
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

        # estabelece a conexão
        with engine.connect() as conexao:
            query = "SELECT * FROM vendas"
        
        #text(query) transforma a string da query em um objeto comaptivel com SQLALchemy
        #'conexao.consulte' executa essa consulta no banco de dados.

            resultados = conexao.execute(text(query))

            for item in resultados:
                print(f'Id: {item[0]}, Preço: {item[4]}, Quantidade: {item[5]}')

    except ImportError as e:
        print(f'Erro: {e}')
        
        

# chama função que conecta ao banco de dados
    conecta_banco()
