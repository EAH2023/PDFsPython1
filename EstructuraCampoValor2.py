from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox

# Ruta del archivo PDF
pdf_path = "archivo.pdf"  # Cambia esto por la ruta de tu archivo PDF

# Función para extraer bloques de texto con PDFMiner
def extraer_bloques_pdfminer(pdf_path):
    bloques = []
    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextBox):
                 bloques.extend(element.get_text().strip().split("\n"))
    return bloques

# Función para estructurar "campo: valor" con validación
def estructurar_campos(lineas):
    campos_valores = {}
    for i in range(len(lineas) - 1):
        campo = lineas[i].strip()
        valor = lineas[i + 1].strip()
             
         # Validar si tiene sentido como "campo: valor"
        if campo and valor and not campo.isdigit() and len(valor.split()) < 10:
            campos_valores[campo] = valor
    return campos_valores

# Procesar el PDF
lineas = extraer_bloques_pdfminer(pdf_path)
campos_valores = estructurar_campos(lineas)

# Mostrar resultados estructurados
print("Datos estructurados:")
for campo, valor in campos_valores.items():
    print(f"{campo}: {valor}")