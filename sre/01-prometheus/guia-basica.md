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

## 🎯 Cheat Sheet Rápido

```promql
# INSTANT VECTORS (valor actual)
metric_name
metric_name{label="value"}

# RANGE VECTORS (valores en rango)
metric_name[5m]

# RATE (cambio por segundo)
rate(counter_metric[5m])

# AGREGACIONES
sum / avg / max / min / count / topk / bottomk

# GROUPING
by (label1, label2)
without (label1, label2)

# COMPARACIÓN
metric > 100
metric == 1
metric != 0

# MATH
metric1 + metric2
metric1 - metric2
metric1 * 100
metric1 / metric2

# FUNCIONES ÚTILES
abs() - valor absoluto
ceil() / floor() - redondeo
round() - redondear
clamp_max() / clamp_min() - limitar valores
```

---

## 🔧 Configuración Básica

### prometheus.yml Mínimo

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: 'production'

# Alertmanager config
alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']

# Load alert rules
rule_files:
  - 'alerts.yml'

# Scrape configs
scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node1:9100', 'node2:9100']

  - job_name: 'app'
    static_configs:
      - targets: ['app:8080']
    metrics_path: '/metrics'
```

---

## 🚀 Comandos Útiles

```bash
# Validar configuración
promtool check config prometheus.yml

# Validar reglas de alertas
promtool check rules alerts.yml

# Query desde CLI
promtool query instant http://localhost:9090 'up'

# Query rango de tiempo
promtool query range http://localhost:9090 'rate(http_requests_total[5m])'

# Test unitario de alerts
promtool test rules test.yml
```

---

## 📚 Recursos para Profundizar

- [Prometheus Query Examples](https://prometheus.io/docs/prometheus/latest/querying/examples/)
- [PromQL Cheat Sheet](https://promlabs.com/promql-cheat-sheet/)
- [Awesome Prometheus Alerts](https://awesome-prometheus-alerts.grep.to/)

---

## ✅ Checklist de Dominio

- [ ] Puedo explicar los 4 tipos de métricas
- [ ] Sé cuándo usar `rate()` vs `irate()` vs `increase()`
- [ ] Puedo escribir queries con `by` y `without`
- [ ] Entiendo cómo calcular error rates
- [ ] Puedo calcular percentiles con `histogram_quantile()`
- [ ] Sé escribir alertas con `for` y `labels`
- [ ] Conozco los exporters principales
- [ ] Puedo debuggear por qué una métrica no aparece
- [ ] Entiendo cómo funcionan los scrapers
- [ ] Sé calcular SLIs básicos con PromQL
