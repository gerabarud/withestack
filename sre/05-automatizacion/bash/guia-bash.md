# 📝 Bash Scripting - Guía Rápida para SRE

## 🎯 Conceptos Básicos

### Shebang y Ejecución
```bash
#!/bin/bash
# Primera línea del script

# Hacer ejecutable
chmod +x script.sh

# Ejecutar
./script.sh
```

### Variables
```bash
# Asignar variable (sin espacios alrededor de =)
NAME="Juan"
AGE=25

# Usar variable
echo "Hola $NAME"
echo "Edad: ${AGE}"

# Variables de entorno
export MY_VAR="value"

# Argumentos del script
echo "Script: $0"
echo "Primer arg: $1"
echo "Segundo arg: $2"
echo "Todos los args: $@"
echo "Cantidad de args: $#"
```

### Condicionales
```bash
# If básico
if [ "$NAME" = "Juan" ]; then
    echo "Es Juan"
fi

# If-else
if [ $AGE -gt 18 ]; then
    echo "Mayor de edad"
else
    echo "Menor de edad"
fi

# If-elif-else
if [ $AGE -lt 18 ]; then
    echo "Menor"
elif [ $AGE -lt 65 ]; then
    echo "Adulto"
else
    echo "Senior"
fi

# Comparadores numéricos
# -eq  igual
# -ne  no igual
# -gt  mayor que
# -ge  mayor o igual
# -lt  menor que
# -le  menor o igual

# Comparadores de strings
# =    igual
# !=   no igual
# -z   string vacío
# -n   string no vacío

# Operadores lógicos
if [ $AGE -gt 18 ] && [ $AGE -lt 65 ]; then
    echo "Adulto trabajador"
fi

if [ "$NAME" = "Juan" ] || [ "$NAME" = "María" ]; then
    echo "Nombre válido"
fi

# Test de archivos
if [ -f "/etc/passwd" ]; then
    echo "Archivo existe"
fi

if [ -d "/var/log" ]; then
    echo "Directorio existe"
fi

# Otros tests
# -e  existe
# -f  es archivo regular
# -d  es directorio
# -r  es legible
# -w  es escribible
# -x  es ejecutable
# -s  archivo no vacío
```

### Loops
```bash
# For loop
for i in 1 2 3 4 5; do
    echo "Número: $i"
done

# For con rango
for i in {1..10}; do
    echo $i
done

# For con archivos
for file in *.txt; do
    echo "Procesando: $file"
done

# While loop
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    ((count++))
done

# Until loop
count=0
until [ $count -ge 5 ]; do
    echo "Count: $count"
    ((count++))
done

# Leer archivo línea por línea
while IFS= read -r line; do
    echo "Línea: $line"
done < file.txt
```

### Funciones
```bash
# Definir función
greet() {
    local name=$1
    echo "Hola, $name"
}

# Llamar función
greet "Juan"

# Función con return
is_root() {
    if [ "$EUID" -eq 0 ]; then
        return 0  # true
    else
        return 1  # false
    fi
}

# Usar return value
if is_root; then
    echo "Eres root"
else
    echo "No eres root"
fi

# Función que devuelve string (via echo)
get_hostname() {
    echo "$(hostname)"
}

result=$(get_hostname)
echo "Hostname: $result"
```

## 🛠️ Patterns Útiles

### Template Básico de Script
```bash
#!/bin/bash
set -e  # Exit on error
set -u  # Exit on undefined variable
set -o pipefail  # Exit on pipe failure

# Variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="/var/log/$(basename "$0" .sh).log"

# Funciones
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

error() {
    echo "[ERROR] $*" >&2
    exit 1
}

# Main
main() {
    log "Script iniciado"
    
    # Tu código aquí
    
    log "Script completado"
}

# Trap para cleanup
cleanup() {
    log "Cleanup ejecutado"
}

trap cleanup EXIT

# Ejecutar
main "$@"
```

### Parse Arguments
```bash
#!/bin/bash

usage() {
    cat << EOF
Uso: $0 [opciones]

Opciones:
    -h, --help          Mostrar ayuda
    -v, --verbose       Modo verbose
    -f, --file FILE     Archivo de entrada
    -o, --output DIR    Directorio de salida
EOF
}

# Defaults
VERBOSE=0
INPUT_FILE=""
OUTPUT_DIR="."

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            exit 0
            ;;
        -v|--verbose)
            VERBOSE=1
            shift
            ;;
        -f|--file)
            INPUT_FILE="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        *)
            echo "Opción desconocida: $1"
            usage
            exit 1
            ;;
    esac
done

# Validar
if [ -z "$INPUT_FILE" ]; then
    echo "Error: --file es requerido"
    usage
    exit 1
fi

if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: archivo no existe: $INPUT_FILE"
    exit 1
fi

echo "Input: $INPUT_FILE"
echo "Output: $OUTPUT_DIR"
echo "Verbose: $VERBOSE"
```

### Procesamiento de Texto
```bash
# Leer CSV
while IFS=',' read -r col1 col2 col3; do
    echo "Col1: $col1, Col2: $col2, Col3: $col3"
done < data.csv

# Procesar JSON con jq
API_RESPONSE=$(curl -s https://api.example.com/data)
NAME=$(echo "$API_RESPONSE" | jq -r '.name')
AGE=$(echo "$API_RESPONSE" | jq -r '.age')

# Array
files=("file1.txt" "file2.txt" "file3.txt")
for file in "${files[@]}"; do
    echo "$file"
done

# Array asociativo (dict)
declare -A config
config[host]="localhost"
config[port]="8080"
echo "Host: ${config[host]}"
```

### Parallel Execution
```bash
# Ejecutar comandos en paralelo
process_file() {
    local file=$1
    echo "Procesando $file..."
    sleep 2
    echo "Completado $file"
}

export -f process_file

# Usar GNU parallel (si está instalado)
ls *.txt | parallel process_file

# O con xargs
ls *.txt | xargs -P 4 -I {} bash -c 'process_file "{}"'

# O manualmente con &
for file in *.txt; do
    process_file "$file" &
done
wait  # Esperar a que todos terminen
```

## ✅ Tips y Tricks

### Colores en Output
```bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${RED}Error${NC}"
echo -e "${GREEN}Success${NC}"
echo -e "${YELLOW}Warning${NC}"
```

### Progress Bar
```bash
show_progress() {
    local current=$1
    local total=$2
    local width=50
    
    local percent=$((current * 100 / total))
    local completed=$((width * current / total))
    
    printf "\rProgress: ["
    printf "%${completed}s" | tr ' ' '='
    printf "%$((width - completed))s" | tr ' ' '-'
    printf "] %d%%" $percent
}

# Uso
for i in {1..100}; do
    show_progress $i 100
    sleep 0.05
done
echo
```

### Timeout para Comandos
```bash
# Con timeout command
timeout 10s curl https://example.com

# Manual
command &
PID=$!
sleep 10
kill -0 $PID 2>/dev/null && kill $PID
```

## 🎓 Ejercicios

1. Script que haga backup de un directorio con timestamp
2. Script que monitoree uso de CPU y alerte si >80%
3. Script que procese logs y cuente errores por hora
4. Script que verifique si servicios están running
5. Script que limpie archivos viejos (>30 días)
