# 🔍 PromQL Queries Esenciales - Casos de Uso Real

## 🎯 Queries Organizadas por Caso de Uso

---

## 1️⃣ HTTP/API Monitoring

### Requests Rate (QPS - Queries Per Second)

```promql
# Total requests por segundo
sum(rate(http_requests_total[5m]))

# Requests por segundo por servicio
sum(rate(http_requests_total[5m])) by (service)

# Requests por segundo por endpoint
sum(rate(http_requests_total[5m])) by (path)

# Requests por segundo por método HTTP
sum(rate(http_requests_total[5m])) by (method)

# Requests por status code
sum(rate(http_requests_total[5m])) by (status)
```

### Error Rates

```promql
# Error rate absoluto (requests 5xx por segundo)
sum(rate(http_requests_total{status=~"5.."}[5m]))

# Error rate porcentaje
sum(rate(http_requests_total{status=~"5.."}[5m])) 
/ 
sum(rate(http_requests_total[5m])) * 100

# Error rate por servicio
sum(rate(http_requests_total{status=~"5.."}[5m])) by (service)
/
sum(rate(http_requests_total[5m])) by (service) * 100

# 4xx errors (client errors)
sum(rate(http_requests_total{status=~"4.."}[5m])) by (path)

# Success rate (2xx)
sum(rate(http_requests_total{status=~"2.."}[5m]))
/
sum(rate(http_requests_total[5m])) * 100
```

### Latency (Response Time)

```promql
# Latencia promedio (usando histogram)
rate(http_request_duration_seconds_sum[5m])
/
rate(http_request_duration_seconds_count[5m])

# Latencia p50 (mediana)
histogram_quantile(0.50, 
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le)
)

# Latencia p95
histogram_quantile(0.95, 
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le)
)

# Latencia p99 (tail latency)
histogram_quantile(0.99, 
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le)
)

# Latencia p99 por endpoint
histogram_quantile(0.99, 
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le, path)
)

# Requests con latencia > 1 segundo
sum(rate(http_request_duration_seconds_bucket{le="1"}[5m])) by (path)
/
sum(rate(http_request_duration_seconds_count[5m])) by (path) < 0.95
```

### Throughput

```promql
# Bytes received por segundo
sum(rate(http_request_size_bytes_sum[5m]))

# Bytes sent por segundo
sum(rate(http_response_size_bytes_sum[5m]))

# Bandwidth total (MB/s)
(sum(rate(http_request_size_bytes_sum[5m])) + 
 sum(rate(http_response_size_bytes_sum[5m]))) / 1024 / 1024
```

---

## 2️⃣ CPU Monitoring

### Node/Host CPU

```promql
# CPU usage % por nodo (método 1)
100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# CPU usage % por nodo (método 2)
(1 - avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m]))) * 100

# CPU por modo (user, system, iowait, etc)
avg by (mode) (rate(node_cpu_seconds_total[5m])) * 100

# Nodos con CPU > 80%
(100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)) > 80

# Top 5 nodos con mayor CPU
topk(5, 
  100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
)

# CPU iowait (problemas de disk I/O)
avg by (instance) (rate(node_cpu_seconds_total{mode="iowait"}[5m])) * 100
```

### Container/Pod CPU

```promql
# CPU usage de todos los containers
sum(rate(container_cpu_usage_seconds_total[5m])) by (pod)

# CPU usage % (vs límite asignado)
sum(rate(container_cpu_usage_seconds_total[5m])) by (pod)
/
sum(container_spec_cpu_quota / container_spec_cpu_period) by (pod) * 100

# Top 10 pods consumiendo más CPU
topk(10, sum(rate(container_cpu_usage_seconds_total[5m])) by (pod))

# Pods con CPU throttling (limitados por cuota)
sum(rate(container_cpu_cfs_throttled_seconds_total[5m])) by (pod) > 0

# CPU throttling % (qué % del tiempo están limitados)
sum(rate(container_cpu_cfs_throttled_seconds_total[5m])) by (pod)
/
sum(rate(container_cpu_cfs_periods_total[5m])) by (pod) * 100

# Pods cerca del límite de CPU (>80%)
(sum(rate(container_cpu_usage_seconds_total[5m])) by (pod)
/
sum(container_spec_cpu_quota / container_spec_cpu_period) by (pod)) > 0.8
```

