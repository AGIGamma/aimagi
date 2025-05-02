# Script para configurar entornos virtuales para diferentes editores

param (
    [string]$editor
)

switch ($editor) {
    "vscode" {
        Write-Host "Configurando entorno para VS Code..."
        .\.venv\Scripts\Activate.ps1
    }
    "cursor" {
        Write-Host "Configurando entorno para Cursor..."
        .\.venv\Scripts\Activate.ps1
    }
    "windsurf" {
        Write-Host "Configurando entorno para Windsurf..."
        .\.venv\Scripts\Activate.ps1
    }
    default {
        Write-Host "Editor no reconocido. Por favor, elige entre: vscode, cursor, windsurf."
    }
}
