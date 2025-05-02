# Script de inicialización del proyecto

# Script de inicialización del proyecto

# Función para verificar y crear entornos virtuales
function VerificarEntorno {
    param(
        [string]$editor,
        [string]$requirements = "requirements.txt"
    )
    
    if (-not (Test-Path "venv_$editor")) {
        Write-Host "Creando entorno virtual para $editor..." -ForegroundColor Yellow
        try {
            python -m venv "venv_$editor"
            
            # Activar entorno y instalar dependencias
            .\venv_$editor\Scripts\Activate
            pip install -r $requirements
            deactivate
            Write-Host "Entorno virtual creado exitosamente." -ForegroundColor Green
        }
        catch {
            Write-Host "Error al crear el entorno virtual: $_" -ForegroundColor Red
            exit 1
        }
    }
    else {
        Write-Host "Entorno virtual ya existe." -ForegroundColor Cyan
    }
}

# Función para verificar dependencias
function VerificarDependencias {
    param($editor)
    
    Write-Host "Verificando dependencias..." -ForegroundColor Cyan
    try {
        .\venv_$editor\Scripts\pip list
        Write-Host "Dependencias verificadas exitosamente." -ForegroundColor Green
    }
    catch {
        Write-Host "Error al verificar dependencias: $_" -ForegroundColor Red
        exit 1
    }
}

# Función para activar entorno y configurar editor
function InicializarEditor {
    param($editor)
    
    # Verificar y crear entorno si no existe
    VerificarEntorno -editor $editor
    
    # Verificar dependencias
    VerificarDependencias -editor $editor
    
    # Activar entorno
    Write-Host "Activando entorno virtual para $editor..." -ForegroundColor Green
    try {
        .\venv_$editor\Scripts\Activate
        $env:PYTHONPATH = "$pwd"
        Write-Host "Entorno virtual activado exitosamente." -ForegroundColor Green
    }
    catch {
        Write-Host "Error al activar el entorno virtual: $_" -ForegroundColor Red
        exit 1
    }
    
    # Mensaje de bienvenida
    Write-Host ""`n`n" -ForegroundColor White
    Write-Host "=========================================" -ForegroundColor Cyan
    Write-Host "  Bienvenido a AIMAGI - $editor" -ForegroundColor Green
    Write-Host "=========================================" -ForegroundColor Cyan
    Write-Host ""`n -ForegroundColor White
    Write-Host "Entorno configurado y listo para usar." -ForegroundColor Green
    Write-Host ""`n -ForegroundColor White
}

# Función principal
function Start-AIMAGI {
    # Verificar Python
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        Write-Host "Python no está instalado. Por favor, instala Python primero." -ForegroundColor Red
        exit 1
    }

    # Determinar el editor actual
    $editor = "windsurf"  # Por defecto

    # Verificar si existe un archivo de configuración específico
    if (Test-Path ".editor_config.json") {
        try {
            $config = Get-Content ".editor_config.json" | ConvertFrom-Json
            $editor = $config.editor
            Write-Host "Editor configurado: $editor" -ForegroundColor Cyan
        }
        catch {
            Write-Host "Error al leer la configuración: $_" -ForegroundColor Yellow
            Write-Host "Usando editor por defecto: windsurf" -ForegroundColor Cyan
        }
    }

    # Inicializar el editor
    InicializarEditor -editor $editor
}

# Ejecutar el script
Start-AIMAGI

# Mantener la ventana abierta
Write-Host "Presione cualquier tecla para salir..." -ForegroundColor Yellow
$host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | Out-Null
