import os
import pytest
from pathlib import Path
from utils.config import load_config, get_default_config

def test_load_config():
    """Verifica que la configuración se cargue correctamente"""
    # Crear archivo de prueba
    test_env_path = Path("tests/test.env")
    test_env_path.write_text("""
DEBUG=true
LOG_LEVEL=DEBUG
API_KEY=test_key
""")
    
    try:
        config = load_config(test_env_path)
        assert config["DEBUG"] == "true"
        assert config["LOG_LEVEL"] == "DEBUG"
        assert config["API_KEY"] == "test_key"
        
    finally:
        # Limpiar archivo de prueba
        test_env_path.unlink()

def test_default_config():
    """Verifica que la configuración por defecto sea correcta"""
    config = get_default_config()
    assert config.debug is False
    assert config.log_level == "INFO"
    assert config.api_key is None
