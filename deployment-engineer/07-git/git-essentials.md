# Git - Comandos Esenciales

## 1. Configuración Inicial

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
git config --list                # Ver configuración
```

## 2. Repositorio Básico

### Inicializar y Clonar
```bash
git init                         # Iniciar nuevo repo
git clone https://github.com/user/repo.git
git clone -b rama --single-branch repo.git  # Rama específica
```

## 3. Flujo Básico

### Staging y Commit
```bash
git status                       # Ver estado
git add file.txt                 # Añadir archivo al staging
git add .                        # Añadir todos los cambios
git commit -m "Mensaje del commit"
git commit -am "Incluir archivos modificados"
git commit --amend               # Modificar último commit
```

### Historial
```bash
git log                          # Ver historial
git log --oneline                # Formato compacto
git log -n 5                     # Últimos 5 commits
git log --grep="keyword"         # Buscar por mensaje
git log -p                       # Ver cambios (patch)
git show commit_id               # Ver commit específico
```

## 4. Ramas (Branches)

### Crear y Cambiar Ramas
```bash
git branch                       # Ver ramas locales
git branch -a                    # Ver todas ramas (local + remoto)
git branch nueva-rama            # Crear rama
git checkout nueva-rama          # Cambiar a rama
git checkout -b nueva-rama       # Crear y cambiar en uno
git switch nueva-rama            # Alternativa moderna a checkout
```

### Eliminar Rama
```bash
git branch -d nombre-rama        # Eliminar rama local
git branch -D nombre-rama        # Forzar eliminar
git push origin --delete nombre-rama  # Eliminar en remoto
```

## 5. Fusión de Ramas

### Merge
```bash
git checkout main
git merge otra-rama              # Fusionar otra-rama en main
git merge --no-ff otra-rama      # Crear commit de merge
```

### Rebase
```bash
git checkout feature
git rebase main                  # Rebase de feature sobre main
git checkout main
git merge feature                # Fast-forward merge
```

### Conflictos
```bash
# Git marca conflictos automáticamente
# Resuelve manualmente, luego:
git add archivo_resuelto
git commit -m "Resolver conflicto"

# O abortar
git merge --abort
git rebase --abort
```

## 6. Cambios y Deshacer

### Visualizar Cambios
```bash
git diff                         # Cambios en workspace vs staging
git diff --staged                # Cambios en staging vs último commit
git diff rama1 rama2             # Diferencia entre ramas
```

### Deshacer Cambios
```bash
git restore file.txt             # Deshacer cambios (no staged)
git restore --staged file.txt    # Sacar de staging
git revert commit_id             # Crear nuevo commit revirtiendo
git reset --soft HEAD~1          # Deshacer commit, mantener cambios
git reset --hard HEAD~1          # Deshacer commit, perder cambios
git clean -fd                    # Limpiar archivos no rastreados
```

## 7. Repositorio Remoto

### Configurar Remoto
```bash
git remote -v                    # Ver remotos
git remote add origin https://github.com/user/repo.git
git remote remove origin
git remote set-url origin https://nueva-url.git
```

### Push y Pull
```bash
git push origin main             # Enviar rama main
git push origin rama --force     # Forzar push (cuidado!)
git pull origin main             # Descargar y fusionar
git fetch origin                 # Solo descargar (sin fusionar)
git pull --rebase                # Pull con rebase
```

## 8. Etiquetas (Tags)

### Crear Etiquetas
```bash
git tag v1.0                     # Etiqueta ligera
git tag -a v1.0 -m "Version 1.0"  # Etiqueta anotada
git tag -l                       # Listar etiquetas
```

### Enviar Etiquetas
```bash
git push origin v1.0             # Enviar etiqueta específica
git push origin --tags           # Enviar todas etiquetas
```

## 9. Stash - Guardar Cambios Temporalmente

```bash
git stash                        # Guardar cambios temporalmente
git stash list                   # Ver stashes guardados
git stash pop                    # Recuperar último stash
git stash apply stash@{0}        # Aplicar stash sin eliminarlo
git stash drop stash@{0}         # Eliminar stash
```

## 10. Búsqueda y Debugging

### Bisect - Buscar Commit Problemático
```bash
git bisect start
git bisect bad HEAD              # HEAD es malo
git bisect good v1.0             # v1.0 era bueno
# Git te hace checkout en medio, pruebas, luego:
git bisect good                  # O git bisect bad
# Continúa hasta encontrar el commit malo
git bisect reset                 # Terminar bisect
```

### Blame - Ver Quién Cambió Qué
```bash
git blame archivo.txt            # Ver autor de cada línea
git blame -L 10,20 archivo.txt   # Líneas 10-20
```

### Log Avanzado
```bash
git log --oneline --graph --all --decorate  # Gráfico bonito
git log --author="nombre"        # Cambios de autor
git log --after="2024-01-01"     # Cambios después de fecha
```

## 11. Flujo de Trabajo Común

```bash
# Clonar repo
git clone https://github.com/user/repo.git
cd repo

# Crear rama para feature
git checkout -b feature/nueva-funcionalidad

# Hacer cambios y commits
git add .
git commit -m "Implementar nueva funcionalidad"

# Actualizar desde main
git fetch origin
git rebase origin/main

# Enviar rama
git push origin feature/nueva-funcionalidad

# Crear Pull Request en GitHub
# (esperar revisión y aprobación)

# Después de merge en GitHub, limpiar localmente
git checkout main
git pull origin main
git branch -d feature/nueva-funcionalidad
```

## 12. Configuración de .gitignore

```bash
# .gitignore
*.log
*.tmp
__pycache__/
node_modules/
.env
*.pyc
.DS_Store
dist/
build/
```

---
**Nivel**: Básico
**Tiempo estimado de estudio**: 2-3 horas
