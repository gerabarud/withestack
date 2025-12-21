# � GUÍA COMPLETA TESTGORILLA - WHITESTACK

> **Índice Maestro - Acceso Rápido a Todos los Temas**  
> *Usa Ctrl+F para buscar términos específicos*

---

## 🗂️ ÍNDICE GENERAL

### 1. 🐧 [LINUX AVANZADO](#🐧-linux-avanzado---guía-de-estudio)
- [Comandos Básicos y Avanzados](#comandos-básicos-y-avanzados)
  - Navegación y Búsqueda (find, grep)
  - Monitoreo de Sistema (ps, top, free, df, iostat)
  - Gestión de Servicios (systemctl, journalctl)
  - Manipulación de Texto (awk, sed, cut, sort)
- [Gestión de Archivos y Sistemas](#gestión-de-archivos-y-sistemas)
  - Permisos y Propietarios (chmod, chown, ACLs, SUID, SGID, sticky bit)
  - LVM - Logical Volume Management (pvs, vgs, lvs, lvextend)
  - Sistemas de Archivos (mount, fstab, fsck)
- [Configuración de Red](#configuración-de-red)
  - Interfaces de Red (ip, ifconfig, netplan)
  - VLANs (802.1Q)
  - Bonding/Link Aggregation (modos 0-6)
  - Enrutamiento (ip route, forwarding)
  - IPTables (filter, nat, MASQUERADE, DNAT/SNAT)
  - Diagnóstico de Red (ping, traceroute, tcpdump, netstat, ss)
- [Bash Scripting](#bash-scripting)
  - Variables, Arrays, Control de Flujo
  - Loops (for, while, until)
  - Funciones
  - Script de Deployment Avanzado

### 2. ☸️ [KUBERNETES](#☸️-kubernetes---guía-completa)
- [Conceptos Fundamentales](#conceptos-fundamentales)
  - Terminología (Cluster, Node, Pod, Deployment, Service)
  - Arquitectura (Control Plane, Worker Nodes)
- [Arquitectura de Kubernetes](#arquitectura-de-kubernetes)
  - API Server, etcd, Scheduler, Controller Manager
  - Kubelet, Kube-proxy, Container Runtime
- [Pods y Contenedores](#pods-y-contenedores)
  - kubectl get/describe/logs/exec
  - Pods multi-container
  - Recursos y límites (requests/limits)
- [Deployments y ReplicaSets](#deployments-y-replicasets)
  - Crear y gestionar Deployments
  - Escalado (scale, autoscale)
  - Rollouts y Rollbacks
  - Estrategias de actualización (RollingUpdate, Recreate)
- [Services y Networking](#services-y-networking)
  - ClusterIP, NodePort, LoadBalancer
  - Ingress
- [Volumes y Storage](#volumes-y-storage)
  - emptyDir, hostPath
  - PersistentVolume (PV) y PersistentVolumeClaim (PVC)
  - StorageClass
- [ConfigMaps y Secrets](#configmaps-y-secrets)
  - Crear y usar ConfigMaps
  - Gestionar Secrets (base64)
- [Probes y Health Checks](#probes-y-health-checks)
  - Liveness Probe
  - Readiness Probe
  - Startup Probe
- [Init Containers](#init-containers)
- [Debugging y Troubleshooting](#debugging-y-troubleshooting)
  - Estados de Pods (Pending, CrashLoopBackOff, ImagePullBackOff)
  - Comandos de diagnóstico
- [Helm](#helm)
  - Comandos básicos
  - Estructura de un Chart

### 3. 🐳 [DOCKER Y CONTAINERD](#🐳-docker-y-containerd---guía-completa)
- [Conceptos Fundamentales](#conceptos-fundamentales-1)
  - Arquitectura (Docker Engine, Images, Containers, Registry)
- [Ciclo de Vida de Contenedores](#ciclo-de-vida-de-contenedores)
  - docker run/start/stop/restart/rm
  - docker inspect/logs/stats/exec
- [Imágenes Docker](#imágenes-docker)
  - docker pull/push/rmi
  - Dockerfile (FROM, RUN, COPY, ADD, CMD, ENTRYPOINT, EXPOSE)
  - Multi-stage builds
  - Tags y Registry
- [Volúmenes y Almacenamiento](#volúmenes-y-almacenamiento)
  - Volumes, Bind Mounts, tmpfs
- [Redes Docker](#redes-docker)
  - bridge, host, none, overlay
  - docker network create/connect
- [Docker Compose](#docker-compose)
  - docker-compose.yml
  - docker-compose up/down/logs
- [Containerd](#containerd)
  - ctr, crictl
- [Troubleshooting](#troubleshooting)

### 4. 🌐 [NETWORKING AVANZADO](#🌐-networking-avanzado---guía-completa)
- [Conceptos de Red](#conceptos-de-red)
  - Modelo OSI (7 capas)
  - Subnetting (CIDR, máscaras)
  - Puertos comunes
- [Interfaces y Configuración](#interfaces-y-configuración)
  - Comandos ip
  - Netplan
- [VLANs](#vlans)
  - 802.1Q, VLAN ID
- [Bonding/Link Aggregation](#bonding-link-aggregation)
  - Modos (active-backup, LACP, etc.)
- [Routing](#routing)
  - Tablas de ruteo
  - IP Forwarding
- [IPTables](#iptables)
  - Tablas (filter, nat, mangle)
  - Chains (INPUT, OUTPUT, FORWARD, PREROUTING, POSTROUTING)
  - NAT (SNAT, DNAT, MASQUERADE)
  - Port Forwarding
- [Troubleshooting de Red](#troubleshooting-de-red)
  - ping, traceroute, dig, nslookup
  - netstat, ss, lsof
  - tcpdump, iftop

### 5. 🤖 [ANSIBLE](#🤖-ansible---guía-de-automatización)
- [Conceptos Fundamentales](#conceptos-fundamentales-2)
  - Agentless, Idempotente
  - Control Node, Managed Nodes, Inventory, Playbook, Roles, Modules
- [Inventarios](#inventarios)
  - Formato INI y YAML
  - Variables de host
- [Playbooks](#playbooks)
  - Estructura básica (tasks, handlers, variables)
  - Ejecutar playbooks
  - Condicionales (when)
  - Loops
  - Block/Rescue/Always
- [Roles](#roles)
  - Estructura de un rol
  - Usar roles
- [Variables](#variables)
  - Precedencia
  - group_vars, host_vars
- [Módulos Importantes](#módulos-importantes)
  - apt, yum, pip
  - file, copy, template, lineinfile
  - user, group, service, systemd
  - command, shell, script
  - git, docker_container
- [Troubleshooting](#troubleshooting-1)

### 6. 🏗️ [TERRAFORM](#🏗️-terraform---infrastructure-as-code)
- [Conceptos Fundamentales](#conceptos-fundamentales-3)
  - IaC, Workflow (init/plan/apply/destroy)
- [Sintaxis HCL](#sintaxis-hcl)
  - Bloques (terraform, provider, resource, data, variable, output)
- [Providers y Recursos](#providers-y-recursos)
  - AWS, Azure, GCP
  - VPC, Subnet, Security Group, EC2, EBS
- [Variables y Outputs](#variables-y-outputs)
  - Tipos de variables
  - terraform.tfvars
- [State Management](#state-management)
  - terraform.tfstate
  - Remote State (S3, Azure, GCS)
  - State Locking
- [Módulos](#módulos)
  - Crear y usar módulos
- [Troubleshooting](#troubleshooting-2)

### 7. 🔧 [GIT AVANZADO](#🔧-git-avanzado---control-de-versiones)
- [Comandos Básicos Revisión](#comandos-básicos-revisión)
- [Branching Avanzado](#branching-avanzado)
  - Crear/eliminar branches
  - Merge strategies (fast-forward, no-ff, squash)
  - Resolver conflictos
- [Rebase](#rebase)
  - Rebase básico
  - Interactive rebase
  - Rebase vs Merge
- [Cherry-pick](#cherry-pick)
- [Stash](#stash)
- [Reset y Revert](#reset-y-revert)
  - git reset (--soft, --mixed, --hard)
  - git revert
- [GitOps Workflows](#gitops-workflows)
  - Git Flow
  - GitHub Flow
  - Conventional Commits

### 8. ☁️ [OPENSTACK](#☁️-openstack---guía-básica)
- [¿Qué es OpenStack?](#qué-es-openstack)
- [Arquitectura y Componentes](#arquitectura-y-componentes)
  - Nova (Compute), Neutron (Networking), Cinder (Block Storage)
  - Swift (Object Storage), Glance (Image), Keystone (Identity)
  - Horizon (Dashboard), Heat (Orchestration)
- [CLI Essentials](#cli-essentials)
  - Glance (imágenes)
  - Nova (instancias, flavors, keypairs)
  - Neutron (redes, subnets, routers, security groups, floating IPs)
  - Cinder (volúmenes)
  - Keystone (proyectos, usuarios, roles)
- [Conceptos Clave](#conceptos-clave)
  - Flavors, Security Groups, Floating IPs, Quotas

### 9. 📊 [SISTEMAS DE MONITOREO](#📊-sistemas-de-monitoreo---guía-básica)
- [Grafana](#grafana) - Dashboards, Datasources, Alerts
- [Kibana](#kibana) - ELK Stack, Discover, Visualize
- [Prometheus](#prometheus) - Time-series, PromQL, Alertmanager
- [Zabbix](#zabbix) - Agent, Templates, Triggers
- [Nagios](#nagios) - Hosts, Services, Checks

### 10. 📊 [PROMETHEUS - GUÍA COMPLETA](#📊-prometheus---guía-completa)
- [¿Qué es Prometheus?](#qué-es-prometheus)
- [Conceptos Fundamentales](#conceptos-fundamentales-4)
  - Arquitectura, Tipos de métricas (Counter, Gauge, Histogram, Summary)
- [PromQL: Lenguaje de Queries](#promql-lenguaje-de-queries)
  - Queries básicas
  - Funciones (rate, irate, increase, sum, avg, by, without)
- [Top 20 Queries para el Test](#top-20-queries-para-el-test)
  - HTTP/API Monitoring
  - CPU/Memory Monitoring
  - Disk/Network
  - Availability
- [Alertas en Prometheus](#alertas-en-prometheus)
  - Estructura de alertas
  - Alertas comunes
- [Exporters Comunes](#exporters-comunes)
  - node_exporter, kube-state-metrics, blackbox_exporter

### 11. 🐍 [PYTHON PARA DEVOPS/SRE](#🐍-python-para-devopssre---guía-completa)
- [Conceptos Básicos](#conceptos-básicos)
  - Variables, Strings, Listas, Diccionarios, Sets
- [Control de Flujo](#control-de-flujo)
  - If-Elif-Else, Loops (for, while)
- [Funciones](#funciones)
  - Definición, *args, **kwargs, Lambda
- [Módulos y Imports](#módulos-y-imports)
- [Trabajar con Archivos](#trabajar-con-archivos)
  - Leer/escribir, JSON, YAML, CSV
- [Trabajar con APIs (Requests)](#trabajar-con-apis-requests)
- [System Administration (psutil)](#system-administration-psutil)
- [Ejecutar Comandos Shell](#ejecutar-comandos-shell)
- [Regular Expressions (Regex)](#regular-expressions-regex)
- [Logging](#logging)
- [CLI Arguments (argparse)](#cli-arguments-argparse)
- [Variables de Entorno](#variables-de-entorno)
- [Error Handling](#error-handling)
- [Scripts Útiles para DevOps](#scripts-útiles-para-devops)

### 12. 🚀 [CI/CD Y GITOPS](#🚀-cicd-y-gitops---guía-práctica)
- [¿Qué es CI/CD?](#qué-es-cicd)
- [GitLab CI](#gitlab-ci---lo-más-usado-en-empresas)
  - .gitlab-ci.yml
  - Stages, Jobs, Variables
  - Ejemplos avanzados
- [GitHub Actions](#github-actions)
  - Workflows, Jobs, Steps
- [Jenkins Pipeline](#jenkins-pipeline)
  - Jenkinsfile (Declarative)
- [Best Practices CI/CD](#best-practices-cicd)
  - Secrets Management
  - Caching
  - Matrix Testing
- [GitOps con ArgoCD](#gitops-con-argocd)
- [Pipeline Patterns](#pipeline-patterns-comunes)
  - Blue-Green Deployment
  - Canary Deployment
- [Monitoring de Pipelines](#monitoring-de-pipelines)

---

# 🐧 Linux Avanzado - Guía de Estudio

## 📚 Índice
1. [Comandos Básicos y Avanzados](#comandos-básicos-y-avanzados)
2. [Gestión de Archivos y Sistemas](#gestión-de-archivos-y-sistemas)
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

- id bajo → CPU saturada
- wa alto → problema de I/O
- Load > cores → sobrecarga
- st alto → problema de virtualización

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
chmod +t /tmp                       # Sticky bit — protección en directorios compartidos
chmod u+s /usr/bin/sudo             # SUID (u+s) — ejecutar como dueño
chmod g+s /shared                   # SGID (g+s) — herencia de grupo

# ACLs (Access Control Lists)
setfacl -m u:john:rw file.txt      # Dar permisos a usuario
getfacl file.txt                   # Ver ACLs
setfacl -R -m g:developers:rwx /project  # ACL recursivo
```

- ❓ ¿Cómo das permisos a un usuario sin cambiar owner? ✔ ACL
- ❓ ¿Cómo evitás que borren archivos en un dir compartido? ✔ Sticky bit
- ❓ ¿Cómo ejecutar un binario como root? ✔ SUID
- ❓ ¿Cómo asegurar grupo consistente en archivos? ✔ SGID


### 💾 LVM (Logical Volume Management)

```bash
# Ver información
pvs                                 # ✔ Lista discos/particiones inicializadas como LVM - Physical volumes (disco/partición)
vgs                                 # ✔ Muestra VGs y cuánto espacio tienen - Volume groups (pool de espacio)
lvs                                 # ✔ Muestra los LVs (tamaños, nombres) - Logical volumes (el “disco” que usás)
pvdisplay /dev/sdb1                 # Info detallada de PV

# Crear LVM
pvcreate /dev/sdb1                 # Crear PV - Inicializa un disco/partición para usarlo en LVM.
vgcreate vg_data /dev/sdb1         # Crear VG - Crea un pool de almacenamiento llamado vg_data.
lvcreate -L 10G -n lv_mysql vg_data  # Crear LV de 10GB - Crea un volumen lógico de 10GB llamado lv_mysql (👉 Esto es lo que después formateás y montás.)

# Extender volumen
lvextend -L +5G /dev/vg_data/lv_mysql  # Añadir 5GB al LV existente.
resize2fs /dev/vg_data/lv_mysql    # Extender filesystem ext4
xfs_growfs /mount/point            # Extender filesystem XFS
```

- ❓ ¿Cómo agregás espacio a un filesystem LVM? ✔ lvextend + resize del FS
- ❓ ¿Dónde ves el espacio libre? ✔ vgs
- ❓ ¿Qué capa agrupa discos? ✔ VG

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
swapon -s                          # Ver Swap
free -m                            # Ver Swap

# Verificar filesystem
fsck /dev/sdb1                     # Check filesystem
fsck -y /dev/sdb1                  # Auto-repair
xfs_repair /dev/sdb2               # Repair XFS
```

- ❓ ¿Cómo hacés un mount permanente? ✔ /etc/fstab
- ❓ ¿Cómo verificás que fstab está bien? ✔ mount -a
- ❓ ¿Qué comando muestra UUID? ✔ blkid

---

## 3. Configuración de Red

### 🌐 Interfaces de Red

```bash
# Ver interfaces
ip addr show                       # Ver todas las interfaces
ip link show                       # Ver estado de links
ifconfig -a                        # Alternativa (deprecated)

# Configurar IP
ip addr add 192.168.1.100/24 dev eth0   # Agrega IP temporal (se pierde al rebooty)
ip addr del 192.168.1.100/24 dev eth0   # Elimina la IP
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

¿Qué es una VLAN?

Una red lógica separada, aunque use el mismo cable.

👉 VLAN = aislamiento

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

¿Qué es bonding?

Unir varias placas en una sola interfaz lógica.

👉 Objetivos:

- Redundancia
- Más ancho de banda

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
- `802.3ad` (4): LACP (Link Aggregation Control Protocol)
- `balance-tlb` (5): Adaptive transmit load balancing
- `balance-alb` (6): Adaptive load balancing

### 🛣️ Enrutamiento

¿Qué es una ruta?

Le dice al sistema: “Para llegar a X, salí por Y”

```bash
# Ver tabla de ruteo
ip route show
route -n                           # Alternativa

# Añadir ruta
ip route add 10.0.0.0/8 via 192.168.1.1 # Todo 10.x → gateway 192.168.1.1
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

¿Qué es?

Firewall a nivel kernel.

👉 Decide:

- qué entra
- qué sale
- qué se redirige
- y si se modifican (NAT)

🧱 Tablas de iptables
| Tabla        | Para qué sirve                         |
| ------------ | -------------------------------------- |
| **filter**   | Permitir o bloquear tráfico (firewall) |
| **nat**      | Modificar IPs/puertos (NAT)            |
| **mangle**   | Tocar campos del paquete               |
| **raw**      | Evitar tracking                        |
| **security** | SELinux                                |

Tabla filter
| Cadena      | Qué controla                    |
| ----------- | ------------------------------- |
| **INPUT**   | Paquetes que **entran al host** |
| **OUTPUT**  | Paquetes que **salen del host** |
| **FORWARD** | Paquetes que pasan **a través** |

Tabla nat
| Cadena          | Momento           |
| --------------- | ----------------- |
| **PREROUTING**  | Antes del ruteo   |
| **POSTROUTING** | Después del ruteo |
| **OUTPUT**      | Tráfico local     |

🔁 Estados de conexión
| Estado          | Significado          |
| --------------- | -------------------- |
| **NEW**         | Nueva conexión       |
| **ESTABLISHED** | Conexión ya aceptada |
| **RELATED**     | Conexión relacionada |
| **INVALID**     | Rota o corrupta      |


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
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT # Permití cualquier paquete que sea respuesta de algo que yo ya acepté antes

iptables -A INPUT -p tcp --dport 22 -j ACCEPT    # SSH
iptables -A INPUT -p tcp --dport 80 -j ACCEPT    # HTTP
iptables -A INPUT -p tcp --dport 443 -j ACCEPT   # HTTPS

# NAT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE  # NAT masquerade 🔁 Cambia IP privada por IP pública
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080 # Redirige puerto 80 → Puerto 8080

# Port forwarding
iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination 10.0.0.5:80 # Redirige puerto 8080 → servidor interno

# Guardar reglas
iptables-save > /etc/iptables/rules.v4
netfilter-persistent save

# Restaurar reglas
iptables-restore < /etc/iptables/rules.v4
```

🧠 Orden típico de firewall (patrón)

```bash
iptables -P INPUT DROP # Todo DROP por defecto
iptables -A INPUT -i lo -j ACCEPT # El sistema puede hablar consigo
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT # Respuestas permitidas
iptables -A INPUT -p tcp --dport 22 -j ACCEPT # Permití nuevas conexiones SSH
``` 

### 🔍 Diagnóstico de Red

```bash
# Conectividad
ping -c 4 8.8.8.8                  # Ping 4 veces - Envía ICMP Echo Request y espera Echo Reply.
traceroute google.com              # Trazar ruta entre vos y el destino.
mtr google.com                     # MTR (mejor que traceroute)

# Puertos y conexiones
netstat -tulpn                     # Ver puertos abiertos (TCP - UDP - Listening - Proceso - No DNS) 
ss -tulpn                          # Alternativa moderna
lsof -i :80                        # Ver qué usa el puerto 80
nmap localhost                     # Escanear puertos

# DNS
dig google.com                     # Consulta DNS
nslookup google.com                # Muestra servidor DNS usado e IPs devueltas
host google.com

# Tráfico de red
tcpdump -i eth0                    # Capturar tráfico
tcpdump -i eth0 port 80            # Solo puerto 80
tcpdump -i eth0 -w capture.pcap    # Guardar a archivo
iftop                              # Ver tráfico en tiempo real
nethogs                            # Ver tráfico por proceso

# ARP
# ARP (Address Resolution Protocol) traduce una IP → MAC dentro de una red local.
# - IP vive en capa 3
# - MAC vive en capa 2
# - ARP es el puente entre ambas
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

# ☸️ Kubernetes - Guía Completa

## 📚 Índice
1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [Arquitectura de Kubernetes](#arquitectura-de-kubernetes)
3. [Pods y Contenedores](#pods-y-contenedores)
4. [Deployments y ReplicaSets](#deployments-y-replicasets)
5. [Services y Networking](#services-y-networking)
6. [Volumes y Storage](#volumes-y-storage)
7. [ConfigMaps y Secrets](#configmaps-y-secrets)
8. [Probes y Health Checks](#probes-y-health-checks)
9. [Init Containers](#init-containers)
10. [Debugging y Troubleshooting](#debugging-y-troubleshooting)
11. [Helm](#helm)
12. [Ejercicios Prácticos](#ejercicios-prácticos)

---

## 1. Conceptos Fundamentales

### 🎯 ¿Qué es Kubernetes?

Kubernetes (K8s) es un sistema de orquestación de contenedores open-source que automatiza el despliegue, escalado y gestión de aplicaciones en contenedores.

**Características principales:**
- 🔄 Auto-healing: Reinicia contenedores fallidos
- 📊 Load balancing: Distribuye tráfico
- 🔐 Secret management: Gestiona información sensible
- 📦 Storage orchestration: Monta sistemas de archivos
- 🚀 Rolling updates: Actualizaciones sin downtime
- 📈 Horizontal scaling: Escala automáticamente

### 📖 Terminología Esencial

| Término | Descripción |
|---------|-------------|
| **Cluster** | Conjunto de nodos que ejecutan aplicaciones containerizadas |
| **Node** | Máquina (física o virtual) que ejecuta pods |
| **Pod** | Unidad mínima de despliegue, contiene uno o más contenedores |
| **Deployment** | Declara el estado deseado de pods y ReplicaSets |
| **Service** | Abstracción que define acceso a un conjunto de pods |
| **Namespace** | Aislamiento lógico de recursos en el cluster |
| **Label** | Par clave-valor para identificar y seleccionar objetos |

---

## 2. Arquitectura de Kubernetes

### 🏗️ Componentes del Control Plane

```
┌─────────────────────────────────────────┐
│         Control Plane (Master)          │
├─────────────────────────────────────────┤
│  ┌──────────┐  ┌───────────────────┐   │
│  │ API      │  │ Controller        │   │
│  │ Server   │  │ Manager           │   │
│  └──────────┘  └───────────────────┘   │
│  ┌──────────┐  ┌───────────────────┐   │
│  │ Scheduler│  │ etcd (Key-Value   │   │
│  │          │  │ Store)            │   │
│  └──────────┘  └───────────────────┘   │
└─────────────────────────────────────────┘
            │
            ├─────────────┬─────────────┐
            ▼             ▼             ▼
┌───────────────┐ ┌───────────────┐ ┌──────────────┐
│   Node 1      │ │   Node 2      │ │   Node 3     │
├───────────────┤ ├───────────────┤ ├──────────────┤
│ Kubelet       │ │ Kubelet       │ │ Kubelet      │
│ Kube-proxy    │ │ Kube-proxy    │ │ Kube-proxy   │
│ Container     │ │ Container     │ │ Container    │
│ Runtime       │ │ Runtime       │ │ Runtime      │
│  ┌────┐┌────┐ │ │  ┌────┐┌────┐ │ │  ┌────┐      │
│  │Pod ││Pod │ │ │  │Pod ││Pod │ │ │  │Pod │      │
│  └────┘└────┘ │ │  └────┘└────┘ │ │  └────┘      │
└───────────────┘ └───────────────┘ └──────────────┘
```

**Control Plane:**
- **API Server**: Frontend del control plane, expone la API de K8s
- **etcd**: Almacén de datos distribuido para el estado del cluster
- **Scheduler**: Asigna pods a nodos
- **Controller Manager**: Ejecuta controladores (Deployment, ReplicaSet, etc.)

**Worker Nodes:**
- **Kubelet**: Agente que se ejecuta en cada nodo
- **Kube-proxy**: Mantiene reglas de red
- **Container Runtime**: Docker, containerd, CRI-O

---

## 3. Pods y Contenedores

### 🚀 Crear y Gestionar Pods

```bash
# Comandos básicos
kubectl get pods                           # Listar pods
kubectl get pods -A                        # Todos los namespaces
kubectl get pods -o wide                   # Info adicional (IP, nodo)
kubectl get pods --watch                   # Watch mode
kubectl get pods -l app=nginx              # Filtrar por label

# Describir pod (info detallada)
kubectl describe pod nginx-pod

# Ver logs
kubectl logs nginx-pod                     # Logs del pod
kubectl logs nginx-pod -f                  # Follow logs
kubectl logs nginx-pod -c container-name   # Logs de contenedor específico
kubectl logs nginx-pod --previous          # Logs del contenedor anterior

# Ejecutar comandos en pod
kubectl exec nginx-pod -- ls /usr/share/nginx/html
kubectl exec -it nginx-pod -- /bin/bash    # Shell interactivo

# Eliminar pod
kubectl delete pod nginx-pod
kubectl delete pod --all                   # Eliminar todos
```

### 📝 Pod YAML Básico

```yaml
# pod-simple.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
    env: production
spec:
  containers:
  - name: nginx
    image: nginx:1.21
    ports:
    - containerPort: 80
```

```bash
# Crear pod desde YAML
kubectl apply -f pod-simple.yaml

# Ver YAML de pod existente
kubectl get pod nginx-pod -o yaml
```

### 🔧 Pod Multi-Container

```yaml
# pod-multi-container.yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
spec:
  containers:
  - name: web
    image: nginx:1.21
    ports:
    - containerPort: 80
    volumeMounts:
    - name: shared-data
      mountPath: /usr/share/nginx/html
  
  - name: content-updater
    image: busybox:1.34
    command: ["/bin/sh"]
    args:
      - -c
      - >
        while true; do
          echo "Updated at $(date)" > /data/index.html;
          sleep 60;
        done
    volumeMounts:
    - name: shared-data
      mountPath: /data
  
  volumes:
  - name: shared-data
    emptyDir: {}
```

### 🎯 Recursos y Límites

```yaml
# pod-resources.yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-pod
spec:
  containers:
  - name: app
    image: nginx:1.21
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"        # 0.25 CPU
      limits:
        memory: "128Mi"
        cpu: "500m"        # 0.5 CPU
```

---

## 4. Deployments y ReplicaSets

### 🚀 Deployments

Los Deployments gestionan el estado deseado de los pods y permiten actualizaciones declarativas.

```yaml
# deployment-nginx.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3                    # Número de pods
  selector:
    matchLabels:
      app: nginx
  template:                      # Template del Pod
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "100m"
          limits:
            memory: "128Mi"
            cpu: "200m"
```

```bash
# Gestionar Deployments
kubectl apply -f deployment-nginx.yaml
kubectl get deployments
kubectl get rs                             # Ver ReplicaSets
kubectl describe deployment nginx-deployment

# Escalar
kubectl scale deployment nginx-deployment --replicas=5
kubectl autoscale deployment nginx-deployment --min=2 --max=10 --cpu-percent=80

# Ver historial de rollouts
kubectl rollout history deployment nginx-deployment
kubectl rollout status deployment nginx-deployment

# Actualizar imagen
kubectl set image deployment/nginx-deployment nginx=nginx:1.22

# Rollback
kubectl rollout undo deployment nginx-deployment
kubectl rollout undo deployment nginx-deployment --to-revision=2

# Pausar/Reanudar rollout
kubectl rollout pause deployment nginx-deployment
kubectl rollout resume deployment nginx-deployment
```

### 🔄 Estrategias de Actualización

```yaml
# deployment-strategies.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deployment
spec:
  replicas: 4
  strategy:
    type: RollingUpdate           # o Recreate
    rollingUpdate:
      maxSurge: 1                 # Máximo de pods adicionales
      maxUnavailable: 1           # Máximo de pods no disponibles
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: app
        image: myapp:v1
```

**Tipos de estrategias:**
- **RollingUpdate**: Actualización gradual (default)
- **Recreate**: Elimina todos los pods antes de crear nuevos

---

## 5. Services y Networking

### 🌐 Tipos de Services

```yaml
# service-clusterip.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: ClusterIP              # Default, solo accesible dentro del cluster
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80                   # Puerto del service
    targetPort: 80             # Puerto del contenedor
```

```yaml
# service-nodeport.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
spec:
  type: NodePort               # Accesible desde fuera por IP del nodo
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30080            # Puerto en los nodos (30000-32767)
```

```yaml
# service-loadbalancer.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-lb
spec:
  type: LoadBalancer           # Crea un LB externo (cloud provider)
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

```bash
# Comandos de Services
kubectl get services
kubectl get svc                            # Alias
kubectl describe service nginx-service
kubectl get endpoints                      # Ver endpoints del service

# Exponer deployment como service
kubectl expose deployment nginx-deployment --type=LoadBalancer --port=80
```

### 🔗 Ingress

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx-service
            port:
              number: 80
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 8080
```

---

## 6. Volumes y Storage

### 💾 Tipos de Volumes

```yaml
# pod-emptydir.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-emptydir
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: cache
      mountPath: /cache
  volumes:
  - name: cache
    emptyDir: {}                # Directorio temporal, se pierde al eliminar pod
```

```yaml
# pod-hostpath.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-hostpath
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: data
      mountPath: /data
  volumes:
  - name: data
    hostPath:
      path: /mnt/data           # Path en el nodo
      type: DirectoryOrCreate
```

### 📦 PersistentVolume y PersistentVolumeClaim

```yaml
# pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-data
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce            # RWO, ROX, RWX
  persistentVolumeReclaimPolicy: Retain  # Retain, Delete, Recycle
  storageClassName: standard
  hostPath:
    path: /mnt/data
```

```yaml
# pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-data
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard
```

```yaml
# pod-with-pvc.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-storage
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: data
      mountPath: /data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: pvc-data
```

```bash
# Comandos de storage
kubectl get pv                             # PersistentVolumes
kubectl get pvc                            # PersistentVolumeClaims
kubectl describe pv pv-data
kubectl describe pvc pvc-data
```

### 🗄️ StorageClass

```yaml
# storageclass.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-storage
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
  fsType: ext4
reclaimPolicy: Delete
allowVolumeExpansion: true
```

---

## 7. ConfigMaps y Secrets

### ⚙️ ConfigMaps

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  app.properties: |
    database.host=mysql
    database.port=3306
    log.level=INFO
  nginx.conf: |
    server {
        listen 80;
        server_name localhost;
    }
```

```bash
# Crear ConfigMap desde comando
kubectl create configmap app-config --from-literal=key1=value1 --from-literal=key2=value2
kubectl create configmap app-config --from-file=config.properties
kubectl create configmap nginx-config --from-file=nginx.conf

# Ver ConfigMaps
kubectl get configmaps
kubectl describe configmap app-config
kubectl get configmap app-config -o yaml
```

**Usar ConfigMap en Pod:**

```yaml
# pod-with-configmap.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-configmap
spec:
  containers:
  - name: app
    image: nginx
    envFrom:
    - configMapRef:
        name: app-config         # Todas las keys como env vars
    env:
    - name: DATABASE_HOST        # Key específica
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: database.host
    volumeMounts:
    - name: config
      mountPath: /etc/config
  volumes:
  - name: config
    configMap:
      name: app-config           # Montar como archivos
```

### 🔐 Secrets

```yaml
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  username: YWRtaW4=             # base64 encoded: admin
  password: cGFzc3dvcmQxMjM=     # base64 encoded: password123
```

```bash
# Crear Secret
kubectl create secret generic db-secret \
  --from-literal=username=admin \
  --from-literal=password=password123

# Desde archivo
kubectl create secret generic tls-secret \
  --from-file=tls.crt=cert.crt \
  --from-file=tls.key=cert.key

# Ver Secrets (sin decodificar)
kubectl get secrets
kubectl describe secret db-secret

# Ver valor decodificado
kubectl get secret db-secret -o jsonpath='{.data.password}' | base64 -d
```

**Usar Secret en Pod:**

```yaml
# pod-with-secret.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-secret
spec:
  containers:
  - name: app
    image: myapp
    env:
    - name: DB_USERNAME
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: username
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: password
    volumeMounts:
    - name: secret
      mountPath: /etc/secret
      readOnly: true
  volumes:
  - name: secret
    secret:
      secretName: db-secret
```

---

## 8. Probes y Health Checks

### 🏥 Liveness, Readiness y Startup Probes

```yaml
# pod-with-probes.yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-probes
spec:
  containers:
  - name: app
    image: myapp:v1
    ports:
    - containerPort: 8080
    
    # Liveness Probe: ¿Está vivo el contenedor?
    # Si falla, Kubernetes reinicia el contenedor
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 3
      periodSeconds: 3
      timeoutSeconds: 1
      failureThreshold: 3
    
    # Readiness Probe: ¿Está listo para recibir tráfico?
    # Si falla, se quita del Service
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 5
      timeoutSeconds: 1
      successThreshold: 1
      failureThreshold: 3
    
    # Startup Probe: Para apps de arranque lento
    # Deshabilita liveness/readiness hasta que pase
    startupProbe:
      httpGet:
        path: /startup
        port: 8080
      initialDelaySeconds: 0
      periodSeconds: 10
      failureThreshold: 30      # 300s máximo de arranque
```

**Tipos de Probes:**

```yaml
# HTTP Probe
livenessProbe:
  httpGet:
    path: /health
    port: 8080
    httpHeaders:
    - name: Custom-Header
      value: Awesome

# TCP Probe
livenessProbe:
  tcpSocket:
    port: 8080

# Exec Probe (ejecuta comando)
livenessProbe:
  exec:
    command:
    - cat
    - /tmp/healthy
```

---

## 9. Init Containers

Init containers se ejecutan antes que los contenedores de la aplicación y deben completarse exitosamente.

```yaml
# pod-with-init-containers.yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  initContainers:
  - name: init-db
    image: busybox:1.34
    command: ['sh', '-c', 'until nslookup mydb; do echo waiting for mydb; sleep 2; done']
  
  - name: init-config
    image: busybox:1.34
    command: ['sh', '-c', 'echo "Config initialized" > /work-dir/config.txt']
    volumeMounts:
    - name: workdir
      mountPath: /work-dir
  
  containers:
  - name: myapp
    image: myapp:v1
    volumeMounts:
    - name: workdir
      mountPath: /app/config
  
  volumes:
  - name: workdir
    emptyDir: {}
```

**Casos de uso:**
- Esperar a que un servicio esté disponible
- Registrar el pod en un sistema externo
- Descargar configuración o datos
- Preparar el sistema de archivos

---

## 10. Debugging y Troubleshooting

### 🔍 Comandos de Debugging

```bash
# Ver estado de recursos
kubectl get all
kubectl get pods --all-namespaces
kubectl get events --sort-by='.lastTimestamp'

# Describir recursos (info detallada + eventos)
kubectl describe pod pod-name
kubectl describe deployment deployment-name
kubectl describe node node-name

# Logs
kubectl logs pod-name
kubectl logs pod-name -c container-name     # Multi-container
kubectl logs pod-name --previous            # Logs del contenedor anterior
kubectl logs -f pod-name                    # Follow
kubectl logs --tail=100 pod-name            # Últimas 100 líneas
kubectl logs --since=1h pod-name            # Última hora

# Ejecutar comandos en contenedor
kubectl exec pod-name -- ls /app
kubectl exec -it pod-name -- /bin/bash
kubectl exec -it pod-name -c container-name -- /bin/sh

# Port forwarding (acceder a pod desde localhost)
kubectl port-forward pod-name 8080:80
kubectl port-forward svc/service-name 8080:80

# Copiar archivos
kubectl cp pod-name:/path/to/file ./local-file
kubectl cp ./local-file pod-name:/path/to/file

# Debug interactivo (crea pod temporal)
kubectl run -it debug --image=busybox --rm -- /bin/sh
kubectl debug pod-name -it --image=busybox

# Ver recursos del cluster
kubectl top nodes                           # Uso de recursos por nodo
kubectl top pods                            # Uso de recursos por pod
kubectl top pods --containers               # Por contenedor

# Ver configuración
kubectl config view
kubectl config get-contexts
kubectl config use-context context-name

# Editar recursos en vivo
kubectl edit deployment deployment-name
kubectl edit pod pod-name
```

### 🐛 Troubleshooting Común

**1. Pod en estado Pending:**
```bash
kubectl describe pod pod-name
# Verificar:
# - Recursos insuficientes en nodos
# - PVC sin PV disponible
# - Nodo con taints que el pod no tolera
```

**2. Pod en CrashLoopBackOff:**
```bash
kubectl logs pod-name --previous
kubectl describe pod pod-name
# Verificar:
# - Errores en logs
# - Liveness probe fallando
# - Comando de inicio incorrecto
```

**3. ImagePullBackOff:**
```bash
kubectl describe pod pod-name
# Verificar:
# - Nombre de imagen correcto
# - Image pull secrets configurados
# - Registry accesible
```

**4. Pod Running pero no responde:**
```bash
kubectl exec -it pod-name -- /bin/sh
# Dentro del pod:
netstat -tulpn                              # Ver puertos
ps aux                                      # Ver procesos
curl localhost:8080/health                  # Test local

# Verificar readiness probe
kubectl describe pod pod-name | grep -A 5 Readiness
```

### 📊 Debugging Avanzado

```yaml
# pod-debug.yaml - Pod con herramientas de debugging
apiVersion: v1
kind: Pod
metadata:
  name: debug-pod
spec:
  containers:
  - name: debug
    image: nicolaka/netshoot                # Imagen con herramientas de red
    command: ["sleep", "3600"]
```

```bash
# Desde el debug pod:
kubectl exec -it debug-pod -- /bin/bash

# Herramientas disponibles:
ping 10.0.0.1
nslookup service-name
curl http://service-name:80
tcpdump -i eth0
iperf3 -s                                   # Test de ancho de banda
```

---

## 11. Helm

Helm es el gestor de paquetes de Kubernetes.

### 📦 Comandos Básicos de Helm

```bash
# Añadir repositorio
helm repo add stable https://charts.helm.sh/stable
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Buscar charts
helm search repo nginx
helm search hub wordpress

# Instalar chart
helm install my-release bitnami/nginx
helm install my-release bitnami/nginx --namespace my-namespace --create-namespace
helm install my-release ./my-chart          # Desde directorio local

# Listar releases
helm list
helm list -A                                # Todos los namespaces

# Ver estado
helm status my-release
helm get values my-release                  # Ver valores configurados
helm get manifest my-release                # Ver manifiestos generados

# Actualizar release
helm upgrade my-release bitnami/nginx --set replicaCount=3
helm upgrade my-release bitnami/nginx -f values.yaml

# Rollback
helm rollback my-release 1                  # A versión específica
helm history my-release                     # Ver historial

# Desinstalar
helm uninstall my-release

# Crear chart propio
helm create my-chart
```

### 📋 Estructura de un Helm Chart

```
my-chart/
├── Chart.yaml              # Metadata del chart
├── values.yaml             # Valores por defecto
├── templates/              # Templates de K8s
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── _helpers.tpl        # Helpers/funciones
│   └── NOTES.txt           # Notas post-instalación
└── charts/                 # Charts dependientes
```

**Chart.yaml:**
```yaml
apiVersion: v2
name: my-app
description: A Helm chart for my application
version: 1.0.0
appVersion: "1.0"
```

**values.yaml:**
```yaml
replicaCount: 3

image:
  repository: nginx
  tag: "1.21"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

resources:
  limits:
    cpu: 100m
    memory: 128Mi
  requests:
    cpu: 100m
    memory: 128Mi
```

**templates/deployment.yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-chart.fullname" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "my-chart.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "my-chart.selectorLabels" . | nindent 8 }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: 80
        resources:
          {{- toYaml .Values.resources | nindent 12 }}
```

---

## 🎓 Preguntas Típicas del Test

1. **¿Cuál es la diferencia entre Deployment y ReplicaSet?**
   - Deployment gestiona ReplicaSets y permite rolling updates
   - ReplicaSet solo mantiene el número deseado de pods

2. **¿Qué hace el Liveness Probe?**
   - Verifica si el contenedor está vivo
   - Si falla, Kubernetes lo reinicia

3. **¿Cuándo usar emptyDir vs PersistentVolume?**
   - emptyDir: datos temporales, se pierden al eliminar pod
   - PersistentVolume: datos persistentes

4. **¿Qué tipos de Services existen?**
   - ClusterIP: interno al cluster
   - NodePort: accesible por IP del nodo
   - LoadBalancer: crea LB externo

5. **¿Para qué sirven los Init Containers?**
   - Se ejecutan antes que los contenedores principales
   - Útiles para inicialización, wait de dependencias

---

# 🐳 Docker y Containerd - Guía Completa

## 📚 Índice
1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [Ciclo de Vida de Contenedores](#ciclo-de-vida-de-contenedores)
3. [Imágenes Docker](#imágenes-docker)
4. [Volúmenes y Almacenamiento](#volúmenes-y-almacenamiento)
5. [Redes Docker](#redes-docker)
6. [Docker Compose](#docker-compose)
7. [Containerd](#containerd)
8. [Troubleshooting](#troubleshooting)
9. [Ejercicios Prácticos](#ejercicios-prácticos)

---

## 1. Conceptos Fundamentales

### 🎯 ¿Qué es Docker?

Docker es una plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores.

**Componentes principales:**
- **Docker Engine**: Runtime que ejecuta contenedores
- **Docker Images**: Plantillas inmutables para contenedores
- **Docker Containers**: Instancias en ejecución de imágenes
- **Docker Registry**: Almacén de imágenes (Docker Hub)
- **Dockerfile**: Archivo de instrucciones para construir imágenes

**Arquitectura:**
```
┌─────────────────────────────────────┐
│         Docker Client               │
│  (docker CLI commands)              │
└───────────────┬─────────────────────┘
                │ REST API
┌───────────────▼─────────────────────┐
│         Docker Daemon               │
│  (dockerd)                          │
├─────────────────────────────────────┤
│  - Container Runtime                │
│  - Image Management                 │
│  - Network Management               │
│  - Volume Management                │
└───────────────┬─────────────────────┘
                │
┌───────────────▼─────────────────────┐
│      containerd (Runtime)           │
└───────────────┬─────────────────────┘
                │
┌───────────────▼─────────────────────┐
│        runc (OCI Runtime)           │
└─────────────────────────────────────┘
```

---

## 2. Ciclo de Vida de Contenedores

### 🚀 Comandos Básicos

```bash
# Ver contenedores
docker ps                              # Contenedores en ejecución
docker ps -a                           # Todos los contenedores
docker ps -q                           # Solo IDs
docker ps --filter "status=exited"     # Filtrar por estado

# Crear y ejecutar contenedor
docker run nginx                       # Crear y ejecutar
docker run -d nginx                    # Detached (background)
docker run -it ubuntu /bin/bash        # Interactive + TTY
docker run --name my-nginx nginx       # Con nombre personalizado
docker run -p 8080:80 nginx            # Mapeo de puertos
docker run -e VAR=value nginx          # Variables de entorno
docker run --rm nginx                  # Auto-eliminar al parar

# Ejemplo completo
docker run -d \
  --name web-server \
  --restart unless-stopped \
  -p 80:80 \
  -p 443:443 \
  -v /host/data:/container/data \
  -e MYSQL_ROOT_PASSWORD=secret \
  nginx:1.21

# Iniciar/Parar/Reiniciar
docker start container-name            # Iniciar contenedor parado
docker stop container-name             # Parar contenedor (SIGTERM)
docker stop -t 30 container-name       # Wait 30s antes de SIGKILL
docker kill container-name             # Forzar parada (SIGKILL)
docker restart container-name          # Reiniciar

# Pausar/Despausar
docker pause container-name            # Pausar procesos
docker unpause container-name          # Reanudar procesos

# Eliminar contenedores
docker rm container-name               # Eliminar contenedor parado
docker rm -f container-name            # Forzar eliminación
docker rm $(docker ps -aq)             # Eliminar todos
docker container prune                 # Eliminar contenedores parados
```

### 🔍 Inspección y Monitoreo

```bash
# Inspeccionar contenedor
docker inspect container-name          # Info completa en JSON
docker inspect -f '{{.State.Status}}' container-name
docker inspect -f '{{.NetworkSettings.IPAddress}}' container-name

# Ver logs
docker logs container-name             # Ver logs
docker logs -f container-name          # Follow logs
docker logs --tail 100 container-name  # Últimas 100 líneas
docker logs --since 30m container-name # Últimos 30 minutos
docker logs --timestamps container-name

# Estadísticas de recursos
docker stats                           # Stats de todos los contenedores
docker stats container-name            # Stats de uno específico
docker stats --no-stream               # Una sola vez (no streaming)

# Procesos
docker top container-name              # Ver procesos del contenedor
docker top container-name aux          # Formato completo

# Eventos
docker events                          # Ver eventos en tiempo real
docker events --since '2023-01-01'
```

### 💻 Ejecutar Comandos en Contenedores

```bash
# Ejecutar comando
docker exec container-name ls /app    # Ejecutar comando
docker exec -it container-name /bin/bash  # Shell interactivo
docker exec -u root container-name whoami  # Como usuario específico
docker exec -w /app container-name pwd     # En directorio específico

# Attach a contenedor en ejecución
docker attach container-name           # Conectar a STDOUT/STDERR

# Copiar archivos
docker cp container-name:/path/file.txt ./local/     # Del contenedor
docker cp ./local/file.txt container-name:/path/     # Al contenedor

# Ver cambios en filesystem
docker diff container-name             # Ver archivos modificados
```

---

## 3. Imágenes Docker

### 📦 Gestión de Imágenes

```bash
# Ver imágenes
docker images                          # Listar imágenes
docker images -a                       # Incluir intermedias
docker images -q                       # Solo IDs
docker images --filter "dangling=true" # Imágenes huérfanas

# Buscar imágenes
docker search nginx                    # Buscar en Docker Hub
docker search --limit 5 nginx          # Limitar resultados

# Descargar imágenes
docker pull nginx                      # Última versión
docker pull nginx:1.21                 # Versión específica
docker pull nginx:1.21-alpine          # Con tag
docker pull ubuntu@sha256:abc123...    # Por digest

# Eliminar imágenes
docker rmi image-name                  # Eliminar imagen
docker rmi -f image-name               # Forzar eliminación
docker image prune                     # Eliminar imágenes sin usar
docker image prune -a                  # Eliminar todas no usadas

# Información de imagen
docker inspect nginx                   # Info completa
docker history nginx                   # Ver capas de la imagen
docker image ls --digests              # Ver digests
```

### 📝 Dockerfile

```dockerfile
# Dockerfile - Ejemplo completo
FROM ubuntu:22.04

# Metadata
LABEL maintainer="you@example.com"
LABEL version="1.0"
LABEL description="My application"

# Variables de build
ARG APP_VERSION=1.0
ARG DEBIAN_FRONTEND=noninteractive

# Instalar dependencias
RUN apt-get update && \
    apt-get install -y \
        nginx \
        curl \
        vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Variables de entorno
ENV APP_HOME=/app \
    APP_USER=appuser \
    PATH=/app/bin:$PATH

# Crear usuario no-root
RUN useradd -m -u 1000 $APP_USER && \
    mkdir -p $APP_HOME && \
    chown -R $APP_USER:$APP_USER $APP_HOME

# Directorio de trabajo
WORKDIR $APP_HOME

# Copiar archivos
COPY --chown=$APP_USER:$APP_USER ./src ./
COPY --chown=$APP_USER:$APP_USER ./config/app.conf /etc/app/

# Agregar archivos (con auto-extract de tar)
ADD https://example.com/file.tar.gz /tmp/

# Exponer puertos
EXPOSE 8080 8443

# Volúmenes
VOLUME ["/data", "/logs"]

# Usuario por defecto
USER $APP_USER

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/health || exit 1

# Comando por defecto
CMD ["nginx", "-g", "daemon off;"]
# o
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["--config", "/etc/app/config.yaml"]
```

**Diferencias clave:**
- `CMD`: Comando por defecto, puede ser sobrescrito
- `ENTRYPOINT`: Punto de entrada fijo, CMD se pasa como argumentos
- `RUN`: Ejecuta comando en build time
- `CMD/ENTRYPOINT`: Ejecuta en runtime
- `COPY`: Copia archivos locales
- `ADD`: Como COPY pero con auto-extract y URLs

### 🏗️ Construir Imágenes

```bash
# Build básico
docker build -t myapp:1.0 .
docker build -t myapp:latest -t myapp:1.0 .  # Múltiples tags

# Con argumentos
docker build --build-arg APP_VERSION=2.0 -t myapp:2.0 .

# Sin cache
docker build --no-cache -t myapp:1.0 .

# Desde Dockerfile específico
docker build -f Dockerfile.prod -t myapp:prod .

# Multi-stage build
docker build --target production -t myapp:prod .

# Ver progreso
docker build --progress=plain -t myapp:1.0 .
```

**Dockerfile Multi-stage:**
```dockerfile
# Build stage
FROM golang:1.19 AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp

# Production stage
FROM alpine:3.17
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/myapp .
CMD ["./myapp"]
```

### 🏷️ Tags y Registry

```bash
# Etiquetar imagen
docker tag myapp:1.0 myregistry.com/myapp:1.0
docker tag myapp:1.0 myapp:latest

# Push a registry
docker login myregistry.com
docker push myregistry.com/myapp:1.0
docker logout myregistry.com

# Guardar/Cargar imágenes
docker save myapp:1.0 > myapp.tar        # Exportar
docker save myapp:1.0 | gzip > myapp.tar.gz
docker load < myapp.tar                  # Importar
docker load -i myapp.tar

# Exportar/Importar contenedor
docker export container-name > container.tar
docker import container.tar myapp:imported
```

---

## 4. Volúmenes y Almacenamiento

### 💾 Tipos de Almacenamiento

**1. Volumes (Recomendado):**
```bash
# Crear volumen
docker volume create my-volume
docker volume ls
docker volume inspect my-volume
docker volume rm my-volume
docker volume prune                    # Eliminar no usados

# Usar volumen
docker run -d \
  -v my-volume:/data \
  nginx

# Volumen anónimo
docker run -d -v /data nginx           # Docker crea nombre random
```

**2. Bind Mounts:**
```bash
# Montar directorio del host
docker run -d \
  -v /host/path:/container/path \
  nginx

# Con permisos readonly
docker run -d \
  -v /host/path:/container/path:ro \
  nginx

# Usando --mount (más explícito)
docker run -d \
  --mount type=bind,source=/host/path,target=/container/path \
  nginx
```

**3. tmpfs (memoria RAM):**
```bash
# Montar tmpfs
docker run -d \
  --tmpfs /tmp:rw,size=100m \
  nginx
```

### 📊 Comparación

| Tipo | Ubicación | Gestión | Uso |
|------|-----------|---------|-----|
| **Volume** | Docker area | Docker | Producción, persistencia |
| **Bind Mount** | Cualquier path | Usuario | Desarrollo, config |
| **tmpfs** | RAM | Docker | Datos temporales, sensibles |

```bash
# Ejemplos prácticos
# Base de datos con volumen
docker run -d \
  --name mysql \
  -v mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8

# Desarrollo con bind mount
docker run -d \
  --name dev-web \
  -v $(pwd)/src:/app/src \
  -p 3000:3000 \
  node:18

# Compartir volumen entre contenedores
docker run -d --name web -v shared-data:/data nginx
docker run -d --name backup --volumes-from web ubuntu
```

---

## 5. Redes Docker

### 🌐 Tipos de Redes

```bash
# Ver redes
docker network ls
docker network inspect bridge

# Crear redes
docker network create my-network
docker network create --driver bridge my-bridge
docker network create --subnet=172.18.0.0/16 my-subnet

# Conectar contenedor a red
docker run -d --name web --network my-network nginx
docker network connect my-network existing-container
docker network disconnect my-network existing-container

# Eliminar red
docker network rm my-network
docker network prune                   # Eliminar no usadas
```

**Tipos de drivers:**

1. **bridge** (default): Red privada en el host
```bash
docker network create --driver bridge isolated-network
docker run -d --name app1 --network isolated-network nginx
docker run -d --name app2 --network isolated-network mysql
# app1 y app2 pueden comunicarse por nombre
```

2. **host**: Usa la red del host directamente
```bash
docker run -d --network host nginx
# No hay aislamiento, usa puertos del host directamente
```

3. **none**: Sin red
```bash
docker run -d --network none nginx
```

4. **overlay**: Para Docker Swarm (multi-host)

### 🔗 Conectividad

```bash
# DNS interno
# Los contenedores en la misma red pueden resolverse por nombre
docker run -d --name web --network my-net nginx
docker run -d --name app --network my-net ubuntu

# Desde 'app':
# ping web
# curl http://web:80

# Alias de red
docker network connect --alias database my-network mysql-container

# Exponer puertos
docker run -d -p 8080:80 nginx                    # Host:Container
docker run -d -p 127.0.0.1:8080:80 nginx          # IP específica
docker run -d -P nginx                            # Puertos aleatorios
docker port container-name                        # Ver puertos

# Ver procesos y puertos
netstat -tulpn | grep docker
ss -tulpn | grep docker
```

---

## 6. Docker Compose

Docker Compose permite definir aplicaciones multi-contenedor.

### 📝 docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    image: nginx:1.21
    container_name: web-server
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - web-content:/usr/share/nginx/html
    environment:
      - NGINX_HOST=example.com
      - NGINX_PORT=80
    depends_on:
      - app
    networks:
      - frontend
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 30s
      timeout: 10s
      retries: 3
  
  app:
    build:
      context: ./app
      dockerfile: Dockerfile
      args:
        APP_VERSION: 1.0
    image: myapp:latest
    environment:
      - DATABASE_HOST=db
      - DATABASE_PORT=3306
      - DATABASE_NAME=${DB_NAME}
      - DATABASE_USER=${DB_USER}
      - DATABASE_PASSWORD=${DB_PASSWORD}
    env_file:
      - .env
    volumes:
      - ./app:/app
      - app-logs:/var/log/app
    depends_on:
      db:
        condition: service_healthy
    networks:
      - frontend
      - backend
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
  
  db:
    image: mysql:8.0
    container_name: mysql-db
    environment:
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
      - MYSQL_DATABASE=${DB_NAME}
      - MYSQL_USER=${DB_USER}
      - MYSQL_PASSWORD=${DB_PASSWORD}
    volumes:
      - db-data:/var/lib/mysql
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    networks:
      - backend
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
  
  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    networks:
      - backend

volumes:
  web-content:
  app-logs:
  db-data:
  redis-data:

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true
```

### 🎮 Comandos Docker Compose

```bash
# Iniciar servicios
docker-compose up                      # Foreground
docker-compose up -d                   # Detached
docker-compose up --build              # Build antes de iniciar
docker-compose up --force-recreate     # Recrear contenedores

# Parar y eliminar
docker-compose down                    # Para y elimina contenedores
docker-compose down -v                 # También elimina volúmenes
docker-compose down --rmi all          # También elimina imágenes

# Ver estado
docker-compose ps                      # Listar servicios
docker-compose ps -a                   # Incluir parados
docker-compose top                     # Ver procesos

# Logs
docker-compose logs                    # Todos los servicios
docker-compose logs -f web             # Follow de un servicio
docker-compose logs --tail=100 app     # Últimas 100 líneas

# Ejecutar comandos
docker-compose exec web bash           # Shell en servicio
docker-compose exec db mysql -u root -p
docker-compose run --rm app npm test   # Ejecutar comando one-off

# Escalar servicios
docker-compose up -d --scale app=3     # 3 instancias de app

# Build
docker-compose build                   # Build todos
docker-compose build app               # Build servicio específico
docker-compose build --no-cache        # Sin cache

# Validar
docker-compose config                  # Validar y ver configuración
docker-compose config --services       # Listar servicios
```

**.env file:**
```bash
# .env
DB_NAME=myapp
DB_USER=appuser
DB_PASSWORD=secret123
MYSQL_ROOT_PASSWORD=rootsecret
```

---

## 7. Containerd

Containerd es el runtime de contenedores de bajo nivel usado por Docker y Kubernetes.

### 🔧 Comandos Containerd (ctr)

```bash
# Namespace
ctr namespaces ls

# Imágenes
ctr -n k8s.io images ls                # Listar imágenes
ctr -n k8s.io images pull docker.io/library/nginx:latest
ctr -n k8s.io images rm nginx:latest

# Contenedores
ctr -n k8s.io containers ls            # Listar contenedores
ctr -n k8s.io containers info <id>     # Info de contenedor

# Tasks (procesos)
ctr -n k8s.io tasks ls                 # Listar tasks
ctr -n k8s.io tasks exec -t <id> sh    # Ejecutar comando

# Snapshots (capas)
ctr -n k8s.io snapshots ls
```

### 🎯 crictl (Kubernetes CRI)

```bash
# Pods
crictl pods                            # Listar pods
crictl pods --name my-pod
crictl inspectp <pod-id>               # Inspeccionar pod

# Contenedores
crictl ps                              # Contenedores en ejecución
crictl ps -a                           # Todos los contenedores
crictl inspect <container-id>

# Imágenes
crictl images                          # Listar imágenes
crictl rmi <image-id>                  # Eliminar imagen

# Logs y ejecución
crictl logs <container-id>
crictl exec -it <container-id> sh

# Stats
crictl stats                           # Estadísticas
crictl stats <container-id>
```

---

## 8. Troubleshooting

### 🔍 Diagnóstico Común

```bash
# Contenedor no inicia
docker logs container-name --tail 100
docker inspect container-name | grep -A 10 State
docker events --since '10m'

# Ver errores de salud
docker inspect --format='{{json .State.Health}}' container-name

# Verificar recursos
docker stats --no-stream
docker system df                       # Uso de disco

# Limpieza
docker system prune                    # Limpia todo no usado
docker system prune -a                 # Más agresivo
docker system prune -a --volumes       # Incluye volúmenes

# Ver espacio en disco
docker system df -v                    # Detallado

# Problemas de red
docker network inspect bridge
docker exec container-name ping -c 3 google.com
docker exec container-name netstat -tulpn
docker exec container-name ss -tulpn

# Problemas de permisos
docker exec -u 0 container-name ls -la /path
docker exec -u 0 container-name chown -R user:group /path
```

### 🐛 Problemas Comunes

**1. Contenedor se reinicia constantemente:**
```bash
docker logs container-name
docker inspect container-name | grep RestartCount
# Verificar comando de inicio, health checks, recursos
```

**2. "Cannot connect to Docker daemon":**
```bash
sudo systemctl status docker
sudo systemctl start docker
sudo usermod -aG docker $USER
newgrp docker
```

**3. Sin espacio en disco:**
```bash
docker system df
docker system prune -a --volumes
du -sh /var/lib/docker/*
```

**4. Puerto ya en uso:**
```bash
netstat -tulpn | grep :8080
lsof -i :8080
# Cambiar puerto o detener proceso
```

---

## 🎓 Preguntas Típicas

1. **¿Diferencia entre CMD y ENTRYPOINT?**
   - ENTRYPOINT: ejecutable fijo
   - CMD: argumentos por defecto, pueden sobrescribirse

2. **¿Cuándo usar volume vs bind mount?**
   - Volume: producción, gestionado por Docker
   - Bind mount: desarrollo, acceso directo a archivos del host

3. **¿Cómo optimizar tamaño de imagen?**
   - Multi-stage builds
   - Usar imágenes alpine
   - Limpiar cache en mismo RUN
   - .dockerignore

4. **¿Diferencia entre docker stop y docker kill?**
   - stop: envía SIGTERM, espera, luego SIGKILL
   - kill: envía SIGKILL inmediatamente

---

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

# 🤖 Ansible - Guía de Automatización

## 📚 Índice
1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [Inventarios](#inventarios)
3. [Playbooks](#playbooks)
4. [Roles](#roles)
5. [Variables](#variables)
6. [Módulos Importantes](#módulos-importantes)
7. [Troubleshooting](#troubleshooting)

---

## 1. Conceptos Fundamentales

### 🎯 ¿Qué es Ansible?

Ansible es una herramienta de automatización IT que permite:
- Configurar sistemas
- Desplegar aplicaciones
- Orquestar tareas complejas
- Sin necesidad de agentes (usa SSH)

**Características:**
- ✅ Agentless (sin agentes en nodos)
- ✅ Declarativo (describe el estado deseado)
- ✅ Idempotente (se puede ejecutar múltiples veces)
- ✅ YAML (fácil de leer y escribir)

**Componentes:**
- **Control Node**: Máquina donde se ejecuta Ansible
- **Managed Nodes**: Servidores gestionados
- **Inventory**: Lista de hosts
- **Playbook**: Archivo de automatización
- **Roles**: Forma de organizar playbooks
- **Modules**: Unidades de código ejecutables

---

## 2. Inventarios

### 📝 Formato INI

```ini
# inventory.ini
[webservers]
web1.example.com
web2.example.com ansible_host=192.168.1.10
web3.example.com ansible_port=2222

[databases]
db1.example.com
db2.example.com

[databases:vars]
ansible_user=dbadmin
ansible_ssh_private_key_file=~/.ssh/db_key

[production:children]
webservers
databases

[production:vars]
env=production
```

### 📝 Formato YAML

```yaml
# inventory.yml
all:
  children:
    webservers:
      hosts:
        web1.example.com:
        web2.example.com:
          ansible_host: 192.168.1.10
        web3.example.com:
          ansible_port: 2222
    
    databases:
      hosts:
        db1.example.com:
        db2.example.com:
      vars:
        ansible_user: dbadmin
        ansible_ssh_private_key_file: ~/.ssh/db_key
    
    production:
      children:
        webservers:
        databases:
      vars:
        env: production
```

### 🔧 Comandos de Inventario

```bash
# Listar hosts
ansible-inventory -i inventory.ini --list
ansible-inventory -i inventory.ini --graph
ansible all --list-hosts
ansible webservers --list-hosts

# Ping a hosts
ansible all -m ping
ansible webservers -m ping -i inventory.ini

# Variables de host
ansible-inventory -i inventory.ini --host web1.example.com
```

---

## 3. Playbooks

### 📜 Estructura Básica

```yaml
# playbook.yml
---
- name: Configure web servers
  hosts: webservers
  become: yes                    # Usar sudo
  become_user: root              # Usuario sudo
  gather_facts: yes              # Recolectar info del sistema
  
  vars:
    app_port: 8080
    app_user: webapp
  
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
    
    - name: Start nginx service
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Copy config file
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
        owner: root
        group: root
        mode: '0644'
      notify: Restart nginx
  
  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted
```

### 🎮 Ejecutar Playbooks

```bash
# Ejecución básica
ansible-playbook playbook.yml
ansible-playbook -i inventory.ini playbook.yml

# Con variables extras
ansible-playbook playbook.yml -e "app_port=9090"
ansible-playbook playbook.yml -e "@vars.yml"

# Check mode (dry-run)
ansible-playbook playbook.yml --check

# Diff mode (ver cambios)
ansible-playbook playbook.yml --check --diff

# Limitar a hosts específicos
ansible-playbook playbook.yml --limit web1.example.com
ansible-playbook playbook.yml --limit webservers

# Desde un task específico
ansible-playbook playbook.yml --start-at-task="Install nginx"

# Tags
ansible-playbook playbook.yml --tags "config"
ansible-playbook playbook.yml --skip-tags "slow"

# Verbose
ansible-playbook playbook.yml -v     # -v, -vv, -vvv, -vvvv
```

### 🎯 Características Avanzadas

```yaml
# playbook-advanced.yml
---
- name: Advanced playbook features
  hosts: all
  gather_facts: yes
  
  vars:
    packages:
      - nginx
      - git
      - curl
  
  tasks:
    # Condicionales
    - name: Install packages on Ubuntu
      apt:
        name: "{{ packages }}"
        state: present
      when: ansible_distribution == "Ubuntu"
    
    - name: Install packages on CentOS
      yum:
        name: "{{ packages }}"
        state: present
      when: ansible_distribution == "CentOS"
    
    # Loops
    - name: Create multiple users
      user:
        name: "{{ item }}"
        state: present
      loop:
        - alice
        - bob
        - charlie
    
    # Loop con diccionarios
    - name: Add users with details
      user:
        name: "{{ item.name }}"
        uid: "{{ item.uid }}"
        state: present
      loop:
        - { name: 'alice', uid: 1001 }
        - { name: 'bob', uid: 1002 }
    
    # Registro de resultados
    - name: Check if service exists
      command: systemctl status nginx
      register: nginx_status
      ignore_errors: yes
    
    - name: Show nginx status
      debug:
        var: nginx_status
    
    # Condicional con registro
    - name: Start nginx if not running
      service:
        name: nginx
        state: started
      when: nginx_status.rc != 0
    
    # Block (agrupación de tasks)
    - name: Configure application
      block:
        - name: Install dependencies
          apt:
            name: python3-pip
            state: present
        
        - name: Install python packages
          pip:
            name: flask
            state: present
      
      rescue:
        - name: Handle errors
          debug:
            msg: "Installation failed, rolling back"
      
      always:
        - name: Always cleanup
          file:
            path: /tmp/install
            state: absent
    
    # Tags
    - name: Configure firewall
      ufw:
        rule: allow
        port: 80
      tags:
        - security
        - firewall
```

---

## 4. Roles

### 📁 Estructura de un Rol

```
roles/
└── nginx/
    ├── README.md
    ├── defaults/
    │   └── main.yml        # Variables por defecto
    ├── files/
    │   └── index.html      # Archivos estáticos
    ├── handlers/
    │   └── main.yml        # Handlers
    ├── meta/
    │   └── main.yml        # Metadata y dependencias
    ├── tasks/
    │   └── main.yml        # Tasks principales
    ├── templates/
    │   └── nginx.conf.j2   # Templates Jinja2
    ├── tests/
    │   ├── inventory
    │   └── test.yml
    └── vars/
        └── main.yml        # Variables del rol
```

### 📝 Ejemplo de Rol

**tasks/main.yml:**
```yaml
---
# roles/nginx/tasks/main.yml
- name: Install nginx
  apt:
    name: nginx
    state: present
    update_cache: yes
  tags: install

- name: Copy nginx config
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
  notify: Restart nginx
  tags: config

- name: Ensure nginx is running
  service:
    name: nginx
    state: started
    enabled: yes
  tags: service
```

**handlers/main.yml:**
```yaml
---
# roles/nginx/handlers/main.yml
- name: Restart nginx
  service:
    name: nginx
    state: restarted

- name: Reload nginx
  service:
    name: nginx
    state: reloaded
```

**defaults/main.yml:**
```yaml
---
# roles/nginx/defaults/main.yml
nginx_port: 80
nginx_user: www-data
nginx_worker_processes: auto
nginx_worker_connections: 1024
```

**templates/nginx.conf.j2:**
```nginx
user {{ nginx_user }};
worker_processes {{ nginx_worker_processes }};

events {
    worker_connections {{ nginx_worker_connections }};
}

http {
    server {
        listen {{ nginx_port }};
        server_name {{ ansible_hostname }};
        
        location / {
            root /var/www/html;
            index index.html;
        }
    }
}
```

### 🎮 Usar Roles

```yaml
# playbook-with-roles.yml
---
- name: Configure web servers
  hosts: webservers
  become: yes
  
  roles:
    - common
    - nginx
    - { role: deploy_app, app_version: '1.2.3' }
  
  # O con tasks antes/después
  pre_tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
  
  roles:
    - nginx
  
  post_tasks:
    - name: Verify nginx
      uri:
        url: http://localhost
        return_content: yes
```

```bash
# Crear estructura de rol
ansible-galaxy init nginx
ansible-galaxy init roles/myapp

# Instalar roles de Ansible Galaxy
ansible-galaxy install geerlingguy.nginx
ansible-galaxy install -r requirements.yml

# requirements.yml
# - name: geerlingguy.nginx
#   version: 3.1.4
# - src: https://github.com/user/role.git
#   name: custom-role
```

---

## 5. Variables

### 📊 Precedencia de Variables (menor a mayor)

1. role defaults
2. inventory file/script group vars
3. inventory group_vars/all
4. playbook group_vars/all
5. inventory group_vars/*
6. playbook group_vars/*
7. inventory file/script host vars
8. inventory host_vars/*
9. playbook host_vars/*
10. host facts
11. play vars
12. play vars_prompt
13. play vars_files
14. role vars
15. block vars
16. task vars
17. extra vars (-e)

### 📝 Definir Variables

```yaml
# En playbook
---
- name: Example
  hosts: all
  vars:
    app_name: myapp
    app_version: "1.0"
  vars_files:
    - vars/main.yml
    - vars/secrets.yml
  
  tasks:
    - name: Show variable
      debug:
        msg: "{{ app_name }} version {{ app_version }}"
```

```yaml
# group_vars/webservers.yml
---
http_port: 80
https_port: 443
server_name: www.example.com
```

```yaml
# host_vars/web1.example.com.yml
---
server_id: 1
backup_server: yes
```

### 🎯 Usar Variables

```yaml
# Variables simples
- name: Install {{ package_name }}
  apt:
    name: "{{ package_name }}"
    state: present

# Variables de diccionario
user:
  name: john
  uid: 1001
  shell: /bin/bash

- name: Create user
  user:
    name: "{{ user.name }}"
    uid: "{{ user['uid'] }}"
    shell: "{{ user.shell }}"

# Variables de lista
packages:
  - nginx
  - git
  - curl

- name: Install packages
  apt:
    name: "{{ item }}"
    state: present
  loop: "{{ packages }}"

# Facts (variables del sistema)
- debug:
    msg: "{{ ansible_hostname }}"
- debug:
    msg: "{{ ansible_default_ipv4.address }}"
- debug:
    msg: "{{ ansible_distribution }} {{ ansible_distribution_version }}"

# Variables registradas
- name: Get service status
  command: systemctl status nginx
  register: result
  
- debug:
    var: result.stdout_lines
```

---

## 6. Módulos Importantes

### 📦 Gestión de Paquetes

```yaml
# APT (Debian/Ubuntu)
- name: Install packages
  apt:
    name:
      - nginx
      - git
    state: present
    update_cache: yes

# YUM/DNF (CentOS/RHEL)
- name: Install packages
  yum:
    name: nginx
    state: latest

# PIP (Python)
- name: Install python packages
  pip:
    name: flask
    version: 2.0.1
    state: present
```

### 📁 Archivos y Directorios

```yaml
# Crear directorio
- name: Create directory
  file:
    path: /app/data
    state: directory
    owner: appuser
    group: appgroup
    mode: '0755'

# Crear archivo
- name: Create file
  file:
    path: /app/config.txt
    state: touch
    mode: '0644'

# Copiar archivo
- name: Copy file
  copy:
    src: files/config.yaml
    dest: /etc/app/config.yaml
    owner: root
    mode: '0644'

# Template (Jinja2)
- name: Deploy config template
  template:
    src: templates/app.conf.j2
    dest: /etc/app/app.conf
    backup: yes

# Línea en archivo
- name: Add line to file
  lineinfile:
    path: /etc/hosts
    line: "192.168.1.10 server1.local"
    state: present

# Bloque en archivo
- name: Add block to file
  blockinfile:
    path: /etc/nginx/nginx.conf
    block: |
      server {
          listen 8080;
      }
    marker: "# {mark} ANSIBLE MANAGED BLOCK"
```

### 👤 Usuarios y Grupos

```yaml
# Crear usuario
- name: Create user
  user:
    name: appuser
    uid: 1001
    group: appgroup
    shell: /bin/bash
    home: /home/appuser
    create_home: yes
    state: present

# Crear grupo
- name: Create group
  group:
    name: appgroup
    gid: 1001
    state: present
```

### 🔧 Servicios

```yaml
# Gestionar servicio
- name: Start nginx
  service:
    name: nginx
    state: started
    enabled: yes

# Systemd
- name: Reload systemd
  systemd:
    daemon_reload: yes

- name: Enable service
  systemd:
    name: myapp
    enabled: yes
    state: started
```

### 💻 Comandos y Scripts

```yaml
# Comando simple
- name: Run command
  command: /usr/bin/uptime
  register: uptime_result

# Shell (con pipes y redirects)
- name: Run shell command
  shell: echo "test" | grep test > /tmp/output.txt

# Script
- name: Run script
  script: scripts/deploy.sh
  args:
    creates: /tmp/deployed.flag
```

### 🌐 Git

```yaml
# Clonar repositorio
- name: Clone repository
  git:
    repo: https://github.com/user/repo.git
    dest: /app/repo
    version: main
    force: yes
```

### 🐳 Docker

```yaml
# Contenedor Docker
- name: Run nginx container
  docker_container:
    name: nginx
    image: nginx:latest
    state: started
    ports:
      - "80:80"
    volumes:
      - /host/data:/data
```
--- 

### 🐛 Comandos de Troubleshooting

```bash
# Syntax check
ansible-playbook playbook.yml --syntax-check

# Dry run
ansible-playbook playbook.yml --check

# Ver cambios
ansible-playbook playbook.yml --check --diff

# Modo verbose
ansible-playbook playbook.yml -vvv

# Step mode (confirmar cada task)
ansible-playbook playbook.yml --step

# Listar tasks
ansible-playbook playbook.yml --list-tasks
ansible-playbook playbook.yml --list-tags

# Probar conexión
ansible all -m ping -i inventory.ini
ansible all -m setup -i inventory.ini  # Gather facts
```

---

## 🎓 Preguntas Típicas

1. **¿Qué es idempotencia?**
   - Ejecutar múltiples veces produce el mismo resultado

2. **¿Diferencia entre copy y template?**
   - copy: archivos estáticos
   - template: procesados con Jinja2

3. **¿Cuándo usar command vs shell?**
   - command: comandos simples, más seguro
   - shell: cuando necesitas pipes, redirects

4. **¿Qué hace un handler?**
   - Task que se ejecuta cuando es notificado
   - Se ejecuta al final del playbook
   - Útil para reiniciar servicios

---

# 🏗️ Terraform - Infrastructure as Code

## 📚 Índice
1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [Sintaxis HCL](#sintaxis-hcl)
3. [Providers y Recursos](#providers-y-recursos)
4. [Variables y Outputs](#variables-y-outputs)
5. [State Management](#state-management)
6. [Módulos](#módulos)
7. [Troubleshooting](#troubleshooting)

---

## 1. Conceptos Fundamentales

### 🎯 ¿Qué es Terraform?

Terraform es una herramienta de Infrastructure as Code (IaC) que permite:
- Definir infraestructura en código
- Provisionar recursos en múltiples providers
- Gestionar el ciclo de vida de la infraestructura
- Trabajar con estado compartido

**Componentes clave:**
- **Provider**: Plugin para interactuar con APIs (AWS, Azure, GCP, etc.)
- **Resource**: Componente de infraestructura (VM, red, disco)
- **Data Source**: Información de recursos existentes
- **Module**: Conjunto reutilizable de recursos
- **State**: Registro del estado actual de la infraestructura

### 🔄 Workflow Terraform

```bash
# 1. Inicializar (descargar providers)
terraform init

# 2. Planear (ver cambios)
terraform plan

# 3. Aplicar (ejecutar cambios)
terraform apply

# 4. Destruir (eliminar recursos)
terraform destroy
```

---

## 2. Sintaxis HCL

### 📝 Estructura Básica

```hcl
# main.tf

# Provider configuration
terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Resource
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  tags = {
    Name = "WebServer"
    Env  = "Production"
  }
}

# Data source
data "aws_ami" "ubuntu" {
  most_recent = true
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
  
  owners = ["099720109477"]
}

# Output
output "instance_ip" {
  value = aws_instance.web.public_ip
}
```

### 🔤 Tipos de Bloques

```hcl
# Terraform block - configuración global
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}

# Variable block
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

# Local values
locals {
  common_tags = {
    Project = "MyApp"
    Env     = var.environment
  }
}

# Module block
module "vpc" {
  source = "./modules/vpc"
  
  cidr_block = "10.0.0.0/16"
  tags       = local.common_tags
}
```

---

## 3. Providers y Recursos

### ☁️ AWS Provider Example

```hcl
# providers.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region     = var.aws_region
  access_key = var.aws_access_key  # Mejor usar AWS CLI config
  secret_key = var.aws_secret_key  # o variables de entorno
}

# Multiple providers (multi-region)
provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

# Use specific provider
resource "aws_instance" "west_server" {
  provider = aws.west
  
  ami           = "ami-123456"
  instance_type = "t2.micro"
}
```

### 🖥️ Recursos Comunes

```hcl
# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "main-vpc"
  }
}

# Subnet
resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
  
  map_public_ip_on_launch = true
  
  tags = {
    Name = "public-subnet"
  }
}

# Security Group
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group for web servers"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    description = "HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    description = "HTTPS from anywhere"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "web-sg"
  }
}

# EC2 Instance
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  subnet_id     = aws_subnet.public.id
  
  vpc_security_group_ids = [aws_security_group.web.id]
  
  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y nginx
              systemctl start nginx
              EOF
  
  tags = {
    Name = "web-server"
  }
}

# EBS Volume
resource "aws_ebs_volume" "data" {
  availability_zone = aws_instance.web.availability_zone
  size              = 20
  
  tags = {
    Name = "data-volume"
  }
}

resource "aws_volume_attachment" "data_attach" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.data.id
  instance_id = aws_instance.web.id
}
```

### 🔗 Referencias entre Recursos

```hcl
# Implicit dependency (reference)
resource "aws_instance" "web" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public.id  # Referencia
}

# Explicit dependency
resource "aws_instance" "app" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
  
  depends_on = [
    aws_security_group.web,
    aws_subnet.public
  ]
}
```

---

## 4. Variables y Outputs

### 📊 Variables

```hcl
# variables.tf
variable "environment" {
  description = "Environment name"
  type        = string
  default     = "development"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
  
  validation {
    condition     = contains(["t2.micro", "t2.small", "t2.medium"], var.instance_type)
    error_message = "Instance type must be t2.micro, t2.small, or t2.medium."
  }
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

variable "tags" {
  description = "Resource tags"
  type        = map(string)
  default = {
    Project = "MyApp"
    Managed = "Terraform"
  }
}

variable "server_config" {
  description = "Server configuration"
  type = object({
    instance_type = string
    disk_size     = number
    enable_backup = bool
  })
  default = {
    instance_type = "t2.micro"
    disk_size     = 20
    enable_backup = true
  }
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}
```

**Formas de asignar variables:**

```bash
# 1. Archivo terraform.tfvars
# terraform.tfvars
environment = "production"
instance_type = "t2.small"

# 2. Archivo .tfvars específico
terraform apply -var-file="prod.tfvars"

# 3. Línea de comandos
terraform apply -var="instance_type=t2.small"

# 4. Variables de entorno
export TF_VAR_instance_type="t2.small"
terraform apply

# 5. Interactivo (si no está definida)
terraform apply
# > var.instance_type
#   Enter a value:
```

### 📤 Outputs

```hcl
# outputs.tf
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.web.id
}

output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.web.public_ip
}

output "instance_private_ip" {
  description = "Private IP of the EC2 instance"
  value       = aws_instance.web.private_ip
  sensitive   = false
}

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

# Output from module
output "vpc_cidr" {
  value = module.vpc.vpc_cidr_block
}
```

```bash
# Ver outputs
terraform output
terraform output instance_public_ip
terraform output -json
```

---

## 5. State Management

### 💾 Terraform State

El state file (`terraform.tfstate`) almacena el estado actual de la infraestructura.

```bash
# Ver state
terraform show
terraform state list
terraform state show aws_instance.web

# Manipular state
terraform state mv aws_instance.old aws_instance.new
terraform state rm aws_instance.web
terraform state pull > backup.tfstate
terraform state push backup.tfstate

# Refresh state
terraform refresh
terraform apply -refresh-only
```

### 🗄️ Remote State

```hcl
# Backend S3 (AWS)
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

# Backend Azure
terraform {
  backend "azurerm" {
    resource_group_name  = "terraform-rg"
    storage_account_name = "tfstate"
    container_name       = "tfstate"
    key                  = "prod.terraform.tfstate"
  }
}

# Backend GCS (Google Cloud)
terraform {
  backend "gcs" {
    bucket = "my-terraform-state"
    prefix = "prod"
  }
}
```

```bash
# Inicializar backend
terraform init

# Migrar backend
terraform init -migrate-state

# Reconfigurar backend
terraform init -reconfigure
```

### 🔒 State Locking

```hcl
# DynamoDB table para locking (AWS)
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  
  attribute {
    name = "LockID"
    type = "S"
  }
}
```

---

## 6. Módulos

### 📦 Crear Módulo

```
modules/
└── vpc/
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    └── README.md
```

**modules/vpc/main.tf:**
```hcl
resource "aws_vpc" "main" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support   = var.enable_dns_support
  
  tags = merge(
    var.tags,
    {
      Name = var.vpc_name
    }
  )
}

resource "aws_subnet" "public" {
  count = length(var.public_subnet_cidrs)
  
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.public_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]
  
  map_public_ip_on_launch = true
  
  tags = merge(
    var.tags,
    {
      Name = "${var.vpc_name}-public-${count.index + 1}"
    }
  )
}
```

**modules/vpc/variables.tf:**
```hcl
variable "vpc_name" {
  description = "Name of the VPC"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for VPC"
  type        = string
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
}

variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
}

variable "enable_dns_hostnames" {
  description = "Enable DNS hostnames"
  type        = bool
  default     = true
}

variable "enable_dns_support" {
  description = "Enable DNS support"
  type        = bool
  default     = true
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}
```

**modules/vpc/outputs.tf:**
```hcl
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "vpc_cidr_block" {
  description = "CIDR block of the VPC"
  value       = aws_vpc.main.cidr_block
}

output "public_subnet_ids" {
  description = "IDs of public subnets"
  value       = aws_subnet.public[*].id
}
```

### 🎮 Usar Módulo

```hcl
# main.tf
module "vpc" {
  source = "./modules/vpc"
  
  vpc_name             = "production-vpc"
  cidr_block           = "10.0.0.0/16"
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24"]
  availability_zones   = ["us-east-1a", "us-east-1b"]
  
  tags = {
    Environment = "production"
    Project     = "myapp"
  }
}

# Usar outputs del módulo
resource "aws_instance" "web" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
  subnet_id     = module.vpc.public_subnet_ids[0]
}

output "vpc_id" {
  value = module.vpc.vpc_id
}
```

---

## 7. Troubleshooting

### 🔍 Comandos de Debugging

```bash
# Validar sintaxis
terraform validate

# Formatear código
terraform fmt
terraform fmt -recursive

# Ver plan detallado
terraform plan -out=tfplan
terraform show tfplan

# Aplicar con log
TF_LOG=DEBUG terraform apply
TF_LOG=TRACE terraform apply
TF_LOG_PATH=terraform.log terraform apply

# Graph (dependencias)
terraform graph | dot -Tpng > graph.png

# Console interactivo
terraform console
> aws_instance.web.public_ip
> var.instance_type
```

### 🐛 Problemas Comunes

**1. State lock:**
```bash
# Forzar unlock (usar con cuidado)
terraform force-unlock <LOCK_ID>
```

**2. State drift:**
```bash
# Refresh state
terraform refresh
terraform apply -refresh-only

# Comparar
terraform plan
```

**3. Import recursos existentes:**
```bash
# Importar recurso
terraform import aws_instance.web i-1234567890abcdef0

# Generar configuración (Terraform 1.5+)
terraform plan -generate-config-out=generated.tf
```

**4. Destruir recurso específico:**
```bash
terraform destroy -target=aws_instance.web
```

---

## 🎓 Preguntas Típicas

1. **¿Qué es el state de Terraform?**
   - Archivo que mapea configuración con recursos reales
   - Almacena metadata y estado actual

2. **¿Diferencia entre plan y apply?**
   - plan: muestra cambios sin aplicar
   - apply: ejecuta los cambios

3. **¿Para qué sirven los módulos?**
   - Reutilizar configuración
   - Organizar código
   - Abstracción y encapsulación

4. **¿Cómo manejar secretos?**
   - Variables sensibles
   - Vault/secrets managers
   - Backends cifrados

5. **¿Qué es un provider?**
   - Plugin que interactúa con APIs
   - Define recursos disponibles

---

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

# ☁️ OpenStack - Guía Básica

## 📚 Índice
1. [¿Qué es OpenStack?](#qué-es-openstack)
2. [Arquitectura y Componentes](#arquitectura-y-componentes)
3. [CLI Essentials](#cli-essentials)
4. [Conceptos Clave](#conceptos-clave)

---

## 1. ¿Qué es OpenStack?

OpenStack es una plataforma open source de cloud computing para crear y gestionar nubes públicas y privadas.

**Casos de uso:**
- Infraestructura como Servicio (IaaS)
- Nubes privadas empresariales
- NFV (Network Functions Virtualization)
- Plataformas de telecomunicaciones

---

## 2. Arquitectura y Componentes

### 🏗️ Componentes Principales

| Componente | Servicio | Función |
|------------|----------|---------|
| **Nova** | Compute | Gestión de instancias (VMs) |
| **Neutron** | Networking | Redes virtuales, routers, firewalls |
| **Cinder** | Block Storage | Volúmenes persistentes |
| **Swift** | Object Storage | Almacenamiento de objetos (S3-like) |
| **Glance** | Image | Gestión de imágenes (OS templates) |
| **Keystone** | Identity | Autenticación y autorización |
| **Horizon** | Dashboard | UI web |
| **Heat** | Orchestration | Templates de infraestructura (IaC) |

### 🔄 Flujo de Trabajo

```
User → Keystone (auth) → Horizon/CLI
                          ↓
        Nova (create VM) → Glance (get image)
                          ↓
                       Neutron (setup network)
                          ↓
                       Cinder (attach volume)
```

---

## 3. CLI Essentials

### 🔧 Configuración

```bash
# Instalar cliente
pip install python-openstackclient

# Variables de entorno (openrc)
export OS_AUTH_URL=http://controller:5000/v3
export OS_PROJECT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=secret
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_DOMAIN_NAME=Default
export OS_IDENTITY_API_VERSION=3

# Source el archivo
source openrc
```

### 📦 Comandos Básicos

```bash
# Ver información
openstack --version
openstack --help

# Autenticación
openstack token issue

# Listados generales
openstack catalog list          # Servicios disponibles
openstack endpoint list         # Endpoints de servicios
```

### 🖼️ Glance - Imágenes

```bash
# Listar imágenes
openstack image list
openstack image show <image-id>

# Crear imagen
openstack image create "Ubuntu 20.04" \
  --file ubuntu-20.04.qcow2 \
  --disk-format qcow2 \
  --container-format bare \
  --public

# Eliminar imagen
openstack image delete <image-id>
```

### 💻 Nova - Compute

```bash
# Listar instancias
openstack server list
openstack server list --all-projects
openstack server show <instance-id>

# Crear instancia
openstack server create \
  --flavor m1.small \
  --image ubuntu-20.04 \
  --network private \
  --key-name my-key \
  --security-group default \
  my-instance

# Gestionar instancia
openstack server start <instance>
openstack server stop <instance>
openstack server reboot <instance>
openstack server delete <instance>

# Flavor (tamaños de VM)
openstack flavor list
openstack flavor show m1.small

# Keypairs
openstack keypair create --public-key ~/.ssh/id_rsa.pub my-key
openstack keypair list
openstack keypair delete my-key

# Console
openstack console url show <instance>
openstack console log show <instance>
```

### 🌐 Neutron - Networking

```bash
# Redes
openstack network list
openstack network show <network>
openstack network create private-net

# Subnets
openstack subnet list
openstack subnet create private-subnet \
  --network private-net \
  --subnet-range 192.168.1.0/24 \
  --gateway 192.168.1.1 \
  --dns-nameserver 8.8.8.8

# Routers
openstack router list
openstack router create my-router
openstack router set --external-gateway public my-router
openstack router add subnet my-router private-subnet

# Security Groups
openstack security group list
openstack security group create web-sg
openstack security group rule create \
  --protocol tcp \
  --dst-port 80:80 \
  --remote-ip 0.0.0.0/0 \
  web-sg

# Floating IPs
openstack floating ip list
openstack floating ip create public
openstack server add floating ip <instance> <floating-ip>

# Ports
openstack port list
openstack port show <port-id>
```

### 💾 Cinder - Block Storage

```bash
# Volúmenes
openstack volume list
openstack volume show <volume-id>

# Crear volumen
openstack volume create \
  --size 10 \
  --type ssd \
  my-volume

# Attach/Detach
openstack server add volume <instance> <volume>
openstack server remove volume <instance> <volume>

# Snapshot
openstack volume snapshot create \
  --volume <volume-id> \
  my-snapshot

# Eliminar
openstack volume delete <volume-id>
```

### 👥 Keystone - Identity

```bash
# Proyectos
openstack project list
openstack project create --domain default dev-project

# Usuarios
openstack user list
openstack user create --project dev-project \
  --password secret123 \
  devuser

# Roles
openstack role list
openstack role add --project dev-project --user devuser member

# Domains
openstack domain list
```

---

## 4. Conceptos Clave

### 🎯 Flavors

Definen el tamaño de las instancias (vCPUs, RAM, disco).

```bash
openstack flavor list

# Crear flavor personalizado
openstack flavor create \
  --ram 2048 \
  --disk 20 \
  --vcpus 2 \
  custom.medium
```

### 🔐 Security Groups

Reglas de firewall para instancias.

```bash
# Regla SSH
openstack security group rule create \
  --protocol tcp \
  --dst-port 22 \
  --remote-ip 0.0.0.0/0 \
  default

# Regla HTTP
openstack security group rule create \
  --protocol tcp \
  --dst-port 80 \
  --remote-ip 0.0.0.0/0 \
  web-sg
```

### 🌍 Networking Concepts

**Network Types:**
- **Tenant/Private**: Redes aisladas por proyecto
- **Provider/External**: Redes físicas/públicas
- **Shared**: Compartidas entre proyectos

**Floating IPs:**
- IPs públicas asignables a instancias
- Permiten acceso desde internet

### 📊 Quotas

```bash
# Ver quotas
openstack quota show <project>

# Modificar quotas
openstack quota set --instances 20 <project>
openstack quota set --cores 40 <project>
openstack quota set --ram 51200 <project>
```

---

## 🎓 Preguntas Típicas

1. **¿Qué es Nova?**
   - Servicio de compute, gestiona VMs

2. **¿Diferencia entre Cinder y Swift?**
   - Cinder: block storage (volúmenes)
   - Swift: object storage (archivos)

3. **¿Para qué sirve Keystone?**
   - Autenticación y autorización
   - Gestión de usuarios, proyectos, roles

4. **¿Qué es un flavor?**
   - Plantilla de recursos para VMs
   - Define vCPUs, RAM, disco

5. **¿Cómo funciona Neutron?**
   - Redes virtuales, subnets, routers
   - Security groups, floating IPs

---

# 📊 Sistemas de Monitoreo - Guía Básica

## 📚 Índice
1. [Grafana](#grafana)
2. [Kibana](#kibana)
3. [Prometheus](#prometheus)
4. [Zabbix](#zabbix)
5. [Nagios](#nagios)

---

## 1. Grafana

### 🎯 ¿Qué es Grafana?

Plataforma de visualización y analytics para métricas.

**Características:**
- Dashboards interactivos
- Múltiples datasources (Prometheus, InfluxDB, Elasticsearch)
- Alertas
- Plugins

### 🚀 Conceptos Básicos

```bash
# Instalar (Docker)
docker run -d -p 3000:3000 grafana/grafana

# Acceder: http://localhost:3000
# User/Pass default: admin/admin
```

**Componentes:**
- **Dashboard**: Colección de panels
- **Panel**: Visualización individual (gráfico, tabla, etc.)
- **Datasource**: Origen de datos (Prometheus, MySQL, etc.)
- **Query**: Consulta a datasource
- **Alert**: Notificación basada en condición

---

## 2. Kibana

### 🎯 ¿Qué es Kibana?

UI de visualización para Elasticsearch (parte del ELK Stack).

**ELK Stack:**
- **E**lasticsearch: Motor de búsqueda
- **L**ogstash: Procesamiento de logs
- **K**ibana: Visualización

### 📊 Uso Básico

```bash
# Kibana con Docker
docker run -d -p 5601:5601 \
  -e ELASTICSEARCH_HOSTS=http://elasticsearch:9200 \
  kibana:8.0.0

# Acceder: http://localhost:5601
```

**Funcionalidades:**
- **Discover**: Explorar logs
- **Visualize**: Crear gráficos
- **Dashboard**: Combinar visualizaciones
- **Dev Tools**: Consultas a Elasticsearch

**Ejemplo de consulta:**
```json
GET /logs-*/_search
{
  "query": {
    "match": {
      "level": "ERROR"
    }
  }
}
```

---

## 3. Prometheus

### 🎯 ¿Qué es Prometheus?

Sistema de monitoreo y alertas basado en métricas.

**Características:**
- Time-series database
- Pull model (scraping)
- PromQL (lenguaje de consulta)
- Alertmanager

### 📝 Configuración Básica

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
  
  - job_name: 'kubernetes'
    kubernetes_sd_configs:
      - role: pod
```

### 🔍 PromQL Ejemplos

```promql
# CPU usage
rate(cpu_usage_seconds_total[5m])

# Memory disponible
node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100

# HTTP requests por segundo
rate(http_requests_total[1m])

# Error rate
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))
```

---

## 4. Zabbix

### 🎯 ¿Qué es Zabbix?

Plataforma enterprise de monitoreo para redes y aplicaciones.

**Características:**
- Agentless o con agente
- Auto-discovery
- Templates
- Triggers y alertas

### 🔧 Conceptos

```bash
# Instalar agente
apt install zabbix-agent

# Configurar
nano /etc/zabbix/zabbix_agentd.conf
# Server=192.168.1.10
# Hostname=web-server-01

systemctl restart zabbix-agent
```

**Componentes:**
- **Server**: Servidor central
- **Agent**: Recolector en hosts
- **Proxy**: Para redes distribuidas
- **Frontend**: UI web

**Items comunes:**
- system.cpu.load
- vm.memory.size
- net.if.in[eth0]
- vfs.fs.size[/,used]

---

## 5. Nagios

### 🎯 ¿Qué es Nagios?

Sistema de monitoreo de infraestructura IT.

**Características:**
- Monitoreo de hosts y servicios
- Plugins extensibles
- Alertas
- Reporting

### 📝 Configuración Ejemplo

```bash
# /etc/nagios/objects/hosts.cfg
define host {
    use                     linux-server
    host_name               web-server-01
    alias                   Web Server 01
    address                 192.168.1.10
}

# /etc/nagios/objects/services.cfg
define service {
    use                     generic-service
    host_name               web-server-01
    service_description     HTTP
    check_command           check_http
}

define service {
    use                     generic-service
    host_name               web-server-01
    service_description     SSH
    check_command           check_ssh
}
```

**Checks comunes:**
```bash
check_ping
check_http
check_ssh
check_disk
check_load
check_memory
```

---

## 🎯 Comparación Rápida

| Tool | Tipo | Uso Principal |
|------|------|---------------|
| **Grafana** | Visualización | Dashboards de métricas |
| **Kibana** | Visualización | Análisis de logs (ELK) |
| **Prometheus** | Métricas | Time-series, K8s |
| **Zabbix** | All-in-one | Enterprise monitoring |
| **Nagios** | Alerting | Monitoreo tradicional |

---

## 🎓 Preguntas Típicas

1. **¿Para qué sirve Grafana?**
   - Visualización de métricas
   - Dashboards interactivos

2. **¿Qué es el ELK Stack?**
   - Elasticsearch + Logstash + Kibana
   - Para gestión y análisis de logs

3. **¿Cómo funciona Prometheus?**
   - Pull model (scraping)
   - Time-series database
   - PromQL para consultas

4. **¿Diferencia entre Zabbix y Nagios?**
   - Zabbix: más moderno, auto-discovery
   - Nagios: más veterano, simple

---


# 📊 Prometheus - Guía Completa

## 🎯 ¿Qué es Prometheus?

Prometheus es un sistema de monitoreo y alerting open-source diseñado para confiabilidad y escalabilidad. Es el estándar de facto en Kubernetes y cloud-native applications.

---

## 🔑 Conceptos Fundamentales

### Arquitectura

```
┌─────────────┐
│  Your Apps  │──── Instrumentación (métricas)
└─────────────┘
       │
       ▼
┌─────────────┐
│  Exporters  │──── Exponen métricas en formato Prometheus
└─────────────┘
       │
       ▼ (HTTP Pull)
┌─────────────┐
│ Prometheus  │──── Scraping, almacenamiento, queries
│   Server    │
└─────────────┘
       │
       ├──▶ ┌──────────┐
       │    │ Grafana  │──── Visualización
       │    └──────────┘
       │
       └──▶ ┌──────────────┐
            │ Alertmanager │──── Notificaciones
            └──────────────┘
```

### Tipos de Métricas

| Tipo | Descripción | Ejemplo | Cuándo usar |
|------|-------------|---------|-------------|
| **Counter** | Solo incrementa (nunca baja) | `http_requests_total` | Requests, errores, tareas completadas |
| **Gauge** | Puede subir o bajar | `memory_usage_bytes` | Temperatura, memoria, conexiones activas |
| **Histogram** | Muestras observaciones en buckets | `http_request_duration_seconds` | Latencias, tamaños de response |
| **Summary** | Similar a histogram, calcula cuantiles | `rpc_duration_seconds` | Latencias con percentiles |

---

## 📝 PromQL: Lenguaje de Queries

### Queries Básicas

```promql
# 1. Selección simple - obtener métrica actual
http_requests_total

# 2. Filtrado por labels
http_requests_total{status="200", method="GET"}

# 3. Regex en labels
http_requests_total{status=~"2.."}  # status 200-299
http_requests_total{path!~"/health.*"}  # path que NO empiece con /health

# 4. Range vectors - datos en un rango de tiempo
http_requests_total[5m]  # últimos 5 minutos
```

### Funciones Esenciales

#### 1. `rate()` - Tasa de cambio por segundo
```promql
# Requests por segundo (últimos 5 minutos)
rate(http_requests_total[5m])

# SIEMPRE usar con counters
# NUNCA con gauges
```

#### 2. `irate()` - Instant rate (más sensible)
```promql
# Rate instantáneo (últimos 2 puntos)
irate(http_requests_total[5m])

# Útil para detectar spikes rápidos
```

#### 3. `increase()` - Incremento total
```promql
# Total de requests en la última hora
increase(http_requests_total[1h])
```

#### 4. Agregaciones
```promql
# Sum - total across all instances
sum(rate(http_requests_total[5m]))

# Avg - promedio
avg(node_cpu_seconds_total) by (mode)

# Max/Min
max(memory_usage_bytes) by (pod)
min(memory_usage_bytes) by (pod)

# Count - número de series
count(up == 1)  # servicios UP
```

#### 5. `by` y `without` - Agrupación
```promql
# Agrupar POR ciertos labels
sum(rate(http_requests_total[5m])) by (status, method)

# Mantener TODOS los labels EXCEPTO estos
sum(rate(http_requests_total[5m])) without (instance, pod)
```

---

## 🔥 Top 20 Queries para el Test

### HTTP / API Monitoring

```promql
# 1. Request rate total
sum(rate(http_requests_total[5m]))

# 2. Request rate por status code
sum(rate(http_requests_total[5m])) by (status)

# 3. Error rate (porcentaje)
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) * 100

# 4. Success rate (%)
sum(rate(http_requests_total{status=~"2.."}[5m])) / sum(rate(http_requests_total[5m])) * 100

# 5. Latencia promedio (histogram)
rate(http_request_duration_seconds_sum[5m]) / rate(http_request_duration_seconds_count[5m])

# 6. Latencia p95
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

# 7. Latencia p99
histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))
```

### CPU Monitoring

```promql
# 8. CPU usage por nodo
100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# 9. CPU usage de containers
sum(rate(container_cpu_usage_seconds_total[5m])) by (pod)

# 10. Top 5 pods con más CPU
topk(5, sum(rate(container_cpu_usage_seconds_total[5m])) by (pod))
```

### Memory Monitoring

```promql
# 11. Memory usage (bytes)
container_memory_usage_bytes

# 12. Memory usage (%)
container_memory_usage_bytes / container_spec_memory_limit_bytes * 100

# 13. Memory available en nodos
node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100

# 14. Pods cerca del límite de memoria (>80%)
(container_memory_usage_bytes / container_spec_memory_limit_bytes) > 0.8
```

### Disk & Network

```promql
# 15. Disk usage (%)
(node_filesystem_size_bytes - node_filesystem_free_bytes) / node_filesystem_size_bytes * 100

# 16. Network received rate
rate(node_network_receive_bytes_total[5m])

# 17. Network transmitted rate
rate(node_network_transmit_bytes_total[5m])
```

### Availability & Uptime

```promql
# 18. Services UP vs DOWN
up

# 19. Availability en últimas 24h (%)
avg_over_time(up[24h]) * 100

# 20. Alert: service down > 5 minutos
up == 0
```

---

## 🚨 Alertas en Prometheus

### Estructura de una Alert Rule

```yaml
# prometheus-alerts.yml
groups:
  - name: example_alerts
    interval: 30s
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m])) by (service)
          /
          sum(rate(http_requests_total[5m])) by (service)
          > 0.05
        for: 5m
        labels:
          severity: critical
          team: backend
        annotations:
          summary: "High error rate on {{ $labels.service }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

### Componentes de una Alerta

| Campo | Descripción |
|-------|-------------|
| `alert` | Nombre de la alerta |
| `expr` | Query PromQL (condición) |
| `for` | Duración antes de disparar |
| `labels` | Metadata para routing |
| `annotations` | Información descriptiva |

### Alertas Comunes (Memorizar)

```yaml
# 1. CPU alto
- alert: HighCPU
  expr: node_cpu_usage > 80
  for: 5m

# 2. Memory alto
- alert: HighMemory
  expr: (node_memory_usage_bytes / node_memory_total_bytes) > 0.85
  for: 5m

# 3. Disk lleno
- alert: DiskAlmostFull
  expr: (node_filesystem_free_bytes / node_filesystem_size_bytes) < 0.1
  for: 10m

# 4. Pod crasheando
- alert: PodCrashLooping
  expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
  for: 5m

# 5. Service down
- alert: ServiceDown
  expr: up == 0
  for: 2m

# 6. High latency
- alert: HighLatency
  expr: histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])) > 1
  for: 5m

# 7. Error rate alto
- alert: HighErrorRate
  expr: |
    sum(rate(http_requests_total{status=~"5.."}[5m])) 
    / 
    sum(rate(http_requests_total[5m])) > 0.05
  for: 5m
```

---

## 📦 Exporters Comunes

### ¿Qué es un Exporter?

Un exporter es un servicio que:
1. Colecta métricas de un sistema/aplicación
2. Las expone en formato Prometheus
3. Prometheus las "scrape" vía HTTP

### Exporters Esenciales

| Exporter | Monitorea | Puerto | Uso |
|----------|-----------|--------|-----|
| **node_exporter** | Métricas de sistema Linux | 9100 | CPU, RAM, disk, network |
| **kube-state-metrics** | Estado de objetos K8s | 8080 | Pods, deployments, nodes |
| **blackbox_exporter** | Endpoints externos | 9115 | HTTP, ICMP, TCP, DNS |
| **mysqld_exporter** | MySQL/MariaDB | 9104 | Queries, connections |
| **postgres_exporter** | PostgreSQL | 9187 | Queries, connections |
| **redis_exporter** | Redis | 9121 | Keys, memory, commands |
| **elasticsearch_exporter** | Elasticsearch | 9114 | Cluster health, indices |

### Configuración de Scraping

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node1:9100', 'node2:9100']
    scrape_interval: 15s
    scrape_timeout: 10s

  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
```

---

## 🎓 Ejemplos Prácticos

### Ejemplo 1: Monitorear un Servicio Web

```yaml
# Métricas expuestas por tu app en /metrics
http_requests_total{method="GET", status="200", path="/api/users"} 1543
http_requests_total{method="POST", status="201", path="/api/users"} 234
http_request_duration_seconds_bucket{le="0.1"} 1200
http_request_duration_seconds_bucket{le="0.5"} 1700
http_request_duration_seconds_bucket{le="1.0"} 1750
http_request_duration_seconds_bucket{le="+Inf"} 1777

# Queries útiles:
# Request rate por endpoint
sum(rate(http_requests_total[5m])) by (path)

# Latencia p95 por endpoint
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (path, le))
```

### Ejemplo 2: Monitorear Kubernetes

```promql
# Pods no ready
kube_pod_status_ready{condition="false"} == 1

# Deployments con réplicas insuficientes
kube_deployment_status_replicas_available / kube_deployment_spec_replicas < 1

# Nodes con alta presión de memoria
kube_node_status_condition{condition="MemoryPressure", status="true"} == 1

# CPU throttling en containers
rate(container_cpu_cfs_throttled_seconds_total[5m]) > 0.1
```

### Ejemplo 3: Calcular SLI (Service Level Indicator)

```promql
# SLI: Availability (% de requests exitosos)
sum(rate(http_requests_total{status=~"2.."}[30d])) 
/ 
sum(rate(http_requests_total[30d])) * 100

# SLI: Latency (% de requests bajo 500ms)
sum(rate(http_request_duration_seconds_bucket{le="0.5"}[30d])) 
/ 
sum(rate(http_request_duration_seconds_count[30d])) * 100

# Error Budget (si SLO es 99.9% availability)
# Error budget = 100 - 99.9 = 0.1%
# Requests que pueden fallar:
sum(rate(http_requests_total[30d])) * 0.001
```

---

## ❓ Preguntas Típicas de TestGorilla

### Pregunta 1: Tipo de Métrica
**P: ¿Qué tipo de métrica deberías usar para monitorear el número total de requests HTTP?**
- A) Gauge
- B) Counter ✅
- C) Histogram
- D) Summary

**R: B) Counter** - Porque el total de requests solo incrementa, nunca decrece.

### Pregunta 2: PromQL
**P: ¿Cuál query muestra la tasa de requests por segundo en los últimos 5 minutos?**
- A) `http_requests_total[5m]`
- B) `rate(http_requests_total[5m])` ✅
- C) `irate(http_requests_total[5m])`
- D) `increase(http_requests_total[5m])`

**R: B) rate()** - Calcula la tasa por segundo en el rango especificado.

### Pregunta 3: Alertas
**P: ¿Qué hace el parámetro `for: 5m` en una alerta?**
- A) La alerta se ejecuta cada 5 minutos
- B) La condición debe ser verdadera por 5 minutos antes de disparar ✅
- C) La alerta expira después de 5 minutos
- D) La alerta envía notificaciones cada 5 minutos

**R: B)** - `for` define el tiempo que la condición debe mantenerse antes de activar la alerta.

### Pregunta 4: Debugging
**P: Un counter muestra valores decrecientes en tu query. ¿Cuál es la causa más probable?**
- A) Error en la instrumentación
- B) El servicio se reinició ✅
- C) Prometheus tiene un bug
- D) La query está mal escrita

**R: B)** - Los counters se resetean a 0 cuando un servicio se reinicia. Usa `rate()` o `increase()` para manejar esto.

---

# 🐍 Python para DevOps/SRE - Guía Completa

## 🎯 ¿Por qué Python en DevOps?

Python es el lenguaje preferido para automatización, scripting y herramientas DevOps por:
- ✅ Sintaxis clara y legible
- ✅ Librerías excelentes para system admin (psutil, requests, paramiko)
- ✅ Integración con APIs REST
- ✅ Procesamiento de datos (JSON, YAML, CSV)
- ✅ Amplia comunidad y documentación

---

## 📚 Conceptos Básicos

### Variables y Tipos de Datos

```python
# Variables (tipado dinámico)
name = "Juan"
age = 25
is_admin = True
salary = 50000.50

# None (equivalente a null)
config = None

# Type hints (Python 3.5+)
def greet(name: str) -> str:
    return f"Hola, {name}"

# Múltiples asignaciones
x, y, z = 1, 2, 3

# Swap
a, b = b, a
```

### Strings

```python
# Strings básicos
name = "DevOps Engineer"
company = 'Whitestack'

# Multi-línea
config = """
server:
  host: localhost
  port: 8080
"""

# f-strings (Python 3.6+) - RECOMENDADO
name = "Juan"
age = 25
print(f"Hola {name}, tienes {age} años")
print(f"El doble es {age * 2}")

# Métodos útiles
text = "  hello world  "
text.strip()           # "hello world"
text.upper()           # "  HELLO WORLD  "
text.lower()           # "  hello world  "
text.replace("world", "python")  # "  hello python  "
text.split()           # ["hello", "world"]

# Verificaciones
"hello" in text        # True
text.startswith("  ")  # True
text.endswith("  ")    # True

# Join
words = ["hello", "world"]
"-".join(words)        # "hello-world"
```

### Listas (Arrays)

```python
# Crear lista
servers = ["web1", "web2", "db1"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

# Acceder elementos
servers[0]           # "web1"
servers[-1]          # "db1" (último)
servers[0:2]         # ["web1", "web2"] (slice)

# Modificar
servers.append("cache1")      # Agregar al final
servers.insert(0, "lb1")      # Insertar en posición
servers.remove("db1")         # Eliminar por valor
servers.pop()                 # Eliminar último
servers.pop(0)                # Eliminar por índice

# Búsqueda
"web1" in servers            # True
servers.index("web2")        # 1
servers.count("web1")        # 1

# Ordenar
numbers.sort()               # Modifica lista
sorted(numbers)              # Retorna nueva lista
servers.reverse()            # Invertir

# List comprehension (muy usado!)
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Transformar
servers_upper = [s.upper() for s in servers]
```

### Diccionarios (Maps/Objects)

```python
# Crear diccionario
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

# Acceder
config["host"]              # "localhost"
config.get("host")          # "localhost"
config.get("missing", "default")  # "default"

# Modificar
config["timeout"] = 30      # Agregar/modificar
del config["debug"]         # Eliminar

# Verificar
"host" in config            # True
"missing" in config         # False

# Iterar
for key in config:
    print(key, config[key])

for key, value in config.items():
    print(f"{key}: {value}")

# Keys y values
config.keys()               # dict_keys(['host', 'port', ...])
config.values()             # dict_values(['localhost', 8080, ...])

# Dict comprehension
squared = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Sets (Conjuntos)

```python
# Crear set (elementos únicos)
servers = {"web1", "web2", "web3"}
numbers = {1, 2, 3, 3, 3}  # {1, 2, 3}

# Operaciones
servers.add("db1")
servers.remove("web1")
"web2" in servers          # True

# Operaciones de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1 | set2                # {1, 2, 3, 4, 5} - unión
set1 & set2                # {3} - intersección
set1 - set2                # {1, 2} - diferencia
```

---

## 🔄 Control de Flujo

### If-Elif-Else

```python
age = 25

if age < 18:
    print("Menor de edad")
elif age < 65:
    print("Adulto")
else:
    print("Senior")

# Ternario
status = "Mayor" if age >= 18 else "Menor"

# Múltiples condiciones
if age > 18 and age < 65:
    print("Adulto trabajador")

if status == "admin" or status == "root":
    print("Acceso total")

# Verificar None
config = None
if config is None:
    print("Config no definido")

# Verificar vacío
if not servers:  # Lista vacía
    print("No hay servers")

if servers:  # Lista con elementos
    print("Hay servers")
```

### Loops

```python
# For loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Iterar lista
servers = ["web1", "web2", "db1"]
for server in servers:
    print(server)

# Con índice
for i, server in enumerate(servers):
    print(f"{i}: {server}")

# Iterar diccionario
config = {"host": "localhost", "port": 8080}
for key, value in config.items():
    print(f"{key} = {value}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break y continue
for i in range(10):
    if i == 3:
        continue  # Saltar esta iteración
    if i == 7:
        break     # Salir del loop
    print(i)

# Else en loops (raramente usado)
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completado sin break")
```

---

## 🔧 Funciones

### Funciones Básicas

```python
# Función simple
def greet(name):
    return f"Hola, {name}"

result = greet("Juan")

# Con valor por defecto
def greet(name="Usuario"):
    return f"Hola, {name}"

greet()          # "Hola, Usuario"
greet("Juan")    # "Hola, Juan"

# Múltiples parámetros
def add(a, b):
    return a + b

# Type hints
def add(a: int, b: int) -> int:
    return a + b

# Múltiples returns
def get_stats():
    return 100, 200, 300

cpu, memory, disk = get_stats()

# *args - argumentos variables
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4, 5)  # 15

# **kwargs - argumentos con nombre
def print_config(**config):
    for key, value in config.items():
        print(f"{key}: {value}")

print_config(host="localhost", port=8080, debug=True)

# Docstrings
def calculate_cpu(usage: float, cores: int) -> float:
    """
    Calcula el uso de CPU en %.
    
    Args:
        usage: Uso actual de CPU
        cores: Número de cores
    
    Returns:
        Porcentaje de uso
    """
    return (usage / cores) * 100
```

### Lambda Functions

```python
# Lambda (funciones anónimas)
square = lambda x: x ** 2
square(5)  # 25

# Con map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Con filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# Con sorted
servers = [{"name": "web1", "cpu": 80}, {"name": "db1", "cpu": 60}]
sorted_servers = sorted(servers, key=lambda x: x["cpu"])
```

---

## 📦 Módulos y Imports

```python
# Import completo
import os
import sys
import json

os.path.exists("/tmp")
json.loads('{"key": "value"}')

# Import específico
from os import path, environ
from datetime import datetime, timedelta

path.exists("/tmp")
now = datetime.now()

# Import con alias
import requests as req
import pandas as pd
import numpy as np

response = req.get("http://example.com")

# Import todo (no recomendado)
from os import *

# Import relativo (mismo package)
from .module import function
from ..parent import something
```

### Módulos Útiles para DevOps

```python
# OS y Sistema
import os
import sys
import subprocess
import shutil
import glob

# Archivos y paths
from pathlib import Path
import tempfile

# Tiempo
import time
from datetime import datetime, timedelta

# Networking
import socket
import requests
import urllib

# Datos
import json
import yaml
import csv
import configparser

# System monitoring
import psutil

# Regex
import re

# Logging
import logging

# Argumentos CLI
import argparse

# Variables de entorno
from dotenv import load_dotenv
```

---

## 📁 Trabajar con Archivos

### Leer y Escribir

```python
# Leer archivo completo
with open("file.txt", "r") as f:
    content = f.read()

# Leer línea por línea
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Leer todas las líneas en lista
with open("file.txt", "r") as f:
    lines = f.readlines()

# Escribir archivo
with open("output.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

# Append
with open("log.txt", "a") as f:
    f.write(f"[{datetime.now()}] Log entry\n")

# Escribir lista de líneas
lines = ["line1\n", "line2\n", "line3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# Pathlib (moderno)
from pathlib import Path

file = Path("data.txt")
content = file.read_text()
file.write_text("nuevo contenido")

# Verificar existencia
if file.exists():
    print("Archivo existe")

if file.is_file():
    print("Es un archivo")

if file.is_dir():
    print("Es un directorio")
```

### JSON

```python
import json

# Leer JSON
with open("config.json", "r") as f:
    config = json.load(f)

# Escribir JSON
data = {"name": "server1", "port": 8080}
with open("config.json", "w") as f:
    json.dump(data, f, indent=2)

# String to dict
json_string = '{"key": "value"}'
data = json.loads(json_string)

# Dict to string
json_string = json.dumps(data, indent=2)

# Pretty print
print(json.dumps(data, indent=2))
```

### YAML

```python
import yaml

# Leer YAML
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Escribir YAML
data = {
    "server": {
        "host": "localhost",
        "port": 8080
    }
}
with open("config.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)
```

### CSV

```python
import csv

# Leer CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # Lista de valores

# Leer CSV con dict
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# Escribir CSV
data = [
    ["Name", "Age", "City"],
    ["Juan", 25, "Madrid"],
    ["María", 30, "Barcelona"]
]
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Escribir dict a CSV
data = [
    {"name": "Juan", "age": 25},
    {"name": "María", "age": 30}
]
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)
```

---

## 🌐 Trabajar con APIs (Requests)

```python
import requests

# GET request
response = requests.get("https://api.example.com/data")
print(response.status_code)  # 200
print(response.text)         # Response body
data = response.json()       # Parse JSON

# Con headers
headers = {
    "Authorization": "Bearer token123",
    "Content-Type": "application/json"
}
response = requests.get("https://api.example.com/data", headers=headers)

# Con query parameters
params = {"limit": 10, "offset": 0}
response = requests.get("https://api.example.com/data", params=params)
# URL: https://api.example.com/data?limit=10&offset=0

# POST request
data = {"name": "server1", "type": "web"}
response = requests.post("https://api.example.com/servers", json=data)

# PUT request
response = requests.put("https://api.example.com/servers/1", json=data)

# DELETE request
response = requests.delete("https://api.example.com/servers/1")

# Timeout
response = requests.get("https://api.example.com/data", timeout=5)

# Error handling
try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # Raise exception si status >= 400
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timeout")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# Session (mantiene cookies, headers)
session = requests.Session()
session.headers.update({"Authorization": "Bearer token"})
response = session.get("https://api.example.com/data")
```

---

## 🖥️ System Administration (psutil)

```python
import psutil
import os

# CPU
cpu_percent = psutil.cpu_percent(interval=1)
cpu_count = psutil.cpu_count()
cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)

# Memory
memory = psutil.virtual_memory()
print(f"Total: {memory.total / (1024**3):.2f} GB")
print(f"Used: {memory.used / (1024**3):.2f} GB")
print(f"Percent: {memory.percent}%")

# Disk
disk = psutil.disk_usage('/')
print(f"Total: {disk.total / (1024**3):.2f} GB")
print(f"Used: {disk.used / (1024**3):.2f} GB")
print(f"Free: {disk.free / (1024**3):.2f} GB")
print(f"Percent: {disk.percent}%")

# Disk I/O
disk_io = psutil.disk_io_counters()
print(f"Read: {disk_io.read_bytes / (1024**2):.2f} MB")
print(f"Write: {disk_io.write_bytes / (1024**2):.2f} MB")

# Network
net_io = psutil.net_io_counters()
print(f"Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
print(f"Recv: {net_io.bytes_recv / (1024**2):.2f} MB")

# Procesos
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
    print(proc.info)

# Proceso específico
proc = psutil.Process(os.getpid())
print(f"CPU: {proc.cpu_percent()}")
print(f"Memory: {proc.memory_info().rss / (1024**2):.2f} MB")
print(f"Threads: {proc.num_threads()}")
print(f"Files: {len(proc.open_files())}")

# Boot time
import datetime
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
print(f"Boot time: {boot_time}")
```

---

## 🐚 Ejecutar Comandos Shell

```python
import subprocess
import os

# Run simple command
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
print(result.returncode)

# Con shell (cuidado con seguridad!)
result = subprocess.run("ls -la | grep .txt", shell=True, capture_output=True, text=True)

# Check si comando exitoso
try:
    subprocess.run(["ls", "/nonexistent"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with code {e.returncode}")

# Capturar output
output = subprocess.check_output(["date"])
print(output.decode())

# Con timeout
try:
    subprocess.run(["sleep", "10"], timeout=5)
except subprocess.TimeoutExpired:
    print("Command timeout")

# Input a comando
result = subprocess.run(
    ["grep", "error"],
    input="line1\nerror in line2\nline3",
    text=True,
    capture_output=True
)
print(result.stdout)  # "error in line2"

# Pipe entre comandos (método correcto)
ps = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
grep = subprocess.Popen(["grep", "python"], stdin=ps.stdout, stdout=subprocess.PIPE)
ps.stdout.close()
output = grep.communicate()[0]

# Alternativa con os.system (legacy, evitar)
os.system("ls -la")
```

---

## 🔍 Regular Expressions (Regex)

```python
import re

text = "Server: web1, IP: 192.168.1.100, Port: 8080"

# Buscar
match = re.search(r"IP: ([\d.]+)", text)
if match:
    print(match.group(1))  # "192.168.1.100"

# Buscar todas las ocurrencias
ips = re.findall(r"\d+\.\d+\.\d+\.\d+", text)
# ["192.168.1.100"]

# Replace
new_text = re.sub(r"\d+\.\d+\.\d+\.\d+", "10.0.0.1", text)

# Split
parts = re.split(r",\s*", text)

# Match completo
if re.match(r"Server:", text):
    print("Empieza con 'Server:'")

# Compiled regex (mejor performance si se usa múltiples veces)
ip_pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")
ips = ip_pattern.findall(text)

# Grupos nombrados
match = re.search(r"IP: (?P<ip>[\d.]+)", text)
if match:
    print(match.group("ip"))

# Ejemplos útiles para DevOps
log_line = "2024-01-15 10:30:45 ERROR Failed to connect"
match = re.search(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)", log_line)
if match:
    date, time, level, message = match.groups()
```

---

## 📝 Logging

```python
import logging

# Configuración básica
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()  # También en consola
    ]
)

logger = logging.getLogger(__name__)

# Niveles de log
logger.debug("Debug message")      # Desarrollo
logger.info("Info message")        # Info general
logger.warning("Warning message")  # Advertencia
logger.error("Error message")      # Error
logger.critical("Critical!")       # Crítico

# Con variables
user = "admin"
logger.info(f"User {user} logged in")

# Con exception
try:
    1 / 0
except Exception as e:
    logger.error("Error occurred", exc_info=True)  # Incluye traceback
    # O más corto:
    logger.exception("Error occurred")

# Logger avanzado
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Usar
logger.info("Application started")
```

---

## 🎯 CLI Arguments (argparse)

```python
import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Monitor de servicios',
        epilog='Ejemplo: python monitor.py --host localhost --port 8080'
    )
    
    # Argumentos posicionales
    parser.add_argument('action', choices=['start', 'stop', 'status'])
    
    # Argumentos opcionales
    parser.add_argument(
        '--host',
        default='localhost',
        help='Host to monitor'
    )
    
    parser.add_argument(
        '-p', '--port',
        type=int,
        default=8080,
        help='Port number'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',  # Flag boolean
        help='Verbose output'
    )
    
    parser.add_argument(
        '--config',
        type=argparse.FileType('r'),
        help='Config file'
    )
    
    # Parse
    args = parser.parse_args()
    
    # Usar
    print(f"Action: {args.action}")
    print(f"Host: {args.host}")
    print(f"Port: {args.port}")
    
    if args.verbose:
        print("Verbose mode enabled")
    
    if args.config:
        content = args.config.read()

if __name__ == '__main__':
    main()

# Uso:
# python script.py start --host example.com -p 9000 -v
```

---

## 🔐 Variables de Entorno

```python
import os
from dotenv import load_dotenv

# Leer variable de entorno
db_host = os.environ.get('DB_HOST', 'localhost')  # Con default
api_key = os.environ['API_KEY']  # Sin default (error si no existe)

# Establecer variable
os.environ['MY_VAR'] = 'value'

# .env file (requiere python-dotenv)
# .env:
# DB_HOST=localhost
# DB_PORT=5432
# DB_PASSWORD=secret

load_dotenv()  # Cargar .env
db_host = os.environ['DB_HOST']
```

---

## 🚨 Error Handling

```python
# Try-except básico
try:
    result = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")

# Múltiples excepciones
try:
    # código
    pass
except ValueError:
    print("Error de valor")
except KeyError:
    print("Key no encontrada")
except (TypeError, AttributeError) as e:
    print(f"Error de tipo o atributo: {e}")

# Capturar todas las excepciones
try:
    # código
    pass
except Exception as e:
    print(f"Error: {e}")

# Finally (siempre se ejecuta)
try:
    f = open("file.txt")
    # código
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    f.close()  # Siempre se ejecuta

# Else (se ejecuta si no hay excepción)
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print(f"Resultado: {result}")

# Raise exception
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# Custom exception
class ConfigError(Exception):
    pass

def load_config():
    raise ConfigError("Config file missing")
```

---

## 🎓 Scripts Útiles para DevOps

### 1. Health Check de URLs

```python
#!/usr/bin/env python3
import requests
import sys

urls = [
    "https://api.example.com/health",
    "https://web.example.com",
    "https://db.example.com:5432"
]

failed = []

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✓ {url}")
        else:
            print(f"✗ {url} - Status {response.status_code}")
            failed.append(url)
    except requests.exceptions.RequestException as e:
        print(f"✗ {url} - Error: {e}")
        failed.append(url)

if failed:
    print(f"\n{len(failed)} checks failed")
    sys.exit(1)
else:
    print("\nAll checks passed")
    sys.exit(0)
```

### 2. Limpiar Logs Viejos

```python
#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timedelta

log_dir = Path("/var/log/myapp")
days_to_keep = 7
cutoff = datetime.now() - timedelta(days=days_to_keep)

for log_file in log_dir.glob("*.log*"):
    mtime = datetime.fromtimestamp(log_file.stat().st_mtime)
    if mtime < cutoff:
        print(f"Deleting {log_file}")
        log_file.unlink()
```

### 3. Parse de Logs

```python
#!/usr/bin/env python3
import re
from collections import Counter

log_file = "/var/log/nginx/access.log"
ip_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')

ips = []
with open(log_file) as f:
    for line in f:
        match = ip_pattern.search(line)
        if match:
            ips.append(match.group(1))

# Top 10 IPs
top_ips = Counter(ips).most_common(10)
for ip, count in top_ips:
    print(f"{ip}: {count} requests")
```

---

## ✅ Best Practices

1. **Use virtual environments**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Type hints**
```python
def process_data(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}
```

3. **Docstrings**
```python
def calculate(x: int, y: int) -> int:
    """Calculate sum of two numbers.
    
    Args:
        x: First number
        y: Second number
    
    Returns:
        Sum of x and y
    """
    return x + y
```

4. **Context managers**
```python
# Siempre usar with para archivos
with open("file.txt") as f:
    content = f.read()
# Archivo se cierra automáticamente
```

5. **List comprehensions > loops**
```python
# ✅ Pythonic
squares = [x**2 for x in range(10)]

# ❌ No pythonic
squares = []
for x in range(10):
    squares.append(x**2)
```

---

## 📚 Librerías Esenciales DevOps

```bash
# Instalar con pip
pip install psutil          # System monitoring
pip install requests        # HTTP requests
pip install pyyaml          # YAML
pip install python-dotenv   # .env files
pip install paramiko        # SSH
pip install fabric          # Deployment
pip install ansible         # Automation
pip install docker          # Docker API
pip install kubernetes      # K8s API
pip install prometheus-client  # Prometheus
pip install click           # CLI apps (alternativa a argparse)
```

---

# 🚀 CI/CD y GitOps - Guía Práctica

## 🎯 ¿Qué es CI/CD?

**CI (Continuous Integration)**: Integrar código frecuentemente con tests automáticos  
**CD (Continuous Delivery)**: Deploy automático a ambientes (staging, producción)

---

## 🔄 GitLab CI - Lo más usado en empresas

### Archivo: `.gitlab-ci.yml`

```yaml
# Stages del pipeline
stages:
  - test
  - build
  - deploy

# Variables globales
variables:
  DOCKER_REGISTRY: "registry.example.com"
  APP_NAME: "myapp"

# Job: Tests
test:
  stage: test
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - pytest tests/
    - flake8 .
  coverage: '/TOTAL.*\s+(\d+%)$/'
  only:
    - merge_requests
    - main

# Job: Build Docker Image
build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $DOCKER_REGISTRY
    - docker build -t $DOCKER_REGISTRY/$APP_NAME:$CI_COMMIT_SHA .
    - docker build -t $DOCKER_REGISTRY/$APP_NAME:latest .
    - docker push $DOCKER_REGISTRY/$APP_NAME:$CI_COMMIT_SHA
    - docker push $DOCKER_REGISTRY/$APP_NAME:latest
  only:
    - main

# Job: Deploy to Staging
deploy_staging:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context staging
    - kubectl set image deployment/$APP_NAME $APP_NAME=$DOCKER_REGISTRY/$APP_NAME:$CI_COMMIT_SHA
    - kubectl rollout status deployment/$APP_NAME
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - main

# Job: Deploy to Production (manual)
deploy_production:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context production
    - kubectl set image deployment/$APP_NAME $APP_NAME=$DOCKER_REGISTRY/$APP_NAME:$CI_COMMIT_SHA
    - kubectl rollout status deployment/$APP_NAME
  environment:
    name: production
    url: https://example.com
  when: manual  # Requiere aprobación manual
  only:
    - main
```

---

### GitLab CI - Ejemplos Avanzados

#### Pipeline con Tests, Security Scan, y Deploy

```yaml
stages:
  - test
  - security
  - build
  - deploy

# Tests unitarios
unit_tests:
  stage: test
  image: node:18-alpine
  script:
    - npm ci
    - npm run test:unit
  coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

# Tests de integración
integration_tests:
  stage: test
  image: node:18-alpine
  services:
    - postgres:14
    - redis:7
  variables:
    DATABASE_URL: "postgresql://test:test@postgres:5432/testdb"
    REDIS_URL: "redis://redis:6379"
  script:
    - npm ci
    - npm run test:integration

# Lint
lint:
  stage: test
  image: node:18-alpine
  script:
    - npm ci
    - npm run lint
    - npm run format:check

# Security scan con Trivy
security_scan:
  stage: security
  image: aquasec/trivy:latest
  script:
    - trivy image --severity HIGH,CRITICAL $DOCKER_REGISTRY/$APP_NAME:latest
  allow_failure: true

# SAST (Static Application Security Testing)
sast:
  stage: security
  image: returntocorp/semgrep
  script:
    - semgrep --config=auto --json --output=sast-report.json .
  artifacts:
    reports:
      sast: sast-report.json

# Build multi-arch
build_multiarch:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $DOCKER_REGISTRY
    - docker buildx create --use
  script:
    - docker buildx build \
        --platform linux/amd64,linux/arm64 \
        --tag $DOCKER_REGISTRY/$APP_NAME:$CI_COMMIT_SHA \
        --tag $DOCKER_REGISTRY/$APP_NAME:latest \
        --push .
  only:
    - main

# Deploy con Helm
deploy_helm:
  stage: deploy
  image: alpine/helm:latest
  script:
    - helm upgrade --install $APP_NAME ./helm-chart \
        --set image.tag=$CI_COMMIT_SHA \
        --set ingress.host=staging.example.com \
        --namespace staging \
        --create-namespace \
        --wait
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - main
```

---

## 🔧 GitHub Actions

### Archivo: `.github/workflows/ci.yml`

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # Tests
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov flake8
      
      - name: Run tests
        run: |
          pytest --cov=. --cov-report=xml
      
      - name: Lint
        run: flake8 .
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml

  # Build Docker Image
  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.event_name == 'push'
    permissions:
      contents: read
      packages: write
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Log in to Container Registry
        uses: docker/login-action@v2
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v4
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=sha,prefix={{branch}}-
            type=semver,pattern={{version}}
      
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}

  # Deploy to staging
  deploy_staging:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment:
      name: staging
      url: https://staging.example.com
    
    steps:
      - name: Deploy to Kubernetes
        uses: azure/k8s-deploy@v4
        with:
          namespace: staging
          manifests: |
            k8s/deployment.yaml
            k8s/service.yaml
          images: |
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
```

---

## 🎯 Jenkins Pipeline

### Jenkinsfile (Declarative)

```groovy
pipeline {
    agent any
    
    environment {
        DOCKER_REGISTRY = 'registry.example.com'
        APP_NAME = 'myapp'
        DOCKER_CREDENTIALS = credentials('docker-registry-creds')
        KUBECONFIG = credentials('kubeconfig')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    pip install -r requirements.txt
                    pytest tests/ --junitxml=test-results.xml
                    flake8 . --output-file=flake8-report.txt
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REGISTRY}", 'docker-registry-creds') {
                        def app = docker.build("${APP_NAME}:${BUILD_NUMBER}")
                        app.push()
                        app.push('latest')
                    }
                }
            }
        }
        
        stage('Security Scan') {
            steps {
                sh "trivy image ${DOCKER_REGISTRY}/${APP_NAME}:${BUILD_NUMBER}"
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    kubectl --kubeconfig=$KUBECONFIG set image \
                        deployment/${APP_NAME} \
                        ${APP_NAME}=${DOCKER_REGISTRY}/${APP_NAME}:${BUILD_NUMBER} \
                        -n staging
                    
                    kubectl --kubeconfig=$KUBECONFIG rollout status \
                        deployment/${APP_NAME} \
                        -n staging
                '''
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy to production?', ok: 'Deploy'
                
                sh '''
                    kubectl --kubeconfig=$KUBECONFIG set image \
                        deployment/${APP_NAME} \
                        ${APP_NAME}=${DOCKER_REGISTRY}/${APP_NAME}:${BUILD_NUMBER} \
                        -n production
                    
                    kubectl --kubeconfig=$KUBECONFIG rollout status \
                        deployment/${APP_NAME} \
                        -n production
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            slackSend(
                color: 'good',
                message: "Deployment successful: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
            )
        }
        failure {
            slackSend(
                color: 'danger',
                message: "Deployment failed: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
            )
        }
    }
}
```

---

## 🔐 Best Practices CI/CD

### 1. Secrets Management

```yaml
# GitLab CI - usando variables protegidas
deploy:
  script:
    - echo $DB_PASSWORD | docker login --username $DB_USER --password-stdin
  only:
    - main

# GitHub Actions - usando secrets
- name: Login
  env:
    PASSWORD: ${{ secrets.DB_PASSWORD }}
  run: echo "$PASSWORD" | docker login --username user --password-stdin
```

### 2. Caching Dependencies

```yaml
# GitLab CI
test:
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
      - .pip-cache/
  before_script:
    - pip install --cache-dir .pip-cache -r requirements.txt

# GitHub Actions
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

### 3. Matrix Testing

```yaml
# GitLab CI
test:
  parallel:
    matrix:
      - PYTHON_VERSION: ['3.9', '3.10', '3.11']
        NODE_VERSION: ['16', '18', '20']
  image: python:${PYTHON_VERSION}
  script:
    - pytest

# GitHub Actions
test:
  strategy:
    matrix:
      python-version: [3.9, '3.10', 3.11]
      os: [ubuntu-latest, macos-latest, windows-latest]
  runs-on: ${{ matrix.os }}
  steps:
    - uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
```

---

## 🎯 GitOps con ArgoCD

### Application Manifest

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  
  source:
    repoURL: https://github.com/company/myapp
    targetRevision: main
    path: k8s/overlays/production
    helm:
      values: |
        image:
          tag: v1.2.3
        replicas: 3
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
  
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  
  syncPolicy:
    automated:
      prune: true      # Eliminar recursos que no están en Git
      selfHeal: true   # Auto-corregir drift
    syncOptions:
      - CreateNamespace=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

---

## 🔄 Pipeline Patterns Comunes

### 1. Blue-Green Deployment

```yaml
# Paso 1: Deploy nueva versión (green)
deploy_green:
  script:
    - kubectl apply -f deployment-green.yaml
    - kubectl wait --for=condition=available deployment/myapp-green

# Paso 2: Smoke tests
smoke_tests:
  script:
    - curl http://myapp-green-service/health
    - ./run-smoke-tests.sh

# Paso 3: Switch traffic
switch_traffic:
  script:
    - kubectl patch service myapp -p '{"spec":{"selector":{"version":"green"}}}'

# Paso 4: Cleanup old version
cleanup:
  script:
    - kubectl delete deployment myapp-blue
```

### 2. Canary Deployment

```yaml
# Paso 1: Deploy canary (10% traffic)
deploy_canary:
  script:
    - kubectl apply -f deployment-canary.yaml
    - kubectl set image deployment/myapp-canary myapp=$IMAGE:$TAG
    - kubectl patch virtualservice myapp -p '{"spec":{"http":[{"route":[{"destination":{"host":"myapp-stable"},"weight":90},{"destination":{"host":"myapp-canary"},"weight":10}]}]}}'

# Paso 2: Monitor metrics
monitor:
  script:
    - ./check-error-rate.sh  # Si error rate OK, continuar
    - ./check-latency.sh

# Paso 3: Increase to 50%
increase_traffic:
  script:
    - kubectl patch virtualservice myapp -p '{"spec":{"http":[{"route":[{"destination":{"host":"myapp-stable"},"weight":50},{"destination":{"host":"myapp-canary"},"weight":50}]}]}}'

# Paso 4: Promote to 100%
promote:
  script:
    - kubectl set image deployment/myapp-stable myapp=$IMAGE:$TAG
    - kubectl delete deployment myapp-canary
```

---

## 📊 Monitoring de Pipelines

### Métricas Clave

```promql
# Pipeline success rate
sum(rate(ci_pipeline_status{status="success"}[1h])) 
/ 
sum(rate(ci_pipeline_status[1h])) * 100

# Pipeline duration
histogram_quantile(0.95, 
  rate(ci_pipeline_duration_seconds_bucket[1h])
)

# Deployment frequency
sum(increase(deployments_total[1d]))

# Lead time (commit to production)
histogram_quantile(0.95, 
  rate(deployment_lead_time_seconds_bucket[1d])
)

# MTTR (Mean Time To Recovery)
avg(incident_resolution_seconds)

# Change failure rate
sum(rate(deployment_status{status="failed"}[7d])) 
/ 
sum(rate(deployment_status[7d])) * 100
```
--- 

## 🎓 Conceptos Clave TestGorilla

**P: ¿Qué es CI?**  
R: Integrar código frecuentemente con tests automáticos para detectar bugs temprano

**P: ¿Diferencia entre Continuous Delivery y Continuous Deployment?**  
R: Delivery = listo para producción (manual), Deployment = automático a producción

**P: ¿Qué es GitOps?**  
R: Usar Git como source of truth para infraestructura. Todo cambio via Git.

**P: ¿Qué es un pipeline stage?**  
R: Fase del pipeline (test, build, deploy). Si una falla, se detiene.

**P: ¿Cuándo usar deployment manual vs automático?**  
R: Manual para producción (control), automático para staging/dev (velocidad)
