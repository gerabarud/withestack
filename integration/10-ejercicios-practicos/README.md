# 🎯 Ejercicios Prácticos y Simulaciones

## 📚 Índice
1. [Ejercicios Linux](#ejercicios-linux)
2. [Ejercicios Kubernetes](#ejercicios-kubernetes)
3. [Ejercicios Docker](#ejercicios-docker)
4. [Ejercicios Ansible](#ejercicios-ansible)
5. [Ejercicios Terraform](#ejercicios-terraform)
6. [Ejercicios Git](#ejercicios-git)
7. [Escenarios de Troubleshooting](#escenarios-de-troubleshooting)
8. [Simulación de Test](#simulación-de-test)

---

## 1. Ejercicios Linux

### 🎯 Ejercicio 1: Configuración de Red

**Objetivo:** Configurar una interfaz de red con IP estática, crear una VLAN y configurar iptables.

```bash
# 1. Configurar IP estática en eth0
sudo ip addr add 192.168.1.100/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 192.168.1.1

# 2. Crear VLAN 10
sudo ip link add link eth0 name eth0.10 type vlan id 10
sudo ip addr add 10.0.10.1/24 dev eth0.10
sudo ip link set eth0.10 up

# 3. Configurar iptables para permitir HTTP/HTTPS/SSH
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -P INPUT DROP

# 4. Verificar
ip addr show
iptables -L -n -v
```

### 🎯 Ejercicio 2: Script de Monitoreo

**Objetivo:** Crear script que monitoree sistema y envíe alertas.

```bash
#!/bin/bash
# monitor.sh

# Variables
THRESHOLD_CPU=80
THRESHOLD_MEM=80
THRESHOLD_DISK=85
LOG_FILE="/var/log/system_monitor.log"

# Función de logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# CPU Usage
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
CPU_USAGE=${CPU_USAGE%.*}

if [ "$CPU_USAGE" -gt "$THRESHOLD_CPU" ]; then
    log "ALERT: CPU usage is ${CPU_USAGE}%"
fi

# Memory Usage
MEM_USAGE=$(free | grep Mem | awk '{print ($3/$2) * 100.0}')
MEM_USAGE=${MEM_USAGE%.*}

if [ "$MEM_USAGE" -gt "$THRESHOLD_MEM" ]; then
    log "ALERT: Memory usage is ${MEM_USAGE}%"
fi

# Disk Usage
DISK_USAGE=$(df -h / | tail -1 | awk '{print $5}' | cut -d'%' -f1)

if [ "$DISK_USAGE" -gt "$THRESHOLD_DISK" ]; then
    log "ALERT: Disk usage is ${DISK_USAGE}%"
fi

# Top processes
log "Top 5 CPU processes:"
ps aux --sort=-%cpu | head -6 | tail -5 >> "$LOG_FILE"

log "Top 5 Memory processes:"
ps aux --sort=-%mem | head -6 | tail -5 >> "$LOG_FILE"
```

### 🎯 Ejercicio 3: Troubleshooting

**Escenario:** Un servicio web no responde.

```bash
# 1. Verificar si el servicio está corriendo
systemctl status nginx

# 2. Ver logs
journalctl -u nginx -n 50

# 3. Verificar puertos
ss -tulpn | grep :80
netstat -tulpn | grep :80

# 4. Verificar conectividad
curl -v http://localhost

# 5. Verificar firewall
iptables -L -n | grep 80

# 6. Verificar permisos
ls -la /var/www/html

# 7. Verificar espacio en disco
df -h

# 8. Verificar procesos
ps aux | grep nginx
```

---

## 2. Ejercicios Kubernetes

### 🎯 Ejercicio 1: Deployment Completo

**Objetivo:** Desplegar aplicación web con base de datos.

```yaml
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: webapp

---
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: webapp
data:
  DATABASE_HOST: "mysql-service"
  DATABASE_PORT: "3306"
  DATABASE_NAME: "myapp"

---
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
  namespace: webapp
type: Opaque
stringData:
  username: appuser
  password: secretpass123

---
# mysql-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
  namespace: webapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
        - name: MYSQL_DATABASE
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: DATABASE_NAME
        - name: MYSQL_USER
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: username
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
        ports:
        - containerPort: 3306
        volumeMounts:
        - name: mysql-storage
          mountPath: /var/lib/mysql
      volumes:
      - name: mysql-storage
        persistentVolumeClaim:
          claimName: mysql-pvc

---
# mysql-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql-service
  namespace: webapp
spec:
  selector:
    app: mysql
  ports:
  - port: 3306
    targetPort: 3306

---
# mysql-pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pvc
  namespace: webapp
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi

---
# web-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
  namespace: webapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: web
        image: nginx:1.21
        envFrom:
        - configMapRef:
            name: app-config
        env:
        - name: DB_USER
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: username
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
        ports:
        - containerPort: 80
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5

---
# web-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: webapp-service
  namespace: webapp
spec:
  type: LoadBalancer
  selector:
    app: webapp
  ports:
  - port: 80
    targetPort: 80
```

**Desplegar:**
```bash
kubectl apply -f .
kubectl get all -n webapp
kubectl logs -n webapp deployment/webapp
```

### 🎯 Ejercicio 2: Debugging

**Escenario:** Un pod está en CrashLoopBackOff.

```bash
# 1. Ver el pod
kubectl get pods -n webapp

# 2. Describir el pod
kubectl describe pod <pod-name> -n webapp

# 3. Ver logs
kubectl logs <pod-name> -n webapp
kubectl logs <pod-name> -n webapp --previous

# 4. Ver eventos
kubectl get events -n webapp --sort-by='.lastTimestamp'

# 5. Ejecutar comando en el pod
kubectl exec -it <pod-name> -n webapp -- /bin/bash

# 6. Ver configuración
kubectl get pod <pod-name> -n webapp -o yaml

# 7. Verificar recursos
kubectl top pod <pod-name> -n webapp
```

---

## 3. Ejercicios Docker

### 🎯 Ejercicio 1: Multi-stage Build

**Objetivo:** Crear Dockerfile optimizado para aplicación Go.

```dockerfile
# Dockerfile
# Build stage
FROM golang:1.19-alpine AS builder

WORKDIR /build

# Copy go mod files
COPY go.mod go.sum ./
RUN go mod download

# Copy source
COPY . .

# Build
RUN CGO_ENABLED=0 GOOS=linux go build -o app .

# Production stage
FROM alpine:3.17

# Install CA certificates
RUN apk --no-cache add ca-certificates

# Create non-root user
RUN adduser -D -u 1000 appuser

WORKDIR /app

# Copy binary from builder
COPY --from=builder /build/app .

# Change ownership
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --quiet --tries=1 --spider http://localhost:8080/health || exit 1

CMD ["./app"]
```

**Build y test:**
```bash
docker build -t myapp:1.0 .
docker run -d -p 8080:8080 --name myapp myapp:1.0
docker logs -f myapp
docker inspect myapp
docker exec -it myapp sh
```

### 🎯 Ejercicio 2: Docker Compose Stack

**Objetivo:** Stack completo con múltiples servicios.

```yaml
# docker-compose.yml
version: '3.8'

services:
  nginx:
    image: nginx:1.21-alpine
    container_name: nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./html:/usr/share/nginx/html
    depends_on:
      - app
    networks:
      - frontend
    restart: unless-stopped

  app:
    build:
      context: ./app
      dockerfile: Dockerfile
    container_name: app
    environment:
      - DB_HOST=db
      - DB_PORT=5432
      - DB_NAME=myapp
      - DB_USER=appuser
      - DB_PASSWORD=secret
      - REDIS_HOST=redis
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - frontend
      - backend
    restart: unless-stopped

  db:
    image: postgres:14-alpine
    container_name: postgres
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=appuser
      - POSTGRES_PASSWORD=secret
    volumes:
      - db-data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U appuser"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    container_name: redis
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    networks:
      - backend
    restart: unless-stopped

volumes:
  db-data:
  redis-data:

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true
```

**Comandos:**
```bash
docker-compose up -d
docker-compose ps
docker-compose logs -f app
docker-compose exec app sh
docker-compose down -v
```

---

## 4. Ejercicios Ansible

### 🎯 Ejercicio 1: Playbook de Configuración

**Objetivo:** Configurar servidor web con Ansible.

```yaml
# playbook.yml
---
- name: Configure web servers
  hosts: webservers
  become: yes
  
  vars:
    app_user: webapp
    app_dir: /var/www/myapp
    nginx_port: 80
  
  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
        cache_valid_time: 3600
    
    - name: Install packages
      apt:
        name:
          - nginx
          - python3-pip
          - git
        state: present
    
    - name: Create app user
      user:
        name: "{{ app_user }}"
        system: yes
        shell: /bin/bash
        create_home: yes
    
    - name: Create app directory
      file:
        path: "{{ app_dir }}"
        state: directory
        owner: "{{ app_user }}"
        group: "{{ app_user }}"
        mode: '0755'
    
    - name: Clone application
      git:
        repo: https://github.com/user/repo.git
        dest: "{{ app_dir }}"
        version: main
      become_user: "{{ app_user }}"
    
    - name: Copy nginx config
      template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/sites-available/myapp
        owner: root
        group: root
        mode: '0644'
      notify: Reload nginx
    
    - name: Enable site
      file:
        src: /etc/nginx/sites-available/myapp
        dest: /etc/nginx/sites-enabled/myapp
        state: link
      notify: Reload nginx
    
    - name: Remove default site
      file:
        path: /etc/nginx/sites-enabled/default
        state: absent
      notify: Reload nginx
    
    - name: Ensure nginx is running
      service:
        name: nginx
        state: started
        enabled: yes
  
  handlers:
    - name: Reload nginx
      service:
        name: nginx
        state: reloaded
```

---

## 5. Ejercicios Terraform

### 🎯 Ejercicio 1: Infraestructura AWS

**Objetivo:** Crear VPC con subnets y EC2 instance.

```hcl
# main.tf
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
  region = var.aws_region
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "${var.project_name}-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  
  tags = {
    Name = "${var.project_name}-igw"
  }
}

# Public Subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.public_subnet_cidr
  availability_zone       = "${var.aws_region}a"
  map_public_ip_on_launch = true
  
  tags = {
    Name = "${var.project_name}-public-subnet"
  }
}

# Route Table
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
  
  tags = {
    Name = "${var.project_name}-public-rt"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

# Security Group
resource "aws_security_group" "web" {
  name        = "${var.project_name}-web-sg"
  description = "Security group for web servers"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 80
    to_port     = 80
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
    Name = "${var.project_name}-web-sg"
  }
}

# EC2 Instance
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = aws_subnet.public.id
  
  vpc_security_group_ids = [aws_security_group.web.id]
  
  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y nginx
              systemctl start nginx
              systemctl enable nginx
              EOF
  
  tags = {
    Name = "${var.project_name}-web-server"
  }
}

# variables.tf
variable "aws_region" {
  default = "us-east-1"
}

variable "project_name" {
  default = "myproject"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  default = "10.0.1.0/24"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "ami_id" {
  description = "Ubuntu 20.04 AMI"
  default     = "ami-0c55b159cbfafe1f0"
}

# outputs.tf
output "instance_public_ip" {
  value = aws_instance.web.public_ip
}

output "instance_id" {
  value = aws_instance.web.id
}
```

---

## 6. Ejercicios Git

### 🎯 Ejercicio 1: Rebase Interactivo

```bash
# 1. Crear repositorio de prueba
mkdir git-practice && cd git-practice
git init

# 2. Hacer varios commits
echo "A" > file.txt && git add . && git commit -m "Add A"
echo "B" >> file.txt && git add . && git commit -m "Add B"
echo "C" >> file.txt && git add . && git commit -m "Add C"
echo "D" >> file.txt && git add . && git commit -m "Typo"
echo "E" >> file.txt && git add . && git commit -m "Add E"

# 3. Rebase interactivo para combinar commits
git rebase -i HEAD~5

# En el editor, cambiar:
# pick xxx Add A
# pick xxx Add B
# pick xxx Add C
# squash xxx Typo  # Combinar con anterior
# pick xxx Add E

# 4. Ver resultado
git log --oneline
```

### 🎯 Ejercicio 2: Cherry-pick

```bash
# Crear branches con commits
git checkout -b feature-1
echo "Feature 1" > feature1.txt && git add . && git commit -m "Feature 1"

git checkout -b feature-2 main
echo "Feature 2" > feature2.txt && git add . && git commit -m "Feature 2"
echo "Bugfix" > bugfix.txt && git add . && git commit -m "Important bugfix"

# Cherry-pick el bugfix a main
git checkout main
git log feature-2 --oneline  # Ver commits
git cherry-pick <bugfix-hash>

# Verificar
git log --oneline
```

---

## 7. Escenarios de Troubleshooting

### 🐛 Escenario 1: Pod no inicia

**Síntomas:** Pod en estado Pending

```bash
kubectl describe pod my-pod
# Possible causes:
# - Insufficient resources
# - PVC waiting for PV
# - Node selector not matching
# - Taints/tolerations

# Solutions:
kubectl get nodes
kubectl describe node <node-name>
kubectl get pv
kubectl get pvc
```

### 🐛 Escenario 2: Contenedor crasheando

**Síntomas:** CrashLoopBackOff

```bash
kubectl logs my-pod --previous
kubectl describe pod my-pod

# Common causes:
# - Liveness probe failing
# - Application error
# - Missing dependencies
# - Wrong command/args
```

### 🐛 Escenario 3: Servicio no accesible

```bash
# 1. Verificar pods
kubectl get pods -l app=myapp

# 2. Verificar service
kubectl get svc myapp-service
kubectl describe svc myapp-service

# 3. Verificar endpoints
kubectl get endpoints myapp-service

# 4. Test desde otro pod
kubectl run -it test --image=busybox --rm -- sh
wget -O- http://myapp-service:80
```

---

## 8. Simulación de Test

### 📝 Preguntas Tipo TestGorilla

**1. ¿Cuál comando muestra los procesos que usan más CPU?**
```bash
a) top -o %CPU
b) ps aux --sort=-%cpu
c) htop
d) Todas las anteriores ✓
```

**2. ¿Cómo ves los logs de un servicio systemd?**
```bash
a) systemctl logs nginx
b) journalctl -u nginx ✓
c) tail -f /var/log/nginx
d) cat /var/log/syslog
```

**3. En Kubernetes, ¿qué hace el Liveness Probe?**
```
a) Verifica si el pod está listo para recibir tráfico
b) Verifica si el contenedor está vivo, lo reinicia si falla ✓
c) Verifica si el pod tiene recursos suficientes
d) Verifica la conectividad de red
```

**4. ¿Diferencia entre git merge y git rebase?**
```
a) merge crea merge commit, rebase reescribe historial ✓
b) No hay diferencia
c) rebase es más rápido
d) merge es para branches públicos solo
```

**5. ¿Qué hace terraform plan?**
```
a) Aplica cambios
b) Muestra cambios sin aplicar ✓
c) Valida sintaxis
d) Destruye recursos
```

---

## 🎓 Checklist Final

Antes del test, asegúrate de poder:

### Linux
- [ ] Configurar red (IP, VLAN, routes)
- [ ] Escribir scripts bash
- [ ] Usar iptables
- [ ] Troubleshoot servicios

### Kubernetes
- [ ] Crear deployments, services
- [ ] Usar configmaps y secrets
- [ ] Debugging de pods
- [ ] Entender probes

### Docker
- [ ] Escribir Dockerfiles
- [ ] Usar docker-compose
- [ ] Gestionar volúmenes y redes
- [ ] Troubleshoot contenedores

### Ansible
- [ ] Escribir playbooks
- [ ] Usar roles
- [ ] Gestionar inventarios
- [ ] Loops y condicionales

### Terraform
- [ ] Crear recursos básicos
- [ ] Usar variables y outputs
- [ ] Entender state
- [ ] Troubleshoot

### Git
- [ ] Rebase interactivo
- [ ] Cherry-pick
- [ ] Resolver conflictos
- [ ] GitOps workflows

---

**💡 Consejo Final:** Practica estos ejercicios. TestGorilla evalúa conocimiento práctico, no solo teoría.
