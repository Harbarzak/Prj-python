import cv2
import numpy as np
import trimesh

def image_to_3d(image_path, output_path, depth_scale=10):
    # Cargar la imagen en escala de grises
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"No se pudo cargar la imagen en la ruta: {image_path}")

    # Normalizar la imagen
    image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    # Escalar la profundidad
    z = image * depth_scale

    # Obtener las dimensiones de la imagen
    height, width = image.shape
    x = np.linspace(0, width, width)
    y = np.linspace(0, height, height)
    x, y = np.meshgrid(x, y)

    # Crear una nube de puntos
    points = np.c_[x.ravel(), y.ravel(), z.ravel()]

    # Crear una malla triangular
    faces = []
    for i in range(height - 1):
        for j in range(width - 1):
            idx = i * width + j
            faces.append([idx, idx + 1, idx + width])
            faces.append([idx + 1, idx + width + 1, idx + width])

    faces = np.array(faces)

    # Crear el objeto de malla
    mesh = trimesh.Trimesh(vertices=points, faces=faces)

    # Exportar la malla como archivo STL
    mesh.export(output_path)

    print(f'Modelo STL guardado en {output_path}')

# Rutas de la imagen de entrada y el archivo STL de salida
image_path = 'D:\PROYECTOS\PYHTON-PROJECTS\scale.png'
output_path = 'D:\PROYECTOS\PYHTON-PROJECTS\modelo.stl'

# Convertir la imagen a modelo 3D
image_to_3d(image_path, output_path)

