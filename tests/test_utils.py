import pytest
from pathlib import Path
from utils.config import ConfigModel
import logging

@pytest.fixture
def config_model():
    """Fixture para ConfigModel"""
    return ConfigModel()

@pytest.fixture
def test_config_file(tmp_path):
    """Fixture para archivo de configuración de prueba"""
    config_path = tmp_path / "test_config.env"
    config_path.write_text("""
DEBUG=true
LOG_LEVEL=DEBUG
API_KEY=test_key
""")
    return config_path

def test_config_model_default_values(config_model):
    """Verifica los valores por defecto del modelo de configuración"""
    assert config_model.debug is False
    assert config_model.log_level == "INFO"
    assert config_model.api_key is None

def test_config_model_update(config_model):
    """Verifica la actualización del modelo de configuración"""
    config_model.debug = True
    config_model.log_level = "DEBUG"
    config_model.api_key = "test_key"
    
    assert config_model.debug is True
    assert config_model.log_level == "DEBUG"
    assert config_model.api_key == "test_key"

def test_config_model_invalid_log_level(config_model):
    """Verifica el manejo de niveles de logging inválidos"""
    with pytest.raises(ValueError):
        config_model.log_level = "INVALID"

def test_config_model_invalid_debug_value(config_model):
    """Verifica el manejo de valores inválidos para debug"""
    with pytest.raises(AttributeError):
        config_model.debug = "invalid"

def test_config_model_string_representation(config_model):
    """Verifica la representación en string del modelo"""
    config_model.debug = True
    config_model.log_level = "DEBUG"
    config_model.api_key = "test_key"
    
    config_str = str(config_model)
    assert "debug=True" in config_str
    assert "log_level=DEBUG" in config_str
    assert "api_key=test_key" in config_str

def test_config_model_dict_conversion(config_model):
    """Verifica la conversión a diccionario"""
    config_model.debug = True
    config_model.log_level = "DEBUG"
    config_model.api_key = "test_key"
    
    config_dict = config_model.__dict__
    assert config_dict["debug"] is True
    assert config_dict["log_level"] == "DEBUG"
    assert config_dict["api_key"] == "test_key"

def test_config_model_logging_config(config_model, caplog):
    """Verifica la configuración de logging"""
    caplog.set_level(logging.DEBUG)
    
    config_model.debug = True
    config_model.log_level = "DEBUG"
    
    logger = logging.getLogger(__name__)
    logger.debug("Mensaje de prueba")
    
    assert "Mensaje de prueba" in caplog.text
