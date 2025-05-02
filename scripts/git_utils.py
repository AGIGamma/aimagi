"""
Utilidades para manejo de Git en AIMAGI.
"""

import os
import subprocess
from typing import Optional

def create_branch(branch_name: str, base_branch: str = "develop") -> None:
    """
    Crea y cambia a una nueva rama.
    
    Args:
        branch_name: Nombre de la nueva rama
        base_branch: Rama base (default: develop)
    """
    print(f"Creando rama {branch_name} desde {base_branch}...")
    subprocess.run(["git", "checkout", base_branch])
    subprocess.run(["git", "pull", "origin", base_branch])
    subprocess.run(["git", "checkout", "-b", branch_name])

def update_branch(branch_name: str, base_branch: str = "develop") -> None:
    """
    Actualiza una rama con los cambios de la rama base.
    
    Args:
        branch_name: Nombre de la rama actual
        base_branch: Rama base (default: develop)
    """
    print(f"Actualizando {branch_name} desde {base_branch}...")
    subprocess.run(["git", "checkout", base_branch])
    subprocess.run(["git", "pull", "origin", base_branch])
    subprocess.run(["git", "checkout", branch_name])
    subprocess.run(["git", "rebase", base_branch])

def create_pull_request(branch_name: str, title: str, description: str) -> None:
    """
    Crea una solicitud de cambios (pull request).
    
    Args:
        branch_name: Nombre de la rama
        title: Título de la solicitud
        description: Descripción de los cambios
    """
    print(f"Creando pull request para {branch_name}...")
    subprocess.run(["git", "push", "origin", branch_name])
    # TODO: Implementar creación automática de PR usando API de GitHub

def resolve_conflicts(file_path: str) -> Optional[str]:
    """
    Ayuda a resolver conflictos en un archivo.
    
    Args:
        file_path: Ruta al archivo con conflictos
        
    Returns:
        str: Mensaje de resolución o None si no se resuelve
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "<<<<<<< HEAD" in content:
            print(f"¡Alerta! Conflictos detectados en {file_path}")
            return f"Conflictos detectados en {file_path}"
            
        return None
    except Exception as e:
        print(f"Error al verificar conflictos: {e}")
        return f"Error al verificar {file_path}: {e}"

def check_git_status() -> str:
    """
    Verifica el estado actual del repositorio.
    
    Returns:
        str: Estado del repositorio
    """
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    # Ejemplo de uso
    print("\nEstado actual del repositorio:")
    print(check_git_status())
    
    # Crear una rama de ejemplo
    create_branch("feature/test-branch")
    
    # Verificar conflictos
    conflicts = resolve_conflicts("test_file.txt")
    if conflicts:
        print(f"\n{conflicts}")
