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

## 9. Ejercicios Prácticos

### 🎯 Ejercicio 1: Aplicación Multi-Container

Crea una aplicación con:
- Frontend (Nginx)
- Backend (Node.js)
- Database (PostgreSQL)
- Redis cache
- Todo con Docker Compose

### 🎯 Ejercicio 2: Dockerfile Optimizado

Crea un Dockerfile que:
- Use multi-stage build
- Minimice el tamaño de imagen
- No ejecute como root
- Incluya health check

### 🎯 Ejercicio 3: Debugging

Un contenedor está crasheando. Diagnóstica y soluciona:
- Revisa logs
- Verifica configuración
- Comprueba recursos
- Corrige el problema

---

## 📝 Comandos Esenciales

```bash
# Top 25 comandos críticos
docker ps
docker ps -a
docker run -d
docker stop
docker start
docker restart
docker rm
docker logs -f
docker exec -it <container> bash
docker inspect
docker stats
docker images
docker pull
docker push
docker build -t
docker rmi
docker volume create
docker volume ls
docker network create
docker network ls
docker-compose up -d
docker-compose down
docker-compose logs -f
docker system prune
crictl ps
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

## 🔗 Recursos

- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Containerd](https://containerd.io/)

---

**💡 Consejo:** Practica creando Dockerfiles y docker-compose.yml. El test evaluará tu entendimiento del ciclo de vida y troubleshooting.
