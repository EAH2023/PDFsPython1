import re
from PyPDF2 import PdfReader

# Función para extraer fechas
def extraer_fechas(pdf_path):
    # Abrir el archivo PDF
    lector = PdfReader(pdf_path)
    texto_completo = ""

    # Extraer texto de todas las páginas
    for pagina in lector.pages:
        texto_completo += pagina.extract_text()

    # Buscar fechas con formato dd/mm/yy o similar
    patron_fecha = r'\b\d{1,2} -\d{1,2} -\d{2,2}\b'
    fechas = re.findall(patron_fecha, texto_completo)

    return fechas

# Ruta al archivo PDF
ruta_pdf = input("Introduce la ruta del archivo PDF: ")

try:
    fechas_encontradas = extraer_fechas(ruta_pdf)
    if fechas_encontradas:
        print("Fechas encontradas en el documento:")
        for fecha in fechas_encontradas:
            print(fecha)
    else:
        print("No se encontraron fechas en el documento.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
