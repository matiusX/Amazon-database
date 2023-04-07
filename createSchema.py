# pip install psycopg2
import psycopg2

# Crie um BD utilizando o pgAdmin ou o psql pelo terminal com o seguinte comando:
# CREATE DATABASE nome_database;

# Altere de acordo com seus dados
host="localhost"
nome_database="myowndatabase"
user="postgres"
password="2703"     

# Conecta com o BD criado
conn = psycopg2.connect("host=" + host +
                        " dbname=" + nome_database +
                        " user=" + user +
                        " password=" + password)

# Abre um cursor para fazer operações no BD
cur = conn.cursor()

# Executa um comando: Cria uma tabela
cur.execute("CREATE TABLE grape (id integer PRIMARY KEY, num integer, data varchar);")

# Aplica as mudanças no BD
conn.commit()

# Fecha a conexão
cur.close()
conn.close()