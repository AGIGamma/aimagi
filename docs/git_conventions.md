# Convenciones de Git para AIMAGI

## Estructura de Ramas

### Ramas Principales
- `main`: Rama principal con código estable
- `develop`: Rama de desarrollo
- `hotfix/*`: Ramas para correcciones urgentes

### Ramas de Características
- `feature/*`: Para nuevas funcionalidades
- `bugfix/*`: Para correcciones de errores
- `refactor/*`: Para mejoras de código

## Convenciones de Commits

### Formato de Mensajes
```
tipo(scope): descripción breve

Cuerpo del commit (opcional)

Footer (opcional)
```

### Tipos de Commits
- `feat`: Nueva funcionalidad
- `fix`: Corrección de error
- `docs`: Cambios en documentación
- `style`: Cambios de formato (sin afectar la lógica)
- `refactor`: Cambios de código sin cambios funcionales
- `test`: Adición o corrección de tests
- `chore`: Cambios en la configuración del proyecto

### Ejemplos
```
feat(models): agregar modelo de usuario

fix(utils): corregir error en función de validación

docs(api): actualizar documentación de endpoints

refactor(core): mejorar estructura de módulos
```

## Flujo de Trabajo

1. **Crear Rama**
```bash
git checkout develop
git checkout -b feature/nombre-funcionalidad
```

2. **Desarrollo**
- Hacer commits pequeños y coherentes
- Ejecutar pruebas después de cada cambio
- Mantener el código limpio y documentado

3. **Solicitud de Cambios**
```bash
git checkout develop
git pull origin develop
git checkout feature/nombre-funcionalidad
git rebase develop
```

4. **Merge**
- Solo después de revisión y aprobación
- Usar merge o rebase según la política del equipo

## Resolución de Conflictos

1. **Identificar Conflictos**
```bash
git status
git diff
```

2. **Resolver Conflictos**
- Usar herramientas visuales de merge
- Mantener la consistencia del código
- Documentar cambios importantes

3. **Completar Resolución**
```bash
git add .
git commit -m "fix: resolver conflictos en archivo"```
