# Guía de Uso de AIMAGI

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/aimagi.git
cd aimagi
```

2. Crear entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Configuración

1. Crear archivo `.env`:
```bash
cp .env.example .env
```

2. Editar `.env` con tus configuraciones:
```env
DEBUG=true
LOG_LEVEL=DEBUG
API_KEY=tu_api_key
```

## Ejecución

1. Iniciar el servicio:
```bash
python src/main.py
```

2. Verificar estado:
```bash
curl http://localhost:5000/api/health
```

## Desarrollo

### Estructura del Proyecto
```
AIMAGI/
├── src/
│   ├── core/
│   │   ├── config.py
│   │   └── utils.py
│   ├── models/
│   │   └── base.py
│   └── utils/
│       ├── config.py
│       └── logging.py
├── tests/
│   ├── test_config.py
│   └── test_structure.py
└── docs/
    ├── api.md
    ├── usage.md
    └── git_conventions.md
```

### Ejecutar Tests
```bash
pytest tests/ -v
```

### Formato de Código
```bash
black src/ tests/
```

### Verificar Calidad
```bash
flake8 src/ tests/
```

## Contribución

1. Crear rama:
```bash
git checkout -b feature/nombre-funcionalidad
```

2. Desarrollar cambios

3. Ejecutar tests:
```bash
pytest tests/ -v
```

4. Crear pull request:
```bash
git push origin feature/nombre-funcionalidad
```

## Mejores Prácticas

1. **Nombres de Variables**:
   - Uso de snake_case
   - Descriptivos y claros
   - Evitar abreviaturas

2. **Funciones**:
   - Una función por responsabilidad
   - Documentación clara
   - Tests unitarios

3. **Clases**:
   - Uso de PascalCase
   - Herencia limitada
   - Métodos pequeños

4. **Tests**:
   - Cobertura > 80%
   - Tests unitarios
   - Tests de integración
   - Tests de aceptación

## Resolución de Problemas

### Problemas Comunes

1. **Error de Configuración**
   - Verificar `.env`
   - Revisar logs
   - Verificar permisos

2. **Problemas de Dependencias**
   - Reinstalar venv
   - Verificar requirements.txt
   - Limpiar cache

3. **Errores en Tests**
   - Verificar mocks
   - Revisar fixtures
   - Limpiar estado

## Soporte

- Documentación: docs/
- Issues: https://github.com/tu-usuario/aimagi/issues
- Soporte: support@aimagi.com
