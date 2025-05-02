"""
Core functionality module for AIMAGI project.
This module contains the core business logic and main functionality.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Cargar variables de entorno
env_path = Path(__file__).parent.parent.parent / 'config' / 'environments' / 'default.env'
load_dotenv(dotenv_path=env_path)

# Configuración global
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
MODEL_PATH = Path(os.getenv('MODEL_PATH', 'models/'))
DATA_PATH = Path(os.getenv('DATA_PATH', 'data/'))
