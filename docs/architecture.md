# Arquitectura del Proyecto AIMAGI

## Estructura del Proyecto

```
AIMAGI/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── utils.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── base.py
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       └── logging.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
├── config/
│   ├── __init__.py
│   └── settings.py
└── docs/
    ├── architecture.md
    ├── api.md
    └── usage.md
```

## Componentes Principales

### Core
- `config.py`: Manejo de configuración global
- `utils.py`: Funciones utilitarias principales

### Models
- `base.py`: Definiciones base de modelos

### Utils
- `config.py`: Configuración específica
- `logging.py`: Sistema de logging personalizado

## Flujo de Inicialización

1. **Entrada**: [main.py](cci:7://file:///c:/Users/Lenovo/OneDrive/Desktop/AIMAGI/src/main.py:0:0-0:0)
   - Configuración del logging
   - Carga de configuración
   - Inicialización de componentes

2. **Configuración**
   - Carga de configuración global
   - Configuración de componentes
   - Validación de configuración

3. **Inicialización**
   - Core components
   - Models
   - Services

## Sistema de Logging

Niveles de logging:
- DEBUG: Detalles de desarrollo
- INFO: Operaciones normales
- WARNING: Advertencias
- ERROR: Errores
- CRITICAL: Errores críticos

Formato: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`
