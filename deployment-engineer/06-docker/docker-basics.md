# Docker - Nivel Básico

## 1. Instalación

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install docker.io
sudo usermod -aG docker $USER    # Añadir usuario al grupo docker
newgrp docker                    # Aplicar grupo sin reiniciar
```

## 2. Conceptos Básicos

- **Imagen**: Template (plantilla) inmutable
- **Contenedor**: Instancia ejecutable de una imagen
- **Registry**: Repositorio de imágenes (Docker Hub)
- **Dockerfile**: Archivo con instrucciones para construir imagen

## 3. Comandos Básicos

### Imágenes
```bash
docker images                    # Listar imágenes locales
docker pull ubuntu              # Descargar imagen
docker build -t myimage:1.0 .   # Construir desde Dockerfile
docker tag myimage:latest myimage:1.0  # Etiquetar imagen
docker rmi myimage              # Eliminar imagen
docker search nginx             # Buscar en Docker Hub
```

### Contenedores
```bash
docker run -d --name mycontainer -p 8080:80 nginx   # Ejecutar contenedor
docker ps                       # Listar contenedores activos
docker ps -a                    # Listar todos contenedores
docker stop mycontainer         # Detener contenedor
docker start mycontainer        # Iniciar contenedor
docker restart mycontainer      # Reiniciar
docker rm mycontainer           # Eliminar contenedor
docker logs mycontainer         # Ver logs
docker exec -it mycontainer bash # Entrar en contenedor
```

### Opciones Comunes de run
```bash
-d                              # Detached (background)
-it                             # Interactive terminal
--name                          # Nombre del contenedor
-p 8080:80                      # Port mapping: host:container
-e VAR=valor                    # Variable de entorno
-v /host:/container             # Volume mount
--network bridge                # Red del contenedor
--restart always                # Política restart
```

## 4. Dockerfile

### Estructura Básica
```dockerfile
FROM ubuntu:20.04

MAINTAINER Tu Nombre <email@example.com>

RUN apt-get update && \
    apt-get install -y nginx

COPY ./config /etc/nginx/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Instrucciones Comunes
```dockerfile
FROM                            # Imagen base
RUN                             # Ejecutar comando
COPY                            # Copiar desde host
ADD                             # Copiar y descomponer
EXPOSE                          # Puerto expuesto
ENV                             # Variable de entorno
WORKDIR                         # Directorio trabajo
CMD                             # Comando por defecto
ENTRYPOINT                      # Script entrada
VOLUME                          # Punto de montaje
```

## 5. Volúmenes

### Tipos de Volúmenes
```bash
# Bind mount (desde host)
docker run -v /home/user/data:/app/data myimage

# Named volume
docker volume create myvolume
docker run -v myvolume:/app/data myimage

# Anonymous volume
docker run -v /app/data myimage
```

### Gestionar Volúmenes
```bash
docker volume ls                # Listar volúmenes
docker volume inspect myvolume  # Info del volumen
docker volume rm myvolume       # Eliminar volumen
```

## 6. Redes Docker

### Tipos de Redes
```bash
# Bridge (por defecto)
docker network create --driver bridge mynetwork

# Host (usa red del host)
docker run --network host myimage

# None
docker run --network none myimage
```

### Conectar Contenedores
```bash
docker network create mynetwork
docker run -d --network mynetwork --name web nginx
docker run -d --network mynetwork --name db postgres
# Los contenedores pueden comunicarse por nombre (web, db)
```

## 7. Docker Compose (Básico)

### Archivo docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    image: nginx
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - mynetwork
    depends_on:
      - db
  
  db:
    image: postgres:12
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: myapp
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - mynetwork

volumes:
  db_data:

networks:
  mynetwork:
    driver: bridge
```

### Comandos Docker Compose
```bash
docker-compose up                # Levantar servicios
docker-compose up -d             # Levantar en background
docker-compose down              # Detener y eliminar
docker-compose ps               # Ver estado
docker-compose logs -f          # Ver logs en tiempo real
docker-compose exec web bash    # Entrar en contenedor
```

## 8. Mejores Prácticas

### Optimizar Imágenes
```dockerfile
# Usar imágenes base pequeñas
FROM alpine:3.14

# Combinar RUN para reducir capas
RUN apk update && \
    apk add --no-cache nginx && \
    rm -rf /var/cache/apk/*

# No ejecutar como root
USER www-data
```

### Seguridad
```dockerfile
# Escanear vulnerabilidades
docker scan myimage

# No usar latest
FROM ubuntu:20.04

# Especificar versiones
RUN apt-get install nginx=1.20.1
```

## 9. Troubleshooting Común

```bash
# Ver logs detallados
docker logs -f mycontainer

# Inspeccionar contenedor
docker inspect mycontainer

# Ver procesos del contenedor
docker top mycontainer

# Estadísticas
docker stats mycontainer

# Debugging dentro del contenedor
docker exec -it mycontainer sh
```

## 10. Casos de Uso Comunes

### Ejecutar Servidor Web
```bash
docker run -d -p 8080:80 --name webserver nginx
curl localhost:8080
```

### Ejecutar Base de Datos
```bash
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=secret \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  postgres:12
```

### Ejecutar Aplicación Personalizada
```bash
# Dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

# Construir
docker build -t myapp:1.0 .

# Ejecutar
docker run -d -p 5000:5000 myapp:1.0
```

---
**Nivel**: Básico
**Tiempo estimado de estudio**: 3-4 horas
