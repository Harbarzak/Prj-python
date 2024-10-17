import json
from pdfminer.high_level import extract_text

def convert_pdf_to_text(pdf_path):
    text = extract_text(pdf_path)
    return text

def format_text_as_json(text, category):
    # Tokenizar el texto aquí si es necesario
    # Por ejemplo, dividir el texto en párrafos o frases
    
    # Crear lista de diccionarios con el texto tokenizado
    data = [{"texto": paragraph.strip()} for paragraph in text.split("\n") if paragraph.strip()]

    # Crear el JSON con la categoría correspondiente
    json_data = {category: data}
    return json_data

def save_json(data, output_file):
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

def main(pdf_path, output_file, category):
    text = convert_pdf_to_text(pdf_path)
    json_data = format_text_as_json(text, category)
    save_json(json_data, output_file)

if __name__ == "__main__":
    pdf_file = "D:\PDF\ROL\LA-LLAMADA-DE-CHTULHU\guia-rapida-cht.pdf"  # Nombre de tu archivo PDF
    output_file = "datos.json"  # Nombre del archivo JSON de salida
    category = "reglas"  # Categoría de los datos (por ejemplo, "reglas")
    main(pdf_file, output_file, category)
