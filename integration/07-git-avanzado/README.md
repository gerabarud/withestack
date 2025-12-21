# 🔧 Git Avanzado - Control de Versiones

## 📚 Índice
1. [Comandos Básicos Revisión](#comandos-básicos-revisión)
2. [Branching Avanzado](#branching-avanzado)
3. [Rebase](#rebase)
4. [Cherry-pick](#cherry-pick)
5. [Stash](#stash)
6. [Reset y Revert](#reset-y-revert)
7. [GitOps Workflows](#gitops-workflows)

---

## 1. Comandos Básicos Revisión

```bash
# Configuración inicial
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
git config --list

# Inicializar repositorio
git init
git clone https://github.com/user/repo.git

# Flujo básico
git add file.txt                    # Agregar archivo
git add .                           # Agregar todos
git commit -m "Mensaje"             # Commit
git status                          # Ver estado
git log                             # Ver historial
git log --oneline --graph           # Log compacto

# Remoto
git remote add origin URL
git remote -v
git push origin main
git pull origin main
git fetch origin
```

---

## 2. Branching Avanzado

### 🌿 Crear y Gestionar Branches

```bash
# Crear branch
git branch feature-login           # Crear
git checkout feature-login         # Cambiar
git checkout -b feature-signup     # Crear y cambiar

# Listar branches
git branch                         # Locales
git branch -r                      # Remotas
git branch -a                      # Todas
git branch -v                      # Con último commit

# Eliminar branch
git branch -d feature-login        # Eliminar (si merged)
git branch -D feature-login        # Forzar eliminación
git push origin --delete feature-login  # Eliminar remota

# Renombrar branch
git branch -m old-name new-name
```

### 🔀 Merge Strategies

```bash
# Fast-forward merge (default si es posible)
git checkout main
git merge feature-branch

# No fast-forward (siempre crea merge commit)
git merge --no-ff feature-branch

# Squash (combina commits en uno)
git merge --squash feature-branch
git commit -m "Feature: Add login"

# Merge con estrategia específica
git merge -X theirs feature-branch  # Preferir cambios de feature
git merge -X ours feature-branch    # Preferir cambios de main
```

### ⚔️ Resolver Conflictos

```bash
# Ver conflictos
git status
git diff

# Marcar conflicto resuelto
git add file.txt
git commit

# Abortar merge
git merge --abort

# Ver archivos en conflicto
git diff --name-only --diff-filter=U

# Herramientas de merge
git mergetool
```

---

## 3. Rebase

El rebase reescribe el historial aplicando commits sobre otra base.

### 🔄 Rebase Básico

```bash
# Rebase sobre main
git checkout feature-branch
git rebase main

# O en un comando
git rebase main feature-branch

# Si hay conflictos:
# 1. Resolver conflictos
# 2. git add <files>
# 3. git rebase --continue

# Abortar rebase
git rebase --abort

# Saltar commit conflictivo
git rebase --skip
```

**Antes del rebase:**
```
      C---D feature
     /
A---B main
```

**Después del rebase:**
```
          C'--D' feature
         /
A---B main
```

### 🎨 Interactive Rebase

```bash
# Rebase interactivo de últimos 3 commits
git rebase -i HEAD~3
git rebase -i <commit-hash>

# Opciones en editor:
# pick   = usar commit
# reword = cambiar mensaje
# edit   = editar commit
# squash = combinar con anterior
# fixup  = como squash pero descarta mensaje
# drop   = eliminar commit
```

**Ejemplo:**
```bash
pick a1b2c3d Add feature
pick e4f5g6h Fix typo
pick i7j8k9l Update docs

# Cambiar a:
pick a1b2c3d Add feature
squash e4f5g6h Fix typo  # Combinar con anterior
reword i7j8k9l Update docs  # Cambiar mensaje
```

### 📊 Rebase vs Merge

| Aspecto | Rebase | Merge |
|---------|--------|-------|
| **Historial** | Lineal, limpio | Con branches |
| **Conflictos** | Por cada commit | Una vez |
| **Uso** | Features privadas | Trabajo colaborativo |
| **Regla** | ⚠️ NO rebase en ramas públicas | ✅ Seguro siempre |

---

## 4. Cherry-pick

Cherry-pick aplica commits específicos de una rama a otra.

```bash
# Cherry-pick un commit
git cherry-pick <commit-hash>

# Cherry-pick múltiples commits
git cherry-pick <hash1> <hash2>

# Cherry-pick rango de commits
git cherry-pick <hash1>..<hash2>

# Sin hacer commit automático
git cherry-pick -n <hash>  # --no-commit

# Editar mensaje
git cherry-pick -e <hash>  # --edit

# Si hay conflictos:
# 1. Resolver
# 2. git add <files>
# 3. git cherry-pick --continue

# Abortar
git cherry-pick --abort
```

**Ejemplo de uso:**
```bash
# Tienes un bugfix en feature-branch que necesitas en main

git checkout main
git cherry-pick abc123  # Hash del commit con el bugfix
```

---

## 5. Stash

Stash guarda temporalmente cambios sin commitear.

```bash
# Guardar cambios
git stash
git stash save "WIP: working on feature"

# Listar stashes
git stash list
# stash@{0}: WIP: working on feature
# stash@{1}: On main: trying something

# Ver contenido de stash
git stash show
git stash show -p stash@{0}  # Ver diff

# Aplicar stash
git stash apply              # Aplica último, mantiene stash
git stash apply stash@{1}    # Aplica específico
git stash pop                # Aplica y elimina

# Eliminar stash
git stash drop stash@{0}
git stash clear              # Eliminar todos

# Crear branch desde stash
git stash branch new-branch stash@{0}

# Stash con untracked files
git stash -u
git stash --include-untracked

# Stash todo (incluso ignored)
git stash -a
git stash --all
```

---

## 6. Reset y Revert

### ⏪ Git Reset

Mueve HEAD y opcionalmente modifica staging y working directory.

```bash
# Soft reset (solo mueve HEAD)
git reset --soft HEAD~1
# Commits deshace pero cambios quedan staged

# Mixed reset (default - mueve HEAD y unstage)
git reset HEAD~1
git reset --mixed HEAD~1
# Commits deshace, cambios quedan en working directory

# Hard reset (mueve HEAD, limpia staging y working)
git reset --hard HEAD~1
# ⚠️ PELIGRO: Elimina cambios permanentemente

# Reset a commit específico
git reset --hard abc123

# Reset archivo específico
git reset HEAD file.txt
git reset --hard HEAD file.txt
```

**Visualización:**
```
--soft:  HEAD → staged → working
--mixed: HEAD → unstaged → working
--hard:  HEAD (todo eliminado)
```

### ↩️ Git Revert

Crea un nuevo commit que deshace cambios (seguro para ramas públicas).

```bash
# Revert último commit
git revert HEAD

# Revert commit específico
git revert abc123

# Revert sin commit automático
git revert -n HEAD

# Revert rango de commits
git revert HEAD~3..HEAD

# Revert merge commit
git revert -m 1 <merge-commit-hash>
```

**Reset vs Revert:**
- **Reset**: Reescribe historial (solo ramas privadas)
- **Revert**: Crea nuevo commit (seguro para públicas)

---

## 7. GitOps Workflows

### 🌊 Git Flow

```bash
# Branches principales:
# - main: producción
# - develop: desarrollo

# Feature branches
git checkout -b feature/login develop
# ... desarrollo ...
git checkout develop
git merge --no-ff feature/login
git branch -d feature/login

# Release branches
git checkout -b release/1.0.0 develop
# ... preparar release ...
git checkout main
git merge --no-ff release/1.0.0
git tag -a 1.0.0
git checkout develop
git merge --no-ff release/1.0.0
git branch -d release/1.0.0

# Hotfix branches
git checkout -b hotfix/1.0.1 main
# ... fix crítico ...
git checkout main
git merge --no-ff hotfix/1.0.1
git tag -a 1.0.1
git checkout develop
git merge --no-ff hotfix/1.0.1
git branch -d hotfix/1.0.1
```

### 🚀 GitHub Flow (más simple)

```bash
# 1. Crear branch desde main
git checkout -b feature/new-feature main

# 2. Commits
git add .
git commit -m "Add feature"
git push origin feature/new-feature

# 3. Pull Request en GitHub

# 4. Merge a main (squash or merge commit)

# 5. Delete branch
git push origin --delete feature/new-feature
git branch -d feature/new-feature
```

### 📋 Convenciones de Commits

```bash
# Conventional Commits
<type>[optional scope]: <description>

[optional body]

[optional footer]

# Tipos:
feat:     nueva funcionalidad
fix:      corrección de bug
docs:     documentación
style:    formato, no afecta código
refactor: refactorización
test:     añadir tests
chore:    tareas de mantenimiento

# Ejemplos:
git commit -m "feat: add user authentication"
git commit -m "fix: resolve login timeout issue"
git commit -m "docs: update API documentation"
git commit -m "refactor: simplify database queries"
```

---

## 🔍 Comandos Avanzados Útiles

```bash
# Log avanzado
git log --graph --oneline --all
git log --author="John" --since="2 weeks ago"
git log --grep="bug" --oneline
git log -p file.txt  # Ver cambios en archivo

# Diff avanzado
git diff HEAD~2 HEAD
git diff main..feature-branch
git diff --stat
git diff --name-only

# Blame (quién modificó cada línea)
git blame file.txt
git blame -L 10,20 file.txt

# Bisect (encontrar commit que introdujo bug)
git bisect start
git bisect bad                    # Current commit is bad
git bisect good v1.0              # v1.0 is good
# Git hace checkout automático, pruebas, marcar:
git bisect good  # o git bisect bad
# Repetir hasta encontrar
git bisect reset

# Reflog (historial de HEAD)
git reflog
git reset --hard HEAD@{2}  # Recuperar commit "perdido"

# Tags
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"
git tag -l "v1.*"
git push origin v1.0.0
git push origin --tags

# Clean (eliminar untracked files)
git clean -n                      # Dry run
git clean -f                      # Eliminar archivos
git clean -fd                     # Archivos y directorios

# Submodules
git submodule add URL path
git submodule update --init --recursive
git submodule update --remote

# Worktrees (múltiples working directories)
git worktree add ../hotfix main
git worktree list
git worktree remove ../hotfix
```

---

## 🐛 Troubleshooting

```bash
# Deshacer último commit (sin perder cambios)
git reset --soft HEAD~1

# Cambiar mensaje del último commit
git commit --amend -m "New message"

# Añadir archivos al último commit
git add forgotten-file.txt
git commit --amend --no-edit

# Descartar cambios locales
git checkout -- file.txt          # Archivo específico
git checkout .                    # Todos los archivos

# Recuperar archivo eliminado
git checkout HEAD file.txt

# Ver qué contiene un commit
git show <commit-hash>

# Ver archivos en commit
git show --name-only <commit-hash>

# Sincronizar con remoto
git fetch --prune                 # Limpiar refs obsoletas
git remote prune origin

# Cambiar URL de remoto
git remote set-url origin NEW_URL

# Ver configuración
git config --list
git config user.email
```

---

## 📝 .gitignore

```bash
# .gitignore - Ejemplos

# Node
node_modules/
npm-debug.log
.env

# Python
__pycache__/
*.pyc
.venv/
*.egg-info/

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Build
dist/
build/
*.log

# Secrets
*.key
*.pem
secrets.yml
```

---

## 🎓 Preguntas Típicas

1. **¿Diferencia entre merge y rebase?**
   - Merge: conserva historial, crea merge commit
   - Rebase: reescribe historial, queda lineal

2. **¿Cuándo usar cherry-pick?**
   - Aplicar commits específicos a otra rama
   - Útil para hotfixes

3. **¿Diferencia entre reset y revert?**
   - Reset: reescribe historial (privado)
   - Revert: crea commit nuevo (público)

4. **¿Para qué sirve git stash?**
   - Guardar cambios temporalmente
   - Cambiar de rama sin commit

5. **¿Qué es interactive rebase?**
   - Reescribir/reorganizar commits
   - Limpiar historial antes de merge

---

## 🔗 Recursos

- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Git Documentation](https://git-scm.com/docs)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

---

**💡 Consejo:** Practica rebase y cherry-pick en repositorio de prueba. El test evaluará estos comandos avanzados.
