"""
Pruebas para validar la lógica intrínseca del proyecto AIMAGI.
"""

import unittest
from pathlib import Path
import sys

# Agregar el directorio src al path para poder importar los módulos
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from core import DEBUG, LOG_LEVEL
from utils.config import load_config

class TestLogic(unittest.TestCase):
    def test_debug_flag(self):
        """Test que verifica que la bandera DEBUG se carga correctamente."""
        self.assertIsInstance(DEBUG, bool)

    def test_log_level(self):
        """Test que verifica que LOG_LEVEL es válido."""
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        self.assertIn(LOG_LEVEL, valid_levels)

    def test_load_config(self):
        """Test que verifica la funcionalidad de carga de configuración."""
        config = load_config(Path('config/environments/default.env'))
        self.assertIsInstance(config, dict)
        self.assertIn('DEBUG', config)
        self.assertIn('LOG_LEVEL', config)

if __name__ == "__main__":
    unittest.main()
