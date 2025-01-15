from PyPDF2 import PdfReader

# Función para extraer texto página por página
def extraer_texto_pagina_por_pagina(pdf_path):
    # Abrir el archivo PDF
    lector = PdfReader(pdf_path)
    texto_paginas = {}

    # Recorrer todas las páginas del PDF
    for i, pagina in enumerate(lector.pages, start=1):
        texto = pagina.extract_text()
        texto_paginas[f"Página {i}"] = texto.strip() if texto else "(Sin texto extraído)"
    
    return texto_paginas

# Ruta al archivo PDF
ruta_pdf = "archivo2.pdf"

try:
    # Extraer texto página por página
    texto_por_pagina = extraer_texto_pagina_por_pagina(ruta_pdf)

    # Imprimir el contenido de cada página
    print("\nContenido extraído del PDF, página por página:")
    for pagina, contenido in texto_por_pagina.items():
        print(f"\n{pagina}:\n{contenido}")
except Exception as e:
    print(f"Ocurrió un error: {e}")

