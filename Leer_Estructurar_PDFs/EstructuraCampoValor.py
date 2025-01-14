from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox

# Ruta del archivo PDF
pdf_path = "archivo2.pdf"  # Cambia esto por la ruta a tu archivo PDF

# Función para extraer bloques de texto usando PDFMiner
def extraer_bloques_pdfminer(pdf_path):
    bloques = []
    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextBox):
                bloques.append(element.get_text().strip())
    return bloques

# Función para estructurar los datos en formato "campo: valor"
def estructurar_campos(bloques):
    campos_valores = {}
    for i in range(0, len(bloques) - 1, 2):  # Avanzar en pares (campo, valor)
        campo = bloques[i].strip()
        valor = bloques[i + 1].strip() if i + 1 < len(bloques) else ""
        if campo and valor:  # Ambos deben contener texto
            campos_valores[campo] = valor
    return campos_valores

# Procesar el PDF
bloques = extraer_bloques_pdfminer(pdf_path)
campos_valores = estructurar_campos(bloques)

# Mostrar resultados
print("Datos estructurados:")
for campo, valor in campos_valores.items():
    print(f"{campo}: {valor}")