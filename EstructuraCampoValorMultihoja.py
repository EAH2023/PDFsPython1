from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox

# Ruta del archivo PDF
pdf_path = "archivo2.pdf"

# Función para extraer texto página por página
def extraer_datos_pdf(pdf_path):
    datos_por_pagina = []
    for page_number, page_layout in enumerate(extract_pages(pdf_path)):
        pagina_actual = []
        for element in page_layout:
            if isinstance(element, LTTextBox):
                texto = element.get_text().strip()
                pagina_actual.append(texto)
        datos_por_pagina.append(pagina_actual)
    return datos_por_pagina

# Función para procesar datos y extraer campos clave
def procesar_datos(datos_por_pagina):
    resultados = []
    for numero_pagina, pagina in enumerate(datos_por_pagina, start=1):
        campos = {
            "Fecha": "",
            "Oficina": "",
            "Moneda": "",
            "Número de recibo": "",
            "Referencia emisor": "",
            "Concepto": "",
            "Importe": "",
            "Referencia única mandato": "",
            "Fecha firma mandato": "",
            "Fecha vencimiento": ""
        }
        for i, linea in enumerate(pagina):
            if "Fecha" in linea and "Oficina" in linea:
                partes = linea.split()
                campos["Fecha"] = partes[0]
                campos["Oficina"] = partes[1]
                campos["Moneda"] = partes[-1]
            elif "Número de recibo" in linea:
                partes = pagina[i + 1].split()
                campos["Número de recibo"] = partes[0]
                campos["Referencia emisor"] = partes[1]
            elif "Concepto" in linea:
                campos["Concepto"] = pagina[i + 1] if i + 1 < len(pagina) else ""
            elif "Importe" in linea:
                campos["Importe"] = pagina[i + 1] if i + 1 < len(pagina) else ""
            elif "Referencia única mandato" in linea:
                partes = pagina[i + 1].split()
                campos["Referencia única mandato"] = partes[0]
                campos["Fecha firma mandato"] = partes[1]
                campos["Fecha vencimiento"] = partes[2]
        resultados.append(campos)
    return resultados

# Procesar el PDF
datos_por_pagina = extraer_datos_pdf(pdf_path)
resultados = procesar_datos(datos_por_pagina)

# Mostrar resultados estructurados
for pagina, resultado in enumerate(resultados, start=1):
    print(f"\nResultados de la página {pagina}:")
    for campo, valor in resultado.items():
        print(f"{campo}: {valor}")
