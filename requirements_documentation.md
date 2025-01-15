# Documentación de Dependencias

Este proyecto utiliza las siguientes dependencias, que se enumeran en `requirements.txt`. A continuación se describe el propósito de cada paquete:

## Paquetes Principales
- **fitz==0.0.1.dev2:** Proporciona una interfaz para trabajar con archivos PDF mediante la biblioteca PyMuPDF.
- **openpyxl==3.1.5:** Herramienta para crear, leer y modificar archivos Excel (.xlsx y .xlsm).
- **pandas==2.2.3:** Biblioteca para manipulación y análisis de datos estructurados en tablas (DataFrames).

## Herramientas para Procesar PDFs
- **pdfminer==20191125:** Permite extraer texto, fuentes y metadatos de archivos PDF.
- **pdfplumber==0.11.5:** Extiende las funcionalidades de `pdfminer` con soporte para extraer tablas, imágenes y textos de forma avanzada.

## Paquetes Adicionales
- **PyPDF2==3.0.1:** Ofrece herramientas para dividir, fusionar y modificar archivos PDF.
- **scikit_learn==1.6.1:** Incluye algoritmos para aprendizaje automático, como regresión, clasificación y clustering.

---

## Instrucciones de Instalación
Para instalar todas las dependencias, ejecuta el siguiente comando en tu entorno virtual:
```bash
pip install -r requirements.txt
