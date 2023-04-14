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

###############################################################
vet_products = []
vet_categories = []
vet_reviews = []
with open('/home/matheus/Documents/A_COMPUTACAO/BD1/Trabalho-1-BD/ufam-db-tp1/database/5_data.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for i in range(0, len(linhas)):
    linha = linhas[i]
    #Tratamendo do ID e caso produto sem info
    if linha.startswith("Id:"):
        #Novo elemento
        id = linha.split(':')
        id[1] = int(id[1])
        print(id)  
    
    #Tratamento do ASIN
    elif linha.startswith("ASIN:"):
        asin = linha.split(':')
        asin[1] = asin[1][:-2].lstrip()
        print(asin)
        
        #caso de produto descontinuado
        prox_linha = linhas[i+1]
        if(prox_linha.startswith("  d")):
            produto = Produto(id, asin, None, None, None, None, None, None)
            vet_products.append(produto)
    
    #Tratamento do titulo
    elif linha.startswith("  title:"):
        title = linha.split(":", 1)
        title[0] = title[0].lstrip()
        title[1] = title[1][1:-2]
        print(title)

    #Tratamento dos grupos
    elif linha.startswith("  group:"):
        group = linha.split(":", 1)
        group[0] = group[0].lstrip()
        group[1] = group[1][1:-1]
        print(group)
    
    #tratamento dos ranks
    elif linha.startswith("  salesrank:"):
        salesrank = linha.split(":", 1)
        salesrank[0] = salesrank[0].lstrip()
        salesrank[1] = salesrank[1][:-1].lstrip()
        print(salesrank)
    
    #tratamento dos similares
    elif linha.startswith("  similar:"):
        similar = linha.split(':')
        similar[0] = similar[0].lstrip() #titulo "similar"
        similar[1] = similar[1].split("  ", 1)
        similar[1][0] = int(similar[1][0]) #quantidade de similares
        if(similar[1][0] == 0):
            similar[1] = [0, []]
        else: 
            similar[1][1] =  similar[1][1][:-1].split("  ")
            for i in similar[1]:
                similar.append(i)
            similar.pop(1)
        print(similar)
    
    #trata as categorias: vai na tabela principal e na tabela categories
    elif linha.startswith("  categories:"):
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
    elif linha.startswith("  reviews:"):
        reviews_infos = linha.split(":", 1)
        reviews_infos[0] = reviews_infos[0].lstrip()
        reviews_infos[1] = reviews_infos[1].split("  ")
        for item in reviews_infos[1]:
            aux = item.split(":")
            aux[0] = aux[0].lstrip()
            aux[1] = float(aux[1])
            reviews_infos.append(aux)
        reviews_infos.pop(1)
        reviews_infos[1]
        print(reviews_infos)
        posicao_review = i+1
        linha_atual = linhas[posicao_review]
        while(linha_atual != ""):
            print("EXISTE UMA REVIEW AKIR!!! TA BOM, GOSTOSAS????????: {}".format(linha_atual))
            
            #atualiza posicao
            posicao_review = posicao_review + 1
            linha_atual = linhas[posicao_review]
arquivo.close()