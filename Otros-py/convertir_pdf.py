from pdfminer.high_level import extract_text
import re
from unidecode import unidecode

def clean_text(text):
    # Eliminar caracteres especiales
    text = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ0-9\s]', '', text)
    # Convertir a ASCII (elimina tildes)
    text = unidecode(text)
    return text

# Ruta al archivo PDF
pdf_path = 'D:\PROYECTOS\PYHTON-PROJECTS\CHTLU-Manual-Guardian.pdf'

# Extraer texto
texto = extract_text(pdf_path)

# Limpiar el texto
texto_limpio = clean_text(texto)

# Guardar el texto limpio en un archivo .txt
with open('CHTLU-Manual-Guardian.txt', 'w', encoding='utf-8') as file:
    file.write(texto_limpio)

print("Conversión y limpieza completa. El texto se ha guardado en 'CHTLU-Manual-Guardian.txt'.")
