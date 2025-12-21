# 📊 Sistemas de Monitoreo - Guía Básica

## 📚 Índice
1. [Grafana](#grafana)
2. [Kibana](#kibana)
3. [Prometheus](#prometheus)
4. [Zabbix](#zabbix)
5. [Nagios](#nagios)

---

## 1. Grafana

### 🎯 ¿Qué es Grafana?

Plataforma de visualización y analytics para métricas.

**Características:**
- Dashboards interactivos
- Múltiples datasources (Prometheus, InfluxDB, Elasticsearch)
- Alertas
- Plugins

### 🚀 Conceptos Básicos

```bash
# Instalar (Docker)
docker run -d -p 3000:3000 grafana/grafana

# Acceder: http://localhost:3000
# User/Pass default: admin/admin
```

**Componentes:**
- **Dashboard**: Colección de panels
- **Panel**: Visualización individual (gráfico, tabla, etc.)
- **Datasource**: Origen de datos (Prometheus, MySQL, etc.)
- **Query**: Consulta a datasource
- **Alert**: Notificación basada en condición

---

## 2. Kibana

### 🎯 ¿Qué es Kibana?

UI de visualización para Elasticsearch (parte del ELK Stack).

**ELK Stack:**
- **E**lasticsearch: Motor de búsqueda
- **L**ogstash: Procesamiento de logs
- **K**ibana: Visualización

### 📊 Uso Básico

```bash
# Kibana con Docker
docker run -d -p 5601:5601 \
  -e ELASTICSEARCH_HOSTS=http://elasticsearch:9200 \
  kibana:8.0.0

# Acceder: http://localhost:5601
```

**Funcionalidades:**
- **Discover**: Explorar logs
- **Visualize**: Crear gráficos
- **Dashboard**: Combinar visualizaciones
- **Dev Tools**: Consultas a Elasticsearch

**Ejemplo de consulta:**
```json
GET /logs-*/_search
{
  "query": {
    "match": {
      "level": "ERROR"
    }
  }
}
```

---

## 3. Prometheus

### 🎯 ¿Qué es Prometheus?

Sistema de monitoreo y alertas basado en métricas.

**Características:**
- Time-series database
- Pull model (scraping)
- PromQL (lenguaje de consulta)
- Alertmanager

### 📝 Configuración Básica

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
  
  - job_name: 'kubernetes'
    kubernetes_sd_configs:
      - role: pod
```

### 🔍 PromQL Ejemplos

```promql
# CPU usage
rate(cpu_usage_seconds_total[5m])

# Memory disponible
node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100

# HTTP requests por segundo
rate(http_requests_total[1m])

# Error rate
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))
```

---

## 4. Zabbix

### 🎯 ¿Qué es Zabbix?

Plataforma enterprise de monitoreo para redes y aplicaciones.

**Características:**
- Agentless o con agente
- Auto-discovery
- Templates
- Triggers y alertas

### 🔧 Conceptos

```bash
# Instalar agente
apt install zabbix-agent

# Configurar
nano /etc/zabbix/zabbix_agentd.conf
# Server=192.168.1.10
# Hostname=web-server-01

systemctl restart zabbix-agent
```

**Componentes:**
- **Server**: Servidor central
- **Agent**: Recolector en hosts
- **Proxy**: Para redes distribuidas
- **Frontend**: UI web

**Items comunes:**
- system.cpu.load
- vm.memory.size
- net.if.in[eth0]
- vfs.fs.size[/,used]

---

## 5. Nagios

### 🎯 ¿Qué es Nagios?

Sistema de monitoreo de infraestructura IT.

**Características:**
- Monitoreo de hosts y servicios
- Plugins extensibles
- Alertas
- Reporting

### 📝 Configuración Ejemplo

```bash
# /etc/nagios/objects/hosts.cfg
define host {
    use                     linux-server
    host_name               web-server-01
    alias                   Web Server 01
    address                 192.168.1.10
}

# /etc/nagios/objects/services.cfg
define service {
    use                     generic-service
    host_name               web-server-01
    service_description     HTTP
    check_command           check_http
}

define service {
    use                     generic-service
    host_name               web-server-01
    service_description     SSH
    check_command           check_ssh
}
```

**Checks comunes:**
```bash
check_ping
check_http
check_ssh
check_disk
check_load
check_memory
```

---

## 🎯 Comparación Rápida

| Tool | Tipo | Uso Principal |
|------|------|---------------|
| **Grafana** | Visualización | Dashboards de métricas |
| **Kibana** | Visualización | Análisis de logs (ELK) |
| **Prometheus** | Métricas | Time-series, K8s |
| **Zabbix** | All-in-one | Enterprise monitoring |
| **Nagios** | Alerting | Monitoreo tradicional |

---

## 🎓 Preguntas Típicas

1. **¿Para qué sirve Grafana?**
   - Visualización de métricas
   - Dashboards interactivos

2. **¿Qué es el ELK Stack?**
   - Elasticsearch + Logstash + Kibana
   - Para gestión y análisis de logs

3. **¿Cómo funciona Prometheus?**
   - Pull model (scraping)
   - Time-series database
   - PromQL para consultas

4. **¿Diferencia entre Zabbix y Nagios?**
   - Zabbix: más moderno, auto-discovery
   - Nagios: más veterano, simple

---

## 🔗 Recursos

- [Grafana Docs](https://grafana.com/docs/)
- [Kibana Guide](https://www.elastic.co/guide/en/kibana/current/index.html)
- [Prometheus Docs](https://prometheus.io/docs/)

---

**💡 Consejo:** Conoce los conceptos básicos. TestGorilla puede preguntar sobre cuándo usar cada herramienta.
