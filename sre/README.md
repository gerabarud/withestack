# 🚀 Guía de Estudio DevOps/SRE - Whitestack

## 📋 Sobre este proyecto

Este es tu repositorio de preparación para el puesto **DevOps/SRE - Prometheus, Grafana** en Whitestack.

Contiene material de estudio estructurado, ejemplos prácticos, comandos y ejercicios basados en los requisitos del puesto y las evaluaciones típicas de TestGorilla.

---

## 🎯 Áreas Clave del Test

TestGorilla típicamente evalúa estas competencias para roles DevOps/SRE:

### 1. **Monitoreo y Observabilidad** (CRÍTICO para Whitestack)
   - ✅ Prometheus: queries, alertas, exporters
   - ✅ Grafana: dashboards, visualizaciones, data sources
   - ✅ Elasticsearch & Kibana
   - ✅ Métricas, logs y trazas distribuidas

### 2. **Contenedores y Orquestación**
   - ✅ Docker: Dockerfiles, ciclo de vida, networking
   - ✅ Kubernetes: pods, deployments, services, troubleshooting
   - ✅ Helm charts básico

### 3. **Automatización y Scripting**
   - ✅ Bash scripting avanzado
   - ✅ Python para automatización
   - ✅ CI/CD pipelines (GitLab CI, Jenkins)

### 4. **Linux System Administration**
   - ✅ Comandos esenciales
   - ✅ Networking básico
   - ✅ Troubleshooting de sistemas

### 5. **Cloud & Infrastructure as Code**
   - ✅ OpenStack (específico para Whitestack)
   - ✅ AWS/GCP/Azure conceptos básicos
   - ✅ Terraform básico

### 6. **Incident Management & SRE Practices**
   - ✅ Debugging de aplicaciones
   - ✅ Análisis de performance
   - ✅ SLIs, SLOs, SLAs
   - ✅ Post-mortems

---

## 📚 Estructura del Proyecto

```
sre/
├── README.md                          # Este archivo
├── 01-prometheus/                     # Guías de Prometheus
│   ├── guia-basica.md
│   ├── queries-esenciales.md
│   ├── alertas.md
│   ├── exporters.md
│   └── ejemplos/
├── 02-grafana/                        # Guías de Grafana
│   ├── guia-basica.md
│   ├── dashboards.md
│   ├── queries.md
│   └── ejemplos/
├── 03-kubernetes/                     # Guías de Kubernetes
│   ├── conceptos-basicos.md
│   ├── comandos-kubectl.md
│   ├── troubleshooting.md
│   └── manifiestos/
├── 04-docker/                         # Guías de Docker
│   ├── guia-basica.md
│   ├── dockerfiles.md
│   ├── networking.md
│   └── ejemplos/
├── 05-automatizacion/                 # Scripts y automatización
│   ├── bash/
│   │   ├── guia-bash.md
│   │   └── scripts/
│   └── python/
│       ├── guia-python.md
│       └── scripts/
├── 06-linux/                          # Linux essentials
│   ├── comandos-esenciales.md
│   ├── networking.md
│   └── troubleshooting.md
├── 07-cicd/                           # CI/CD y GitOps
│   ├── gitlab-ci.md
│   ├── jenkins.md
│   └── ejemplos/
├── 08-sre-practices/                  # Prácticas SRE
│   ├── sli-slo-sla.md
│   ├── incident-response.md
│   └── debugging.md
├── 09-cloud/                          # Cloud platforms
│   ├── openstack.md
│   ├── aws-basics.md
│   └── terraform-basics.md
└── 10-ejercicios-practicos/          # Ejercicios integrados
    ├── escenarios-troubleshooting.md
    ├── ejercicios-monitoring.md
    └── desafios-kubernetes.md
```

---

## 🎓 Plan de Estudio Sugerido (7-10 días)

### **Semana 1: Fundamentos Críticos**