---

## 3️⃣ Memory Monitoring

### Node/Host Memory

```promql
# Memory usage en bytes
node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes

# Memory usage %
((node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) 
/ 
node_memory_MemTotal_bytes) * 100

# Memory disponible %
(node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100

# Nodos con poca memoria (<20% disponible)
(node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100 < 20

# Swap usage %
((node_memory_SwapTotal_bytes - node_memory_SwapFree_bytes)
/
node_memory_SwapTotal_bytes) * 100

# Cache y buffers
node_memory_Cached_bytes + node_memory_Buffers_bytes
```

### Container/Pod Memory

```promql
# Memory usage actual de pods
sum(container_memory_usage_bytes) by (pod)

# Memory usage % (vs límite)
sum(container_memory_usage_bytes) by (pod)
/
sum(container_spec_memory_limit_bytes) by (pod) * 100

# Memory working set (memoria realmente en uso)
sum(container_memory_working_set_bytes) by (pod)

# Top 10 pods usando más memoria
topk(10, sum(container_memory_usage_bytes) by (pod))

# Pods cerca del límite de memoria (>80%)
(sum(container_memory_usage_bytes) by (pod)
/
sum(container_spec_memory_limit_bytes) by (pod)) > 0.8

# Pods con OOM kills (Out Of Memory)
sum(container_memory_failcnt) by (pod) > 0

# Memory RSS (Resident Set Size)
sum(container_memory_rss) by (pod)
```

---

## 4️⃣ Disk Monitoring

```promql
# Disk usage en bytes
node_filesystem_size_bytes - node_filesystem_free_bytes

# Disk usage %
((node_filesystem_size_bytes - node_filesystem_free_bytes)
/
node_filesystem_size_bytes) * 100

# Disk disponible %
(node_filesystem_free_bytes / node_filesystem_size_bytes) * 100

# Disks con >85% de uso
((node_filesystem_size_bytes - node_filesystem_free_bytes)
/
node_filesystem_size_bytes) * 100 > 85

# Disk I/O read rate (bytes/s)
rate(node_disk_read_bytes_total[5m])

# Disk I/O write rate (bytes/s)
rate(node_disk_written_bytes_total[5m])

# Disk I/O operations per second (IOPS)
rate(node_disk_reads_completed_total[5m]) + 
rate(node_disk_writes_completed_total[5m])

# Average disk I/O time
rate(node_disk_io_time_seconds_total[5m])

# Inodes usage %
((node_filesystem_files - node_filesystem_files_free)
/
node_filesystem_files) * 100
```

---

## 5️⃣ Network Monitoring

```promql
# Network received (bytes/s)
rate(node_network_receive_bytes_total[5m])

# Network transmitted (bytes/s)
rate(node_network_transmit_bytes_total[5m])

# Total network traffic (MB/s)
(rate(node_network_receive_bytes_total[5m]) + 
 rate(node_network_transmit_bytes_total[5m])) / 1024 / 1024

# Packets received per second
rate(node_network_receive_packets_total[5m])

# Packets transmitted per second
rate(node_network_transmit_packets_total[5m])

# Network errors (receive)
rate(node_network_receive_errs_total[5m])

# Network errors (transmit)
rate(node_network_transmit_errs_total[5m])

# Network drops (receive)
rate(node_network_receive_drop_total[5m])

# Top interfaces por tráfico
topk(5, 
  sum(rate(node_network_receive_bytes_total[5m])) by (device)
)

# TCP connections established
node_netstat_Tcp_CurrEstab

# TCP connections por estado
node_netstat_Tcp_{TIME_WAIT,CLOSE_WAIT,ESTABLISHED}
```

---

## 6️⃣ Kubernetes Specific

### Pod Status

```promql
# Pods running
sum(kube_pod_status_phase{phase="Running"})

# Pods not ready
kube_pod_status_ready{condition="false"} == 1

# Pods pending
sum(kube_pod_status_phase{phase="Pending"})

# Pods failed
sum(kube_pod_status_phase{phase="Failed"})

# Pod restarts (últimos 15 min)
rate(kube_pod_container_status_restarts_total[15m]) > 0

# Pods crashlooping
rate(kube_pod_container_status_restarts_total[15m]) > 0.1

# Containers waiting
kube_pod_container_status_waiting
```

