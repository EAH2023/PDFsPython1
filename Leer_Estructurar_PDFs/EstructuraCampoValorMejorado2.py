from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox

# Ruta del archivo PDF
pdf_path = "archivo.pdf"  # Cambia esto por la ruta de tu archivo PDF

# Función para extraer bloques de texto con PDFMiner por página
def extraer_bloques_pdfminer_por_pagina(pdf_path):
    print("Extrayendo bloques de texto del PDF página por página...")
    paginas = []
    for page_number, page_layout in enumerate(extract_pages(pdf_path)):
        bloques = []
        for element in page_layout:
            if isinstance(element, LTTextBox):
                bloques.extend(element.get_text().strip().split("\n"))
        print(f"Bloques extraídos de la página {page_number + 1}:")
        print(bloques)  # Depuración: Ver bloques de la página actual
        paginas.append(bloques)
    return paginas

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

# Procesar el PDF página por página
paginas_bloques = extraer_bloques_pdfminer_por_pagina(pdf_path)

# Analizar cada página por separado
print("\nAnalizando cada página...")
for numero_pagina, bloques in enumerate(paginas_bloques, start=1):
    print(f"\nPágina {numero_pagina}:")
    campos_valores = estructurar_campos_mejorado(bloques)
    print(f"Datos estructurados para la página {numero_pagina}:")
    for campo, valor in campos_valores.items():
        print(f"{campo}: {valor}")
