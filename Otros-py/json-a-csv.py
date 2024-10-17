import json
import csv

def json_to_csv(json_file, csv_file):
    # Leer el archivo JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Verificar que el JSON sea una lista de diccionarios
    if not isinstance(data, list):
        raise ValueError("El archivo JSON debe contener una lista de objetos")

    # Obtener las claves para el encabezado del CSV
    #keys = data[0].keys()

    # Escribir el archivo CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        #writer = csv.DictWriter(f, fieldnames=keys)
        #writer.writeheader()
        #writer.writerows(data)
         writer = csv.writer(f)
        writer.writerow(["text"])  # Escribir encabezado
        writer.writerows(data) 
# Ejemplo de uso
json_file = 'D:\PROYECTOS\FINE-TUNING-IA\TXT-LIMPIO\guia-cht.json'
csv_file = 'D:\PROYECTOS\FINE-TUNING-IA\TXT-LIMPIO\guia-cht.csv'
json_to_csv(json_file, csv_file)
