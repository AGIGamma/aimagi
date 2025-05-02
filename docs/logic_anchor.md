# Ancla Base de Lógica del Proyecto

## Propósito
Este documento sirve como referencia central para la lógica intrínseca del proyecto AIMAGI. Su objetivo es garantizar que el modelo y los colaboradores mantengan el contexto y la coherencia en todas las iteraciones.

## Lógica Principal
1. **Estructura del Proyecto**:
   - `src/`: Contiene el código fuente principal.
   - `tests/`: Contiene las pruebas unitarias y de integración.
   - `config/`: Contiene configuraciones y variables de entorno.

2. **Flujo de Trabajo**:
   - El archivo principal es `src/main.py`.
   - Los módulos se cargan dinámicamente desde `src/core/` y `src/models/`.

3. **Dependencias Clave**:
   - `torch`: Para modelos de aprendizaje profundo.
   - `transformers`: Para modelos de lenguaje natural.
   - `dotenv`: Para cargar configuraciones desde archivos `.env`.

4. **Relaciones entre Módulos**:
   - `core`: Contiene la lógica central del proyecto.
   - `models`: Define y carga los modelos utilizados.
   - `utils`: Proporciona utilidades comunes como carga de configuraciones.

## Reglas de Validación
1. **Pruebas Unitarias**:
   - Todas las funciones deben tener pruebas asociadas en `tests/`.

2. **Sincronización**:
   - Los cambios deben ser monitoreados por `sync_changes.py`.

3. **Documentación**:
   - Cada módulo debe estar documentado en su archivo correspondiente.

## Próximos Pasos
- Implementar pruebas adicionales para validar la lógica.
- Configurar un sistema de validación continua.
- Actualizar este documento conforme evolucione el proyecto.
