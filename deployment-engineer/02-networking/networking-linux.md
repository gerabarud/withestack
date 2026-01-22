# Networking en Linux - Nivel Intermedio

## 1. Configuración de Interfaces de Red

### Ver Estado de Interfaces
```bash
ip link show                    # Listar interfaces
ip addr show                    # Ver IPs asignadas
ethtool eth0                    # Info detallada de interfaz
```

### Traer Interfaz UP/DOWN
```bash
sudo ip link set eth0 up
sudo ip link set eth0 down
sudo ifup eth0
sudo ifdown eth0
```

## 2. Netplan - Configuración Persistente (Ubuntu/Debian)

### Ubicación de Archivos
```
/etc/netplan/
```

### Ejemplo de Configuración IP Estática
```yaml
# /etc/netplan/01-netcfg.yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.100/24
      routes:
        - to: 0.0.0.0/0
          via: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
```

### Aplicar Cambios
```bash
sudo netplan validate            # Validar sintaxis
sudo netplan apply               # Aplicar configuración
sudo netplan --debug apply       # Debug
```

## 3. Bonding - Agregación de Interfaces

### Crear Bond
```bash
sudo nano /etc/netplan/02-bonding.yaml
```

```yaml
network:
  version: 2
  ethernets:
    eth0:
      match:
        name: eth0
    eth1:
      match:
        name: eth1
  bonds:
    bond0:
      interfaces:
        - eth0
        - eth1
      dhcp4: no
      addresses:
        - 192.168.1.100/24
      routes:
        - to: 0.0.0.0/0
          via: 192.168.1.1
      parameters:
        mode: active-backup      # o balance-alb, balance-rr, etc
        mii-monitor-interval: 100
```

### Aplicar Bond
```bash
sudo netplan apply
ip link show bond0               # Verificar bond
```

### Modos de Bonding
- **balance-rr**: Round-robin (distribución)
- **active-backup**: Solo uno activo (failover)
- **balance-alb**: Balance adaptatico
- **balance-xor**: XOR para equilibrio
- **802.3ad**: Agregación Link (LACP)

## 4. VLANs - Redes Virtuales

### Crear VLAN
```bash
sudo ip link add link eth0 name eth0.100 type vlan id 100
sudo ip addr add 192.168.100.100/24 dev eth0.100
sudo ip link set eth0.100 up
```

### Configuración Persistente con Netplan
```yaml
network:
  version: 2
  ethernets:
    eth0:
      match:
        name: eth0
  vlans:
    vlan100:
      id: 100
      link: eth0
      dhcp4: no
      addresses:
        - 192.168.100.100/24
    vlan200:
      id: 200
      link: eth0
      dhcp4: no
      addresses:
        - 192.168.200.100/24
```

### Verificar VLANs
```bash
ip link show
cat /proc/net/vlan/config
```

## 5. Enrutamiento

### Ver Tabla de Rutas
```bash
ip route show                   # Rutas actuales
ip -4 route show                # Solo IPv4
ip -6 route show                # Solo IPv6
route -n                        # Formato antiguo
```

### Añadir Rutas
```bash
sudo ip route add 10.0.0.0/8 via 192.168.1.1
sudo ip route add default via 192.168.1.1
sudo ip route del 10.0.0.0/8
```

### Rutas Persistentes (netplan)
```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.100/24
      routes:
        - to: 0.0.0.0/0
          via: 192.168.1.1
        - to: 10.0.0.0/8
          via: 192.168.1.254
```

## 6. DNS

### Ver Configuración DNS
```bash
cat /etc/resolv.conf            # Resolvers (NO editar)
systemd-resolve --status        # Estado de DNS
getent hosts hostname           # Resolver hostname
```

### Configurar DNS con Netplan
```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: yes
      nameservers:
        addresses: 
          - 8.8.8.8
          - 8.8.4.4
        search:
          - example.com
          - test.com
```

### Probar Resolución
```bash
nslookup google.com
dig google.com
```

## 7. Validación de Conectividad

### Herramientas Básicas
```bash
ping -c 4 8.8.8.8               # Verificar conectividad ICMP
traceroute 8.8.8.8              # Camino del paquete
mtr -r 8.8.8.8                  # MTR interactivo
```

### Puertos Abiertos
```bash
netstat -tulpn                  # Puertos escuchando (deprecated)
ss -tulpn                       # Alternativa moderna
sudo nmap -p- localhost         # Escanear puertos
telnet hostname 22              # Verificar puerto específico
curl -v http://hostname         # Prueba HTTP
```

### Ancho de Banda
```bash
iperf3                          # Medir velocidad
speedtest-cli                   # Test de velocidad
```

## 8. Firewall - UFW

### Operaciones Básicas
```bash
sudo ufw status                 # Ver estado
sudo ufw enable                 # Activar
sudo ufw disable                # Desactivar
```

### Reglas
```bash
sudo ufw allow 22/tcp           # Permitir SSH
sudo ufw allow 80/tcp           # Permitir HTTP
sudo ufw deny 23/tcp            # Denegar Telnet
sudo ufw allow from 192.168.1.0/24
sudo ufw delete allow 22        # Borrar regla
sudo ufw reset                  # Reset a defecto
```

## 9. Firewall - iptables/netfilter

### Ver Reglas
```bash
sudo iptables -L -n -v          # Listar reglas
sudo iptables -L INPUT -n       # Solo INPUT
```

### Ejemplos de Reglas
```bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
sudo iptables -P INPUT DROP     # Policy por defecto
```

### Persistencia (iptables-persistent)
```bash
sudo apt install iptables-persistent
sudo iptables-save > /etc/iptables/rules.v4
```

## 10. SSH - Configuración Avanzada

### Configuración del Servidor
```bash
# /etc/ssh/sshd_config
Port 22
AddressFamily any
ListenAddress 0.0.0.0
ListenAddress ::

# Autenticación
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no

# Sesión
ClientAliveInterval 300
ClientAliveCountMax 3

# Acceso
AllowUsers user1 user2
DenyUsers baduser
```

### Recargar SSH
```bash
sudo systemctl restart ssh
```

### Probar Conectividad
```bash
ssh-keyscan -t rsa hostname    # Obtener key SSH
ssh -vv user@hostname           # Debug connection
```

---
**Nivel**: Intermedio
**Tiempo estimado de estudio**: 5-6 horas
