# 🔍 Ejercicios Prácticos de Troubleshooting

## 🎯 Metodología de Troubleshooting

```
1. IDENTIFICAR el problema
   └─ ¿Qué está fallando exactamente?
   └─ ¿Cuándo empezó?
   └─ ¿Qué cambió recientemente?

2. RECOLECTAR información
   └─ Logs
   └─ Métricas
   └─ Estado del sistema

3. FORMULAR hipótesis
   └─ ¿Cuáles son las causas posibles?

4. PROBAR hipótesis
   └─ Verificar cada teoría sistemáticamente

5. IMPLEMENTAR solución
   └─ Aplicar fix
   └─ Verificar que funciona

6. DOCUMENTAR
   └─ Post-mortem
   └─ Lecciones aprendidas
```

---

## 🚨 Escenario 1: Web Application Down

### Síntomas
```
- Usuarios reportan error 502 Bad Gateway
- Nginx está running
- La aplicación no responde
```

### Tu Proceso de Troubleshooting

**Paso 1: Verificar que el problema existe**
```bash
# Test del endpoint
curl -I http://localhost

# Output esperado con problema:
# HTTP/1.1 502 Bad Gateway
```

**Paso 2: Verificar servicios**
```bash
# ¿Está Nginx running?
systemctl status nginx

# ¿Está la aplicación running?
systemctl status myapp
# o
ps aux | grep myapp

# ¿Qué puertos están escuchando?
ss -tulpn | grep :8080
```

**Paso 3: Revisar logs**
```bash
# Logs de Nginx
tail -f /var/log/nginx/error.log

# Buscar errores recientes
journalctl -u myapp -n 100 --no-pager

# Si es Docker
docker logs myapp-container
```

**Paso 4: Verificar conectividad**
```bash
# ¿Nginx puede conectar al backend?
curl http://localhost:8080

# Test de puerto
telnet localhost 8080
# o
nc -zv localhost 8080
```

**Posibles Causas y Soluciones**

#### Causa 1: Aplicación crashed
```bash
# Verificar
systemctl status myapp
# Salida: "Active: failed"

# Ver por qué crasheó
journalctl -u myapp -n 50

# Solución
systemctl restart myapp

# Verificar
curl http://localhost:8080
```

#### Causa 2: Aplicación no está escuchando en puerto correcto
```bash
# Verificar configuración
cat /etc/myapp/config.yaml | grep port

# Verificar qué puerto usa realmente
ss -tulpn | grep myapp

# Si hay mismatch, corregir config de Nginx o app
```

#### Causa 3: Firewall bloqueando
```bash
# Verificar reglas de firewall
sudo iptables -L -n

# Agregar regla si necesario
sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
```

#### Causa 4: Out of memory (OOMKilled)
```bash
# Verificar en logs
dmesg | grep -i "out of memory"
journalctl | grep -i "killed process"

# Ver uso de memoria
free -h
ps aux --sort=-%mem | head

# Solución: Aumentar memoria o optimizar app
```

---

## 🚨 Escenario 2: Kubernetes Pod en CrashLoopBackOff

### Síntomas
```
- Pod se reinicia constantemente
- Estado: CrashLoopBackOff
- Aplicación no disponible
```

### Troubleshooting Steps

**Paso 1: Ver estado del pod**
```bash
kubectl get pods
# NAME                     READY   STATUS             RESTARTS
# myapp-7d8f9c5b4-abc123   0/1     CrashLoopBackOff   5

kubectl describe pod myapp-7d8f9c5b4-abc123
```

**Paso 2: Revisar eventos**
```bash
kubectl describe pod myapp-7d8f9c5b4-abc123 | grep -A 20 Events

# Buscar pistas:
# - Back-off restarting failed container
# - Error: ImagePullBackOff
# - Liveness probe failed
```

**Paso 3: Ver logs**
```bash
# Logs actuales
kubectl logs myapp-7d8f9c5b4-abc123

# Logs del contenedor anterior (el que crasheó)
kubectl logs myapp-7d8f9c5b4-abc123 --previous
```

**Paso 4: Entrar al pod (si está running momentáneamente)**
```bash
kubectl exec -it myapp-7d8f9c5b4-abc123 -- /bin/bash

# Dentro del pod
env                    # verificar variables de entorno
ls -la /app           # verificar archivos
cat /app/config.yaml  # verificar config
```

**Posibles Causas y Soluciones**

