import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from datasets import Dataset

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Función para limpiar el texto extraído
def clean_text(text):
    text_cleaned = re.sub(r'\[.*?\]', '', text)
    text_cleaned = text_cleaned.replace('\n', ' ').replace('\r', '')
    return text_cleaned

def remove_stopwords(text, language):
    tokens = word_tokenize(text, language=language)
    stop_words = set(stopwords.words(language))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    return ' '.join(filtered_tokens)

def lemmatize_text(text, language):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text, language=language)
    lemmatized_text = ' '.join([lemmatizer.lemmatize(word) for word in tokens])
    return lemmatized_text

# Leer datos del archivo JSON
with open('wikipedia_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Limpiar y preparar los datos
cleaned_data = []
for entry in data:
    cleaned_content = clean_text(entry['text'])
    cleaned_content = remove_stopwords(cleaned_content, 'english')
    cleaned_content = remove_stopwords(cleaned_content, 'spanish')
    cleaned_content = lemmatize_text(cleaned_content, 'english')
    cleaned_content = lemmatize_text(cleaned_content, 'spanish')
    cleaned_data.append({'text': cleaned_content})

# Convertir la lista de diccionarios en un diccionario adecuado para Dataset
dataset_dict = {'text': [entry['text'] for entry in cleaned_data]}

# Crear un dataset de Hugging Face con el contenido preprocesado
dataset = Dataset.from_dict(dataset_dict)

# Guardar el dataset preprocesado en un archivo JSON
dataset.to_json('cleaned_wikipedia_data.json')

print("Datos preprocesados guardados en cleaned_wikipedia_data.json")
