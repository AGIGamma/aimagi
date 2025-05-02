"""
Ejemplo de flujo de trabajo con Git usando las utilidades de AIMAGI.
"""

from git_utils import create_branch, update_branch, create_pull_request

def main():
    """
    Ejemplo de flujo de trabajo completo.
    """
    # 1. Crear rama de característica
    feature_branch = "feature/nueva-funcionalidad"
    create_branch(feature_branch)
    
    # 2. Desarrollar la funcionalidad
    print("\nDesarrollando la funcionalidad...")
    # Aquí iría el código de desarrollo
    
    # 3. Actualizar rama con cambios de develop
    update_branch(feature_branch)
    
    # 4. Crear pull request
    pr_title = "Implementar nueva funcionalidad"
    pr_description = """
    Implementación de la nueva funcionalidad solicitada.
    
    Cambios principales:
    - Agregado nuevo módulo
    - Actualizado tests
    - Mejorado documentación
    """
    
    create_pull_request(feature_branch, pr_title, pr_description)

if __name__ == "__main__":
    main()