#### Causa 1: Aplicación crashea al iniciar
```bash
# Ver logs
kubectl logs myapp-7d8f9c5b4-abc123 --previous

# Output podría mostrar:
# Error: Cannot connect to database
# Connection refused: localhost:5432

# Solución: Verificar config de DB
kubectl get configmap myapp-config -o yaml
kubectl get secret db-credentials -o yaml

# Corregir y aplicar
kubectl apply -f configmap.yaml
kubectl rollout restart deployment myapp
```

#### Causa 2: Liveness Probe falla
```bash
# Ver configuración del probe
kubectl get pod myapp-7d8f9c5b4-abc123 -o yaml | grep -A 10 livenessProbe

# Podría ser:
# - App tarda mucho en iniciar (aumentar initialDelaySeconds)
# - Endpoint /health no existe
# - Timeout muy corto

# Solución: Ajustar deployment
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
      - name: myapp
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 60  # ⬅️ aumentar
          periodSeconds: 10
```

#### Causa 3: Falta ConfigMap o Secret
```bash
# Ver referencias en pod spec
kubectl get pod myapp-7d8f9c5b4-abc123 -o yaml | grep -E "configMap|secret"

# Verificar que existen
kubectl get configmap
kubectl get secret

# Crear si falta
kubectl create configmap myapp-config --from-file=config.yaml
```

#### Causa 4: Recursos insuficientes
```bash
# Ver resource limits
kubectl describe pod myapp-7d8f9c5b4-abc123 | grep -A 5 "Limits\|Requests"

# Ver si fue OOMKilled
kubectl describe pod myapp-7d8f9c5b4-abc123 | grep -i "oom"

# Solución: Aumentar limits
spec:
  containers:
  - name: myapp
    resources:
      requests:
        memory: "256Mi"
        cpu: "250m"
      limits:
        memory: "512Mi"  # ⬅️ aumentar
        cpu: "500m"
```

---

## 🚨 Escenario 3: Alto Uso de CPU en Producción

### Síntomas
```
- Alertas de CPU > 90%
- Sistema lento
- Usuarios reportan timeouts
```

### Troubleshooting Steps

**Paso 1: Confirmar el problema**
```bash
# Ver CPU usage actual
top
# Press 'P' para ordenar por CPU
# Press '1' para ver cada core

# O usar htop (más visual)
htop

# Ver load average
uptime
# Interpretar: Si load > número de cores, hay problema
```

**Paso 2: Identificar proceso culpable**
```bash
# Top procesos por CPU
ps aux --sort=-%cpu | head -20

# Watch en tiempo real
watch -n 1 'ps aux --sort=-%cpu | head -20'

# Con más detalle
top -c  # muestra comando completo
```

**Paso 3: Investigar el proceso**
```bash
# Supongamos PID 12345 está usando 95% CPU
PID=12345

# Ver detalles del proceso
ps aux | grep $PID
cat /proc/$PID/cmdline
ls -la /proc/$PID/

# Ver qué archivos tiene abiertos
lsof -p $PID

# Ver syscalls que está haciendo
strace -p $PID

# Ver threads del proceso
ps -T -p $PID
```

**Paso 4: Análisis según tipo de app**

#### Si es aplicación web (Node.js, Python, etc)
```bash
# Ver logs de la aplicación
tail -f /var/log/myapp/app.log

# Si hay query lento en DB
# Ver queries activas en PostgreSQL
psql -c "SELECT pid, now() - query_start AS duration, query 
         FROM pg_stat_activity 
         WHERE state = 'active' 
         ORDER BY duration DESC;"

# Si hay loop infinito o bug
# Attach debugger o matar proceso
kill -TERM $PID
# Luego investigar código
```

#### Si es Docker container
```bash
# Ver stats de containers
docker stats

# Identificar container problemático
docker top <container-id>

# Ver logs
docker logs <container-id> --tail 100

# Entrar al container
docker exec -it <container-id> bash
top
```

#### Si es Kubernetes pod
```bash
# Ver top pods
kubectl top pods -A --sort-by=cpu

# Ver detalles del pod problemático
kubectl describe pod <pod-name>

# Ver logs
kubectl logs <pod-name> -f

# CPU throttling?
# Verificar si está siendo throttled
kubectl get pod <pod-name> -o yaml | grep -A 5 "limits\|requests"
```

**Posibles Causas y Soluciones**

