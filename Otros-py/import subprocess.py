import subprocess
import sys

def update_pip_packages():
    # Actualizar pip primero
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    
    # Obtener la lista de paquetes instalados
    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'list', '--outdated', '--format=json']).decode('utf-8')
    
    # Convertir la salida JSON a una lista de Python
    import json
    outdated_packages = json.loads(installed_packages)
    
    # Actualizar cada paquete
    for package in outdated_packages:
        package_name = package['name']
        print(f"Actualizando {package_name}...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', package_name])
            print(f"{package_name} actualizado exitosamente.")
        except subprocess.CalledProcessError:
            print(f"Error al actualizar {package_name}.")

    print("Proceso de actualización completado.")

if __name__ == "__main__":
    update_pip_packages()
