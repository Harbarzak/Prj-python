import requests
from bs4 import BeautifulSoup
import json

def get_wikipedia_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al acceder a la página: {url}")
        return {"text": ""}  # Devolver un diccionario vacío en caso de error
    
    soup = BeautifulSoup(response.content, 'html.parser')
    content = ""
    for paragraph in soup.find_all('p'):
        content += paragraph.text
    return {"text": content}

# Lista de URLs de Wikipedia
urls = [
        'https://es.wikipedia.org/wiki/Shub-Niggurath',
        'https://www.miskatonic-university.org/',
        'https://es.wikipedia.org/wiki/Anexo:Bibliograf%C3%ADa_de_H._P._Lovecraft#Narrativa_completa',
        'https://es.wikipedia.org/wiki/El_horror_lovecraftiano',
        'https://es.wikipedia.org/wiki/Dioses_arquet%C3%ADpicos',
        'https://es.wikipedia.org/wiki/Asamatsu_Ken',
        'https://es.wikipedia.org/wiki/Bloop',
        'https://es.wikipedia.org/wiki/Pa%C3%ADs_de_Lovecraft',
        'https://es.wikipedia.org/wiki/August_Derleth',
        'https://es.wikipedia.org/wiki/Yog-Sothoth',
        'https://es.wikipedia.org/wiki/Mythos',
        'https://es.wikipedia.org/wiki/Monstruo_marino',
        'https://es.wikipedia.org/wiki/Tsathoggua',
        'https://es.wikipedia.org/wiki/Leviat%C3%A1n',
        'https://es.wikipedia.org/wiki/Kraken',
        'https://es.wikipedia.org/wiki/H._P._Lovecraft#V%C3%A9ase_tambi%C3%A9n',
        'https://es.wikipedia.org/wiki/H._P._Lovecraft#Biograf%C3%ADa',
        'https://es.wikipedia.org/wiki/H._P._Lovecraft#Trasfondo_creativo',        
        'https://es.wikipedia.org/wiki/El_rastro_de_Cthulhu',
		'https://lovecraft.fandom.com/wiki/The_H.P._Lovecraft_Wiki:Manual_of_Style',
        'https://callofcthulhu.fandom.com/wiki/H._P._Lovecraft',
        'https://lovecraft.fandom.com/wiki/The_H.P._Lovecraft_Wiki:Manual_of_Style/Character_or_Entity',
	    'https://es.wikipedia.org/wiki/La_llamada_de_Cthulhu',
		'https://es.wikipedia.org/wiki/H._P._Lovecraft',
		'https://es.wikipedia.org/wiki/Cthulhu',
		'https://es.wikipedia.org/wiki/Mitos_de_Cthulhu',
	    'https://es.wikipedia.org/wiki/Deidades_de_los_mitos_de_Cthulhu'	
		'https://lovecraft.fandom.com/wiki/The_Case_of_Charles_Dexter_Ward',
		'https://lovecraft.fandom.com/wiki/Feeders_from_Within',
        'https://es.wikipedia.org/wiki/La_llamada_de_Cthulhu_(juego_de_cartas)',	
        'https://es.wikipedia.org/wiki/La_llamada_de_Cthulhu_(juego_de_rol)',	
        'https://lovecraft.fandom.com/wiki/The_H.P._Lovecraft_Wiki:Manual_of_Style/Character_or_Entity',
        'http://www.sinergiaderol.com/hojasdepersonaje/cthulhu-hojas-personaje.html',
        'https://es.wikipedia.org/wiki/Suplemento_(juegos_de_rol)#Suplementos_de_reglas',
   ]

data = []
for url in urls:
    title = url.split('/')[-1].replace('_', ' ')
    content = get_wikipedia_content(url)
    data.append(content)
    
# Guardar los datos en un archivo JSON
with open('wikipedia_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Datos guardados en wikipedia_data.json")
