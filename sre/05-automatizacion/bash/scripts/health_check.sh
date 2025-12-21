#!/bin/bash
# health_check.sh - Monitoreo de salud del sistema
# Envía alertas si detecta problemas

set -u

# Configuración
CPU_THRESHOLD=80
MEMORY_THRESHOLD=85
DISK_THRESHOLD=85
ALERT_EMAIL="admin@example.com"
LOG_FILE="/var/log/health_check.log"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Array para almacenar alertas
declare -a ALERTS

log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

alert() {
    ALERTS+=("$1")
    echo -e "${RED}[ALERT]${NC} $1" | tee -a "$LOG_FILE"
}

ok() {
    echo -e "${GREEN}[OK]${NC} $1" | tee -a "$LOG_FILE"
}

# Check CPU usage
check_cpu() {
    log "Verificando uso de CPU..."
    
    # Obtener CPU usage (últimos 5 segundos)
    CPU_USAGE=$(top -bn2 -d 0.5 | grep "Cpu(s)" | tail -1 | awk '{print $2}' | cut -d'%' -f1)
    CPU_USAGE=${CPU_USAGE%.*}  # Truncar decimales
    
    if [[ $CPU_USAGE -gt $CPU_THRESHOLD ]]; then
        alert "CPU usage alto: ${CPU_USAGE}% (Umbral: ${CPU_THRESHOLD}%)"
        
        # Mostrar top 5 procesos
        log "Top 5 procesos por CPU:"
        ps aux --sort=-%cpu | head -6 | tee -a "$LOG_FILE"
    else
        ok "CPU usage: ${CPU_USAGE}%"
    fi
}

# Check Memory usage
check_memory() {
    log "Verificando uso de memoria..."
    
    # Obtener memoria usada en %
    MEMORY_USAGE=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100)}')
    
    if [[ $MEMORY_USAGE -gt $MEMORY_THRESHOLD ]]; then
        alert "Memoria alta: ${MEMORY_USAGE}% (Umbral: ${MEMORY_THRESHOLD}%)"
        
        # Mostrar top 5 procesos
        log "Top 5 procesos por memoria:"
        ps aux --sort=-%mem | head -6 | tee -a "$LOG_FILE"
    else
        ok "Memoria: ${MEMORY_USAGE}%"
    fi
}

# Check Disk usage
check_disk() {
    log "Verificando uso de disco..."
    
    while read -r line; do
        USAGE=$(echo "$line" | awk '{print $5}' | sed 's/%//')
        MOUNT=$(echo "$line" | awk '{print $6}')
        
        if [[ $USAGE -gt $DISK_THRESHOLD ]]; then
            alert "Disco lleno en ${MOUNT}: ${USAGE}% (Umbral: ${DISK_THRESHOLD}%)"
        else
            ok "Disco ${MOUNT}: ${USAGE}%"
        fi
    done < <(df -h | grep -E '^/dev/' | grep -v '/boot')
}

# Check critical services
check_services() {
    log "Verificando servicios críticos..."
    
    SERVICES=("docker" "nginx" "sshd")
    
    for service in "${SERVICES[@]}"; do
        if systemctl is-active --quiet "$service"; then
            ok "Servicio $service: running"
        else
            alert "Servicio $service: NOT running"
        fi
    done
}

# Check load average
check_load() {
    log "Verificando load average..."
    
    LOAD=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}' | sed 's/,//')
    CORES=$(nproc)
    
    # Load threshold = 2 * cores
    LOAD_THRESHOLD=$((CORES * 2))
    
    # Comparar floats
    if (( $(echo "$LOAD > $LOAD_THRESHOLD" | bc -l) )); then
        alert "Load average alto: $LOAD (Cores: $CORES)"
    else
        ok "Load average: $LOAD (Cores: $CORES)"
    fi
}

# Check network connectivity
check_network() {
    log "Verificando conectividad de red..."
    
    HOSTS=("8.8.8.8" "google.com")
    
    for host in "${HOSTS[@]}"; do
        if ping -c 1 -W 2 "$host" > /dev/null 2>&1; then
            ok "Ping a $host: OK"
        else
            alert "No hay conectividad a $host"
        fi
    done
}

# Send alerts
send_alerts() {
    if [[ ${#ALERTS[@]} -eq 0 ]]; then
        log "No hay alertas que enviar"
        return
    fi
    
    log "Enviando ${#ALERTS[@]} alertas..."
    
    # Construir mensaje
    MESSAGE="ALERTAS DEL SISTEMA $(hostname)\n"
    MESSAGE+="Fecha: $(date)\n\n"
    
    for alert in "${ALERTS[@]}"; do
        MESSAGE+="- $alert\n"
    done
    
    # Enviar email (requiere mailx o sendmail configurado)
    echo -e "$MESSAGE" | mail -s "Health Check Alerts - $(hostname)" "$ALERT_EMAIL" 2>/dev/null || \
        log "No se pudo enviar email. Verifique configuración de mail."
    
    # También enviar a syslog
    echo "$MESSAGE" | logger -t health_check
}

# Generate report
generate_report() {
    log "========================================="
    log "Health Check Report - $(hostname)"
    log "========================================="
    log "Uptime: $(uptime -p)"
    log "CPU Cores: $(nproc)"
    log "Total Memory: $(free -h | awk '/^Mem:/ {print $2}')"
    log "Total Alerts: ${#ALERTS[@]}"
    log "========================================="
}

# Main
main() {
    log "Iniciando health check..."
    
    check_cpu
    check_memory
    check_disk
    check_services
    check_load
    check_network
    
    generate_report
    
    if [[ ${#ALERTS[@]} -gt 0 ]]; then
        send_alerts
        exit 1
    else
        log "Health check completado sin problemas"
        exit 0
    fi
}

main "$@"
