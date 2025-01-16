"""
Este programa:
1.	Extrae bloques de texto de un archivo PDF utilizando PDFMiner.
2.	Estructura los bloques de texto en pares campo: valor.
3.	Imprime los datos estructurados en la consola.
Este flujo te ayuda a transformar y visualizar los datos de un 
archivo PDF de manera organizada.
Lee el contenido del archivo aunque venga con proteccion de lectura.
Los datos estructurados que se obtienen no tienen logica de asociacion
son simplemente una agrupacion campo: valor por la proximidad fisica.
Ver EstructuraCampoValor.docx
"""
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox

# Ruta del archivo PDF
pdf_path = "data/input/archivo.pdf"  # Asegúrate de que esta ruta sea correcta

# Función para extraer bloques de texto usando PDFMiner
def extraer_bloques_pdfminer(pdf_path):
    bloques = []
    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextBox):
                bloque_texto = element.get_text().strip()
                bloques.append(bloque_texto)
                print(f"Bloque extraído: {bloque_texto}")  # Imprimir bloque extraído
    return bloques

# Función para estructurar los datos en formato "campo: valor"
def estructurar_campos(bloques):
    campos_valores = {}
    for i in range(0, len(bloques) - 1, 2):  # Avanzar en pares (campo, valor)
        campo = bloques[i].strip()
        valor = bloques[i + 1].strip() if i + 1 < len(bloques) else ""
        print(f"Campo: {campo}, Valor: {valor}")  # Imprimir campo y valor
        if campo and valor:  # Ambos deben contener texto
            campos_valores[campo] = valor
    return campos_valores

# Procesar el PDF
bloques = extraer_bloques_pdfminer(pdf_path)
print(f"Bloques extraídos: {bloques}")  # Imprimir todos los bloques extraídos

campos_valores = estructurar_campos(bloques)
print("Datos estructurados:")
for campo, valor in campos_valores.items():
    print(f"{campo}: {valor}")
