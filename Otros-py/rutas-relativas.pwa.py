import os
import re

def convert_to_relative_paths(root_dir):
    """
    Convierte las rutas absolutas en los archivos dentro de root_dir a rutas relativas.
    """
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            with open(file_path, 'r') as f:
                content = f.read()

            # Encuentra todas las rutas absolutas (suponiendo que comienzan con '/')
            absolute_paths = re.findall(r'\"(/[^\"]*)\"', content)
            for abs_path in absolute_paths:
                relative_path = os.path.relpath(abs_path, start=root_dir)
                content = content.replace(f'"{abs_path}"', f'"{relative_path}"')

            with open(file_path, 'w') as f:
                f.write(content)

            print(f"Processed {file_path}")

# Directorio raíz donde se encuentran los archivos
root_directory = 'path/to/your/directory'

convert_to_relative_paths(root_directory)