#### Causa 1: Traffic spike (legítimo)
```bash
# Verificar en logs de Nginx/Apache
tail -f /var/log/nginx/access.log | wc -l

# Contar requests por segundo
tail -f /var/log/nginx/access.log | \
  awk '{print $4}' | cut -d: -f1-2 | uniq -c

# Solución: Escalar
# Kubernetes:
kubectl scale deployment myapp --replicas=10

# O configurar HPA
kubectl autoscale deployment myapp --cpu-percent=70 --min=3 --max=10
```

#### Causa 2: Inefficient code/query
```bash
# Profiling de aplicación Python
python -m cProfile -o profile.stats app.py

# Node.js
node --prof app.js

# Ver slow queries en DB
# PostgreSQL
SELECT * FROM pg_stat_statements 
ORDER BY mean_exec_time DESC 
LIMIT 10;

# Solución: Optimizar código/queries
# Agregar índices, cachear, etc
```

#### Causa 3: DoS attack
```bash
# Ver IPs con más requests
awk '{print $1}' /var/log/nginx/access.log | \
  sort | uniq -c | sort -rn | head -20

# Si una IP tiene requests anormales
# Bloquear con iptables
iptables -A INPUT -s <malicious-ip> -j DROP

# O en Nginx
# /etc/nginx/conf.d/block.conf
deny <malicious-ip>;
```

---

## 🚨 Escenario 4: Disco Lleno

### Síntomas
```
- Alerta: Disk usage > 95%
- Aplicaciones fallan al escribir
- "No space left on device"
```

### Troubleshooting Steps

**Paso 1: Confirmar problema**
```bash
df -h
# Buscar filesystem con 95%+

# Ver inodes también (a veces se acaban antes que espacio)
df -i
```

**Paso 2: Encontrar qué está usando espacio**
```bash
# Ver uso por directorio (nivel 1)
du -h --max-depth=1 / 2>/dev/null | sort -rh | head -20

# Más específico
du -h --max-depth=1 /var | sort -rh
du -h --max-depth=1 /var/log | sort -rh

# Encontrar archivos grandes (>100MB)
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null | \
  awk '{print $5, $9}' | sort -rh | head -20
```

**Paso 3: Identificar culpables comunes**
```bash
# Logs
du -sh /var/log/*

# Docker
docker system df
docker system df -v  # verbose

# Journald
journalctl --disk-usage

# Core dumps
find /var -name "core.*" -type f -exec ls -lh {} \;

# APT cache
du -sh /var/cache/apt/archives/
```

**Soluciones**

#### Limpiar logs
```bash
# Rotar logs inmediatamente
logrotate -f /etc/logrotate.conf

# Eliminar logs viejos
find /var/log -name "*.log" -mtime +30 -delete
find /var/log -name "*.gz" -mtime +30 -delete

# Truncar log activo (sin reiniciar servicio)
truncate -s 0 /var/log/app/huge.log

# Configurar mejor rotación
# /etc/logrotate.d/myapp
/var/log/myapp/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
}
```

#### Limpiar Docker
```bash
# Ver uso
docker system df

# Eliminar contenedores stopped
docker container prune

# Eliminar imágenes sin usar
docker image prune -a

# Eliminar volumes sin usar
docker volume prune

# Limpieza total
docker system prune -a --volumes
```

#### Limpiar journald
```bash
# Ver tamaño
journalctl --disk-usage

# Limpiar hasta 100MB
journalctl --vacuum-size=100M

# Limpiar >7 días
journalctl --vacuum-time=7d

# Configurar límite permanente
# /etc/systemd/journald.conf
SystemMaxUse=500M
```

#### Limpiar package managers
```bash
# APT (Debian/Ubuntu)
apt-get clean
apt-get autoclean
apt-get autoremove

# YUM (CentOS/RHEL)
yum clean all
```

---

## 🚨 Escenario 5: Conectividad de Red Intermitente

### Síntomas
```
- Timeouts aleatorios
- Algunas requests funcionan, otras no
- Ping funciona pero HTTP no
```

### Troubleshooting Steps

**Paso 1: Test básico de conectividad**
```bash
# Ping
ping -c 10 target-server

# Si hay packet loss
# 10 packets transmitted, 7 received, 30% packet loss

# Test DNS
dig example.com
nslookup example.com

# Test ruta
traceroute example.com
mtr example.com  # mejor que traceroute
```

