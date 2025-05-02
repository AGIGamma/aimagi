"""
Sistema de configuración para AIMAGI.

Este módulo maneja la carga y validación de la configuración del proyecto.
"""

import logging
from typing import Any, Dict, Optional
from pathlib import Path
from dataclasses import dataclass
from dotenv import dotenv_values

logger = logging.getLogger(__name__)

class ConfigModel:
    """Modelo de configuración base"""
    debug: bool = False
    log_level: str = "INFO"
    api_key: Optional[str] = None
    
    def __init__(self, **entries):
        self.__dict__.update(entries)
        
    def __str__(self):
        return f"debug={self.debug}, log_level={self.log_level}, api_key={self.api_key}"

def load_config(config_path: Path) -> Dict[str, Any]:
    """
    Carga y valida la configuración desde un archivo .env.
    
    Args:
        config_path (Path): Ruta al archivo de configuración
        
    Returns:
        Dict[str, Any]: Diccionario con la configuración cargada
        
    Raises:
        FileNotFoundError: Si el archivo de configuración no existe
    """
    logger.debug(f"Cargando configuración desde: {config_path}")
    
    if not config_path.exists():
        logger.error(f"Archivo de configuración no encontrado: {config_path}")
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    try:
        config_data = dotenv_values(config_path)
        logger.info("Configuración cargada exitosamente")
        return config_data
    except Exception as e:
        logger.error(f"Error al cargar la configuración: {e}")
        raise ValueError(f"Error al cargar la configuración: {e}")

def get_default_config() -> ConfigModel:
    """
    Obtiene la configuración por defecto.
    
    Returns:
        ConfigModel: Configuración por defecto
    """
    return ConfigModel()
