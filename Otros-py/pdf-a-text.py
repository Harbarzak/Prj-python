import fitz  # PyMuPDF

def pdf_to_text(pdf_path):
    # Abre el archivo PDF
    document = fitz.open(pdf_path)
    text = ""

    # Imprime el número de páginas
    num_pages = len(document)
    print(f"Número total de páginas: {num_pages}")

    # Itera sobre cada página del PDF
    for page_num in range(num_pages):
        page = document.load_page(page_num)  # Carga la página
        page_text = page.get_text()  # Extrae el texto de la página
        text += page_text  # Añade el texto de la página al texto completo
        print(f"Texto extraído de la página {page_num + 1}/{num_pages}")

    return text

# Especifica la ruta al archivo PDF
pdf_path = "D:\PDF\ROL\LA-LLAMADA-DE-CHTULHU\manual-del-investigador.pdf"

# Convierte el PDF a texto
pdf_text = pdf_to_text(pdf_path)

# Guarda el texto en un archivo para verificar fácilmente
with open("output_text.txt", "w", encoding="utf-8") as text_file:
    text_file.write(pdf_text)

print("Extracción completa. El texto ha sido guardado en 'output_text.txt'.")