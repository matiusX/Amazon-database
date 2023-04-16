#from typing import List
import re
import classes

class Category:
    def __init__(self, name= str, id= int ):
        self.name = name
        self.id = id
        
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
        
    @id.setter
    def id(self, new_id):
        self._id = new_id

class Review:
    def __init__(self, asin= str, data= str, customer= str,
                 rating= int, votes= int, helpful= int):
        self.asin = asin
        self.data = data
        self.customer = customer
        self.rating = rating
        self.votes = votes
        self.helpful = helpful
        
    @property
    def asin(self):
        return self._asin
    
    @property
    def data(self):
        return self._data
    
    @property
    def customer(self):
        return self._customer
 
    @property
    def rating(self):
        return self._rating

    @property
    def votes(self):
        return self._votes
    
    @property
    def helpful(self):
        return self._helpful  
    
    @asin.setter
    def asin(self, new_asin):
        self._asin = new_asin
        
    @data.setter
    def data(self, new_data):
        self._data = new_data

    @customer.setter
    def customer(self, new_customer):
        self._customer = new_customer

    @rating.setter
    def rating(self, new_rating):
        self._rating = new_rating
        
    @votes.setter
    def votes(self, new_votes):
        self._votes = new_votes
        
    @helpful.setter
    def helpful(self, new_helpful):
        self._helpful = new_helpful

class Reviews_product:
    def __init__(self, asin= str, total= int, downloaded= int,
                 avg_rating= float, reviews_vet= [Review]):
        self.asin = asin
        self.total = total
        self.downloaded = downloaded
        self.avg_rating = avg_rating
        self.reviews_vet = reviews_vet
        
    @property
    def asin(self):
        return self._asin
    
    @property
    def total(self):
        return self._total
    
    @property
    def downloaded(self):
        return self._downloaded
 
    @property
    def avg_rating(self):
        return self._avg_rating

    @property
    def reviews_vet(self):
        return self._reviews_vet
    
    @asin.setter
    def asin(self, new_asin):
        self._asin = new_asin
        
    @total.setter
    def total(self, new_total):
        self._total = new_total
        
    @downloaded.setter
    def downloaded(self, new_downloaded):
        self._downloaded = new_downloaded

    @avg_rating.setter
    def avg_rating(self, new_avg_rating):
        self._avg_rating = new_avg_rating

    @reviews_vet.setter
    def reviews_vet(self, new_reviews_vet):
        self._reviews_vet = new_reviews_vet
    
class Produto:
    def __init__(self, id= int, asin= str,
                 title= str, group= str,
                 salesrank= int, similar= str,
                 categories= Category, reviews = Reviews_product):
        self.id = id
        self.asin = asin
        self.title = title
        self.group = group
        self.salesrank = salesrank
        self.similar = similar
        self.categories = categories
        self.reviews = reviews

    # getter e setter para id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # getter e setter para asin
    @property
    def asin(self):
        return self._asin

    @asin.setter
    def asin(self, value):
        self._asin = value

    # getter e setter para title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    # getter e setter para group
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value

    # getter e setter para salesrank
    @property
    def salesrank(self):
        return self._salesrank

    @salesrank.setter
    def salesrank(self, value):
        self._salesrank = value

    # getter e setter para similar
    @property
    def similar(self):
        return self._similar

    @similar.setter
    def similar(self, value):
        self._similar = value

    # getter e setter para categories
    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        self._categories = value

    # getter e setter para reviews
    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        self._reviews = value

############
#funcoes de extracao
def get_id(linha):
    id = linha.split(':')
    id[1] = int(id[1])
    return id

def get_asin(linha):
    asin = linha.split(':')
    asin[1] = asin[1][:-1].lstrip()
    return asin

def get_title(linha):
    title = linha.split(":", 1)
    title[0] = title[0].lstrip()
    title[1] = title[1][1:-2]
    return title

def get_group(linha):
    group = linha.split(":", 1)
    group[0] = group[0].lstrip()
    group[1] = group[1][1:-1]    
    return group

def get_salesrank(linha):
    salesrank = linha.split(":", 1)
    salesrank[0] = salesrank[0].lstrip()
    salesrank[1] = salesrank[1][:-1].lstrip()  
    return salesrank

def get_similars(linha):
    similar = linha.split(':')
    similar[0] = similar[0].lstrip() #titulo "similar"
    similar[1] = similar[1].split("  ", 1)
    similar[1][0] = int(similar[1][0]) #quantidade de similares
    if(similar[1][0] == 0):
        similar[1] = [0, []]
    else: 
        similar[1][1] =  similar[1][1][:-1].split("  ")
        for item in similar[1]:
            similar.append(item)
        similar.pop(1)
    return similar
