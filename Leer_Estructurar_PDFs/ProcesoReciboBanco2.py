import re
import pandas as pd
import pdfplumber

def procesar_pdf(pdf_path):
    """
    Procesa un archivo PDF y extrae datos estructurados de cada página.
    Divide el campo Concepto en subconceptos con sus importes.
    """
    resultados = []
    
    # Abrir el PDF con pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            texto = page.extract_text()
            if not texto:
                continue
            lineas = texto.splitlines()
            
            # Extraer detalles de las líneas específicas
            fecha_vcto = re.search(r"\d{2}-\d{2}-\d{2}", lineas[2]).group(0) if len(lineas) > 2 and re.search(r"\d{2}-\d{2}-\d{2}", lineas[2]) else None
            importe = re.search(r"(\d+,\d+)$", lineas[13]).group(1) if len(lineas) > 13 and re.search(r"(\d+,\d+)$", lineas[13]) else None
            concepto = lineas[7].strip() if len(lineas) > 7 else None

            # Limpieza y formateo
            if concepto:
                concepto = concepto.replace("TORTOLA 4 ", "")  # Eliminar texto superfluo
                # Dividir en subconceptos (texto seguido de un número decimal)
                subconceptos = re.findall(r"(.*?)(\d+,\d+)", concepto)
                for subconcepto, imp_subconcepto in subconceptos:
                    # Crear una fila por cada subconcepto
                    detalles = {
                        "Página": page_number,
                        "Fecha Vcto": pd.to_datetime(fecha_vcto, format="%d-%m-%y").strftime("%d/%m/%y") if fecha_vcto else None,
                        "Oficina": re.search(r"(\d{4})\s", lineas[2]).group(1) if len(lineas) > 2 and re.search(r"(\d{4})\s", lineas[2]) else None,
                        "Moneda": re.search(r"\s([A-Z]{3})\s", lineas[2]).group(1) if len(lineas) > 2 and re.search(r"\s([A-Z]{3})\s", lineas[2]) else None,
                        "Número de recibo": re.search(r"EUR\s+(\d+)", lineas[2]).group(1) if len(lineas) > 2 and re.search(r"EUR\s+(\d+)", lineas[2]) else None,
                        "Referencia emisor": re.search(r"\d+\s+(\d{20})", lineas[2]).group(1) if len(lineas) > 2 and re.search(r"\d+\s+(\d{20})", lineas[2]) else None,
                        "Concepto": subconcepto.strip(),  # Subconcepto sin el importe
                        "Importe (€)": f"{float(importe.replace(',', '.')):.2f} €" if importe else None,
                        "Imp.Subconcepto (€)": float(imp_subconcepto.replace(",", ".")),  # Importe del subconcepto
                        "Nº IBAN": re.search(r"(ES\d{2}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4})", lineas[16]).group(1) if len(lineas) > 16 and re.search(r"(ES\d{2}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4})", lineas[16]) else None,
                    }
                    resultados.append(detalles)

    return pd.DataFrame(resultados)

def guardar_en_excel(dataframe, output_path):
    """
    Guarda un DataFrame en un archivo Excel.
    """
    dataframe.to_excel(output_path, index=False)
    print(f"Archivo Excel generado: {output_path}")

# Ruta del archivo PDF de entrada
pdf_path = "archivo2.pdf"  # Cambia esto por la ruta de tu archivo PDF

# Ruta del archivo Excel de salida
output_excel = "datos_extraidos.xlsx"

# Procesar el PDF y guardar los resultados en un Excel
df_resultados = procesar_pdf(pdf_path)
guardar_en_excel(df_resultados, output_excel)
