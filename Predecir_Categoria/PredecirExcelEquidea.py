import tkinter as tk
from tkinter import filedialog
import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score

# Paso 1: Seleccionar el archivo Excel
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    archivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    return archivo

ruta_archivo = seleccionar_archivo()
print(f"Archivo seleccionado: {ruta_archivo}")

# Paso 2: Cargar la hoja específica y los datos de la tabla
archivo = load_workbook(ruta_archivo)
hoja = archivo['Movimientos']
tabla = pd.read_excel(ruta_archivo, sheet_name='Movimientos', engine='openpyxl')
# print(tabla.head())  # Para verificar la carga de datos

# Guardar el rango de la tabla original para recrearla después
table_range = hoja.tables['Tabla1'].ref

# Paso 3: Preprocesar los datos
entrenamiento = tabla.dropna(subset=['CUENTA'])
prediccion = tabla[tabla['CUENTA'].isna()]

# Rellenar NaN en 'DESCRIPCION' con una cadena vacía
entrenamiento.loc[:, 'DESCRIPCION'] = entrenamiento['DESCRIPCION'].fillna('')
prediccion.loc[:, 'DESCRIPCION'] = prediccion['DESCRIPCION'].fillna('')

vectorizer = CountVectorizer()
X_entrenamiento = vectorizer.fit_transform(entrenamiento['DESCRIPCION'])
X_prediccion = vectorizer.transform(prediccion['DESCRIPCION'])

encoder = LabelEncoder()
y_entrenamiento = encoder.fit_transform(entrenamiento['CUENTA'])

# Paso 4: Entrenar el modelo con validación cruzada
modelo = MultinomialNB()

# Validación cruzada para evaluar la precisión del modelo
if len(set(y_entrenamiento)) > 1 and min(y_entrenamiento) >= 5:
    scores = cross_val_score(modelo, X_entrenamiento, y_entrenamiento, cv=5)
    print(f"Precisión Media de Validación Cruzada: {scores.mean()}")
else:
    print("Advertencia: Algunas clases tienen menos de 5 miembros, se omite la validación cruzada.")

# Entrenar el modelo con todos los datos de entrenamiento
modelo.fit(X_entrenamiento, y_entrenamiento)

# Paso 5: Predecir las categorías
predicciones = modelo.predict(X_prediccion)
categorias_predichas = encoder.inverse_transform(predicciones)
prediccion.loc[:, 'CUENTA'] = categorias_predichas

# Paso 6: Guardar los resultados en el archivo Excel sin duplicar datos y preservando formatos
for idx, row in prediccion.iterrows():
    hoja[f'D{idx+2}'] = row['CUENTA']  # Reemplaza "G" con la columna adecuada para "CUENTA"

# Guardar el archivo actualizado
archivo.save(ruta_archivo)
print("Categorías predichas y guardadas en el archivo Excel, preservando los formatos.")
