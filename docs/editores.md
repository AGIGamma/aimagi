# Configuración de Múltiples Editores

## Estructura del Proyecto

```
AIMAGI/
├── .editores/              # Directorio base para configuraciones
│   ├── cursor/            # Configuración para Cursor
│   ├── windsurf/          # Configuración para Windsurf
│   ├── vscode/           # Configuración para VS Code
│   └── editor_futuro/    # Espacio para nuevos editores
├── venv_cursor/           # Entorno virtual para Cursor
├── venv_windsurf/         # Entorno virtual para Windsurf
├── venv_vscode/           # Entorno virtual para VS Code
└── setup_editores.ps1     # Script de configuración
```

## Configuración

1. **Configurar Entornos Virtuales**
   ```powershell
   # Ejecutar el script de configuración
   .\setup_editores.ps1
   ```

2. **Usar un Editor**
   ```powershell
   # Activar el entorno virtual del editor
   .\venv_cursor\Scripts\Activate
   
   # Trabajar en la rama correspondiente
   git checkout -b feature/cursor
   ```

3. **Agregar un Nuevo Editor**
   1. Crear un nuevo directorio en `.editores/`
   2. Ejecutar el script de configuración con el nombre del nuevo editor
   3. Crear una nueva rama para el nuevo editor

## Mejores Prácticas

1. **Ramas Separadas**
   - Cada editor debe trabajar en su propia rama
   - Realizar commits frecuentes
   - Fusionar cambios cuando estén listos

2. **Entornos Virtuales**
   - Usar un entorno virtual separado para cada editor
   - Mantener las dependencias actualizadas
   - Evitar conflictos entre entornos

3. **Sincronización**
   - Realizar pull requests para fusionar cambios
   - Mantener la documentación actualizada
   - Comunicar cambios importantes al equipo

## Reglas para evitar conflictos

1. **Evitar conflictos de guardado**:
   - Habilitar `formatOnSave` solo en un editor (recomendado: VS Code).
   - Deshabilitar la opción de autoformateo en los otros editores.

2. **Sincronización de cambios**:
   - Usar un sistema de control de versiones (Git) para manejar cambios concurrentes.
   - Realizar `pull` y `push` frecuentes para evitar conflictos.

3. **Entorno virtual**:
   - Asegurarse de que todos los editores apunten al mismo entorno virtual (`.venv`).

## Configuración Específica

### VS Code
- Ruta del entorno virtual: `.venv\\Scripts\\python.exe`
- Habilitar `formatOnSave` en `settings.json`.

### Cursor
- Habilitar `autoSave` y `linting` en la configuración del editor.

### Windsurf
- Habilitar `sync` y `autoReload` para mantener los cambios actualizados.

## Resolución de Conflictos
- Si ocurre un conflicto, usar las herramientas de comparación de Git para resolverlo.
- Comunicar los cambios importantes al equipo antes de realizar `push`.
