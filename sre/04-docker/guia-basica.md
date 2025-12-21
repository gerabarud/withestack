# 🐳 Docker - Guía Completa

## 🎯 ¿Qué es Docker?

Docker es una plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores. Los contenedores son unidades estandarizadas de software que empaquetan código y todas sus dependencias.

---

## 🏗️ Conceptos Fundamentales

### Imagen vs Contenedor

```
┌─────────────────┐
│     IMAGEN      │  ← Template read-only (recipe)
│   nginx:1.21    │    
└─────────────────┘
        │
        │ docker run
        ▼
┌─────────────────┐
│   CONTENEDOR    │  ← Instancia en ejecución (running process)
│  nginx-server   │
└─────────────────┘
```

**Analogía:**
- **Imagen** = Clase en programación
- **Contenedor** = Instancia de esa clase

---

## 🔧 Comandos Docker Esenciales (Top 30)

### Imágenes

```bash
# Listar imágenes locales
docker images
docker image ls

# Descargar imagen
docker pull nginx:1.21
docker pull ubuntu:22.04

# Buscar imágenes en Docker Hub
docker search nginx

# Construir imagen desde Dockerfile
docker build -t myapp:latest .
docker build -t myapp:v1.0 -f Dockerfile.prod .

# Ver historial de capas de una imagen
docker history nginx:1.21

# Inspeccionar imagen
docker image inspect nginx:1.21

# Eliminar imagen
docker rmi nginx:1.21
docker image rm nginx:1.21

# Eliminar imágenes sin usar (dangling)
docker image prune

# Eliminar TODAS las imágenes sin contenedores
docker image prune -a

# Etiquetar imagen
docker tag myapp:latest myapp:v1.0
docker tag myapp:latest myregistry.com/myapp:latest

# Guardar imagen a archivo tar
docker save -o myapp.tar myapp:latest

# Cargar imagen desde archivo tar
docker load -i myapp.tar

# Push imagen a registry
docker push myregistry.com/myapp:latest
```

---

### Contenedores

```bash
# Ejecutar contenedor
docker run nginx
docker run -d nginx                    # detached (background)
docker run -d --name webserver nginx   # con nombre
docker run -d -p 8080:80 nginx         # port mapping
docker run -d -p 8080:80 -v $(pwd):/app nginx  # volume mount
docker run -d -e MY_VAR=value nginx    # variable de entorno
docker run -it ubuntu bash             # interactivo con terminal

# Listar contenedores
docker ps                              # solo running
docker ps -a                           # todos (running + stopped)
docker ps -q                           # solo IDs

# Ver logs de contenedor
docker logs <container-id>
docker logs -f <container-id>          # follow (tail -f)
docker logs --tail 100 <container-id>  # últimas 100 líneas
docker logs --since 10m <container-id> # últimos 10 minutos

# Ejecutar comando en contenedor running
docker exec <container-id> ls /app
docker exec -it <container-id> bash    # shell interactivo
docker exec -it <container-id> sh      # si no tiene bash

# Ver procesos de un contenedor
docker top <container-id>

# Ver estadísticas en tiempo real
docker stats
docker stats <container-id>

# Inspeccionar contenedor (JSON completo)
docker inspect <container-id>

# Ver IP de contenedor
docker inspect <container-id> | grep IPAddress

# Detener contenedor
docker stop <container-id>
docker stop $(docker ps -q)            # detener todos

# Iniciar contenedor detenido
docker start <container-id>

# Reiniciar contenedor
docker restart <container-id>

# Eliminar contenedor
docker rm <container-id>
docker rm -f <container-id>            # forzar (si está running)
docker rm $(docker ps -aq)             # eliminar todos

# Pausar/Despausar contenedor
docker pause <container-id>
docker unpause <container-id>

# Ver cambios en filesystem del contenedor
docker diff <container-id>

# Copiar archivos desde/hacia contenedor
docker cp <container-id>:/path/file ./local-file
docker cp ./local-file <container-id>:/path/file

# Crear imagen desde contenedor en ejecución (no recomendado en prod)
docker commit <container-id> myapp:snapshot

# Ver logs de eventos de Docker
docker events
```

