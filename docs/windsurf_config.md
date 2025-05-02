# Configuración de Windsurf

## Estructura del Proyecto

```
AIMAGI/
├── .editores/
│   └── windsurf/
│       ├── config/          # Configuración de Windsurf
│       │   └── windsurf.json
│       ├── cache/          # Cache de Windsurf
│       └── logs/           # Logs de Windsurf
├── venv_windsurf/          # Entorno virtual de Windsurf
└── .windsurf/              # Configuración global de Windsurf
```

## Configuración Detallada

1. **Entorno Virtual**
   - Ubicación: `venv_windsurf`
   - Dependencias: Manejadas por [requirements.txt](cci:7://file:///c:/Users/Lenovo/OneDrive/Desktop/AIMAGI/requirements.txt:0:0-0:0)
   - Activación: `.\venv_windsurf\Scripts\Activate`

2. **Configuración de Windsurf**
   - Archivo principal: `.editores\windsurf\config\windsurf.json`
   - Cache: `.editores\windsurf\cache`
   - Logs: `.editores\windsurf\logs`

3. **Mejores Prácticas**
   - Mantener el entorno virtual limpio
   - Actualizar dependencias regularmente
   - Limpiar cache cuando sea necesario
   - Revisar logs para debugging

4. **Flujo de Trabajo**
   ```powershell
   # 1. Activar entorno virtual
   .\venv_windsurf\Scripts\Activate
   
   # 2. Verificar dependencias
   pip list
   
   # 3. Limpiar cache si es necesario
   Remove-Item -Path ".editores\windsurf\cache\*" -Recurse -Force
   
   # 4. Ver logs
   Get-Content ".editores\windsurf\logs\*.log"
   ```

## Mantenimiento

1. **Actualizar Dependencias**
   ```powershell
   # Activar entorno
   .\venv_windsurf\Scripts\Activate
   
   # Actualizar pip
   python -m pip install --upgrade pip
   
   # Actualizar dependencias
   pip install -r requirements.txt --upgrade
   ```

2. **Limpiar Entorno**
   ```powershell
   # Desactivar entorno
   deactivate
   
   # Eliminar entorno virtual
   Remove-Item -Path "venv_windsurf" -Recurse -Force
   
   # Crear nuevo entorno
   python -m venv venv_windsurf
   ```

3. **Backup de Configuración**
   - Copiar `.editores\windsurf\config\windsurf.json`
   - Guardar logs importantes
   - Documentar cambios en la configuración