### Deployments

```promql
# Deployments con réplicas insuficientes
kube_deployment_status_replicas_available 
/ 
kube_deployment_spec_replicas < 1

# Deployments rollout en progreso
kube_deployment_status_replicas_updated 
< 
kube_deployment_spec_replicas

# Deployment replicas desired vs available
kube_deployment_spec_replicas - kube_deployment_status_replicas_available > 0
```

### Nodes

```promql
# Nodes ready
sum(kube_node_status_condition{condition="Ready", status="true"})

# Nodes not ready
sum(kube_node_status_condition{condition="Ready", status="false"})

# Nodes con MemoryPressure
kube_node_status_condition{condition="MemoryPressure", status="true"} == 1

# Nodes con DiskPressure
kube_node_status_condition{condition="DiskPressure", status="true"} == 1

# Node capacity CPU
kube_node_status_capacity{resource="cpu"}

# Node allocatable CPU
kube_node_status_allocatable{resource="cpu"}
```

### Resource Requests/Limits

```promql
# CPU request total del cluster
sum(kube_pod_container_resource_requests{resource="cpu"})

# CPU limit total del cluster
sum(kube_pod_container_resource_limits{resource="cpu"})

# Memory request total
sum(kube_pod_container_resource_requests{resource="memory"})

# Memory limit total
sum(kube_pod_container_resource_limits{resource="memory"})

# Pods sin CPU limits
count(kube_pod_container_resource_limits{resource="cpu"} == 0)

# Pods sin memory limits
count(kube_pod_container_resource_limits{resource="memory"} == 0)
```

---

## 7️⃣ Availability & Uptime

```promql
# Services UP
up == 1

# Services DOWN
up == 0

# Count de services UP
count(up == 1)

# Count de services DOWN
count(up == 0)

# Availability % (última hora)
avg_over_time(up[1h]) * 100

# Availability % (últimas 24 horas)
avg_over_time(up[24h]) * 100

# Availability % (últimos 30 días - SLI)
avg_over_time(up[30d]) * 100

# Uptime en segundos desde último restart
time() - process_start_time_seconds

# Services down > 5 minutos
up == 0 and up offset 5m == 0
```

---

## 8️⃣ Database Monitoring

### MySQL

```promql
# Connections activas
mysql_global_status_threads_connected

# Queries por segundo
rate(mysql_global_status_queries[5m])

# Slow queries
rate(mysql_global_status_slow_queries[5m])

# Replication lag
mysql_slave_status_seconds_behind_master

# Table locks
rate(mysql_global_status_table_locks_waited[5m])
```

### PostgreSQL

```promql
# Active connections
pg_stat_activity_count{state="active"}

# Transactions per second
rate(pg_stat_database_xact_commit[5m]) + 
rate(pg_stat_database_xact_rollback[5m])

# Cache hit ratio
sum(pg_stat_database_blks_hit) 
/ 
(sum(pg_stat_database_blks_hit) + sum(pg_stat_database_blks_read)) * 100

# Dead tuples (necesita VACUUM)
pg_stat_user_tables_n_dead_tup
```

### Redis

```promql
# Connected clients
redis_connected_clients

# Memory usage
redis_memory_used_bytes

# Ops per second
rate(redis_commands_processed_total[5m])

# Cache hit rate
rate(redis_keyspace_hits_total[5m])
/
(rate(redis_keyspace_hits_total[5m]) + rate(redis_keyspace_misses_total[5m])) * 100

# Evicted keys
rate(redis_evicted_keys_total[5m])
```

---

## 9️⃣ Application Specific

### JVM (Java)

```promql
# Heap memory usage %
(jvm_memory_used_bytes{area="heap"} 
/ 
jvm_memory_max_bytes{area="heap"}) * 100

# GC time per second
rate(jvm_gc_collection_seconds_sum[5m])

# Threads count
jvm_threads_current

# Classes loaded
jvm_classes_loaded
```

### Go Application

```promql
# Goroutines
go_goroutines

# Memory allocated
go_memstats_alloc_bytes

# GC pause time
rate(go_gc_duration_seconds_sum[5m])

# Go version info
go_info
```

