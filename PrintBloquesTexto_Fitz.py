import fitz  # PyMuPDF

# Abrir el archivo PDF
with fitz.open("archivo.pdf") as pdf_file:

    # Obtener la primera página
    page = pdf_file[0]

    # Obtener bloques de texto (como coordenadas)
    blocks = page.get_text("blocks")

    # Imprimir detalles de los bloques
    for block in blocks:
        print("Bloque de texto::", block)