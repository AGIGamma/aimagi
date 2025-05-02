"""
Punto de entrada principal para la aplicación AIMAGI.

Este módulo inicializa la aplicación y configura los componentes principales.
"""

import logging
import sys
from pathlib import Path
from datetime import datetime
from utils.config import load_config, get_default_config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Configuración del logging base
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="AIMAGI API",
    description="API para el proyecto AIMAGI",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health", tags=["health"])
async def health_check():
    """Verifica el estado del servicio"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/api/config", tags=["config"])
async def get_config():
    """Obtiene la configuración actual"""
    return config.__dict__

@app.get("/api/status", tags=["status"])
async def get_status():
    """Obtiene el estado del sistema"""
    return {
        "uptime": datetime.now() - start_time,
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/api/auth/login", tags=["auth"])
async def login(api_key: str):
    """Autentica con la API key"""
    if api_key == config.api_key:
        return {"token": create_token()}
    return {"error": "Invalid API key"}, 401

def initialize_logging(config):
    """
    Inicializa el sistema de logging según la configuración.
    
    Args:
        config: Objeto de configuración
    """
    log_level = getattr(logging, config.log_level.upper(), logging.INFO)
    logging.getLogger().setLevel(log_level)
    logger.info(f"Nivel de logging configurado: {logging.getLevelName(log_level)}")

def initialize_components():
    """
    Inicializa los componentes principales de la aplicación.
    """
    logger.info("Inicializando componentes...")
    # TODO: Implementar inicialización de componentes específicos

def main():
    """
    Función principal de la aplicación.
    
    Inicializa la configuración y los componentes principales.
    """
    global config, start_time
    start_time = datetime.now()
    
    try:
        # Cargar configuración
        config_path = Path("config/config.json")
        try:
            config = load_config(config_path)
        except FileNotFoundError:
            logger.warning("Usando configuración por defecto")
            config = get_default_config()
        
        # Inicializar logging
        initialize_logging(config)
        
        # Inicializar componentes
        initialize_components()
        
        logger.info("Iniciando aplicación AIMAGI...")
        if config.debug:
            logger.debug("Modo DEBUG activado")
            
        print('AIMAGI System Initialized')
        
        # Iniciar servidor
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=5000,
            log_level=config.log_level.lower(),
            reload=config.debug
        )
        
    except Exception as e:
        logger.error(f"Error al iniciar la aplicación: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
