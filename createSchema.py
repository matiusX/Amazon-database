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

# Executa um comando: Cria a tabela MainTable
cur.execute('''CREATE TABLE MainTable ( 
            ID INT NOT NULL,
            ASIN VARCHAR(10) PRIMARY KEY,
            title VARCHAR(100),
            grupo VARCHAR(20),
            salesrank INT,
            quant_categories INT,
            UNIQUE (ID),
            UNIQUE (salesrank));'''
)

# Executa um comando: Cria a tabela Similar
cur.execute('''CREATE TABLE \"Similar\" ( 
            ASIN_original VARCHAR(10), 
            ASIN_similar VARCHAR(10), 
            PRIMARY KEY (ASIN_original, ASIN_similar), 
            FOREIGN KEY (ASIN_original) REFERENCES MainTable(ASIN));''' 
)

# Executa um comando: Cria a tabela AllCategories
cur.execute('''CREATE TABLE AllCategories ( 
            ID_Categoria INT, 
            Nome_Categoria VARCHAR(100) NOT NULL, 
            UNIQUE (Nome_Categoria),
            PRIMARY KEY (ID_Categoria));'''
) 

# Executa um comando: Cria a tabela Categories
cur.execute('''CREATE TABLE Categories ( 
            ASIN_original VARCHAR(10),
            Num_Categoria INT,
            ID_Categoria INT,
            PRIMARY KEY (ASIN_original, Num_Categoria, ID_Categoria),
            FOREIGN KEY (ASIN_original) REFERENCES MainTable(ASIN),
            FOREIGN KEY (ID_Categoria) REFERENCES AllCategories(ID_Categoria));'''
)

# Executa um comando: Cria a tabela Reviews
cur.execute('''CREATE TABLE Reviews (
            ASIN_original VARCHAR(10), 
            customer VARCHAR(20), 
            data DATE,
            rating INT,
            votes INT,
            helpful INT,
            PRIMARY KEY (ASIN_original, customer), 
            FOREIGN KEY (ASIN_original) REFERENCES MainTable(ASIN));'''
)

# Executa um comando: Cria a tabela ReviewsGeneralInfos
cur.execute('''CREATE TABLE ReviewsGeneralInfos (
            ASIN_original VARCHAR(10),
            total INT,
            downloaded INT,
            avg_rating DECIMAL(2,1),
            PRIMARY KEY (ASIN_original),
            FOREIGN KEY (ASIN_original) REFERENCES MainTable(ASIN));'''
)

# Cria o trigger check_num_categoria -> Num_Categoria não pode ser maior do que quant_categoria 
cur.execute('''CREATE OR REPLACE FUNCTION func_check_num_categoria() RETURNS TRIGGER AS $$
                BEGIN
                    IF EXISTS (
                        SELECT * FROM MainTable 
                        WHERE ASIN = NEW.ASIN_original AND quant_categories < NEW.Num_Categoria
                    ) THEN
                        RAISE EXCEPTION 'O valor de Num_Categoria não pode ser maior que quant_categories';
                    END IF;
                    RETURN NEW;
                END;
                $$ LANGUAGE plpgsql;

                CREATE TRIGGER check_num_categoria 
                BEFORE INSERT ON Categories 
                FOR EACH ROW 
                EXECUTE FUNCTION func_check_num_categoria();'''
)

# Cria o trigger check_asin_similar -> ASIN_original não pode ter ele mesmo como ASIN_similar
cur.execute('''CREATE OR REPLACE FUNCTION func_check_asin_similar() RETURNS TRIGGER AS $$
                BEGIN
                    IF NEW.ASIN_original = NEW.ASIN_similar THEN
                        RAISE EXCEPTION 'ASIN_original não pode ser igual a ASIN_similar';
                    END IF;
                    RETURN NEW;
                END;
                $$ LANGUAGE plpgsql;

                CREATE TRIGGER check_asin_similar
                BEFORE INSERT ON \"Similar\"
                FOR EACH ROW
                EXECUTE FUNCTION func_check_asin_similar();'''
)

# Aplica as mudanças no BD
conn.commit()

# Fecha a conexão
cur.close()
conn.close()