from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox

# Ruta del archivo PDF
pdf_path = "archivo2.pdf"  # Cambia esto por la ruta de tu archivo PDF

# Función para extraer bloques de texto con PDFMiner
def extraer_bloques_pdfminer(pdf_path):
    print("Extrayendo bloques de texto del PDF...")
    bloques = []
    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextBox):
                bloques.extend(element.get_text().strip().split("\n"))
    print("Bloques extraídos:")
    print(bloques)  # Depuración: Ver todos los bloques extraídos
    return bloques

# Función para estructurar "campo: valor" con validación mejorada
def estructurar_campos_mejorado(lineas):
    print("Estructurando campos y valores...")
    campos_valores = {}
    ultimo_campo = None  # Para evitar repeticiones
    posibles_campos = [
        "Fecha", "Oficina", "Adeudo por transferencia", "Ordenante", "Observaciones", 
        "Por cuenta de", "Fecha emisión", "Moneda", "Número de transferencia", 
        "Beneficiario", "Banco beneficiario", "CCC", "Referencia para el beneficiario", 
        "Importe", "Entidad", "Nº IBAN", "BIC"
    ]  # Lista de nombres de campo comunes para validar
    for i in range(len(lineas) - 1):
        campo = lineas[i].strip()
        valor = lineas[i + 1].strip()
        
        # Depuración: Mostrar el campo y valor actuales
        print(f"Campo candidato: '{campo}', Valor candidato: '{valor}'")
        
        # Validar que el campo sea parte de los posibles y evitar repeticiones
        if campo in posibles_campos and campo != ultimo_campo and valor:
            campos_valores[campo] = valor
            ultimo_campo = campo  # Actualizar el último campo procesado
            print(f"Agregado: {campo} -> {valor}")  # Depuración: Campo agregado
        else:
            print(f"Ignorado: {campo}")  # Depuración: Campo no válido o repetido
    print("Estructura final de campos y valores:")
    print(campos_valores)  # Depuración: Ver el resultado final
    return campos_valores

# Procesar el PDF
lineas = extraer_bloques_pdfminer(pdf_path)
campos_valores = estructurar_campos_mejorado(lineas)

# Mostrar los resultados estructurados
print("\nDatos estructurados finales:")
for campo, valor in campos_valores.items():
    print(f"{campo}: {valor}")
