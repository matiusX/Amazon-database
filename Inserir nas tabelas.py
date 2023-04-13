import psycopg2

# Conectar-se ao banco de dados PostgreSQL
#mudar para seus dados
conn = psycopg2.connect(
    dbname="nome_do_banco_de_dados",
    user="nome_de_usuario",
    password="senha",
    host="host"
)

# Criar um cursor
cur = conn.cursor()

cont =0 
# Percorrer a lista de objetos criados anteriormente
for obj in produtos:
    # Extrair os valores do objeto
    id_value = obj.id
    asin_value = obj.asin
    title_value = obj.title
    grupo_value = obj.grupo
    salesrank_value = obj.salesrank
    quant_categories_value = obj.quant_categories

    # Inserir os dados na tabela usando os nomes das colunas
    cur.execute("INSERT INTO MainTable (ID, ASIN, title, grupo, salesrank, quant_categories) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (id_value, asin_value, title_value, grupo_value, salesrank_value, quant_categories_value))
                
    # Inserir os dados na tabela Similar
    cur.execute("INSERT INTO Similar (ASIN_original, ASIN_similar) VALUES (%s, %s)",
            (asin_value, asin_similar[cont]))
    cont+=1

for obj in reviews:
    # Extrair os valores do objeto
    asin_value = obj.asin
    data_value = obj.data
    customer_value = obj.customer
    rating_value = obj.rating
    votes_value = obj.votes
    helpful_value = obj.helpful


    # Insere dados na tabela Reviews
    cur.execute("INSERT INTO Reviews (ASIN_original, customer, data, rating, votes, helpful) VALUES (?, ?, ?, ?, ?, ?)", 
            (asin_value, customer_value, data_value, rating_value, votes_value, helpful_value))
    

for obj in reviews_product:
    # Extrair os valores do objeto
    asin_value = obj.asin
    total_value = obj.total
    downloaded_value = obj.downloaded
    rating_value = obj.rating
    avg_rating_value = obj.avg_rating
    reviews_vet_value = obj.reviews_vet
        

    # Insere dados na tabela ReviewsGeneralInfos
    cur.execute("INSERT INTO ReviewsGeneralInfos (ASIN_original, total, downloaded, avg_rating) VALUES (?, ?, ?, ?)", 
            (asin_value, total_value, downloaded_value, avg_rating_value))
    

for obj in categorias:
    # Insere dados na tabela AllCategories
    cur.execute("INSERT INTO AllCategories (ID_Categoria, Nome_Categoria) VALUES (?, ?)", 
            (id_categoria, nome_categoria))
    
    # Insere dados na tabela Categories
    cur.execute("INSERT INTO Categories (ID, ASIN_original, Num_Categoria, ID_Categoria) VALUES (?, ?, ?, ?)", 
            (id_categoria, asin_original, num_categoria, id_categoria))

# Confirmar a transação e fechar o cursor e a conexão
conn.commit()
cur.close()
conn.close()
