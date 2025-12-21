# 🎯 Cheat Sheet - Comandos Rápidos para el Test

## 🔥 Prometheus PromQL (Top 10)

```promql
# 1. Request rate
sum(rate(http_requests_total[5m]))

# 2. Error rate %
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) * 100

# 3. CPU usage %
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# 4. Memory usage %
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

# 5. P95 latency
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

# 6. Disk usage %
(node_filesystem_size_bytes - node_filesystem_free_bytes) / node_filesystem_size_bytes * 100

# 7. Pods not ready
kube_pod_status_ready{condition="false"} == 1

# 8. Top pods by CPU
topk(10, sum(rate(container_cpu_usage_seconds_total[5m])) by (pod))

# 9. Service up/down
up == 1  # or == 0

# 10. Availability %
avg_over_time(up[24h]) * 100
```

---

## ☸️ Kubernetes (Top 20)

```bash
# Pods
kubectl get pods -A
kubectl describe pod <pod>
kubectl logs <pod> -f
kubectl logs <pod> --previous
kubectl exec -it <pod> -- bash

# Debugging
kubectl get events --sort-by='.lastTimestamp'
kubectl top pods
kubectl top nodes

# Deployments
kubectl get deployments
kubectl scale deployment <name> --replicas=5
kubectl rollout status deployment/<name>
kubectl rollout undo deployment/<name>

# Services
kubectl get svc
kubectl describe svc <name>
kubectl port-forward <pod> 8080:80

# Config
kubectl get configmap
kubectl describe configmap <name>
kubectl get secret
kubectl create secret generic <name> --from-literal=key=value

# Apply
kubectl apply -f manifest.yaml
kubectl delete -f manifest.yaml
```

---

## 🐳 Docker (Top 15)

```bash
# Imágenes
docker images
docker build -t myapp:latest .
docker pull nginx:latest
docker rmi <image-id>

# Contenedores
docker ps
docker ps -a
docker run -d -p 8080:80 --name web nginx
docker logs <container> -f
docker exec -it <container> bash
docker stop <container>
docker rm <container>

# Limpieza
docker system prune -a
docker volume prune

# Compose
docker-compose up -d
docker-compose down
docker-compose logs -f
```

---

## 🐧 Linux (Top 30)

```bash
# Files
ls -la
cd /path
pwd
mkdir -p /path/to/dir
rm -rf directory/
cp -r source/ dest/
mv old new
find / -name "*.log"
grep -r "error" /var/log/

# Process
ps aux | grep nginx
top
htop
kill -9 <PID>
killall <process-name>

# System
systemctl status <service>
systemctl start <service>
systemctl restart <service>
journalctl -u <service> -f

# Network
ss -tulpn
netstat -tulpn
curl -I http://example.com
ping google.com
dig example.com

# Resources
df -h
du -sh /var/log
free -h
uptime

# Text processing
cat file.txt
tail -f /var/log/syslog
head -n 20 file.txt
grep "error" log.txt
awk '{print $1}' file.txt
sed 's/old/new/g' file.txt

# Permisos
chmod 755 script.sh
chown user:group file.txt
ls -l
```

---

## 📊 Grafana

```javascript
// Queries comunes
// CPU
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

// Memory
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

// Requests
sum(rate(http_requests_total[5m]))

// Error rate
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) * 100

// Variables
$namespace, $pod, $service

// Thresholds
Green: < 70
Yellow: 70-85
Red: > 85
```

---

## 🔧 Troubleshooting Rápido

### Web app down (502)
```bash
1. systemctl status myapp
2. curl http://localhost:8080
3. tail -f /var/log/nginx/error.log
4. journalctl -u myapp -n 50
5. ss -tulpn | grep 8080
```

### Pod CrashLoopBackOff
```bash
1. kubectl describe pod <pod>
2. kubectl logs <pod> --previous
3. kubectl get events
4. kubectl get configmap
5. kubectl get pod <pod> -o yaml
```

### High CPU
```bash
1. top / htop
2. ps aux --sort=-%cpu | head
3. systemctl status <service>
4. kubectl top pods -A
5. docker stats
```

### Disk full
```bash
1. df -h
2. du -h --max-depth=1 / | sort -rh
3. find / -type f -size +100M
4. docker system df
5. journalctl --disk-usage
```

---

## 🎯 Respuestas Rápidas TestGorilla

**Q: ¿Qué hace `rate()` en Prometheus?**  
A: Calcula tasa de cambio por segundo de un counter

**Q: ¿Diferencia entre Deployment y Pod?**  
A: Deployment gestiona Pods (replicas, updates), Pod es unidad mínima

**Q: ¿CMD vs ENTRYPOINT en Docker?**  
A: CMD se puede sobrescribir, ENTRYPOINT siempre se ejecuta

**Q: ¿Qué es un Service en K8s?**  
A: Abstracción que expone Pods como servicio de red

**Q: ¿Cómo ver logs de pod anterior (crashed)?**  
A: `kubectl logs <pod> --previous`

**Q: ¿Qué significa ClusterIP?**  
A: Service solo accesible dentro del cluster

**Q: ¿Requests vs Limits en K8s?**  
A: Requests = mínimo garantizado, Limits = máximo permitido

**Q: ¿Qué es un ConfigMap?**  
A: Objeto K8s para almacenar configuración no sensible

**Q: ¿Para qué sirve `docker-compose`?**  
A: Definir y ejecutar apps multi-container

**Q: ¿Qué hace `grep -r`?**  
A: Búsqueda recursiva en directorios

---

## 📝 Comandos para Memorizar

### Must Know (20 comandos críticos)
```bash
# K8s
kubectl get pods -A
kubectl describe pod <pod>
kubectl logs <pod> -f
kubectl exec -it <pod> -- bash
kubectl apply -f file.yaml

# Docker
docker ps -a
docker logs <container> -f
docker exec -it <container> bash
docker-compose up -d

# Linux
systemctl status <service>
journalctl -u <service> -f
tail -f /var/log/syslog
ps aux | grep <process>
top
df -h
free -h
ss -tulpn
curl -I http://url
grep -r "pattern" /path

# PromQL
rate(metric[5m])
sum(...) by (label)
```

---

## 🚨 Errores Comunes a Evitar

1. ❌ `kubectl logs <pod>` cuando crasheó → ✅ `kubectl logs <pod> --previous`
2. ❌ Olvidar `-A` en `kubectl get pods` → ✅ `kubectl get pods -A`
3. ❌ Usar `avg()` con counter → ✅ Usar `rate()` primero
4. ❌ `docker run` sin `-d` → Se queda en foreground
5. ❌ `chmod 777` → Security risk, usar 755 o 644
6. ❌ No verificar que servicio está running antes de debuggear
7. ❌ Olvidar `sudo` para comandos de sistema
8. ❌ No usar `--previous` para ver logs de pod crasheado
9. ❌ Confundir Service con Deployment en K8s
10. ❌ No usar `set -e` en bash scripts críticos
