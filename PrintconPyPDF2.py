import PyPDF2

# Open the PDF file
pdf_file = open('archivo.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages
num_pages = len (pdf_reader.pages)
print(f'Total pages: {num_pages}')

# Extract text from the first page
page = pdf_reader.pages[0]
text = page.extract_text()
print(text)

# Close the PDF file
pdf_file.close()