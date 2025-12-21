# 🌐 Networking Avanzado - Guía Completa

## 📚 Índice
1. [Conceptos de Red](#conceptos-de-red)
2. [Interfaces y Configuración](#interfaces-y-configuración)
3. [VLANs](#vlans)
4. [Bonding/Link Aggregation](#bonding-link-aggregation)
5. [Routing](#routing)
6. [IPTables](#iptables)
7. [Troubleshooting de Red](#troubleshooting-de-red)

---

## 1. Conceptos de Red

### 🌐 Modelo OSI

| Capa | Nombre | Función | Protocolos |
|------|--------|---------|------------|
| 7 | Aplicación | Servicios de red | HTTP, FTP, DNS, SSH |
| 6 | Presentación | Formato de datos | SSL/TLS, JPEG |
| 5 | Sesión | Control de diálogos | NetBIOS, RPC |
| 4 | Transporte | Entrega end-to-end | TCP, UDP |
| 3 | Red | Routing | IP, ICMP, OSPF |
| 2 | Enlace | Acceso al medio | Ethernet, MAC |
| 1 | Física | Transmisión de bits | Cables, señales |

### 📊 Subnetting

```bash
# CIDR Notation
192.168.1.0/24
# /24 = 255.255.255.0 = 256 IPs (254 usables)

# Máscaras comunes
/8  = 255.0.0.0       = 16,777,216 hosts
/16 = 255.255.0.0     = 65,536 hosts
/24 = 255.255.255.0   = 256 hosts
/25 = 255.255.255.128 = 128 hosts
/26 = 255.255.255.192 = 64 hosts
/27 = 255.255.255.224 = 32 hosts
/28 = 255.255.255.240 = 16 hosts
/29 = 255.255.255.248 = 8 hosts
/30 = 255.255.255.252 = 4 hosts (2 usables)

# Calcular subnet
# Red: 192.168.1.0/26
# Broadcast: 192.168.1.63
# Rango usable: 192.168.1.1 - 192.168.1.62
# Gateway típico: 192.168.1.1
```

### 🔌 Puertos Comunes

```bash
20/21   FTP
22      SSH
23      Telnet
25      SMTP
53      DNS
80      HTTP
110     POP3
143     IMAP
443     HTTPS
3306    MySQL
5432    PostgreSQL
6379    Redis
8080    HTTP alternativo
27017   MongoDB
```

---

## 2. Interfaces y Configuración

### 🔧 Comandos ip

```bash
# Ver interfaces
ip link show
ip addr show
ip -s link                  # Con estadísticas

# Levantar/bajar interfaz
ip link set eth0 up
ip link set eth0 down

# Asignar IP
ip addr add 192.168.1.100/24 dev eth0
ip addr del 192.168.1.100/24 dev eth0

# Ver routing table
ip route show
ip route get 8.8.8.8       # Ver ruta a destino específico

# Añadir/eliminar ruta
ip route add 10.0.0.0/8 via 192.168.1.1
ip route del 10.0.0.0/8

# Default gateway
ip route add default via 192.168.1.1
ip route del default

# Estadísticas
ip -s -s link show eth0
```

### 📝 Netplan (Ubuntu 18.04+)

```yaml
# /etc/netplan/01-netcfg.yaml
network:
  version: 2
  renderer: networkd
  
  ethernets:
    # Interfaz con DHCP
    eth0:
      dhcp4: true
      dhcp6: false
    
    # Interfaz con IP estática
    eth1:
      addresses:
        - 192.168.1.100/24
      gateway4: 192.168.1.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
        search:
          - example.com
      routes:
        - to: 10.0.0.0/8
          via: 192.168.1.254
```

```bash
# Aplicar configuración
netplan apply

# Test (rollback automático en 120s)
netplan try

# Ver configuración generada
netplan --debug generate
```

---

## 3. VLANs

### 🏷️ Conceptos

- VLAN: Red lógica sobre red física
- Tag 802.1Q: Marca los frames con VLAN ID
- VLAN ID: 1-4094
- Native VLAN: Sin tag (default 1)

### 🔧 Configuración

```bash
# Cargar módulo
modprobe 8021q

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

**Netplan con VLANs:**
```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: false
  
  vlans:
    eth0.10:
      id: 10
      link: eth0
      addresses:
        - 10.0.10.1/24
    
    eth0.20:
      id: 20
      link: eth0
      addresses:
        - 10.0.20.1/24
```

---

## 4. Bonding (Link Aggregation)

### 🔗 Modos de Bonding

| Modo | Nombre | Descripción |
|------|--------|-------------|
| 0 | balance-rr | Round-robin (load balancing) |
| 1 | active-backup | Activo-pasivo (failover) |
| 2 | balance-xor | XOR policy |
| 3 | broadcast | Broadcast en todas |
| 4 | 802.3ad | LACP (Link Aggregation) |
| 5 | balance-tlb | Adaptive TX load balancing |
| 6 | balance-alb | Adaptive TX+RX load balancing |

### 🔧 Configuración

```bash
# Cargar módulo
modprobe bonding

# Crear bond
ip link add bond0 type bond mode 802.3ad
ip link set eth1 down
ip link set eth2 down
ip link set eth1 master bond0
ip link set eth2 master bond0
ip addr add 192.168.1.100/24 dev bond0
ip link set bond0 up

# Ver estado
cat /proc/net/bonding/bond0
```

**Netplan con Bonding:**
```yaml
network:
  version: 2
  ethernets:
    eth1:
      dhcp4: false
    eth2:
      dhcp4: false
  
  bonds:
    bond0:
      interfaces: [eth1, eth2]
      addresses:
        - 192.168.1.100/24
      gateway4: 192.168.1.1
      parameters:
        mode: 802.3ad
        mii-monitor-interval: 100
        lacp-rate: fast
        transmit-hash-policy: layer3+4
```

---

## 5. Routing

### 🛣️ Tipos de Rutas

```bash
# Ver tabla de ruteo
ip route show
route -n
netstat -rn

# Ruta estática
ip route add 10.0.0.0/8 via 192.168.1.254

# Ruta por interfaz
ip route add 172.16.0.0/16 dev eth1

# Ruta por defecto
ip route add default via 192.168.1.1

# Ruta con métrica (prioridad)
ip route add 10.0.0.0/8 via 192.168.1.254 metric 100

# Múltiples gateways (load balancing)
ip route add default \
  nexthop via 192.168.1.1 weight 1 \
  nexthop via 192.168.1.2 weight 1
```

### 🔀 IP Forwarding

```bash
# Habilitar forwarding (temporal)
echo 1 > /proc/sys/net/ipv4/ip_forward
sysctl -w net.ipv4.ip_forward=1

# Ver estado
cat /proc/sys/net/ipv4/ip_forward
sysctl net.ipv4.ip_forward

# Persistente
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
sysctl -p
```

### 📋 Tablas de Ruteo Múltiples

```bash
# Ver tablas
cat /etc/iproute2/rt_tables

# Crear tabla personalizada
echo "200 isp1" >> /etc/iproute2/rt_tables

# Añadir rutas a tabla
ip route add default via 10.0.1.1 table isp1

# Regla de policy routing
ip rule add from 192.168.1.0/24 table isp1

# Ver reglas
ip rule show

# Ver rutas de tabla
ip route show table isp1
```

---

## 6. IPTables

### 🔥 Conceptos

**Tablas:**
- **filter**: Filtrado de paquetes (INPUT, OUTPUT, FORWARD)
- **nat**: Network Address Translation (PREROUTING, POSTROUTING)
- **mangle**: Modificación de paquetes
- **raw**: Configuración de exenciones

**Chains:**
- **INPUT**: Tráfico entrante al servidor
- **OUTPUT**: Tráfico saliente del servidor
- **FORWARD**: Tráfico atravesando el servidor
- **PREROUTING**: Antes del routing
- **POSTROUTING**: Después del routing

### 🔧 Comandos Básicos

```bash
# Ver reglas
iptables -L -n -v
iptables -t nat -L -n -v

# Políticas por defecto
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Limpiar reglas
iptables -F                # Flush
iptables -X                # Delete chains
iptables -Z                # Zero counters

# Guardar/Restaurar
iptables-save > /etc/iptables/rules.v4
iptables-restore < /etc/iptables/rules.v4
```

### 🛡️ Reglas Comunes

```bash
# Permitir loopback
iptables -A INPUT -i lo -j ACCEPT

# Permitir conexiones establecidas
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Permitir SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Permitir HTTP/HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Permitir desde subnet específica
iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT

# Limitar rate (anti-DoS)
iptables -A INPUT -p tcp --dport 22 -m state --state NEW \
  -m recent --set
iptables -A INPUT -p tcp --dport 22 -m state --state NEW \
  -m recent --update --seconds 60 --hitcount 4 -j DROP

# Log y drop
iptables -A INPUT -j LOG --log-prefix "IPTables-Dropped: "
iptables -A INPUT -j DROP
```

### 🔄 NAT y Port Forwarding

```bash
# Masquerade (NAT para internet)
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# SNAT (Source NAT)
iptables -t nat -A POSTROUTING -s 192.168.1.0/24 \
  -o eth0 -j SNAT --to-source 203.0.113.10

# DNAT (Destination NAT / Port Forwarding)
iptables -t nat -A PREROUTING -p tcp --dport 8080 \
  -j DNAT --to-destination 192.168.1.100:80

# Port forwarding completo
iptables -t nat -A PREROUTING -p tcp -d 203.0.113.10 --dport 80 \
  -j DNAT --to-destination 192.168.1.100:80
iptables -A FORWARD -p tcp -d 192.168.1.100 --dport 80 -j ACCEPT
```

---

## 7. Troubleshooting de Red

### 🔍 Herramientas de Diagnóstico

```bash
# Ping
ping -c 4 8.8.8.8
ping -I eth0 8.8.8.8       # Por interfaz específica

# Traceroute
traceroute google.com
traceroute -n google.com   # Sin resolver DNS
mtr google.com             # Traceroute continuo

# DNS
dig google.com
dig @8.8.8.8 google.com    # DNS server específico
nslookup google.com
host google.com

# Puertos y conexiones
netstat -tulpn             # Puertos escuchando
ss -tulpn                  # Alternativa moderna
lsof -i :80                # Qué usa el puerto 80
lsof -i tcp                # Conexiones TCP

# ARP
arp -a
ip neigh show
arping 192.168.1.1

# Captura de tráfico
tcpdump -i eth0
tcpdump -i eth0 port 80
tcpdump -i eth0 host 192.168.1.100
tcpdump -i eth0 -w capture.pcap

# Ancho de banda
iftop                      # Tráfico por conexión
nethogs                    # Tráfico por proceso
bmon                       # Monitor de ancho de banda
vnstat                     # Estadísticas de tráfico

# Test de velocidad
iperf3 -s                  # Servidor
iperf3 -c server-ip        # Cliente

# Conectividad HTTP
curl -v http://example.com
wget -S http://example.com
telnet example.com 80
nc -zv example.com 80      # Test de puerto
```

### 🐛 Problemas Comunes

**1. Sin conectividad:**
```bash
# Verificar interfaz
ip link show
ip addr show

# Verificar gateway
ip route show
ping -c 1 $(ip route | grep default | awk '{print $3}')

# Verificar DNS
cat /etc/resolv.conf
dig google.com
```

**2. Lentitud de red:**
```bash
# Ver estadísticas
ip -s link

# Ver errores
ethtool -S eth0 | grep error

# MTU
ip link show eth0 | grep mtu
ping -M do -s 1472 8.8.8.8  # Test MTU
```

**3. Pérdida de paquetes:**
```bash
# Ping con estadísticas
ping -c 100 8.8.8.8

# MTR
mtr -r -c 100 8.8.8.8

# Ver drops en interfaz
ip -s link show eth0
```

**4. Problemas de DNS:**
```bash
# Test DNS
dig +trace google.com
nslookup google.com 8.8.8.8

# Flush DNS cache
systemd-resolve --flush-caches
resolvectl flush-caches
```

---

## 📝 Comandos Esenciales

```bash
# Top 30 comandos de networking
ip addr show
ip link show
ip route show
ip neigh show
ping
traceroute
mtr
dig
nslookup
host
netstat -tulpn
ss -tulpn
lsof -i
tcpdump
iptables -L
iptables -t nat -L
nc
telnet
curl
wget
ethtool
ifconfig (legacy)
route (legacy)
arp
arping
nmap
iftop
nethogs
iperf3
vnstat
```

---

## 🎓 Preguntas Típicas

1. **¿Qué es una VLAN?**
   - Red lógica sobre red física
   - Tag 802.1Q identifica VLAN

2. **¿Diferencia entre bonding modo 1 y modo 4?**
   - Modo 1: active-backup (failover)
   - Modo 4: LACP (load balancing + redundancia)

3. **¿Para qué sirve IP forwarding?**
   - Permitir routing entre interfaces
   - Necesario para router/firewall

4. **¿Diferencia entre SNAT y DNAT?**
   - SNAT: modifica IP origen (NAT salida)
   - DNAT: modifica IP destino (port forwarding)

5. **¿Cómo troubleshootear conectividad?**
   - ping → gateway → internet
   - traceroute para ver ruta
   - tcpdump para ver tráfico

---

## 🔗 Recursos

- [Linux Network Administrators Guide](https://tldp.org/LDP/nag2/index.html)
- [IPTables Tutorial](https://www.frozentux.net/iptables-tutorial/iptables-tutorial.html)

---

**💡 Consejo:** Whitestack requiere networking avanzado. Practica VLANs, routing e iptables.
