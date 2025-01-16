import re
from PyPDF2 import PdfReader

# Función para procesar texto línea por línea
def extraer_campos_linea_por_linea(pdf_path):
    lector = PdfReader(pdf_path)
    datos_por_pagina = {}

    for i, pagina in enumerate(lector.pages, start=1):
        texto = pagina.extract_text()
        lineas = texto.split("\n")  # Dividir el texto en líneas
        print(f"\nLíneas extraídas de la página {i}:\n{lineas}\n{'-'*50}")

        # Inicializar campos
        campos = {
            "Fecha": "",
            "Número de recibo": "",
            "Concepto": "",
            "Importe": "",
            "IBAN": "",
            "BIC": ""
        }

        # Procesar línea por línea
        for linea in lineas:
            # Buscar cada campo en la línea
            if re.search(r'\b\d{2}\s-\d{2}\s-\d{2}\b', linea):  # Fecha
                campos["Fecha"] = re.search(r'\b\d{2}\s-\d{2}\s-\d{2}\b', linea).group(0)
            elif "Número de recibo" in linea:  # Número de recibo
                match = re.search(r'Número de recibo\s+(\d+)', linea)
                if match:
                    campos["Número de recibo"] = match.group(1)
            elif "Concepto" in linea:  # Concepto
                match = re.search(r'Concepto\s*(.+)', linea)
                if match:
                    campos["Concepto"] = match.group(1).strip()
            elif "Importe" in linea:  # Importe
                match = re.search(r'Importe\s+([\d.,]+)', linea)
                if match:
                    campos["Importe"] = match.group(1)
            elif "Nº IBAN" in linea:  # IBAN
                match = re.search(r'Nº IBAN\s+([A-Z0-9 ]+)', linea)
                if match:
                    campos["IBAN"] = match.group(1)
            elif "BIC" in linea:  # BIC
                match = re.search(r'BIC\s+([A-Z0-9]+)', linea)
                if match:
                    campos["BIC"] = match.group(1)

        datos_por_pagina[f"Página {i}"] = campos

    return datos_por_pagina

# Ruta al archivo PDF
ruta_pdf = "archivo2.pdf"

try:
    datos = extraer_campos_linea_por_linea(ruta_pdf)
    print("\nDatos estructurados extraídos del PDF:")
    for pagina, campos in datos.items():
        print(f"\n{pagina}:")
        for campo, valor in campos.items():
            print(f"  {campo}: {valor}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
