import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
import os

# Configuración de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ajusta la ruta según tu instalación

def pdf_to_text(pdf_path):
    # Extraer texto del PDF
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def pdf_to_ocr_text(pdf_path):
    # Convertir cada página del PDF en imágenes y aplicar OCR
    text = ""
    images = convert_from_path(pdf_path)
    for image in images:
        text += pytesseract.image_to_string(image, lang='spa')
    return text

def save_text_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    pdf_files = [
    #'D:\PDF\ROL\LA-LLAMADA-DE-CHTULHU\FICHAhoja_personaje_anos_20.pdf',
    #'D:\PDF\ROL\LA-LLAMADA-DE-CHTULHU\La Llamada de Cthulhu 7ª edición - Pantalla del Guardián (2019-06) [SCAN].pdf',
    #'D:\PDF\ROL\LA-LLAMADA-DE-CHTULHULa Llamada de Cthulhu 7ed - Manual del Guardian.pdf',
    'D:\PDF\ROL\LA-LLAMADA-DE-CHTULHUmanual-del-investigador.pdf',
    ]

for pdf_file in pdf_files:
        print(f"Procesando {pdf_file}...")
        
        # Extraer texto directamente
        text = pdf_to_text(pdf_file)
        if not text.strip():
            # Si no se extrajo texto, aplicar OCR
            print(f"Aplicando OCR a {pdf_file}...")
            text = pdf_to_ocr_text(pdf_file)
        
        # Guardar el texto extraído en un archivo
        output_filename = os.path.splitext(os.path.basename(pdf_file))[0] + ".txt"
        save_text_to_file(text, output_filename)
        print(f"Texto guardado en {output_filename}")

if __name__ == "__main__":
    main()
