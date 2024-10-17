import psutil
import time
from collections import defaultdict
import datetime
import os

def get_process_connections(pid):
    try:
        process = psutil.Process(pid)
        return process.connections()
    except psutil.NoSuchProcess:
        return []

def is_suspicious(process, connections):
    trusted_processes = [
        'chrome.exe', 'firefox.exe', 'explorer.exe', 'svchost.exe',
        'brave.exe', 'cursor.exe', 'whatsapp.exe'
    ]
    
    if process.name().lower() not in trusted_processes:
        if connections and any(conn.status == psutil.CONN_ESTABLISHED for conn in connections):
            return True
    return False

def monitor_suspicious_processes():
    process_connections = defaultdict(int)
    output = []
    
    start_time = time.time()
    while True:
        for process in psutil.process_iter(['pid', 'name', 'status']):
            try:
                connections = get_process_connections(process.pid)
                if is_suspicious(process, connections):
                    process_connections[process.name()] += 1
                    output.append(f"Proceso sospechoso detectado: {process.name()} (PID: {process.pid})")
                    for conn in connections:
                        if conn.status == psutil.CONN_ESTABLISHED:
                            output.append(f"  Conexión establecida: {conn.laddr} -> {conn.raddr}")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        output.append("\nResumen de procesos sospechosos:")
        for proc, count in process_connections.items():
            output.append(f"{proc}: detectado {count} veces")
        
        # Escribir en el archivo cada 10 minutos
        if time.time() - start_time >= 600:  # 600 segundos = 10 minutos
            write_to_file(output)
            output = []  # Limpiar la lista de salida
            process_connections = defaultdict(int)  # Reiniciar el conteo
            start_time = time.time()  # Reiniciar el temporizador
        
        time.sleep(30)  # Esperar 30 segundos antes de la próxima revisión

def write_to_file(output):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"procesos_sospechosos_{timestamp}.txt"
    
    with open(filename, "w") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    print("Iniciando monitoreo de procesos sospechosos en segundo plano.")
    print("Los resultados se escribirán en archivos de texto cada 10 minutos.")
    
    try:
        # Iniciar el monitoreo en segundo plano
        import threading
        thread = threading.Thread(target=monitor_suspicious_processes)
        thread.daemon = True  # Esto permite que el script principal termine incluso si el hilo está en ejecución
        thread.start()
        
        # Mantener el script principal en ejecución
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoreo detenido.")