---

## 🔟 Alerting Queries

```promql
# High CPU alert
(100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)) > 80

# High Memory alert
((node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) 
/ node_memory_MemTotal_bytes) * 100 > 85

# High Disk usage
((node_filesystem_size_bytes - node_filesystem_free_bytes)
/ node_filesystem_size_bytes) * 100 > 85

# Service down
up == 0

# High error rate (>5%)
(sum(rate(http_requests_total{status=~"5.."}[5m])) 
/ sum(rate(http_requests_total[5m]))) > 0.05

# High latency (p99 > 1s)
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])) > 1

# Pod restart loop
rate(kube_pod_container_status_restarts_total[15m]) > 0

# Deployment not ready
(kube_deployment_status_replicas_available 
/ kube_deployment_spec_replicas) < 1
```

---

## 📊 SLI/SLO Calculations

### Availability SLI

```promql
# Availability (requests-based)
sum(rate(http_requests_total{status=~"2.."}[30d]))
/
sum(rate(http_requests_total[30d])) * 100

# Availability (uptime-based)
avg_over_time(up[30d]) * 100
```

### Latency SLI

```promql
# % of requests below 500ms
sum(rate(http_request_duration_seconds_bucket{le="0.5"}[30d]))
/
sum(rate(http_request_duration_seconds_count[30d])) * 100
```

### Error Budget

```promql
# Error budget remaining (if SLO is 99.9%)
# Allowed error rate: 0.1%
1 - (
  sum(rate(http_requests_total{status=~"5.."}[30d]))
  /
  sum(rate(http_requests_total[30d]))
) - 0.999
```

---

## 🎯 Pro Tips

### 1. Time Ranges
```promql
[5m]   # 5 minutos
[1h]   # 1 hora
[1d]   # 1 día
[30d]  # 30 días
```

### 2. Offset (datos del pasado)
```promql
# Comparar con hace 1 hora
http_requests_total offset 1h

# Comparar con hace 1 día
cpu_usage offset 1d
```

### 3. Predict Linear (predecir futuro)
```promql
# Predecir cuándo se llenará el disco (en 4 horas)
predict_linear(node_filesystem_free_bytes[1h], 4*3600) < 0
```

### 4. Subqueries
```promql
# Max de los últimos 5 minutos, evaluado cada minuto en la última hora
max_over_time(
  rate(http_requests_total[5m])[1h:1m]
)
```

---

## ✅ Practice Exercise

Intenta escribir queries para:

1. ✏️ CPU promedio de todos los nodos en la última hora
2. ✏️ Top 3 pods usando más memoria
3. ✏️ Error rate de requests en los últimos 30 minutos
4. ✏️ Predecir si algún disco se llenará en las próximas 2 horas
5. ✏️ Pods que se han reiniciado más de 5 veces en la última hora
6. ✏️ Latencia p99 por endpoint, solo para requests exitosos (2xx)
7. ✏️ Availability de cada servicio en los últimos 7 días
8. ✏️ Network bandwidth total del cluster

<details>
<summary>Ver respuestas</summary>

```promql
# 1. CPU promedio última hora
avg_over_time((100 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)[1h:])

# 2. Top 3 pods usando más memoria
topk(3, sum(container_memory_usage_bytes) by (pod))

# 3. Error rate últimos 30 min
sum(rate(http_requests_total{status=~"5.."}[30m])) 
/ 
sum(rate(http_requests_total[30m])) * 100

# 4. Discos que se llenarán en 2h
predict_linear(node_filesystem_free_bytes[1h], 2*3600) < 0

# 5. Pods con >5 restarts en última hora
sum(increase(kube_pod_container_status_restarts_total[1h])) by (pod) > 5

# 6. Latencia p99 por endpoint (solo 2xx)
histogram_quantile(0.99,
  sum(rate(http_request_duration_seconds_bucket{status=~"2.."}[5m])) by (le, path)
)

# 7. Availability 7 días
avg_over_time(up[7d]) by (job) * 100

# 8. Network bandwidth total cluster
sum(rate(node_network_receive_bytes_total[5m])) + 
sum(rate(node_network_transmit_bytes_total[5m]))
```
</details>