#### Día 1-2: Prometheus & Grafana (PRIORIDAD MÁXIMA)
- [ ] Revisar `01-prometheus/` completo
- [ ] Practicar queries PromQL
- [ ] Revisar `02-grafana/` completo
- [ ] Crear 3 dashboards de ejemplo
- [ ] Entender exporters comunes

#### Día 3-4: Kubernetes
- [ ] Revisar `03-kubernetes/` completo
- [ ] Practicar comandos kubectl esenciales
- [ ] Entender troubleshooting de pods
- [ ] Revisar networking básico en K8s

#### Día 5: Docker
- [ ] Revisar `04-docker/` completo
- [ ] Crear 5 Dockerfiles de ejemplo
- [ ] Entender ciclo de vida de contenedores
- [ ] Practicar docker-compose

#### Día 6: Linux & Scripting
- [ ] Revisar `06-linux/` comandos esenciales
- [ ] Practicar `05-automatizacion/bash/`
- [ ] Hacer 10 ejercicios de bash
- [ ] Revisar networking básico

#### Día 7: CI/CD & SRE Practices
- [ ] Revisar `07-cicd/` 
- [ ] Entender GitLab CI pipelines
- [ ] Revisar `08-sre-practices/`
- [ ] Entender SLIs, SLOs, SLAs

### **Últimos días: Práctica Intensiva**
- [ ] Hacer todos los ejercicios en `10-ejercicios-practicos/`
- [ ] Revisar escenarios de troubleshooting
- [ ] Practicar debugging en tiempo real
- [ ] Repasar conceptos débiles

---

## 🔥 Comandos y Conceptos Más Importantes (Memorizar)

### Prometheus PromQL (Top 10)
```promql
# 1. Rate de requests HTTP
rate(http_requests_total[5m])

# 2. CPU usage promedio
avg(rate(container_cpu_usage_seconds_total[5m])) by (pod)

# 3. Memory usage
container_memory_usage_bytes / container_spec_memory_limit_bytes * 100

# 4. Latencia p95
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# 5. Error rate
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))
```

### Kubernetes (Top 15)
```bash
# Pods
kubectl get pods -A
kubectl describe pod <pod-name>
kubectl logs <pod-name> -f
kubectl exec -it <pod-name> -- /bin/bash

# Debugging
kubectl get events --sort-by='.lastTimestamp'
kubectl top pods
kubectl top nodes

# Deployments
kubectl rollout status deployment/<name>
kubectl rollout undo deployment/<name>

# Services & Networking
kubectl get svc
kubectl port-forward <pod-name> 8080:80

# Config
kubectl get configmap
kubectl get secrets
```

### Docker (Top 10)
```bash
# Imágenes
docker build -t myapp:latest .
docker images
docker rmi <image-id>

# Contenedores
docker run -d -p 8080:80 nginx
docker ps -a
docker logs <container-id> -f
docker exec -it <container-id> bash
docker stop <container-id>
docker rm <container-id>

# Limpieza
docker system prune -a
```

### Linux (Top 20)
```bash
# Procesos y recursos
top / htop
ps aux | grep <process>
kill -9 <pid>
systemctl status <service>
journalctl -u <service> -f

# Networking
netstat -tulpn
ss -tulpn
curl -I http://example.com
ping / traceroute / dig

# Archivos
find / -name "*.log"
grep -r "error" /var/log/
tail -f /var/log/syslog
df -h
du -sh /var/log/*

# Permisos
chmod / chown
```

---

## 🧪 TestGorilla: Qué Esperar

### Formato Típico del Test
1. **Duración**: 30-60 minutos por módulo
2. **Tipos de preguntas**:
   - Opción múltiple (conceptos teóricos)
   - Completar comandos
   - Debugging de código/configuraciones
   - Análisis de logs y métricas
   - Escenarios de troubleshooting

### Módulos Comunes para DevOps/SRE
- ✅ **Kubernetes**: administración, troubleshooting
- ✅ **Docker**: Dockerfiles, networking
- ✅ **Linux**: comandos, scripting
- ✅ **Cloud Computing**: conceptos generales
- ✅ **Monitoring**: Prometheus/Grafana específico
- ✅ **Problem Solving**: debugging, análisis de root cause
- ✅ **Git**: comandos básicos
- ✅ **CI/CD**: pipelines, automatización

