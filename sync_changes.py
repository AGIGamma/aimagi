"""
Script para sincronizar cambios en tiempo real entre múltiples editores.
"""

import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configurar logging
logging.basicConfig(
    filename='sync_changes.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        logging.info(f"Archivo modificado: {event.src_path}")
        print(f"Archivo modificado: {event.src_path}")

    def on_created(self, event):
        if event.is_directory:
            return
        logging.info(f"Archivo creado: {event.src_path}")
        print(f"Archivo creado: {event.src_path}")

    def on_deleted(self, event):
        if event.is_directory:
            return
        logging.info(f"Archivo eliminado: {event.src_path}")
        print(f"Archivo eliminado: {event.src_path}")

if __name__ == "__main__":
    path = "c:\\Users\\Lenovo\\OneDrive\\Desktop\\AIMAGI"
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    print(f"Monitoreando cambios en: {path}")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
