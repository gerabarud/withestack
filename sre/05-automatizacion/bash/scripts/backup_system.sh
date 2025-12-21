#!/bin/bash
# backup_system.sh - Sistema de backup con rotación
# Uso: ./backup_system.sh /path/to/source /path/to/backup

set -e  # Exit on error
set -u  # Exit on undefined variable

# Colors para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuración
SOURCE_DIR="${1:-/var/www}"
BACKUP_DIR="${2:-/backup}"
RETENTION_DAYS=7
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_${DATE}.tar.gz"
LOG_FILE="${BACKUP_DIR}/backup.log"

# Funciones
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$LOG_FILE"
    exit 1
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1" | tee -a "$LOG_FILE"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1" | tee -a "$LOG_FILE"
}

# Verificar que directorios existen
check_directories() {
    log "Verificando directorios..."
    
    if [[ ! -d "$SOURCE_DIR" ]]; then
        error "Directorio fuente no existe: $SOURCE_DIR"
    fi
    
    if [[ ! -d "$BACKUP_DIR" ]]; then
        log "Creando directorio de backup: $BACKUP_DIR"
        mkdir -p "$BACKUP_DIR" || error "No se pudo crear directorio de backup"
    fi
}

# Crear backup
create_backup() {
    log "Iniciando backup de $SOURCE_DIR..."
    
    cd "$BACKUP_DIR" || error "No se pudo acceder al directorio de backup"
    
    # Crear tar.gz con progreso
    tar -czf "$BACKUP_FILE" -C "$(dirname "$SOURCE_DIR")" "$(basename "$SOURCE_DIR")" 2>&1 | \
        tee -a "$LOG_FILE" || error "Falló la creación del backup"
    
    # Verificar que el archivo fue creado
    if [[ -f "$BACKUP_FILE" ]]; then
        SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
        success "Backup creado: $BACKUP_FILE (Tamaño: $SIZE)"
    else
        error "El archivo de backup no fue creado"
    fi
}

# Rotar backups antiguos
rotate_backups() {
    log "Rotando backups antiguos (> $RETENTION_DAYS días)..."
    
    DELETED=0
    while IFS= read -r -d '' file; do
        rm -f "$file"
        log "Eliminado: $(basename "$file")"
        ((DELETED++))
    done < <(find "$BACKUP_DIR" -name "backup_*.tar.gz" -type f -mtime +$RETENTION_DAYS -print0)
    
    if [[ $DELETED -eq 0 ]]; then
        log "No hay backups antiguos para eliminar"
    else
        success "Se eliminaron $DELETED backups antiguos"
    fi
}

# Verificar integridad del backup
verify_backup() {
    log "Verificando integridad del backup..."
    
    if tar -tzf "$BACKUP_FILE" > /dev/null 2>&1; then
        success "Backup verificado correctamente"
    else
        error "El backup está corrupto"
    fi
}

# Estadísticas
show_stats() {
    log "=== Estadísticas de Backup ==="
    log "Total de backups: $(find "$BACKUP_DIR" -name "backup_*.tar.gz" | wc -l)"
    log "Espacio usado: $(du -sh "$BACKUP_DIR" | cut -f1)"
    log "Último backup: $BACKUP_FILE"
}

# Main
main() {
    log "========================================="
    log "Iniciando script de backup"
    log "========================================="
    
    check_directories
    create_backup
    verify_backup
    rotate_backups
    show_stats
    
    log "========================================="
    log "Backup completado exitosamente"
    log "========================================="
}

# Trap para cleanup en caso de error
cleanup() {
    if [[ $? -ne 0 ]]; then
        error "El script terminó con errores"
    fi
}

trap cleanup EXIT

# Ejecutar
main "$@"
