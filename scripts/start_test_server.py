"""
Script para iniciar el servidor de desarrollo para pruebas.
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def start_server():
    """
    Inicia el servidor de desarrollo.
    """
    # Cambiar al directorio del proyecto
    project_dir = Path(__file__).parent.parent
    os.chdir(project_dir)
    
    # Crear archivo de configuración temporal
    config_path = project_dir / "tests" / "test_config.env"
    config_path.write_text("""
DEBUG=true
LOG_LEVEL=DEBUG
API_KEY=test_key_123
""")
    
    # Iniciar el servidor
    print("Iniciando servidor de desarrollo...")
    subprocess.Popen(["python", "src/main.py"])
    
    # Esperar a que el servidor se inicie
    time.sleep(2)
    
    print("Servidor iniciado correctamente")

def main():
    """
    Función principal.
    """
    try:
        start_server()
    except Exception as e:
        print(f"Error al iniciar el servidor: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
