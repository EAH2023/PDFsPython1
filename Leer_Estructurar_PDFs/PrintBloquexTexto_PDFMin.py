from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox

for page_layout in extract_pages("archivo2.pdf"):
    for element in page_layout:
        if isinstance(element, LTTextBox):
            print("Bloque de texto:", element.get_text())