**Paso 2: Test de puertos específicos**
```bash
# Telnet
telnet example.com 80

# Netcat
nc -zv example.com 80

# Curl con detalles
curl -v -m 5 http://example.com

# Test múltiple
for i in {1..20}; do 
  curl -o /dev/null -s -w "%{http_code}\n" http://example.com
  sleep 1
done
```

**Paso 3: Verificar configuración local**
```bash
# Ver interfaces
ip addr

# Ver rutas
ip route

# Ver DNS config
cat /etc/resolv.conf

# Test DNS manualmente
dig @8.8.8.8 example.com  # usar Google DNS
```

**Paso 4: Verificar firewall y iptables**
```bash
# Ver reglas iptables
iptables -L -n -v

# Ver conexiones activas
ss -tan | grep ESTAB
netstat -tan | grep ESTAB

# Ver si hay conexiones en TIME_WAIT (muchas = problema)
ss -tan | grep TIME_WAIT | wc -l
```

**Soluciones Comunes**

#### Problema de DNS
```bash
# Síntomas: ping funciona con IP pero no con hostname

# Verificar
dig example.com  # tarda mucho o falla

# Solución temporal: usar DNS público
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf

# Solución permanente (Ubuntu/Debian)
# /etc/systemd/resolved.conf
[Resolve]
DNS=8.8.8.8 1.1.1.1
```

#### Firewall bloqueando
```bash
# Ver si hay denies
grep -i "DPT=80" /var/log/syslog

# Agregar regla
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT

# Guardar reglas
iptables-save > /etc/iptables/rules.v4
```

#### Connection pool exhausted
```bash
# Ver conexiones por estado
ss -tan | awk '{print $2}' | sort | uniq -c

# Si muchas en TIME_WAIT, ajustar kernel params
# /etc/sysctl.conf
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_fin_timeout = 30

# Aplicar
sysctl -p
```

---

## ✅ Checklist de Troubleshooting

Cuando tengas un problema, sigue esta checklist:

**Información básica:**
- [ ] ¿Qué está fallando exactamente?
- [ ] ¿Cuándo empezó?
- [ ] ¿Qué cambió recientemente? (deployment, config, etc)
- [ ] ¿Es consistente o intermitente?
- [ ] ¿Afecta a todos los usuarios o solo algunos?

**Datos a recolectar:**
- [ ] Logs de aplicación
- [ ] Logs de sistema (syslog, journald)
- [ ] Métricas (CPU, RAM, disk, network)
- [ ] Estado de servicios
- [ ] Versiones (app, SO, dependencias)

**Verificaciones estándar:**
- [ ] ¿Servicios running?
- [ ] ¿Puertos escuchando?
- [ ] ¿Logs muestran errores?
- [ ] ¿Recursos suficientes? (CPU, RAM, disk)
- [ ] ¿Conectividad de red OK?
- [ ] ¿Permisos correctos?
- [ ] ¿Configuración correcta?

---

## 🎓 Tips Pro

1. **Usa tmux/screen** para mantener múltiples terminales abiertas
2. **Logs en tiempo real**: `tail -f` es tu amigo
3. **Documenta mientras troubleshooteas**: Ayuda a no perder el hilo
4. **Cambios incrementales**: Cambia una cosa a la vez
5. **No asumas**: Verifica todo, incluso lo obvio
6. **Google el error exacto**: Entre comillas en Google
7. **Busca en logs del sistema**: `journalctl`, `dmesg`, `/var/log/syslog`
8. **Verifica lo obvio primero**: ¿Está el servicio corriendo? ¿Hay espacio en disco?

---

## 📝 Template de Post-Mortem

Después de resolver un incidente, documéntalo:

```markdown
# Post-Mortem: [Título del Incidente]

## Resumen
[Breve descripción del problema]

## Timeline
- 14:32 - Alertas de HTTP 5xx
- 14:35 - Se identifica pod crasheando
- 14:40 - Se encuentra memoria insuficiente
- 14:45 - Se aumenta memory limit
- 14:50 - Servicio recuperado

## Root Cause
[Causa raíz del problema]

## Impact
- Duración: 18 minutos
- Usuarios afectados: ~500
- Requests fallidos: 1,234

## Resolution
[Cómo se resolvió]

## Action Items
- [ ] Aumentar memory limits en staging también
- [ ] Configurar alerta de memory usage
- [ ] Agregar health check más robusto
- [ ] Documentar troubleshooting para próxima vez

## Lessons Learned
[Qué aprendimos]
```
