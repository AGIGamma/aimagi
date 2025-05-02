import pytest
import os
from pathlib import Path

def test_project_structure():
    """Verifica la estructura básica del proyecto"""
    base_dir = Path(__file__).parent.parent
    
    # Verificar directorios principales
    assert (base_dir / "src").exists()
    assert (base_dir / "tests").exists()
    assert (base_dir / "config").exists()
    assert (base_dir / "docs").exists()
    
    # Verificar estructura de src
    src_dir = base_dir / "src"
    assert (src_dir / "core").exists()
    assert (src_dir / "models").exists()
    assert (src_dir / "utils").exists()
    
    # Verificar archivos principales
    assert (base_dir / "src" / "main.py").exists()
    assert (base_dir / "src" / "utils" / "config.py").exists()
    
    # Verificar estructura de tests
    test_dir = base_dir / "tests"
    assert (test_dir / "__init__.py").exists()
    assert (test_dir / "test_config.py").exists()
    assert (test_dir / "test_structure.py").exists()
