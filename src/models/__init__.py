"""
Módulo de modelos para AIMAGI.
Este módulo contiene las definiciones de los modelos y sus funcionalidades.
"""

import logging
from pathlib import Path
from typing import Optional

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)

class AIMAGIModel:
    """
    Clase base para los modelos de AIMAGI.
    """
    
    def __init__(self, model_path: Optional[Path] = None):
        """
        Inicializa el modelo.
        
        Args:
            model_path (Optional[Path]): Ruta al modelo pre-entrenado
        """
        self.model_path = model_path
        self.model = None
        self.tokenizer = None
        
    def load(self) -> None:
        """
        Carga el modelo y el tokenizer.
        """
        if self.model_path is None:
            raise ValueError("model_path no puede ser None")
        
        logger.info(f"Cargando modelo desde: {self.model_path}")
        # TODO: Implementar carga del modelo
