import pytest
import os
import sys
import tempfile
import json
import logging
import requests
from pathlib import Path
from datetime import datetime
from utils.config import load_config, get_default_config
from src.main import main as app_main

# Configurar logging para las pruebas
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TestSystem:
    @pytest.fixture(autouse=True)
    def setup(self, tmp_path):
        """Configuración común para todas las pruebas"""
        self.temp_dir = tmp_path
        self.config_path = self.temp_dir / "test_config.env"
        
        # Crear configuración de prueba
        self.config_path.write_text("""
DEBUG=true
LOG_LEVEL=DEBUG
API_KEY=test_key_123
""")
        
        # Guardar el directorio actual
        self.original_dir = os.getcwd()
        
        # Cambiar al directorio temporal
        os.chdir(self.temp_dir)
        
        # Crear directorios necesarios
        (self.temp_dir / "logs").mkdir(parents=True, exist_ok=True)
        (self.temp_dir / "metrics").mkdir(parents=True, exist_ok=True)
        (self.temp_dir / "data").mkdir(parents=True, exist_ok=True)
        
        yield
        
        # Limpiar después de las pruebas
        os.chdir(self.original_dir)

    def test_system_initialization(self):
        """Verifica la inicialización del sistema"""
        try:
            # Cargar configuración
            config = load_config(self.config_path)
            assert config["DEBUG"] == "true"
            assert config["LOG_LEVEL"] == "DEBUG"
            assert config["API_KEY"] == "test_key_123"
            
            # Inicializar el sistema
            app_main()
            
            # Verificar logs
            log_file = self.temp_dir / "logs" / "app.log"
            assert log_file.exists()
            
            # Verificar estructura de directorios
            assert (self.temp_dir / "data").exists()
            assert (self.temp_dir / "models").exists()
            assert (self.temp_dir / "logs").exists()
            
        except Exception as e:
            logger.error(f"Error en la inicialización: {e}")
            raise

    def test_configuration_validation(self):
        """Verifica la validación de configuración"""
        # Configuración inválida
        invalid_config = self.temp_dir / "invalid_config.env"
        invalid_config.write_text("""
DEBUG=invalid
LOG_LEVEL=INVALID
API_KEY=
""")
        
        with pytest.raises(ValueError):
            load_config(invalid_config)
            
        # Configuración válida
        valid_config = self.temp_dir / "valid_config.env"
        valid_config.write_text("""
DEBUG=false
LOG_LEVEL=INFO
API_KEY=valid_key_123
""")
        
        config = load_config(valid_config)
        assert config["DEBUG"] == "false"
        assert config["LOG_LEVEL"] == "INFO"
        assert config["API_KEY"] == "valid_key_123"

    def test_logging_system(self, caplog):
        """Verifica el sistema de logging"""
        caplog.set_level(logging.DEBUG)
        
        # Inicializar el sistema
        app_main()
        
        # Verificar logs
        assert "Iniciando aplicación AIMAGI..." in caplog.text
        assert "Nivel de logging configurado" in caplog.text
        
        # Verificar archivo de log
        log_file = self.temp_dir / "logs" / "app.log"
        assert log_file.exists()
        
        with open(log_file, 'r', encoding='utf-8') as f:
            log_content = f.read()
            assert "Iniciando aplicación AIMAGI..." in log_content

    def test_error_handling(self, caplog):
        """Verifica el manejo de errores"""
        caplog.set_level(logging.ERROR)
        
        # Simular error
        try:
            raise ValueError("Error de prueba")
        except Exception as e:
            logger.error(f"Error de prueba: {e}")
            
        # Verificar log de error
        assert "Error de prueba" in caplog.text
        
        # Verificar archivo de log
        log_file = self.temp_dir / "logs" / "app.log"
        assert log_file.exists()
        
        with open(log_file, 'r', encoding='utf-8') as f:
            log_content = f.read()
            assert "Error de prueba" in log_content

    def test_system_shutdown(self, caplog):
        """Verifica el apagado del sistema"""
        caplog.set_level(logging.INFO)
        
        # Inicializar el sistema
        app_main()
        
        # Verificar logs de apagado
        assert "Apagando sistema..." in caplog.text
        assert "Sistema apagado correctamente" in caplog.text

    def test_performance_metrics(self):
        """Verifica las métricas de rendimiento"""
        # Inicializar el sistema
        app_main()
        
        # Verificar archivo de métricas
        metrics_file = self.temp_dir / "metrics" / "performance.json"
        assert metrics_file.exists()
        
        with open(metrics_file, 'r', encoding='utf-8') as f:
            metrics = json.load(f)
            assert "startup_time" in metrics
            assert "memory_usage" in metrics
            assert "cpu_usage" in metrics

    def test_data_persistence(self):
        """Verifica la persistencia de datos"""
        # Inicializar el sistema
        app_main()
        
        # Verificar directorio de datos
        data_dir = self.temp_dir / "data"
        assert data_dir.exists()
        
        # Verificar estructura de datos
        assert (data_dir / "models").exists()
        assert (data_dir / "config").exists()
        assert (data_dir / "logs").exists()

    def test_api_endpoints(self):
        """Verifica los endpoints de la API"""
        # Inicializar el sistema
        app_main()
        
        # Verificar endpoints
        health_url = "http://localhost:5000/api/health"
        config_url = "http://localhost:5000/api/config"
        status_url = "http://localhost:5000/api/status"
        
        # Verificar respuesta de health
        response = requests.get(health_url)
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
        
        # Verificar respuesta de config
        response = requests.get(config_url)
        assert response.status_code == 200
        assert "debug" in response.json()
        
        # Verificar respuesta de status
        response = requests.get(status_url)
        assert response.status_code == 200
        assert "uptime" in response.json()

    def test_security_features(self):
        """Verifica las características de seguridad"""
        # Inicializar el sistema
        app_main()
        
        # Verificar autenticación
        auth_url = "http://localhost:5000/api/auth/login"
        response = requests.post(auth_url, json={"api_key": "test_key_123"})
        assert response.status_code == 200
        assert "token" in response.json()
        
        # Verificar protección contra CSRF
        csrf_url = "http://localhost:5000/api/csrf"
        response = requests.get(csrf_url)
        assert response.status_code == 403
        
        # Verificar rate limiting
        for _ in range(100):
            response = requests.get(health_url)
            assert response.status_code == 200
