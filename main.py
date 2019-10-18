from demo import getCarta, cleanText, cleanTags, tokenWords, remStopWords, wordStem, getCategories
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def main():

    path_mnbc = "modelos/mnbc.pickle"
    with open(path_mnbc, "rb") as data:
        mnbc = pickle.load(data)

    tfidf = TfidfVectorizer(ngram_range = (1,2), max_features=100)

    categorias = {
        "politica" : 1,
        "otros" : 0
    }

    texto, etiquetas = getCarta(url)

    # Preparación texto para vectorizar

    texto_limpio = cleanText(texto)
    texto_procesado = tokenWords(texto_limpio)
    texto_procesado = remStopWords(texto_procesado)
    texto_procesado = wordStem(texto_procesado)

    X = [texto]
    X = tfidf.fit_transform(X).toarray()

    etiquetas = cleanTags(etiquetas)
    etiquetas = getCategories(etiquetas, categorias)

    y = etiquetas

    y_pred = mnbc.predict(X)

    
    print("\nArtículo: \n\n{}\n\nPredicción categoria: {} \nCategoría real: {}".format(texto, int(y_pred), y))




if __name__ == '__main__':
    url = input("Introduce una url: ")
    main()