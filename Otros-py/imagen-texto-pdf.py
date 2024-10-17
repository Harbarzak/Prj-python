import fitz  # PyMuPDF
import time
import re
from unidecode import unidecode
import os
import sys
from PIL import Image
import io

def clean_text(text):
    # Eliminar caracteres especiales
    text = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ0-9\s]', '', text)
    # Convertir a ASCII (elimina tildes)
    text = unidecode(text)
    # Eliminar múltiples espacios y líneas en blanco
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_blank_lines(text):
    # Eliminar líneas en blanco
    lines = text.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != '']
    return '\n'.join(non_empty_lines)

# Ruta al archivo PDF usando una cadena cruda
pdf_path = r'D:\PROYECTOS\PYHTON-PROJECTS\Pantalla-Guardian.pdf'

# Ruta al archivo de salida usando una cadena cruda
output_text_path = r'D:\PROYECTOS\PYHTON-PROJECTS\Pantalla-Guardian.txt'
output_image_folder = r'D:\PROYECTOS\PYHTON-PROJECTS\imagenes'

# Crear el directorio de salida para imágenes si no existe
os.makedirs(output_image_folder, exist_ok=True)

# Redirigir stderr a un archivo nulo para evitar mostrar errores de MuPDF
stderr_fileno = sys.stderr.fileno()
with open(os.devnull, 'w') as devnull:
    old_stderr = os.dup(stderr_fileno)
    os.dup2(devnull.fileno(), stderr_fileno)

# Inicio del proceso
start_time = time.time()
print("Iniciando extracción de imágenes del PDF...")

try:
    # Abrir el documento PDF
    doc = fitz.open(pdf_path)
    image_counter = 1

    # Extraer imágenes
    for page_num, page in enumerate(doc):
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_name = f"img{image_counter:02d}.{image_ext}"
            image_path = os.path.join(output_image_folder, image_name)

            # Guardar la imagen
            image = Image.open(io.BytesIO(image_bytes))
            # Convertir a formato sin transparencia si es necesario
            if image.mode in ("RGBA", "LA"):
                background = Image.new(image.mode[:-1], image.size, (255, 255, 255))
                background.paste(image, image.split()[-1])
                image = background

            image.save(image_path)
            image_counter += 1

    # Tiempo de extracción de imágenes
    extract_images_time = time.time()
    print(f"Extracción de imágenes completa en {extract_images_time - start_time:.2f} segundos.")

    # Extracción de texto
    print("Iniciando extracción de texto del PDF...")
    texto = ""
    for page_num, page in enumerate(doc):
        text = page.get_text()
        texto += text

    # Tiempo de extracción de texto
    extract_text_time = time.time()
    print(f"Extracción de texto completa en {extract_text_time - extract_images_time:.2f} segundos. Limpiando el texto...")

    # Limpiar el texto
    texto_limpio = clean_text(texto)
    texto_limpio = remove_blank_lines(texto_limpio)

    # Tiempo de limpieza de texto
    clean_time = time.time()
    print(f"Limpieza de texto completa en {clean_time - extract_text_time:.2f} segundos. Guardando el texto limpio en un archivo .txt...")

    # Guardar el texto limpio en un archivo .txt
    with open(output_text_path, 'w', encoding='utf-8') as file:
        file.write(texto_limpio)

    # Tiempo de guardado del archivo
    save_time = time.time()
    print(f"Texto guardado en {save_time - clean_time:.2f} segundos.")

    # Tiempo total del proceso
    total_time = save_time - start_time
    print(f"Conversión y limpieza completa en {total_time:.2f} segundos. El texto se ha guardado en '{output_text_path}'.")

except Exception as e:
    print(f"Se produjo un error al procesar el archivo PDF: {e}")

# Asegurarse de cerrar el documento PDF
finally:
    if 'doc' in locals():
        doc.close()

# Restaurar stderr
os.dup2(old_stderr, stderr_fileno)
