# Ejercicios Prácticos - Deployment Engineer

## 1. Ejercicio: Administración de Usuarios y Permisos

### Objetivo
Crear una estructura de usuarios con permisos diferenciados para un equipo de infraestructura.

### Pasos
```bash
# 1. Crear grupo para administradores
sudo groupadd sysadmins
sudo groupadd developers
sudo groupadd monitoring

# 2. Crear usuarios
sudo useradd -m -s /bin/bash -G sysadmins admin1
sudo useradd -m -s /bin/bash -G developers dev1
sudo useradd -m -s /bin/bash -G monitoring monitoring1

# 3. Configurar sudoers
sudo visudo
# admin1 ALL=(ALL) ALL
# monitoring1 ALL=(ALL) NOPASSWD: /usr/bin/systemctl, /usr/bin/journalctl

# 4. Crear directorios compartidos
sudo mkdir -p /opt/admin_data
sudo mkdir -p /opt/dev_data
sudo mkdir -p /opt/monitoring_data

# 5. Asignar permisos
sudo chown root:sysadmins /opt/admin_data
sudo chmod 750 /opt/admin_data

sudo chown root:developers /opt/dev_data
sudo chmod 750 /opt/dev_data

sudo chown root:monitoring /opt/monitoring_data
sudo chmod 750 /opt/monitoring_data

# 6. Verificar
id admin1
id dev1
groups monitoring1
```

### Validación
```bash
# Verificar que solo sysadmins puede acceder a admin_data
sudo -u dev1 ls /opt/admin_data  # Debe fallar
sudo -u admin1 ls /opt/admin_data  # Debe funcionar
```

---

## 2. Ejercicio: Configuración de Red - Bonding

### Objetivo
Crear un bond con dos interfaces de red en modo active-backup.

### Pasos
```bash
# 1. Ver interfaces disponibles
ip link show
ethtool eth0

# 2. Crear configuración netplan
sudo nano /etc/netplan/02-bonding.yaml

---
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
        - 192.168.100.100/24
      gateway4: 192.168.100.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
      parameters:
        mode: active-backup
        mii-monitor-interval: 100

# 3. Validar y aplicar
sudo netplan validate
sudo netplan apply

# 4. Verificar
ip link show bond0
cat /proc/net/bonding/bond0

# 5. Probar failover (simular pérdida de eth0)
sudo ip link set eth0 down
sleep 2
cat /proc/net/bonding/bond0  # eth1 debe estar activa
sudo ip link set eth0 up
```

---

## 3. Ejercicio: Configuración de VLANs

### Objetivo
Crear múltiples VLANs en una misma interfaz.

### Pasos
```bash
# 1. Crear configuración netplan
sudo nano /etc/netplan/03-vlans.yaml

---
network:
  version: 2
  ethernets:
    eth2:
      match:
        name: eth2
  vlans:
    vlan100:
      id: 100
      link: eth2
      dhcp4: no
      addresses:
        - 10.0.100.10/24
    vlan200:
      id: 200
      link: eth2
      dhcp4: no
      addresses:
        - 10.0.200.10/24
    vlan300:
      id: 300
      link: eth2
      dhcp4: no
      addresses:
        - 10.0.300.10/24

# 2. Aplicar
sudo netplan apply

# 3. Verificar
ip link show
ip addr show

# 4. Probar conectividad entre VLANs
ping 10.0.100.10
ping 10.0.200.10
ping 10.0.300.10
```

---

## 4. Ejercicio: Bash Scripting - Monitor de Sistema

### Objetivo
Crear script que monitoree recursos del sistema y alerte si superan umbrales.

### Pasos
```bash
# 1. Crear script
cat > ~/monitor_sistema.sh << 'EOF'
#!/bin/bash

# Umbrales
CPU_THRESHOLD=80
MEM_THRESHOLD=75
DISK_THRESHOLD=80

# Colores
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m'

echo "=== Monitor de Sistema ==="
echo "Timestamp: $(date)"

# CPU
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
if (( $(echo "$CPU_USAGE > $CPU_THRESHOLD" | bc -l) )); then
    echo -e "${RED}[ALERTA] CPU: $CPU_USAGE%${NC}"
else
    echo -e "${GREEN}CPU: $CPU_USAGE%${NC}"
fi

# Memoria
MEM_USAGE=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
if [ "$MEM_USAGE" -gt "$MEM_THRESHOLD" ]; then
    echo -e "${RED}[ALERTA] Memoria: $MEM_USAGE%${NC}"
else
    echo -e "${GREEN}Memoria: $MEM_USAGE%${NC}"
fi

# Disco
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | cut -d'%' -f1)
if [ "$DISK_USAGE" -gt "$DISK_THRESHOLD" ]; then
    echo -e "${RED}[ALERTA] Disco: $DISK_USAGE%${NC}"
else
    echo -e "${GREEN}Disco: $DISK_USAGE%${NC}"
fi

# Procesos
PROC_COUNT=$(ps aux | wc -l)
echo "Procesos activos: $PROC_COUNT"

echo "================="
EOF

chmod +x ~/monitor_sistema.sh

# 2. Ejecutar
~/monitor_sistema.sh

# 3. Agregar a cron (cada 5 minutos)
crontab -e
# */5 * * * * /home/user/monitor_sistema.sh >> /tmp/monitor.log
```

---

## 5. Ejercicio: Ansible - Despliegue de Nginx

### Objetivo
Crear playbook para instalar y configurar Nginx en múltiples servidores.

