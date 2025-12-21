# 🐧 Linux Avanzado - Guía de Estudio

## 📚 Índice
1. [Comandos Básicos y Avanzados](#comandos-básicos-y-avanzados)
2. [Gestión de Archivos y Siastemas](#gestión-de-archivos-y-sistemas)
3. [Configuración de Red](#configuración-de-red)
4. [Bash Scripting](#bash-scripting)
5. [Ejercicios Prácticos](#ejercicios-prácticos)

---

## 1. Comandos Básicos y Avanzados

### 🔍 Navegación y Búsqueda

```bash
# Búsqueda de archivos
find /path -name "*.log" -mtime -7  # Archivos .log modificados en últimos 7 días
find / -type f -size +100M           # Archivos mayores a 100MB
find . -type f -perm 644             # Archivos con permisos específicos

# Búsqueda de contenido
grep -r "error" /var/log/            # Búsqueda recursiva
grep -i "warning" file.log           # Case insensitive
grep -E "error|warning" file.log     # Expresiones regulares
grep -c "success" file.log           # Contar ocurrencias

# Búsqueda combinada
find . -name "*.conf" -exec grep -l "database" {} \;
```

### 📊 Monitoreo de Sistema

```bash
# Procesos
ps aux | grep nginx                  # Ver procesos nginx
top -p $(pgrep nginx | tr '\n' ',')  # Top de procesos específicos
htop                                 # Versión mejorada de top
pstree -p                           # Árbol de procesos

# Memoria
free -h                             # Uso de memoria
vmstat 1                            # Estadísticas de memoria cada 1 seg
cat /proc/meminfo                   # Información detallada

# Disco
df -h                               # Espacio en discos
du -sh /var/*                       # Tamaño de directorios
du -h --max-depth=1 /home           # Tamaño con profundidad
iostat -x 1                         # I/O stats cada 1 seg

# CPU
mpstat -P ALL 1                     # Stats por CPU
sar -u 1 5                          # CPU usage 5 veces cada 1 seg
lscpu                               # Información de CPUs
```

### 🔧 Gestión de Servicios (systemd)

```bash
# Control de servicios
systemctl start nginx               # Iniciar servicio
systemctl stop nginx                # Detener servicio
systemctl restart nginx             # Reiniciar servicio
systemctl reload nginx              # Recargar configuración
systemctl enable nginx              # Habilitar en boot
systemctl disable nginx             # Deshabilitar en boot

# Estado y logs
systemctl status nginx              # Estado del servicio
systemctl is-active nginx           # ¿Está activo?
systemctl is-enabled nginx          # ¿Está habilitado?
journalctl -u nginx                 # Logs del servicio
journalctl -u nginx -f              # Seguir logs en tiempo real
journalctl -u nginx --since "1 hour ago"  # Logs de última hora
```

### 📝 Manipulación de Texto

```bash
# AWK - Procesamiento de texto
awk '{print $1}' file.txt           # Imprimir primera columna
awk -F: '{print $1, $3}' /etc/passwd  # Delimiter personalizado
awk '$3 > 1000 {print $1}' /etc/passwd  # Filtrado condicional
ps aux | awk '{sum+=$3} END {print sum}'  # Sumar columnas

# SED - Editor de stream
sed 's/old/new/' file.txt           # Reemplazar primera ocurrencia
sed 's/old/new/g' file.txt          # Reemplazar todas
sed -i 's/old/new/g' file.txt       # Editar archivo in-place
sed -n '10,20p' file.txt            # Imprimir líneas 10-20
sed '/pattern/d' file.txt           # Eliminar líneas con pattern

# CUT - Extraer columnas
cut -d: -f1 /etc/passwd             # Primera columna con delimiter :
cut -c1-10 file.txt                 # Caracteres 1-10
ps aux | tr -s ' ' | cut -d' ' -f2  # PID de procesos

# SORT y UNIQ
sort file.txt                       # Ordenar líneas
sort -n numbers.txt                 # Ordenar numéricamente
sort -k2 file.txt                   # Ordenar por segunda columna
uniq file.txt                       # Eliminar duplicados consecutivos
sort file.txt | uniq -c             # Contar ocurrencias
```

---

## 2. Gestión de Archivos y Sistemas

### 📂 Permisos y Propietarios

```bash
# Permisos básicos
chmod 755 script.sh                 # rwxr-xr-x
chmod u+x script.sh                 # Añadir ejecución al owner
chmod -R 644 /var/www/html          # Recursivo
chown user:group file.txt           # Cambiar owner y grupo
chown -R www-data:www-data /var/www # Recursivo

# Permisos especiales
chmod +t /tmp                       # Sticky bit
chmod u+s /usr/bin/sudo             # SUID
chmod g+s /shared                   # SGID

# ACLs (Access Control Lists)
setfacl -m u:john:rw file.txt      # Dar permisos a usuario
getfacl file.txt                   # Ver ACLs
setfacl -R -m g:developers:rwx /project  # ACL recursivo
```

### 💾 LVM (Logical Volume Management)

```bash
# Ver información
pvs                                 # Physical volumes
vgs                                 # Volume groups
lvs                                 # Logical volumes
pvdisplay /dev/sdb1                # Info detallada de PV

# Crear LVM
pvcreate /dev/sdb1                 # Crear PV
vgcreate vg_data /dev/sdb1         # Crear VG
lvcreate -L 10G -n lv_mysql vg_data  # Crear LV de 10GB

# Extender volumen
lvextend -L +5G /dev/vg_data/lv_mysql  # Añadir 5GB
resize2fs /dev/vg_data/lv_mysql    # Extender filesystem ext4
xfs_growfs /mount/point            # Extender filesystem XFS
```

### 🗄️ Sistemas de Archivos

```bash
# Montar y desmontar
mount /dev/sdb1 /mnt/data          # Montar
umount /mnt/data                   # Desmontar
mount -a                           # Montar todo en /etc/fstab
lsblk                              # Ver dispositivos de bloque
blkid                              # Ver UUIDs de dispositivos

# /etc/fstab - Montaje persistente
# UUID=xxx /mnt/data ext4 defaults 0 2
cat /etc/fstab

# Crear filesystem
mkfs.ext4 /dev/sdb1                # Crear ext4
mkfs.xfs /dev/sdb2                 # Crear XFS
mkswap /dev/sdb3                   # Crear swap
swapon /dev/sdb3                   # Activar swap

# Verificar filesystem
fsck /dev/sdb1                     # Check filesystem
fsck -y /dev/sdb1                  # Auto-repair
xfs_repair /dev/sdb2               # Repair XFS
```

---

## 3. Configuración de Red

### 🌐 Interfaces de Red

```bash
# Ver interfaces
ip addr show                       # Ver todas las interfaces
ip link show                       # Ver estado de links
ifconfig -a                        # Alternativa (deprecated)

# Configurar IP
ip addr add 192.168.1.100/24 dev eth0
ip addr del 192.168.1.100/24 dev eth0
ip link set eth0 up                # Levantar interfaz
ip link set eth0 down              # Bajar interfaz

# Configuración persistente (Ubuntu/Debian - netplan)
cat /etc/netplan/01-network.yaml
```

Ejemplo `/etc/netplan/01-network.yaml`:
```yaml
network:
  version: 2
  ethernets:
    eth0:
      addresses:
        - 192.168.1.100/24
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
```

```bash
# Aplicar configuración netplan
netplan apply
netplan try                        # Test configuration (rollback automático)
```

### 🏷️ VLANs

```bash
# Crear VLAN
ip link add link eth0 name eth0.10 type vlan id 10
ip addr add 10.0.10.1/24 dev eth0.10
ip link set eth0.10 up

# Ver VLANs
cat /proc/net/vlan/config
ip -d link show eth0.10

# Eliminar VLAN
ip link delete eth0.10
```

Configuración persistente (netplan):
```yaml
network:
  version: 2
  vlans:
    eth0.10:
      id: 10
      link: eth0
      addresses: [10.0.10.1/24]
```

### 🔗 Bonding (Link Aggregation)

```bash
# Instalar herramienta
apt install ifenslave

# Crear bond
ip link add bond0 type bond mode 802.3ad
ip link set eth1 master bond0
ip link set eth2 master bond0
ip link set bond0 up

# Ver estado del bond
cat /proc/net/bonding/bond0
```

Configuración netplan:
```yaml
network:
  version: 2
  bonds:
    bond0:
      interfaces: [eth1, eth2]
      parameters:
        mode: 802.3ad
        mii-monitor-interval: 100
      addresses: [192.168.1.100/24]
```

**Modos de bonding:**
- `balance-rr` (0): Round-robin
- `active-backup` (1): Activo-pasivo
- `balance-xor` (2): XOR policy
- `broadcast` (3): Broadcast
- `802.3ad` (4): LACP
- `balance-tlb` (5): Adaptive transmit load balancing
- `balance-alb` (6): Adaptive load balancing

### 🛣️ Enrutamiento

```bash
# Ver tabla de ruteo
ip route show
route -n                           # Alternativa

# Añadir ruta
ip route add 10.0.0.0/8 via 192.168.1.1
ip route add default via 192.168.1.1  # Ruta por defecto

# Eliminar ruta
ip route del 10.0.0.0/8

# Habilitar IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward
sysctl -w net.ipv4.ip_forward=1    # Temporal

# Persistente
cat /etc/sysctl.conf
# net.ipv4.ip_forward=1
sysctl -p                          # Aplicar cambios
```

### 🔥 IPTables (Firewall)

```bash
# Ver reglas
iptables -L -n -v                  # Ver todas las reglas
iptables -t nat -L -n -v           # Ver reglas NAT

# Políticas por defecto
iptables -P INPUT DROP             # Denegar todo el tráfico entrante
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Permitir tráfico
iptables -A INPUT -i lo -j ACCEPT  # Permitir loopback
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT    # SSH
iptables -A INPUT -p tcp --dport 80 -j ACCEPT    # HTTP
iptables -A INPUT -p tcp --dport 443 -j ACCEPT   # HTTPS

# NAT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE  # NAT masquerade
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080

# Port forwarding
iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination 10.0.0.5:80

# Guardar reglas
iptables-save > /etc/iptables/rules.v4
netfilter-persistent save

# Restaurar reglas
iptables-restore < /etc/iptables/rules.v4
```

### 🔍 Diagnóstico de Red

```bash
# Conectividad
ping -c 4 8.8.8.8                  # Ping 4 veces
traceroute google.com              # Trazar ruta
mtr google.com                     # MTR (mejor que traceroute)

# Puertos y conexiones
netstat -tulpn                     # Ver puertos abiertos
ss -tulpn                          # Alternativa moderna
lsof -i :80                        # Ver qué usa el puerto 80
nmap localhost                     # Escanear puertos

# DNS
dig google.com                     # Consulta DNS
nslookup google.com
host google.com

# Tráfico de red
tcpdump -i eth0                    # Capturar tráfico
tcpdump -i eth0 port 80            # Solo puerto 80
tcpdump -i eth0 -w capture.pcap    # Guardar a archivo
iftop                              # Ver tráfico en tiempo real
nethogs                            # Ver tráfico por proceso

# ARP
arp -a                             # Ver tabla ARP
ip neigh show                      # Alternativa moderna
arping 192.168.1.1                 # Ping ARP
```

---

## 4. Bash Scripting

### 📜 Script Básico

```bash
#!/bin/bash

# Variables
NAME="Cloud Engineer"
AGE=30
READONLY_VAR="Cannot change"

# Imprimir
echo "Hello, $NAME"
echo "Age: ${AGE}"

# Entrada del usuario
read -p "Enter your name: " username
echo "Welcome, $username"

# Arrays
FRUITS=("Apple" "Banana" "Orange")
echo "First fruit: ${FRUITS[0]}"
echo "All fruits: ${FRUITS[@]}"
echo "Number of fruits: ${#FRUITS[@]}"

# Comandos
CURRENT_DIR=$(pwd)
FILE_COUNT=$(ls -1 | wc -l)
echo "Files in $CURRENT_DIR: $FILE_COUNT"
```

### 🔀 Control de Flujo

```bash
#!/bin/bash

# If-else
if [ $AGE -gt 18 ]; then
    echo "Adult"
elif [ $AGE -eq 18 ]; then
    echo "Just turned adult"
else
    echo "Minor"
fi

# Test de archivos
if [ -f "/etc/passwd" ]; then
    echo "File exists"
fi

if [ -d "/tmp" ]; then
    echo "Directory exists"
fi

# Operadores de comparación
# -eq: igual
# -ne: no igual
# -gt: mayor que
# -lt: menor que
# -ge: mayor o igual
# -le: menor o igual

# Operadores de archivos
# -f: es archivo regular
# -d: es directorio
# -e: existe
# -r: tiene permisos de lectura
# -w: tiene permisos de escritura
# -x: tiene permisos de ejecución

# Case
case $1 in
    start)
        echo "Starting service..."
        ;;
    stop)
        echo "Stopping service..."
        ;;
    restart)
        echo "Restarting service..."
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac
```

### 🔁 Loops

```bash
#!/bin/bash

# For loop
for i in {1..5}; do
    echo "Number: $i"
done

# For con archivos
for file in /var/log/*.log; do
    echo "Processing $file"
    grep "error" "$file"
done

# For con array
SERVERS=("web1" "web2" "db1")
for server in "${SERVERS[@]}"; do
    ping -c 1 $server
done

# While loop
COUNTER=0
while [ $COUNTER -lt 5 ]; do
    echo "Counter: $COUNTER"
    ((COUNTER++))
done

# Until loop
COUNTER=0
until [ $COUNTER -ge 5 ]; do
    echo "Counter: $COUNTER"
    ((COUNTER++))
done

# Leer archivo línea por línea
while IFS= read -r line; do
    echo "Line: $line"
done < /etc/passwd
```

### 🔧 Funciones

```bash
#!/bin/bash

# Definir función
greet() {
    echo "Hello, $1!"
}

# Llamar función
greet "John"

# Función con retorno
add() {
    local sum=$(($1 + $2))
    echo $sum
}

result=$(add 5 3)
echo "Result: $result"

# Función con múltiples parámetros
deploy_app() {
    local app_name=$1
    local environment=$2
    local version=$3
    
    echo "Deploying $app_name v$version to $environment"
    # Deployment logic here
}

deploy_app "myapp" "production" "1.2.3"
```

### 🎯 Script Avanzado - Deployment

```bash
#!/bin/bash
set -e  # Exit on error
set -u  # Exit on undefined variable

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
    exit 1
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Check if running as root
check_root() {
    if [ "$EUID" -ne 0 ]; then
        error "This script must be run as root"
    fi
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Backup function
backup_config() {
    local config_file=$1
    local backup_dir="/backup/$(date +%Y%m%d)"
    
    mkdir -p "$backup_dir"
    
    if [ -f "$config_file" ]; then
        cp "$config_file" "$backup_dir/"
        log "Backup created: $backup_dir/$(basename $config_file)"
    else
        warning "Config file not found: $config_file"
    fi
}

# Deploy application
deploy() {
    local app_name=$1
    local version=$2
    
    log "Starting deployment of $app_name v$version"
    
    # Pre-deployment checks
    if ! command_exists docker; then
        error "Docker is not installed"
    fi
    
    # Backup
    backup_config "/etc/$app_name/config.yaml"
    
    # Pull image
    log "Pulling Docker image..."
    docker pull "$app_name:$version" || error "Failed to pull image"
    
    # Stop old container
    log "Stopping old container..."
    docker stop "$app_name" 2>/dev/null || true
    docker rm "$app_name" 2>/dev/null || true
    
    # Start new container
    log "Starting new container..."
    docker run -d \
        --name "$app_name" \
        --restart unless-stopped \
        -p 8080:8080 \
        "$app_name:$version" || error "Failed to start container"
    
    # Health check
    log "Performing health check..."
    sleep 5
    
    if ! curl -f http://localhost:8080/health >/dev/null 2>&1; then
        error "Health check failed"
    fi
    
    log "Deployment completed successfully!"
}

# Main
main() {
    if [ $# -lt 2 ]; then
        echo "Usage: $0 <app_name> <version>"
        exit 1
    fi
    
    check_root
    deploy "$1" "$2"
}

main "$@"
```

---

## 5. Ejercicios Prácticos

### 🎯 Ejercicio 1: Monitoreo de Sistema

Crea un script que:
1. Muestre uso de CPU, memoria y disco
2. Identifique los 5 procesos que más consumen CPU
3. Envíe alerta si el disco está >80% lleno

```bash
#!/bin/bash
# Ver solución en: scripts/monitor.sh
```

### 🎯 Ejercicio 2: Configuración de Red

1. Configura una interfaz con IP estática
2. Crea una VLAN 100 en eth0
3. Configura bonding con 2 interfaces
4. Añade reglas de iptables para permitir solo SSH y HTTP

### 🎯 Ejercicio 3: Automatización

Crea un script que:
1. Haga backup de /etc cada día
2. Rote logs antiguos (>7 días)
3. Limpie archivos temporales
4. Envíe reporte por email

---

## 📝 Comandos Esenciales para Memorizar

```bash
# Top 50 comandos para el test
ls, cd, pwd, mkdir, rm, cp, mv, cat, less, head, tail
grep, find, locate, which, whereis
ps, top, htop, kill, killall, pkill
df, du, mount, umount, lsblk
chmod, chown, chgrp, umask
systemctl, service, journalctl
ip, ifconfig, netstat, ss, ping, traceroute
iptables, route, arp
tar, gzip, zip, unzip
ssh, scp, rsync
vi/vim, nano
apt/yum/dnf, dpkg, rpm
cron, at, systemd-timers
sed, awk, cut, sort, uniq, tr
```

---

## 🎓 Preguntas de Test Típicas

1. **¿Cómo verificas qué proceso está usando el puerto 8080?**
   ```bash
   lsof -i :8080
   # o
   ss -tulpn | grep 8080
   ```

2. **¿Cómo encuentras archivos modificados en las últimas 24 horas?**
   ```bash
   find /path -type f -mtime -1
   ```

3. **¿Cómo haces un port forward con iptables?**
   ```bash
   iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
   ```

4. **¿Cómo configuras una IP estática en Ubuntu 20.04+?**
   - Editar `/etc/netplan/*.yaml` y ejecutar `netplan apply`

5. **¿Cómo ves los logs de un servicio systemd?**
   ```bash
   journalctl -u nombre-servicio -f
   ```

---

## 🔗 Recursos Adicionales

- [Linux Command Line Cheat Sheet](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)
- [Bash Scripting Tutorial](https://linuxconfig.org/bash-scripting-tutorial)
- [Networking in Linux](https://www.redhat.com/sysadmin/networking-basics)
- [IPTables Tutorial](https://www.frozentux.net/iptables-tutorial/iptables-tutorial.html)

---

**💡 Consejo Final:** Practica estos comandos en una VM o contenedor. La experiencia práctica es clave para el test.
