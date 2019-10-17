import unidecode
import nltk
from nltk.tokenize import word_tokenize as wtoken
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re


def removeChar(data):
    # Función para eliminar todos los caraceteres que no sean ni letras, ni números

    if type(data) == str:
        result = re.sub("[\W_]+", " ", data)
        result = result.strip()
        return result
    else:
        result = []
        for element in data:
            element = re.sub("[\W_]+", " ", element)
            element = element.strip()
            result.append(element)
        return result


def lowText(data):
    #Función para que el texto esté ni minuscula
    if type(data) == str:
        result = data.lower()
        return result.strip()
    else:
        result = []
        for element in data:
            element = element.lower()
            element = element.strip()
            result.append(element)
        return result


def removeAccents(data):
    # función para quitar los acentos
    if type(data) == str:
        unaccented_data = unidecode.unidecode(data)
        return unaccented_data
    else:
        result = []
        for element in data:
            result.append(unidecode.unidecode(element))
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



def cleanLabels(data):
    # Función para dividir los datos en 2 categorias
    if 'politica' in data:
        data = data.replace(data, 'politica')
        return data
    else:
        data = data.replace(data, 'otros')
        return data