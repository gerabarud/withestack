# 📊 Grafana - Guía Completa de Dashboards y Visualización

## 🎯 ¿Qué es Grafana?

Grafana es la plataforma open-source líder para visualización, monitoreo y análisis de métricas. Se integra con múltiples fuentes de datos (Prometheus, Elasticsearch, MySQL, etc.) y permite crear dashboards interactivos.

---

## 🏗️ Conceptos Fundamentals

### Jerarquía de Componentes

```
Organization
└── Folders
    └── Dashboards
        └── Panels (visualizaciones)
            ├── Queries (datos)
            ├── Transformations (procesamiento)
            └── Alert rules (alertas)
```

### Data Sources Comunes

| Data Source | Uso | Puerto Default |
|-------------|-----|----------------|
| **Prometheus** | Métricas time-series | 9090 |
| **Elasticsearch** | Logs, búsquedas | 9200 |
| **Loki** | Logs agregados | 3100 |
| **MySQL/PostgreSQL** | Datos relacionales | 3306/5432 |
| **InfluxDB** | Time-series DB | 8086 |
| **Graphite** | Métricas legacy | 80 |
| **Jaeger** | Distributed tracing | 16686 |

---

## 📊 Tipos de Paneles (Visualizations)

### 1. Time Series (Gráfico de líneas)
**Uso**: Métricas que cambian en el tiempo
- CPU, memoria, latencia, request rate
- Ideal para tendencias y comparaciones

```
Ejemplo: CPU usage over time
Query: 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

### 2. Stat (Valor único)
**Uso**: Valor actual importante
- Total de requests, usuarios activos, uptime
- Puede incluir sparkline (mini gráfico)

```
Ejemplo: Total Requests per Second
Query: sum(rate(http_requests_total[5m]))
```

### 3. Gauge (Medidor)
**Uso**: Valor actual con rangos (verde/amarillo/rojo)
- CPU %, disk usage %, memory %
- Muestra visualmente si estás en zona de peligro

```
Ejemplo: CPU Usage %
Query: 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
Thresholds: Green < 70, Yellow 70-85, Red > 85
```

### 4. Table (Tabla)
**Uso**: Múltiples métricas por entidad
- Lista de pods con CPU, memoria, status
- Top N items ordenados

```
Ejemplo: Pod Resource Usage
Queries:
  CPU: sum(rate(container_cpu_usage_seconds_total[5m])) by (pod)
  Memory: sum(container_memory_usage_bytes) by (pod)
  Restarts: sum(kube_pod_container_status_restarts_total) by (pod)
```

### 5. Bar Chart (Gráfico de barras)
**Uso**: Comparar valores entre categorías
- Requests por endpoint
- Errors por servicio

```
Ejemplo: Requests by Endpoint
Query: sum(rate(http_requests_total[5m])) by (path)
```

### 6. Pie Chart / Donut
**Uso**: Distribución porcentual
- Requests por status code
- Traffic por región

```
Ejemplo: HTTP Status Distribution
Query: sum(rate(http_requests_total[5m])) by (status)
```

### 7. Heatmap
**Uso**: Distribución de valores en el tiempo
- Latency distributions
- Request size distributions

```
Ejemplo: Latency Heatmap
Query: sum(rate(http_request_duration_seconds_bucket[5m])) by (le)
Format: Heatmap
```

### 8. Alert List
**Uso**: Ver estado de alertas activas
- Dashboard de alertas del sistema
- Vista general de salud

### 9. Logs Panel
**Uso**: Mostrar logs en tiempo real
- Integration con Loki o Elasticsearch
- Filtrado y búsqueda

---

## 🎨 Dashboards Esenciales para el Test

### 1. Dashboard: Node/Host Overview

```
┌─────────────────────────────────────────────────────┐
│ Row: System Health                                  │
├─────────────┬─────────────┬─────────────┬──────────┤
│ CPU Usage   │ Memory Used │ Disk Used   │ Uptime   │
│ [Gauge]     │ [Gauge]     │ [Gauge]     │ [Stat]   │
│ 67%         │ 82%         │ 54%         │ 45d 3h   │
└─────────────┴─────────────┴─────────────┴──────────┘