###############################################################
vet_products = []
vet_categories = []
vet_reviews_general_infos = []
vet_reviews = []
with open('/home/matheus/Documents/A_COMPUTACAO/BD1/Trabalho-1-BD/ufam-db-tp1/database/60_data.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

i = 0
while i < len(linhas):
    linha = linhas[i]
    #Tratamendo do ID e caso produto sem info
    if linha.startswith("Id:"):
        #Novo elemento
        id = get_id(linha)
        asin = get_asin(linhas[i+1])
        if not linhas[i+2].startswith("  d"):
            title = get_title(linhas[i+2])
            group = get_group(linhas[i+3])
            salesrank = get_salesrank(linhas[i+4])
            similar = get_similars(linhas[i+5])
            print(id, asin, title, group, salesrank, similar)
            main_infos = (id, asin, title, group, salesrank, similar)
            vet_products.append(main_infos)
 
    '''
    #Tratamento do ASIN
    elif linha.startswith("ASIN:"):
        asin = get_asin(linha)
        print(asin)
        
        #caso de produto descontinuado
        #comentado pq o professor falou que pode ignorar o descontinuado
        #colocar tres aspas aqui
      #  prox_linha = linhas[i+1]
      #  if(prox_linha.startswith("  d")):
      #      produto = Produto(id, asin, None, None, None, None, None, None)
       #     vet_products.append(produto)
        #colocar comentario aq tres aspas
    
    #Tratamento do titulo
    elif linha.startswith("  title:"):
        title = get_title(linha)
        print(title)

    #Tratamento dos grupos
    elif linha.startswith("  group:"):
        group = get_group(linha)
        print(group)
    
    #tratamento dos ranks
    elif linha.startswith("  salesrank:"):
        salesrank = get_salesrank(linha)
        print(salesrank)
    
    #tratamento dos similares
    elif linha.startswith("  similar:"):
        similar = get_similars(linha)
        print(similar)
    ''' #_.FIM DO COMENTARIO
    
    #trata as categorias: vai na tabela principal e na tabela categories
    if linha.startswith("  categories:"):
        categories_info = linha.split(':')
        categories_info[0] = categories_info[0].lstrip()
        categories_info[1] = int(categories_info[1])
        print(categories_info)
        aux = i+1 #aponta pro comeco das categorias
        index_cat = 1
        linha_cat = linhas[aux]
        while(linha_cat.startswith("   |")): #indica uma categoria
            #manipula a categoria atual            
            linha_cat = linha_cat[3:-1] #tira o /n e espacos no comeco da string
            categories = re.findall(r'\|([\w\s&]+)\[(\d+)\]', linha_cat)
            
            for category in categories:
                id_infos = (asin[1], index_cat)
                category = id_infos + category #adiciona asin e id_categoria naquela categoria
                vet_categories.append(category)
                print(category)

            #vai p proxima categoria e atualiza valor do id_categoria
            aux = aux+1
            index_cat = index_cat + 1
            linha_cat = linhas[aux]
    #trata as reviews: tabela principal, reviews, reviews general infos
    if linha.startswith("  reviews:"):
        reviews_infos = linha.split(":", 1)
        reviews_infos[0] = reviews_infos[0].lstrip()
        reviews_infos[1] = reviews_infos[1].split("  ")
        for item in reviews_infos[1]:
            aux = item.split(":")
            aux[0] = aux[0].lstrip()
            aux[1] = float(aux[1])
            reviews_infos.append(aux)
        reviews_infos.pop(1)
        reviews_infos_tuple = (asin[1], reviews_infos[1][1], reviews_infos[2][1], reviews_infos[3][1])
        vet_reviews_general_infos.append(reviews_infos_tuple) #adicionar sobre informacoes gerais das reviews de um produto
        posicao_review = i+0
        linha_atual = linhas[posicao_review]
        if(reviews_infos[1][1] != 0):#verifica se existem reviews
            pattern="(\d{4}-\d{1,2}-\d{1,2})\s+cutomer:\s+([A-Z0-9]+)\s+rating:\s+(\d)\s+votes:\s+(\d+)\s+helpful:\s+(\d+)"
            while(linha_atual != "\n" and linha_atual != None):#enquanto a linha eh uma review
                review_identifiers = (asin[1], id[1])
                review_data = re.findall(pattern, linha_atual)
                for review in review_data:
                    vet_reviews.append(review_identifiers+review)
                    print(f"{review_identifiers+review}")
                                       
                #vai p proxima linha
                posicao_review = posicao_review+1
                if(posicao_review >= len(linhas)): ##se chegou ao fim, para o programa
                    break
                linha_atual = linhas[posicao_review]
    i = i+1
        
print(vet_categories)  #->vetor que vai ser usado para inserir no banco
print(vet_reviews)  
print(vet_products)  
print(vet_reviews_general_infos)  
arquivo.close()