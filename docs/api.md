# Documentación de la API de AIMAGI

## Estructura General

La API de AIMAGI sigue un patrón RESTful y utiliza JSON para la comunicación.

### Endpoints Principales

- `GET /api/health`: Verifica el estado del servicio
- `POST /api/config`: Maneja la configuración del sistema
- `GET /api/status`: Obtiene el estado actual del sistema

## Autenticación

La API utiliza un sistema de autenticación basado en token:

1. Obtener token:
```http
POST /api/auth/login
Content-Type: application/json

{
    "api_key": "tu_api_key"
}
```

2. Usar token en peticiones:
```http
GET /api/health
Authorization: Bearer <token>
```

## Errores

Los errores se manejan con códigos HTTP estándar:

- `200 OK`: Operación exitosa
- `400 Bad Request`: Petición inválida
- `401 Unauthorized`: Autenticación requerida
- `403 Forbidden`: Permiso denegado
- `404 Not Found`: Recurso no encontrado
- `500 Internal Server Error`: Error interno

## Ejemplos de Uso

### Verificar Estado
```python
import requests

url = "http://localhost:5000/api/health"
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)
print(response.json())
```

### Configurar Sistema
```python
import requests

url = "http://localhost:5000/api/config"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data = {
    "debug": True,
    "log_level": "DEBUG"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

## Respuestas Estándar

### Éxito
```json
{
    "status": "success",
    "data": {
        "message": "Operación exitosa",
        "result": {...}
    }
}
```

### Error
```json
{
    "status": "error",
    "code": 400,
    "message": "Descripción del error",
    "details": {...}
}
```

## Seguridad

- Todos los endpoints requieren autenticación
- Los tokens tienen expiración
- Se implementa rate limiting
- Se registran todas las operaciones

## Monitorización

- Logging detallado
- Métricas de rendimiento
- Alertas de errores
- Monitoreo de recursos