┌─────────────────────────────────────────────────────┐
│ Row: CPU Details                                    │
├────────────────────────────────────────────────────┤
│ CPU Usage by Mode [Time Series]                    │
│ (user, system, iowait, idle)                       │
└────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Row: Memory Details                                 │
├────────────────────────────────────────────────────┤
│ Memory Usage [Time Series]                         │
│ (used, cached, buffers, available)                 │
└────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Row: Disk & Network                                 │
├─────────────────────────┬──────────────────────────┤
│ Disk I/O [Time Series]  │ Network Traffic          │
│ (read, write)           │ [Time Series]            │
│                         │ (rx, tx)                 │
└─────────────────────────┴──────────────────────────┘
```

**Queries principales:**
```javascript
// CPU Usage %
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

// Memory Usage %
((node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes) * 100

// Disk Usage %
((node_filesystem_size_bytes{fstype!~"tmpfs|fuse.*"} - node_filesystem_free_bytes) / node_filesystem_size_bytes) * 100

// Network RX
rate(node_network_receive_bytes_total[5m])

// Network TX
rate(node_network_transmit_bytes_total[5m])
```

---

### 2. Dashboard: Kubernetes Cluster Overview

```
┌─────────────────────────────────────────────────────┐
│ Row: Cluster Status                                 │
├───────────┬───────────┬───────────┬─────────────────┤
│ Nodes     │ Pods      │ Failed    │ CPU Usage       │
│ Ready     │ Running   │ Pods      │ Cluster         │
│ [Stat]    │ [Stat]    │ [Stat]    │ [Gauge]         │
│ 5/5       │ 234       │ 2         │ 56%             │
└───────────┴───────────┴───────────┴─────────────────┘

┌─────────────────────────────────────────────────────┐
│ Row: Pods Health                                    │
├────────────────────────────────────────────────────┤
│ Pod Status [Table]                                  │
│ Name | Restarts | CPU | Memory | Status             │
└────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Row: Resource Usage                                 │
├─────────────────────────┬──────────────────────────┤
│ Top Pods by CPU         │ Top Pods by Memory       │
│ [Bar Chart]             │ [Bar Chart]              │
└─────────────────────────┴──────────────────────────┘
```

**Queries principales:**
```javascript
// Nodes Ready
sum(kube_node_status_condition{condition="Ready", status="true"})

// Pods Running
sum(kube_pod_status_phase{phase="Running"})

// Failed Pods
sum(kube_pod_status_phase{phase="Failed"})

// Pod CPU Usage
sum(rate(container_cpu_usage_seconds_total{pod!=""}[5m])) by (pod)

// Pod Memory Usage
sum(container_memory_usage_bytes{pod!=""}) by (pod)

// Pod Restarts
sum(kube_pod_container_status_restarts_total) by (pod)
```

---

### 3. Dashboard: Application Performance (RED Method)

**RED = Rate, Errors, Duration**

```
┌─────────────────────────────────────────────────────┐
│ Row: Overview (Current Values)                      │
├───────────────┬───────────────┬─────────────────────┤
│ Request Rate  │ Error Rate    │ P95 Latency         │
│ [Stat]        │ [Stat]        │ [Stat]              │
│ 1,234 req/s   │ 0.5%          │ 250ms               │
└───────────────┴───────────────┴─────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Row: Request Rate                                   │
├────────────────────────────────────────────────────┤
│ Requests per Second [Time Series]                  │
│ (by endpoint, by status)                           │
└────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Row: Error Rate                                     │
├────────────────────────────────────────────────────┤
│ Error Rate % [Time Series]                         │
│ (5xx errors / total requests)                      │
└────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Row: Latency                                        │
├─────────────────────────┬──────────────────────────┤
│ Latency Distribution    │ Latency by Endpoint      │
│ [Time Series]           │ [Heatmap]                │
│ (p50, p95, p99)         │                          │
└─────────────────────────┴──────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Row: Traffic Details                                │
├────────────────────────────────────────────────────┤
│ Requests by Endpoint [Bar Chart]                   │
│ Top 10 endpoints by request volume                 │
└────────────────────────────────────────────────────┘
```

**Queries principales:**
```javascript
// Request Rate
sum(rate(http_requests_total[5m]))

// Error Rate %
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) * 100

