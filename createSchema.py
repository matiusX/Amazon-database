# pip install psycopg2
import psycopg2

# Altere de acordo com seus dados
host="localhost"
dbname="myowndatabase"
user="postgres"
password="2703"     

# Conecta com um BD já existente
conn = psycopg2.connect("host=" + host +
                        " dbname=" + dbname +
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