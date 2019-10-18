# Multiclass Categorization

El objetivo del proyecto es entrenar un modelo de Supervised Machine Learning que sea capaz de categorizar por temática las cartas al director remitidas al periódico El País. En una primera etapa del proyecto los artículos se han dividido en dos clases: política y otros. Las principales librerías utilizadas han sido NLTK y Scikit Learn.



## Pasos dados

1. Creación de una base de datos con todas las cartas al director que ha publicado El País desde 1976, año de su creación. Los datos se han obtenido por scraping.
2. Limpieza de la base de datos.
3. Tratamiento de los artículos seleccionados (más de 3.000 -los publicados en los últimos 5 años- de los casi 81.000 que conforman la base de datos) con técnicas de Procesamiento de Lenguaje Natural (NLP por sus siglas en inglés). NLTK ha sido la librería utilizada con técnicas como tokenización, eliminación de las denominadas stop words o la funcionalidad stem para hallar la raíz de la palabras que contiene cada artículo.
4. Una vez procesados los textos, he vectorizado los mismos con la funcionalidad Tf-Idf, de Scikit Learn. Un método que permite hallar la frecuencia de un término en relacción a toda la colección de documentos empleada y, por tanto, determinar la relevancia de esa palabra.
5. He entrenado un total de seis modelos (Logistic Regression, SVM, Random Forest Classifier, MultinomialNB -Naive Bayes-, Linear SVC, Gradient Boosting Classifier) con el objetivo de determinar el mejor para el problema planteado. He utilzado técnicas como cross validation para la elección de los hiperparametros y he obtenido diferentes métricas para determinar la precisión de cada uno. 
6. Una vez entrenados los diferentes modelos todos se han contrastados con la selección de las cartas al director correspondientes al año 1996 para poder medir la efectividad de los mismos. 

## Conclusión

En la fase de entrenamiento los dos modelos que mejores métricas han arrojado han sido Gradient Boosting y Linear SVC, pero con unas cifras con margen para la mejora. La precisión de las predicciones de los artículos con los que posteriormente se contrastaron los modelos, los correspondientes al año 1996, arrojaron un 0.6, lo que confirma que todavía se puede afinar más el proceso, bien sea en la fase de procesamiento de los textos, como en la de elección de los hiperparametros.

Métricas obtenidas con Gradient Boosting.

![alt text](https://raw.githubusercontent.com/inespchavarri/Proyecto-Final/master/output/gradient.png)


Métricas obtenidas con Linear SVC.

![alt text](https://raw.githubusercontent.com/inespchavarri/Proyecto-Final/master/output/LinearSVC.png)


Contraste de los modelos.

![alt text](https://raw.githubusercontent.com/inespchavarri/Proyecto-Final/master/output/modelos.png)

## Próximos pasos

Más allá de la mejora de los modelos, sería interesante ampliar las categorías con las que se podrían clasificar los textos analizados (política internacional, economía, cultura o temas sociales, entre otros asuntos).