---

### Limpieza y Mantenimiento

```bash
# Eliminar contenedores detenidos
docker container prune

# Eliminar imágenes sin usar
docker image prune

# Eliminar volúmenes sin usar
docker volume prune

# Eliminar networks sin usar
docker network prune

# ELIMINAR TODO (contenedores, imágenes, volumes, networks)
docker system prune -a --volumes

# Ver uso de disco por Docker
docker system df
```

---

## 📝 Dockerfile - Crear Imágenes

### Estructura Básica

```dockerfile
# Comentario
FROM imagen-base
RUN comando
COPY origen destino
CMD ["ejecutable", "arg1", "arg2"]
```

### Instrucciones Principales

| Instrucción | Descripción | Ejemplo |
|-------------|-------------|---------|
| `FROM` | Imagen base | `FROM node:18-alpine` |
| `RUN` | Ejecutar comando (build time) | `RUN apt-get update` |
| `CMD` | Comando por defecto (runtime) | `CMD ["npm", "start"]` |
| `ENTRYPOINT` | Comando principal (runtime) | `ENTRYPOINT ["python", "app.py"]` |
| `COPY` | Copiar archivos locales → imagen | `COPY . /app` |
| `ADD` | Similar a COPY + soporta URLs/tar | `ADD file.tar.gz /opt` |
| `WORKDIR` | Directorio de trabajo | `WORKDIR /app` |
| `ENV` | Variable de entorno | `ENV NODE_ENV=production` |
| `EXPOSE` | Documentar puerto | `EXPOSE 8080` |
| `VOLUME` | Punto de montaje | `VOLUME /data` |
| `USER` | Usuario para ejecutar | `USER appuser` |
| `ARG` | Variable de build | `ARG VERSION=1.0` |
| `LABEL` | Metadata | `LABEL maintainer="you@example.com"` |

---

### Ejemplo 1: Python Flask App

```dockerfile
# Imagen base
FROM python:3.11-slim

# Metadata
LABEL maintainer="devops@company.com"
LABEL version="1.0"

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Copiar requirements y instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Usuario no-root (seguridad)
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Puerto que expone la app
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:5000/health || exit 1

# Variables de entorno
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Comando por defecto
CMD ["python", "app.py"]
```

---

### Ejemplo 2: Node.js App

```dockerfile
FROM node:18-alpine

WORKDIR /app

# Copiar package files primero (cache de layers)
COPY package*.json ./

# Instalar dependencias
RUN npm ci --only=production

# Copiar código
COPY . .

# Build (si es necesario)
RUN npm run build

# Usuario no-root
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001
USER nodejs

EXPOSE 3000

CMD ["node", "dist/index.js"]
```

---

### Ejemplo 3: Multi-stage Build (Go)

**Ventaja**: Imagen final pequeña (solo el binario, sin Go SDK)

```dockerfile
# Stage 1: Build
FROM golang:1.21-alpine AS builder

WORKDIR /build

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o app .

# Stage 2: Runtime
FROM alpine:latest

RUN apk --no-cache add ca-certificates

WORKDIR /root/

# Copiar solo el binario desde stage anterior
COPY --from=builder /build/app .

EXPOSE 8080

CMD ["./app"]
```

**Resultado**: Imagen de ~10MB vs ~800MB con Go completo

---

### Ejemplo 4: Nginx con configuración custom

```dockerfile
FROM nginx:1.21-alpine

# Copiar configuración custom
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

# Copiar contenido estático
COPY dist/ /usr/share/nginx/html/

# Exponer puerto
EXPOSE 80

# Nginx ya tiene CMD definido en imagen base
# CMD ["nginx", "-g", "daemon off;"]
```

---

## 🔗 Docker Networking

### Tipos de Networks

```bash
# Listar networks
docker network ls

# Inspeccionar network
docker network inspect bridge

# Crear network
docker network create my-network
docker network create --driver bridge --subnet 172.20.0.0/16 my-custom-net

# Conectar contenedor a network
docker network connect my-network <container-id>

# Desconectar contenedor de network
docker network disconnect my-network <container-id>

# Eliminar network
docker network rm my-network
```

