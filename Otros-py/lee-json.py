import json

# Leer el fichero JSON
with open('D:\PROYECTOS\FINE-TUNING-IA\TXT-LIMPIO\guia-cht.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

# Función para organizar los datos (por ejemplo, por edad)
def organizar_por_edad(datos):
    return sorted(datos, key=lambda x: x['text'])

# Organizar los datos
datos_organizados = organizar_por_edad(datos)

# Mostrar los datos organizados
for persona in datos_organizados:
    print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Ciudad: {persona['ciudad']}")
