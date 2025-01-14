import fitz  # PyMuPDF

# Abrir el archivo PDF
with fitz.open("archivo.pdf") as pdf_file:
    # Obtener el número total de páginas
    num_pages = pdf_file.page_count
    print(f"Total pages: {num_pages}")
   
    # Extraer el texto de la primera página
    if num_pages > 0:
        text = pdf_file[0].get_text("text")  # Respetar el orden visual
        print("Texto extraído de la primera página:")
        print(text)