### Network Drivers

| Driver | Uso | Descripción |
|--------|-----|-------------|
| **bridge** | Default, single host | Contenedores en el mismo host |
| **host** | Performance | Contenedor usa network del host directamente |
| **none** | Aislamiento | Sin networking |
| **overlay** | Multi-host (Swarm) | Contenedores en múltiples hosts |

### Comunicación entre Contenedores

```bash
# Método 1: Crear network y conectar contenedores
docker network create app-net

# Levantar DB
docker run -d --name postgres \
  --network app-net \
  -e POSTGRES_PASSWORD=secret \
  postgres:14

# Levantar app (puede conectar a postgres usando nombre "postgres")
docker run -d --name app \
  --network app-net \
  -e DB_HOST=postgres \
  myapp:latest
```

---

## 💾 Docker Volumes (Persistencia)

### Tipos de Volumes

```bash
# Named volume (recomendado)
docker volume create my-data
docker run -d -v my-data:/app/data myapp

# Bind mount (directorio del host)
docker run -d -v $(pwd)/data:/app/data myapp
docker run -d -v /host/path:/container/path myapp

# Anonymous volume
docker run -d -v /app/data myapp

# Listar volumes
docker volume ls

# Inspeccionar volume
docker volume inspect my-data

# Eliminar volume
docker volume rm my-data

# Eliminar volumes sin usar
docker volume prune
```

### ¿Cuándo usar qué?

| Tipo | Uso |
|------|-----|
| **Named volume** | Datos de producción (DB, uploads) |
| **Bind mount** | Desarrollo (hot reload), configs |
| **Anonymous volume** | Datos temporales |

---

## 🐳 Docker Compose

**docker-compose.yml**: Definir aplicaciones multi-container

### Ejemplo Completo: Web + DB + Cache

```yaml
version: '3.8'

services:
  # Database
  db:
    image: postgres:14-alpine
    container_name: myapp-db
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: dbuser
      POSTGRES_PASSWORD: dbpass
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dbuser"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis cache
  cache:
    image: redis:7-alpine
    container_name: myapp-cache
    networks:
      - backend
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s

  # Web application
  web:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: myapp-web
    ports:
      - "8080:8080"
    environment:
      DB_HOST: db
      DB_PORT: 5432
      DB_NAME: myapp
      REDIS_URL: redis://cache:6379
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_healthy
    volumes:
      - ./uploads:/app/uploads
    networks:
      - frontend
      - backend
    restart: unless-stopped

  # Nginx reverse proxy
  nginx:
    image: nginx:1.21-alpine
    container_name: myapp-nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certs:/etc/nginx/certs:ro
    depends_on:
      - web
    networks:
      - frontend
    restart: unless-stopped

volumes:
  db-data:

networks:
  frontend:
  backend:
```

### Comandos Docker Compose

```bash
# Iniciar servicios (detached)
docker-compose up -d

# Ver logs
docker-compose logs
docker-compose logs -f web
docker-compose logs --tail=100

# Listar servicios
docker-compose ps

# Detener servicios
docker-compose stop

# Detener y eliminar contenedores, networks, volumes
docker-compose down
docker-compose down -v  # también eliminar volumes

# Restart service específico
docker-compose restart web

# Rebuild imagen
docker-compose build
docker-compose build --no-cache web

# Escalar service
docker-compose up -d --scale web=3

# Ejecutar comando en service
docker-compose exec web bash
docker-compose exec db psql -U dbuser myapp

# Ver configuración procesada
docker-compose config
```

---

## 🎯 Best Practices

### 1. Optimizar Dockerfile

✅ **DO:**
```dockerfile
# Usar imagen base pequeña
FROM node:18-alpine  # ~170MB
# vs FROM node:18  # ~900MB

# Orden de layers: Lo que cambia menos primero
COPY package*.json ./
RUN npm ci
COPY . .

# Combinar RUN commands
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Usuario no-root
USER appuser

# Multi-stage builds
FROM golang:1.21 AS builder
# ... build ...
FROM alpine:latest
COPY --from=builder /app/binary .
```

