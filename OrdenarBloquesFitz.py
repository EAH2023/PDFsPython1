import fitz  # PyMuPDF

# Ruta del archivo PDF proporcionado por el usuario
pdf_path = "archivo.pdf"

# Inicializar la variable para almacenar los detalles
pdf_details = {"blocks": [], "images": []}

with fitz.open(pdf_path) as pdf_file:
    # Verificar si tiene páginas
    if pdf_file.page_count > 0:
        # Leer la primera página
        page = pdf_file[0]

        # Extraer bloques de texto con coordenadas
        blocks = page.get_text("blocks")
        pdf_details["blocks"] = blocks

        # Extraer detalles de imágenes presentes en la primera página
        images = page.get_images(full=True)
        pdf_details["images"] = images

print(pdf_details)

sorted_blocks = sorted(blocks, key=lambda x: (x[1], x[0]))  # Ordenar por posición (x, y)     

#Concatenar el texto de los bloques ordenados
texto_ordenado = "\n".join([block[4] for block in sorted_blocks])
print(texto_ordenado)