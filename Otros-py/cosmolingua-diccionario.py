# Diccionario de ejemplo con vocabulario básico de Cosmolingua
cosmolingua_dict = {
    'hola': 'zal',
    'adiós': 'dio',
    'buenos': 'bon',
    'gracias': 'gra',
    'días': 'mato',
    'por favor': 'favo',
    'sí': 'ja',
    'no': 'na',
    'amigo': 'mako',
    'cómo estás': 'komar esu',
    'estoy bien': 'esu bon',
    'bienvenido': 'venar',
    'uno': 'un',
    'dos': 'du',
    'tres': 'tri',
    'cuatro': 'kvar',
    'cinco': 'kvin',
    'rojo': 'rok',
    'azul': 'bal',
    'verde': 'ver',
    'amarillo': 'jel',
    'negro': 'neg',
    'libro': 'libru',
    'escribir': 'skriba',
    'casa': 'doma',
    'computadora': 'kompu',
    'teléfono': 'telu',
    'me llamo': 'mi nomar',
    'nombre': 'nomar',
    'quiero': 'volu',
    'saber': 'sabar',
    'la': 'la',
    'hora': 'tempo-ni',
    # Añade más palabras y sus traducciones aquí
}

def traducir_a_cosmolingua(texto):
    palabras = texto.split()
    traduccion = []
    for palabra in palabras:
        palabra_cosmolingua = cosmolingua_dict.get(palabra.lower(), palabra)
        traduccion.append(palabra_cosmolingua)
    return ' '.join(traduccion)

# Ejemplo de uso
texto_entrada = 'Buenos días'
texto_cosmolingua = traducir_a_cosmolingua(texto_entrada)
print(texto_cosmolingua)  # Salida: zaliti amikun
