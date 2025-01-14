import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Cargar datos de entrenamiento con separador y codificación especificados
datos = pd.read_csv('recibos1.csv', sep=';', encoding='latin1')

# Convertir el texto de 'Concepto' en características numéricas
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(datos['Concepto'])

# Codificar las categorías en números
encoder = LabelEncoder()
y = encoder.fit_transform(datos['Categoría'])

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Crear y entrenar el modelo
modelo = MultinomialNB()
modelo.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = modelo.predict(X_test)

# Evaluar el modelo
precision = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {precision}")

# Función para predecir la categoría de un nuevo concepto
def predecir_categoria(concepto):
    concepto_vectorizado = vectorizer.transform([concepto])
    categoria_codificada = modelo.predict(concepto_vectorizado)[0]
    return encoder.inverse_transform([categoria_codificada])[0]

# Ejemplo de uso
nuevo_concepto = "ABONO REMESA: 202407020003493"
categoria = predecir_categoria(nuevo_concepto)
print(f"El concepto '{nuevo_concepto}' pertenece a la categoría: {categoria}")