❌ **DON'T:**
```dockerfile
# Imagen pesada sin razón
FROM ubuntu:latest

# Cada COPY/RUN crea nueva layer
COPY file1.txt .
COPY file2.txt .
COPY file3.txt .

# Ejecutar como root
# (sin especificar USER)

# Cache de package managers
RUN apt-get update && apt-get install -y curl
# (sin limpiar /var/lib/apt/lists/)
```

---

### 2. .dockerignore

```
# .dockerignore
node_modules
npm-debug.log
.git
.gitignore
.env
.vscode
*.md
Dockerfile*
docker-compose*.yml
*.log
dist
coverage
.pytest_cache
__pycache__
```

---

### 3. Tags Semánticos

```bash
# ✅ Buenas prácticas
docker build -t myapp:1.2.3 .
docker build -t myapp:1.2 .
docker build -t myapp:1 .
docker build -t myapp:latest .

# ❌ Evitar
docker build -t myapp .  # usa "latest" implícito
```

---

### 4. Health Checks

```dockerfile
# En Dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# O en docker-compose.yml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
  interval: 30s
  timeout: 3s
  retries: 3
  start_period: 5s
```

---

### 5. Limitar Recursos

```bash
# Limitar memoria y CPU
docker run -d \
  --memory="512m" \
  --cpus="0.5" \
  nginx

# En docker-compose.yml
services:
  web:
    image: myapp
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

---

## 🚨 Troubleshooting

### Container no inicia

```bash
# Ver logs
docker logs <container-id>

# Inspeccionar
docker inspect <container-id>

# Verificar si puerto está ocupado
netstat -tulpn | grep <puerto>

# Ejecutar en modo interactivo para debug
docker run -it myapp bash
```

### Container consume mucha memoria/CPU

```bash
# Ver stats en tiempo real
docker stats

# Limitar recursos
docker update --memory="512m" --cpus="0.5" <container-id>
```

### No puede conectar entre contenedores

```bash
# Verificar están en misma network
docker network inspect <network-name>

# Ver IP de contenedor
docker inspect <container-id> | grep IPAddress

# Test de conectividad
docker exec <container-id> ping <otro-container>
docker exec <container-id> curl http://<otro-container>:port
```

---

## ❓ Preguntas TestGorilla

### Q1: ¿Cuál es la diferencia entre CMD y ENTRYPOINT?
- **CMD**: Puede ser sobrescrito completamente
- **ENTRYPOINT**: Siempre se ejecuta, args se agregan

```dockerfile
# Ejemplo ENTRYPOINT
ENTRYPOINT ["python"]
CMD ["app.py"]

# docker run myapp        → python app.py
# docker run myapp test.py → python test.py
```

### Q2: ¿Qué hace `docker run -d -p 8080:80 nginx`?
- `-d`: Detached (background)
- `-p 8080:80`: Map puerto 8080 del host → 80 del container

### Q3: ¿Cómo ver logs de un container que ya no existe?
- No es posible. Los logs se pierden al eliminar el container.
- Solución: Usar log driver (syslog, json-file, etc) o enviar a sistema externo (ELK, Loki)

---

## ✅ Checklist de Dominio

- [ ] Entiendo diferencia entre imagen y contenedor
- [ ] Sé crear Dockerfiles básicos y avanzados
- [ ] Conozco multi-stage builds
- [ ] Puedo trabajar con volumes y persistence
- [ ] Entiendo Docker networking
- [ ] Sé usar docker-compose para apps multi-container
- [ ] Conozco best practices (usuario no-root, .dockerignore, etc)
- [ ] Puedo debuggear containers que no inician
- [ ] Entiendo diferencia entre CMD y ENTRYPOINT
- [ ] Sé optimizar imágenes para tamaño pequeño

---

## 📚 Recursos

- [Docker Official Docs](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Play with Docker](https://labs.play-with-docker.com/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