### Pasos
```bash
# 1. Crear inventario
cat > ~/inventory.ini << 'EOF'
[webservers]
web1 ansible_host=192.168.1.10 ansible_user=ubuntu
web2 ansible_host=192.168.1.11 ansible_user=ubuntu
EOF

# 2. Crear playbook
cat > ~/deploy_nginx.yml << 'EOF'
---
- name: Desplegar Nginx
  hosts: webservers
  become: yes
  
  vars:
    nginx_port: 80
    
  tasks:
    - name: Actualizar cache APT
      apt:
        update_cache: yes
    
    - name: Instalar Nginx
      apt:
        name: nginx
        state: present
    
    - name: Crear directorio para sitio
      file:
        path: /var/www/html/{{ inventory_hostname }}
        state: directory
        mode: '0755'
    
    - name: Crear index.html
      copy:
        content: |
          <h1>Bienvenido a {{ inventory_hostname }}</h1>
          <p>Servidor deployado con Ansible</p>
        dest: /var/www/html/index.html
    
    - name: Iniciar Nginx
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Verificar Nginx
      uri:
        url: "http://localhost"
        status_code: 200
EOF

# 3. Ejecutar playbook
ansible-playbook -i ~/inventory.ini ~/deploy_nginx.yml

# 4. Verificar
ansible all -i ~/inventory.ini -m shell -a "curl http://localhost"
```

---

## 6. Ejercicio: Docker - Despliegue de Aplicación

### Objetivo
Crear Dockerfile y ejecutar aplicación en contenedor.

### Pasos
```bash
# 1. Crear directorio
mkdir ~/docker-app
cd ~/docker-app

# 2. Crear aplicación simple
cat > app.py << 'EOF'
#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Docker!'

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF

# 3. Crear requirements.txt
cat > requirements.txt << 'EOF'
Flask==2.0.1
EOF

# 4. Crear Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
EOF

# 5. Construir imagen
docker build -t myapp:1.0 .

# 6. Ejecutar contenedor
docker run -d -p 5000:5000 --name myapp_container myapp:1.0

# 7. Probar
curl http://localhost:5000
curl http://localhost:5000/health

# 8. Ver logs
docker logs myapp_container

# 9. Detener
docker stop myapp_container
```

---

## 7. Ejercicio: Git - Flujo de Trabajo

### Objetivo
Practicar flujo de trabajo con Git (clone, branch, merge).

### Pasos
```bash
# 1. Clonar repositorio
git clone https://github.com/usuario/repo.git
cd repo

# 2. Crear rama para feature
git checkout -b feature/nueva-funcionalidad

# 3. Hacer cambios
echo "Cambios" >> archivo.txt
git add archivo.txt
git commit -m "Implementar nueva funcionalidad"

# 4. Actualizar desde main
git fetch origin
git rebase origin/main

# 5. Enviar rama
git push origin feature/nueva-funcionalidad

# 6. Crear Pull Request (en GitHub)
# https://github.com/usuario/repo/compare/main...feature/nueva-funcionalidad

# 7. Después de aprobación, limpiar
git checkout main
git pull origin main
git branch -d feature/nueva-funcionalidad
```

---

## 8. Ejercicio: Python Scripting - Admin de Servidores

### Objetivo
Crear script Python para ejecutar comandos remotos en múltiples servidores.

```python
#!/usr/bin/env python3
import paramiko
import json

servidores = [
    {"host": "192.168.1.10", "user": "admin"},
    {"host": "192.168.1.11", "user": "admin"},
]

resultados = {}

for servidor in servidores:
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            servidor["host"],
            username=servidor["user"],
            key_filename="/home/user/.ssh/id_rsa"
        )
        
        # Ejecutar comando
        stdin, stdout, stderr = ssh.exec_command("uptime")
        uptime = stdout.read().decode().strip()
        
        resultados[servidor["host"]] = {
            "estado": "activo",
            "uptime": uptime
        }
        
        ssh.close()
    except Exception as e:
        resultados[servidor["host"]] = {
            "estado": "error",
            "error": str(e)
        }

# Mostrar resultados
print(json.dumps(resultados, indent=2))
```

---

## 9. Ejercicio: Firewall y Seguridad

### Objetivo
Configurar firewall y hardening básico del sistema.

```bash
# 1. Habilitar UFW
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing

# 2. Permitir puertos necesarios
sudo ufw allow 22/tcp  # SSH
sudo ufw allow 80/tcp  # HTTP
sudo ufw allow 443/tcp # HTTPS

# 3. Bloquear específicos
sudo ufw deny 23/tcp   # Telnet

# 4. Ver estado
sudo ufw status verbose

# 5. Hardening SSH
sudo nano /etc/ssh/sshd_config
# PermitRootLogin no
# PasswordAuthentication no
# MaxAuthTries 3

sudo systemctl restart ssh

# 6. Verificar
sudo ss -tulpn | grep LISTEN
```

---

## Resumen de Comandos Más Usados en Tests

```bash
# Usuarios
id username
sudo usermod -aG grupo username
groups username

# Networking
ip addr show
ip link show
netstat -tulpn
ss -tulpn
ping -c 4 host

# Procesos
ps aux
ps aux | grep nombre
top
kill -9 PID

# Archivos
ls -la
chmod 755 archivo
chown user:group archivo

# Servicios
sudo systemctl status servicio
sudo systemctl restart servicio
sudo systemctl enable servicio

# Logs
tail -f /var/log/syslog
journalctl -u servicio -f
```

---
**Recomendación**: Practica estos ejercicios en una máquina virtual o entorno de laboratorio.
