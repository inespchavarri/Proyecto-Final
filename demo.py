import pickle
import nltk
from nltk.corpus import stopwords
from nltk.corpus.reader import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize as wtoken
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import requests
from bs4 import BeautifulSoup
import re
import unidecode


### inputs

# modelo

path_mnbc = "modelos/mnbc.pickle"
with open(path_mnbc, "rb") as data:
    mnbc = pickle.load(data)

# TF-IDF

tfidf = TfidfVectorizer(ngram_range = (1,2), max_features=100)

# categorías

categorias = {
    "politica" : 1,
    "otros" : 0
}


### funciones

# obtener cartas

def getCarta(url):
    # Función para obtener el titular, el texto, la fecha y las etiquetas de cada artículo
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    texto = soup.find("div", class_="articulo-cuerpo")
    texto = texto.text.split("\n")
    texto = "".join(texto[:-3]).strip()
    
    etiquetas = soup.find_all("li", itemprop="keywords")
    etiquetas = [item.text for item in etiquetas]
    
    return texto, etiquetas


# NLP

def cleanText(texto):
    # función para preparar el texto para NLP
    result = re.sub("[\W_]+", " ", texto)
    result = result.strip().lower()
    result = unidecode.unidecode(result)
    return result


def cleanTags(etiquetas):
    # función para preparar las etiquetas
    result = []
    for item in etiquetas:
        item = item.lower()
        item = unidecode.unidecode(item)
        result.append(item)
    return result


def tokenWords(data):
    # función para obtener los tokens
    data = wtoken(data)
    return data


def remStopWords(data):
    #función para quitar las stopwords
    data_stopwords = []
    for word in data:
        if word not in stopwords.words("spanish"):
            data_stopwords.append(word)
            
    return data_stopwords


def wordStem(data):
    # función para stem
    data_stem = []
    stemmer = SnowballStemmer("spanish")
    for item in data:
        data_stem.append(stemmer.stem(item))
   
    return " ".join(data_stem)
    

# Obtener las categorias

def getCategories(etiquetas, categorias):
    # función para codificar las categorias. 1 política, 0 otros
    etiquetas = " ".join(etiquetas)
    if 'politica' in etiquetas:
        etiquetas = etiquetas.replace(etiquetas, 'politica')
        return categorias["politica"]
    else:
        etiquetas = etiquetas.replace(etiquetas, 'otros')
        return categorias["otros"]