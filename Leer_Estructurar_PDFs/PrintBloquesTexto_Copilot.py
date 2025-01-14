from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTTextBox
import re

def extract_fields_from_pdf(pdf_path):
    fields = {}
    
    # Procesa cada página del PDF
    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextBox):
                text = element.get_text()

                # Utiliza una expresión regular para encontrar pares de campos y valores
                matches = re.findall(r'(\w+)\s*([\w\s]+)', text)
                
                for match in matches:
                    field_name, field_value = match
                    fields[field_name.strip()] = field_value.strip()

    return fields

pdf_path = 'archivo.pdf'
fields = extract_fields_from_pdf(pdf_path)

for field, value in fields.items():
    print(f'{field}: {value}')

