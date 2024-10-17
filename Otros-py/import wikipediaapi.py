import requests
from bs4 import BeautifulSoup
import unicodedata
import json
import csv
import os

def normalize_text(text):
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = ''.join(text.split())
    return text

def extract_wikipedia_data(urls):
    data = []
    
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('h1', {'id': 'firstHeading'}).text
            paragraphs = soup.find_all('p')
            text = ' '.join([p.text for p in paragraphs])
            normalized_text = normalize_text(text)
            data.append({'title': title, 'content': normalized_text})
        else:
            print(f"Failed to retrieve page at '{url}'")
    
    return data

def save_as_jsonl(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in data:
            json.dump(entry, file)
            file.write('\n')
    print(f"Data saved as JSONL in {os.path.abspath(filename)}")

def save_as_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'content'])
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)
    print(f"Data saved as CSV in {os.path.abspath(filename)}")

def save_as_txt(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in data:
            file.write(f"{entry['title']}\n{entry['content']}\n\n")
    print(f"Data saved as TXT in {os.path.abspath(filename)}")

if __name__ == "__main__":
    print("Starting extraction process...")
    urls = [
        "https://es.wikipedia.org/wiki/Juego_de_rol",
        "https://es.wikipedia.org/wiki/Personaje_jugador",
        "https://es.wikipedia.org/wiki/Personaje_jugador#En_los_juegos_de_rol_de_mesa",
        "https://es.wikipedia.org/wiki/Personaje_no_jugador#Tipos_de_PNJ",
        "https://es.wikipedia.org/wiki/La_llamada_de_Cthulhu_(juego_de_rol)",
        "https://es.wikipedia.org/wiki/Las_mansiones_de_la_locura",
    ]
  
    data = extract_wikipedia_data(urls)
    
    output_directory = "data"
    os.makedirs(output_directory, exist_ok=True)
    
    jsonl_file = os.path.join(output_directory, 'wikipedia_data.jsonl')
    csv_file = os.path.join(output_directory, 'wikipedia_data.csv')
    txt_file = os.path.join(output_directory, 'wikipedia_data.txt')
    
    save_as_jsonl(data, jsonl_file)
    save_as_csv(data, csv_file)
    save_as_txt(data, txt_file)
    
    print("Extraction process completed.")