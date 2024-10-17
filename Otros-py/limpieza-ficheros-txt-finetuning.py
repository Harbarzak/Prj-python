import re
import json
import unicodedata

# Cargar el archivo
file_path = 'D:\PROYECTOS\FINE-TUNING-IA\TXT-LIMPIO\guia-rapida-cht.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Función para eliminar acentos
def remove_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

# Función para limpiar el texto
def clean_text(text):
    # Convertir a minúsculas
    text = text.lower()
    # Eliminar acentos
    text = remove_accents(text)
    # Eliminar caracteres especiales y números
    text = re.sub(r'[^a-zñü\s]', '', text)
    # Eliminar duplicados y datos repetidos
    text = re.sub(r'\bcthulhu guia rapida\b', '', text)
    return text

# Limpiar el texto
cleaned_text = clean_text(text)

# Eliminar stop words (lista manual)
stop_words = set("""
de la que el en y a los del se las por un para con no una su al lo como más pero sus le ya o
fue ha sí porque o él esta son entre cuando muy sin sobre también me hasta hay donde quien desde
todo nos durante todos uno les ni contra otros ese eso ante ellos e esto mí antes algunos qué unos
yo otro otras otra él tanto esa estos mucho quienes nada muchos cual poco ella estar estas algo
nosotros mi mis tú te ti tu tus ellas nos vosotros vosotras os mí conmigo contigo
""".split())

# Tokenización manual
words = re.findall(r'\b\w+\b', cleaned_text)
cleaned_words = [word for word in words if word not in stop_words]

# Crear el texto final
final_text = ' '.join(cleaned_words)

# Crear el archivo JSON para fine-tuning
data = {
    "text": final_text
}

json_path = 'D:\PROYECTOS\FINE-TUNING-IA\TXT-LIMPIO\guia-rapida-cht.json'
with open(json_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

# Guardar el archivo tokenizado
tokenized_path = 'D:\PROYECTOS\FINE-TUNING-IA\TXT-LIMPIO\guia-rapida-cht-tokenized.txt'
with open(tokenized_path, 'w', encoding='utf-8') as tokenized_file:
    tokenized_file.write(' '.join(cleaned_words))

json_path, tokenized_path