### Consejos para el Test
1. **Lee cuidadosamente**: TestGorilla penaliza respuestas incorrectas
2. **Maneja el tiempo**: No te quedes atascado en una pregunta
3. **Prioriza lo que sabes**: Responde primero las que dominas
4. **Comandos exactos**: Presta atención a la sintaxis exacta
5. **Troubleshooting sistemático**: Sigue un método ordenado
6. **YAML/JSON**: Cuidado con la indentación

---

## 📖 Recursos Adicionales Recomendados

### Documentación Oficial
- [Prometheus Docs](https://prometheus.io/docs/)
- [Grafana Docs](https://grafana.com/docs/)
- [Kubernetes Docs](https://kubernetes.io/docs/)
- [Docker Docs](https://docs.docker.com/)

### Práctica Interactiva
- [Prometheus Query Examples](https://prometheus.io/docs/prometheus/latest/querying/examples/)
- [Play with Kubernetes](https://labs.play-with-k8s.com/)
- [Play with Docker](https://labs.play-with-docker.com/)
- [Grafana Play](https://play.grafana.org/)

### Libros Recomendados
- "Site Reliability Engineering" - Google
- "The DevOps Handbook"
- "Prometheus: Up & Running"

---

## 🎯 Checklist Pre-Test

Una semana antes del test, asegúrate de poder hacer esto sin buscar:

### Prometheus
- [ ] Escribir 10 queries PromQL comunes
- [ ] Explicar tipos de métricas (counter, gauge, histogram, summary)
- [ ] Configurar un exporter básico
- [ ] Crear una regla de alerting

### Grafana
- [ ] Crear un dashboard con 5 paneles
- [ ] Conectar múltiples data sources
- [ ] Usar variables en dashboards
- [ ] Configurar alertas básicas

### Kubernetes
- [ ] Desplegar una aplicación multi-container
- [ ] Debuggear un pod que no inicia
- [ ] Escalar un deployment
- [ ] Exponer un servicio

### Docker
- [ ] Escribir un Dockerfile multi-stage
- [ ] Crear un docker-compose con 3 servicios
- [ ] Debuggear un contenedor que crashea
- [ ] Entender networking entre contenedores

### Linux & Scripting
- [ ] Escribir un script bash con funciones y loops
- [ ] Parsear logs con awk/sed/grep
- [ ] Debuggear un servicio que no inicia
- [ ] Analizar uso de CPU/memoria/disco

### SRE
- [ ] Explicar qué es un SLI, SLO y SLA
- [ ] Calcular error budget
- [ ] Describir proceso de incident response
- [ ] Escribir un post-mortem básico

---

## 🚨 Puntos Críticos para Whitestack

Basado en el job posting, pon **EXTRA ATENCIÓN** a:

1. **OpenStack**: Familiarízate con conceptos básicos
2. **Monitoreo de infraestructura compleja**: Routers, switches, clusters
3. **Kubernetes avanzado**: No solo pods, sino arquitectura completa
4. **CI/CD para imágenes**: Pipelines de construcción y deployment
5. **Incidentes en producción**: Metodología de troubleshooting
6. **Dashboards para stakeholders**: Visualizaciones claras y útiles

---

## 💪 ¡Vamos por ese puesto!

**Recuerda**: Whitestack valora:
- 🔧 **Habilidades técnicas sólidas** (lo que vas a demostrar en el test)
- 🚀 **Proactividad y aprendizaje continuo**
- 🤝 **Trabajo en equipo y comunicación**
- 💡 **Pasión por el open-source**

**¡Mucha suerte! 🍀**

---

## 📝 Notas de Estudio

Usa esta sección para tus apuntes personales:

```
Fecha de inicio: _______________
Fecha del test: _______________

Temas que domino:
- 
- 

Temas a reforzar:
- 
- 

Preguntas para investigar:
- 
- 
```
