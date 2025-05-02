# Pautas para Manejar los Componentes del Proyecto AIMAGI

## 1. Configuración del Entorno

### Entorno Virtual
- Activa el entorno virtual antes de trabajar:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- Instala dependencias adicionales con:
  ```powershell
  pip install <nombre_paquete>
  ```

### Archivos de Configuración
- **`default.env`**: Contiene variables de entorno clave. Modifica este archivo para ajustar configuraciones como `DEBUG` o `LOG_LEVEL`.
- **`editor_config.json`**: Configura opciones específicas para editores como VS Code o Windsurf.

---

## 2. Desarrollo

### Estructura del Proyecto
- **`src/`**: Contiene el código fuente principal.
  - **`core/`**: Lógica central del proyecto.
  - **`models/`**: Definición y carga de modelos.
  - **`utils/`**: Funciones auxiliares como carga de configuraciones.
- **`tests/`**: Contiene pruebas unitarias y de integración.

### Archivo Principal
- **`main.py`**: Es el punto de entrada del proyecto. Ejecuta este archivo para iniciar la aplicación:
  ```powershell
  python src/main.py
  ```

---

## 3. Pruebas

### Ejecución de Pruebas
- Usa `pytest` para ejecutar las pruebas:
  ```powershell
  pytest tests/
  ```

### Pruebas Clave
- **`test_logic.py`**: Valida configuraciones y lógica central.
- **`test_main.py`**: Verifica la inicialización básica del sistema.

---

## 4. Sincronización

### Script de Sincronización
- **`sync_changes.py`**: Monitorea cambios en tiempo real. Ejecútalo con:
  ```powershell
  python sync_changes.py
  ```

### Resolución de Conflictos
- Usa Git para manejar conflictos entre editores:
  ```powershell
  git pull
  git merge
  ```

---

## 5. Documentación

### Archivos Clave
- **`logic_anchor.md`**: Contiene la lógica principal del proyecto.
- **`fase_pruebas.md`**: Describe la etapa actual de pruebas y consolidación.

### Actualización
- Documenta cualquier cambio significativo en los archivos de `docs/`.

---

## 6. Flujo de Trabajo

### Antes de Comenzar
- Activa el entorno virtual.
- Asegúrate de que el script `sync_changes.py` esté en ejecución.

### Durante el Desarrollo
- Realiza cambios en módulos específicos.
- Ejecuta pruebas unitarias para validar los cambios.

### Al Finalizar
- Realiza un `commit` y `push` de los cambios:
  ```powershell
  git add .
  git commit -m "Descripción de los cambios"
  git push
  ```

---

## 7. Comunicación

### Colaboración con Windsurf
- Comparte el archivo `fase_pruebas.md` para mantener a todos los colaboradores informados.
- Usa el script de sincronización para evitar conflictos.