// P50 Latency
histogram_quantile(0.50, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

// P95 Latency
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

// P99 Latency
histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

// Requests by Endpoint
sum(rate(http_requests_total[5m])) by (path)
```

---

## 🛠️ Features Avanzadas

### Variables (Template Variables)

Variables permiten dashboards dinámicos y reutilizables.

```javascript
// Variable: Environment
// Query: label_values(environment)
// Result: prod, staging, dev

// Variable: Service
// Query: label_values(http_requests_total{environment="$environment"}, service)
// Result: api, web, worker

// Uso en queries:
sum(rate(http_requests_total{environment="$environment", service="$service"}[5m]))
```

**Tipos de variables:**
- **Query**: Desde data source (ej: lista de pods)
- **Custom**: Lista manual (ej: prod, staging, dev)
- **Interval**: Rangos de tiempo (5m, 15m, 1h)
- **Data source**: Selector de data source
- **Ad hoc filters**: Filtros dinámicos

**Variable Multi-value:**
```javascript
// Permitir selección múltiple
// En query usar: {pod=~"$pod"}
// Seleccionar: pod1, pod2, pod3
// Query generada: {pod=~"pod1|pod2|pod3"}
```

---

### Transformations

Transformaciones procesan los datos antes de visualizarlos.

**1. Merge (Combinar series)**
```
Use case: Combinar CPU y Memory en una tabla
Before:
  Series 1: pod1_cpu = 0.5
  Series 2: pod1_memory = 1024
After:
  pod1: cpu=0.5, memory=1024
```

**2. Filter by name**
```
Use case: Mostrar solo pods que empiezan con "api-"
Regex: api-.*
```

**3. Add field from calculation**
```
Use case: Calcular % de uso
Formula: (used / limit) * 100
```

**4. Sort**
```
Use case: Ordenar tabla por CPU descendente
Field: CPU
Order: Descending
```

**5. Organize fields**
```
Use case: Renombrar y reordenar columnas
Rename: "container_cpu" → "CPU"
Hide: pod_id, namespace
Order: Name, CPU, Memory, Status
```

---

### Alerting en Grafana

```yaml
Alert Name: High CPU Usage
Condition:
  Query: A
  Reducer: avg()
  Math: > 80
  For: 5m

Notifications:
  - Slack: #alerts
  - Email: oncall@company.com
  - PagerDuty: incident

Message:
  CPU usage is {{ $values.A.Value }}% on {{ $labels.instance }}
```

**Estados de alerta:**
- 🟢 **OK**: Condición normal
- 🟡 **Pending**: Condición cumplida, esperando `for` duration
- 🔴 **Alerting**: Alerta activa
- ⚪ **No Data**: Sin datos para evaluar

---

## 🎯 Best Practices

### 1. Organización de Dashboards

```
Estructura recomendada:
├── 📁 Infrastructure
│   ├── Nodes Overview
│   ├── Disk Usage
│   └── Network Traffic
├── 📁 Kubernetes
│   ├── Cluster Overview
│   ├── Pods Details
│   └── Resource Quotas
├── 📁 Applications
│   ├── Service Performance
│   ├── API Metrics
│   └── Database Metrics
└── 📁 Alerts
    └── Active Alerts Dashboard
```

### 2. Naming Conventions

```
✅ Good:
- "Node Overview - Production"
- "API Performance - Service Name"
- "K8s Pods - Namespace"

❌ Bad:
- "Dashboard 1"
- "Test"
- "New Dashboard Copy (3)"
```

### 3. Panel Titles

```
✅ Good:
- "CPU Usage % (Last 6 Hours)"
- "Request Rate per Second by Endpoint"
- "P95 Latency - API Service"

❌ Bad:
- "Panel Title"
- "Metrics"
- "Graph"
```

### 4. Colors & Thresholds

```javascript
// Uso de memoria
Thresholds:
  Green: 0-70%      // OK
  Yellow: 70-85%    // Warning
  Orange: 85-95%    // High
  Red: 95-100%      // Critical

// Error rate
Thresholds:
  Green: 0-1%       // Excellent
  Yellow: 1-5%      // Acceptable
  Red: >5%          // Critical
```

### 5. Time Ranges

```
Dashboard defaults:
- Real-time monitoring: Last 15 minutes, refresh 10s
- Operations: Last 6 hours, refresh 1m
- Analysis: Last 24 hours, refresh 5m
- Reporting: Last 7 days, no auto-refresh
```

---

## 📱 Dashboard para Ejecutivos (High-Level)

```
┌─────────────────────────────────────────────────────┐
│ 🎯 SLA Compliance Dashboard                         │
├───────────────┬───────────────┬─────────────────────┤
│ Availability  │ Performance   │ Error Budget        │
│ [Gauge]       │ [Gauge]       │ [Gauge]             │
│ 99.95%        │ 98.5%         │ 45% remaining       │
│ Target: 99.9% │ Target: 95%   │                     │
└───────────────┴───────────────┴─────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Row: Service Health                                 │
├────────────────────────────────────────────────────┤
│ Services Status [Table]                            │
│ Service | Availability | Latency | Errors | Status │
└────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Row: Trends (Last 7 Days)                           │
├─────────────────────────┬──────────────────────────┤
│ Traffic Trend           │ Error Trend              │
│ [Time Series]           │ [Time Series]            │
└─────────────────────────┴──────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Row: Cost & Efficiency                              │
├───────────────┬─────────────────────────────────────┤
│ Infrastructure│ Request/Cost Efficiency             │
│ Cost (MTD)    │ [Stat]                              │
│ [Stat]        │                                     │
└───────────────┴─────────────────────────────────────┘
```

---

## 🧪 Ejercicios Prácticos

### Ejercicio 1: Crear Panel de CPU
```
1. Agregar Time Series panel
2. Query: 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
3. Legend: "CPU Usage %"
4. Thresholds: 70 (yellow), 85 (red)
5. Unit: Percent (0-100)
6. Min: 0, Max: 100
```

### Ejercicio 2: Tabla de Top 10 Pods por CPU
```
1. Agregar Table panel
2. Query: topk(10, sum(rate(container_cpu_usage_seconds_total[5m])) by (pod))
3. Transformation: Organize fields
   - Rename: Value → CPU Cores
4. Sort by: CPU Cores (desc)
5. Format: CPU Cores → Number, decimals=2
```

### Ejercicio 3: Variable para Namespace
```
1. Dashboard Settings → Variables → Add
2. Name: namespace
3. Type: Query
4. Data source: Prometheus
5. Query: label_values(kube_pod_info, namespace)
6. Multi-value: true
7. Include All: true

Usar en panels:
{namespace=~"$namespace"}
```

---

## 🔍 Troubleshooting Common Issues

### Issue 1: "No data"
**Causas:**
- ✅ Verificar data source connection
- ✅ Verificar query syntax
- ✅ Verificar time range (puede estar muy en el pasado)
- ✅ Verificar si la métrica existe en Prometheus

### Issue 2: "Query timeout"
**Soluciones:**
- ⏱️ Reducir time range
- 📉 Agregar más (`sum`, `avg`) para reducir series
- 🎯 Filtrar con labels específicos
- ⚡ Aumentar timeout en data source settings

### Issue 3: Panel lento
**Optimizaciones:**
- 📊 Usar menor resolution (Step)
- 🎯 Limitar series con `topk()` o `bottomk()`
- ⏱️ Reducir refresh rate
- 💾 Usar recording rules en Prometheus

---

## ✅ Checklist de Dominio Grafana

- [ ] Puedo conectar un data source (Prometheus)
- [ ] Sé crear un dashboard desde cero
- [ ] Puedo crear paneles Time Series con múltiples queries
- [ ] Entiendo cómo usar variables para dashboards dinámicos
- [ ] Sé usar transformations básicas (merge, filter, sort)
- [ ] Puedo configurar thresholds y colores apropiados
- [ ] Entiendo cuándo usar cada tipo de visualización
- [ ] Sé crear alertas básicas en panels
- [ ] Puedo exportar/importar dashboards (JSON)
- [ ] Entiendo el concepto de dashboard para diferentes audiencias

---

## 📚 Recursos Adicionales

- [Grafana Dashboards Library](https://grafana.com/grafana/dashboards/)
- [Grafana Best Practices](https://grafana.com/docs/grafana/latest/best-practices/)
- [Dashboard Examples for Prometheus](https://grafana.com/grafana/dashboards/?search=prometheus)

**Dashboard IDs populares para importar:**
- Node Exporter Full: `1860`
- Kubernetes Cluster Monitoring: `7249`
- Kubernetes Pod Resources: `6417`
