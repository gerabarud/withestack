# ☸️ Kubernetes - Guía Completa para DevOps/SRE

## 🎯 ¿Qué es Kubernetes?

Kubernetes (K8s) es un sistema de orquestación de contenedores open-source que automatiza el despliegue, escalado y gestión de aplicaciones containerizadas.

---

## 🏗️ Arquitectura de Kubernetes

```
┌─────────────────────────────────────────────────────┐
│                  CONTROL PLANE                      │
│  ┌──────────┐  ┌───────────┐  ┌─────────────────┐ │
│  │   API    │  │ Scheduler │  │  Controller     │ │
│  │  Server  │  │           │  │   Manager       │ │
│  └──────────┘  └───────────┘  └─────────────────┘ │
│  ┌──────────────────────────────────────────────┐  │
│  │            etcd (key-value store)            │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│                  WORKER NODES                       │
│  ┌────────────────────────────────────────────────┐ │
│  │ Node 1                                         │ │
│  │  ┌────────┐  ┌────────┐  ┌────────┐          │ │
│  │  │  Pod   │  │  Pod   │  │  Pod   │          │ │
│  │  │ ┌───┐  │  │ ┌───┐  │  │ ┌───┐  │          │ │
│  │  │ │App│  │  │ │App│  │  │ │App│  │          │ │
│  │  │ └───┘  │  │ └───┘  │  │ └───┘  │          │ │
│  │  └────────┘  └────────┘  └────────┘          │ │
│  │  ┌──────────────┐  ┌──────────────┐          │ │
│  │  │   kubelet    │  │ kube-proxy   │          │ │
│  │  └──────────────┘  └──────────────┘          │ │
│  │  ┌──────────────────────────────────┐        │ │
│  │  │  Container Runtime (containerd)  │        │ │
│  │  └──────────────────────────────────┘        │ │
│  └────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────┐ │
│  │ Node 2, Node 3, ...                           │ │
│  └────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

### Componentes del Control Plane
- **API Server**: Punto de entrada para todas las operaciones
- **Scheduler**: Asigna pods a nodos
- **Controller Manager**: Ejecuta controllers (Deployment, ReplicaSet, etc)
- **etcd**: Base de datos clave-valor (state del cluster)

### Componentes de Worker Nodes
- **kubelet**: Agente que ejecuta en cada nodo
- **kube-proxy**: Gestiona networking y load balancing
- **Container Runtime**: Docker, containerd, CRI-O

---

## 📦 Objetos Principales de Kubernetes

### 1. Pod
**Unidad mínima desplegable** - Grupo de uno o más contenedores

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.21
    ports:
    - containerPort: 80
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

### 2. Deployment
**Gestiona el ciclo de vida de Pods** - Actualizaciones, rollbacks, scaling

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80
```

### 3. Service
**Abstracción de red** - Expone Pods como servicio de red

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: ClusterIP  # ClusterIP, NodePort, LoadBalancer
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

**Tipos de Service:**
| Tipo | Descripción | Uso |
|------|-------------|-----|
| **ClusterIP** | IP interna del cluster | Comunicación interna |
| **NodePort** | Puerto en cada nodo | Acceso externo simple |
| **LoadBalancer** | Load balancer externo | Producción cloud |
| **ExternalName** | CNAME DNS | Servicios externos |

### 4. ConfigMap
**Configuración no sensible** - Variables de entorno, archivos config

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database_url: "postgresql://db:5432/myapp"
  log_level: "info"
  app.properties: |
    server.port=8080
    app.name=MyApp
```

### 5. Secret
**Datos sensibles** - Passwords, tokens, keys

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  username: YWRtaW4=        # base64 encoded
  password: cGFzc3dvcmQ=    # base64 encoded
```

### 6. Namespace
**Separación lógica** - Aislamiento de recursos

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production
```

### 7. Ingress
**Routing HTTP/HTTPS** - Exponer servicios con URLs

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app-service
            port:
              number: 80
```

### 8. PersistentVolume (PV) & PersistentVolumeClaim (PVC)
**Almacenamiento persistente**

```yaml
# PersistentVolumeClaim
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: standard
```

---

## 🔧 kubectl - Comandos Esenciales

### Top 30 Comandos que DEBES Memorizar

#### Información del Cluster
```bash
# Ver nodos del cluster
kubectl get nodes

# Info detallada de un nodo
kubectl describe node <node-name>

# Versión del cluster
kubectl version

# Info del cluster
kubectl cluster-info

# Contextos (clusters configurados)
kubectl config get-contexts
kubectl config use-context <context-name>
```

#### Trabajar con Pods
```bash
# Listar pods (namespace actual)
kubectl get pods

# Listar todos los pods (todos los namespaces)
kubectl get pods -A
kubectl get pods --all-namespaces

# Info detallada de un pod
kubectl describe pod <pod-name>

# Logs de un pod
kubectl logs <pod-name>
kubectl logs <pod-name> -f  # follow (tail -f)
kubectl logs <pod-name> --previous  # logs del contenedor anterior (si crasheó)

# Logs de un contenedor específico en un pod multi-container
kubectl logs <pod-name> -c <container-name>

# Ejecutar comando en un pod
kubectl exec <pod-name> -- ls /app
kubectl exec -it <pod-name> -- /bin/bash  # shell interactivo

# Port forwarding (acceder a pod localmente)
kubectl port-forward <pod-name> 8080:80

# Copiar archivos desde/hacia pod
kubectl cp <pod-name>:/path/to/file ./local-file
kubectl cp ./local-file <pod-name>:/path/to/file

# Eliminar pod
kubectl delete pod <pod-name>
kubectl delete pod <pod-name> --force --grace-period=0  # forzar
```

#### Deployments
```bash
# Listar deployments
kubectl get deployments

# Crear deployment
kubectl create deployment nginx --image=nginx:1.21

# Escalar deployment
kubectl scale deployment nginx --replicas=5

# Actualizar imagen de deployment
kubectl set image deployment/nginx nginx=nginx:1.22

# Ver historial de rollouts
kubectl rollout history deployment/nginx

# Status de rollout
kubectl rollout status deployment/nginx

# Rollback a versión anterior
kubectl rollout undo deployment/nginx
kubectl rollout undo deployment/nginx --to-revision=2

# Ver detalles del deployment
kubectl describe deployment nginx

# Editar deployment (abre editor)
kubectl edit deployment nginx

# Eliminar deployment
kubectl delete deployment nginx
```

#### Services
```bash
# Listar services
kubectl get services
kubectl get svc  # shorthand

# Describir service
kubectl describe service nginx-service

# Exponer deployment como service
kubectl expose deployment nginx --port=80 --type=NodePort

# Eliminar service
kubectl delete service nginx-service
```

#### ConfigMaps & Secrets
```bash
# Crear ConfigMap desde literal
kubectl create configmap app-config --from-literal=DB_HOST=localhost

# Crear ConfigMap desde archivo
kubectl create configmap app-config --from-file=config.json

# Ver ConfigMaps
kubectl get configmap
kubectl describe configmap app-config

# Crear Secret
kubectl create secret generic db-secret --from-literal=password=mypass

# Ver Secrets (valores están en base64)
kubectl get secret
kubectl describe secret db-secret

# Decodificar secret
kubectl get secret db-secret -o jsonpath='{.data.password}' | base64 -d
```

#### Namespaces
```bash
# Listar namespaces
kubectl get namespaces

# Crear namespace
kubectl create namespace production

# Trabajar en un namespace específico
kubectl get pods -n production
kubectl get pods --namespace=production

# Cambiar namespace por defecto
kubectl config set-context --current --namespace=production

# Eliminar namespace (¡cuidado! elimina todo dentro)
kubectl delete namespace production
```

#### Apply & Manifests
```bash
# Aplicar manifest (crear o actualizar)
kubectl apply -f deployment.yaml

# Aplicar todos los yamls en un directorio
kubectl apply -f ./manifests/

# Dry-run (ver qué haría sin aplicar)
kubectl apply -f deployment.yaml --dry-run=client

# Ver YAML de un recurso existente
kubectl get deployment nginx -o yaml

# Ver JSON de un recurso
kubectl get deployment nginx -o json

# Eliminar recursos desde manifest
kubectl delete -f deployment.yaml
```

#### Debugging & Troubleshooting
```bash
# Ver eventos del cluster
kubectl get events
kubectl get events --sort-by='.lastTimestamp'

# Eventos de un namespace específico
kubectl get events -n production

# Ver uso de recursos (requiere metrics-server)
kubectl top nodes
kubectl top pods
kubectl top pods -A --sort-by=cpu
kubectl top pods -A --sort-by=memory

# Describir cualquier recurso (troubleshooting)
kubectl describe <resource-type> <resource-name>

# Ver labels de recursos
kubectl get pods --show-labels

# Filtrar por label
kubectl get pods -l app=nginx
kubectl get pods -l environment=production,tier=frontend

# Ver estado completo de un recurso
kubectl get pod <pod-name> -o wide

# Ver todos los recursos en namespace
kubectl get all
kubectl get all -A
```

#### Watch & Monitoring
```bash
# Watch (actualización continua)
kubectl get pods -w
kubectl get pods -A -w

# Wide output (más info)
kubectl get pods -o wide
kubectl get nodes -o wide
```

---

## 🚨 Troubleshooting Común

### Problema 1: Pod en estado "Pending"

**Causas posibles:**
```bash
# 1. Recursos insuficientes
kubectl describe pod <pod-name>
# Buscar: "Insufficient cpu" o "Insufficient memory"

# 2. No hay nodos disponibles
kubectl get nodes

# 3. PVC no bound
kubectl get pvc

# 4. Taints en nodes
kubectl describe node <node-name> | grep Taint
```

**Solución:**
```bash
# Ver qué está bloqueando el scheduling
kubectl describe pod <pod-name> | grep -A 10 Events

# Verificar recursos del cluster
kubectl top nodes
kubectl describe nodes
```

---

### Problema 2: Pod en estado "CrashLoopBackOff"

**Diagnóstico:**
```bash
# 1. Ver logs del contenedor
kubectl logs <pod-name>
kubectl logs <pod-name> --previous  # logs antes del crash

# 2. Ver eventos
kubectl describe pod <pod-name> | grep -A 20 Events

# 3. Revisar configuración
kubectl get pod <pod-name> -o yaml

# 4. Verificar liveness/readiness probes
kubectl describe pod <pod-name> | grep -A 5 "Liveness\|Readiness"
```

**Causas comunes:**
- ❌ Aplicación crashea al iniciar
- ❌ Liveness probe fallando
- ❌ ConfigMap/Secret faltante
- ❌ Permisos insuficientes
- ❌ Dependencia no disponible

---

### Problema 3: Pod en estado "ImagePullBackOff"

**Diagnóstico:**
```bash
kubectl describe pod <pod-name>
# Buscar mensaje de error en Events
```

**Causas:**
- ❌ Imagen no existe
- ❌ Tag incorrecto
- ❌ Registry privado sin credenciales
- ❌ Typo en nombre de imagen

**Solución:**
```bash
# Verificar imagen
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].image}'

# Si es registry privado, crear secret
kubectl create secret docker-registry regcred \
  --docker-server=<registry> \
  --docker-username=<user> \
  --docker-password=<pass>

# Asociar secret al service account
kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "regcred"}]}'
```

---

### Problema 4: Service no accesible

**Diagnóstico:**
```bash
# 1. Verificar service existe
kubectl get svc

# 2. Verificar endpoints (pods detrás del service)
kubectl get endpoints <service-name>

# 3. Verificar selector del service match labels de pods
kubectl describe service <service-name>
kubectl get pods --show-labels

# 4. Test de conectividad desde dentro del cluster
kubectl run test-pod --image=busybox -it --rm -- wget -O- <service-name>

# 5. Verificar kube-proxy
kubectl get pods -n kube-system -l k8s-app=kube-proxy
kubectl logs -n kube-system <kube-proxy-pod>
```

---

### Problema 5: Pod con alto uso de CPU/Memoria

**Diagnóstico:**
```bash
# Ver top pods
kubectl top pods -A --sort-by=cpu
kubectl top pods -A --sort-by=memory

# Ver detalles del pod
kubectl describe pod <pod-name>

# Ver limits y requests
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].resources}'

# Ver si hay throttling (CPU)
# Requiere acceso a métricas avanzadas
kubectl get --raw /apis/metrics.k8s.io/v1beta1/namespaces/default/pods/<pod-name>
```

**Solución:**
```yaml
# Ajustar resources en deployment
spec:
  containers:
  - name: app
    resources:
      requests:
        memory: "256Mi"
        cpu: "500m"
      limits:
        memory: "512Mi"
        cpu: "1000m"
```

---

## 🎯 Conceptos Avanzados Importantes

### Resource Requests vs Limits

```yaml
resources:
  requests:    # Mínimo garantizado (para scheduling)
    cpu: "250m"        # 0.25 cores
    memory: "128Mi"
  limits:      # Máximo permitido (hard limit)
    cpu: "500m"        # 0.5 cores
    memory: "256Mi"
```

**Comportamiento:**
- **CPU**: Si excede limit → throttling (ralentización)
- **Memory**: Si excede limit → OOMKilled (pod reinicia)

### Probes (Health Checks)

```yaml
# Liveness Probe - ¿Está vivo? Si falla → restart
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 3

# Readiness Probe - ¿Está listo? Si falla → saca del service
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 5

# Startup Probe - Para apps con inicio lento
startupProbe:
  httpGet:
    path: /health
    port: 8080
  failureThreshold: 30
  periodSeconds: 10
```

### Rolling Updates

```yaml
spec:
  replicas: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1  # Máximo 1 pod down durante update
      maxSurge: 2        # Máximo 2 pods extra durante update
```

### Labels & Selectors

```yaml
# Labels en pods
metadata:
  labels:
    app: nginx
    environment: production
    tier: frontend
    version: v1.2.3

# Selector en service/deployment
selector:
  matchLabels:
    app: nginx
    environment: production
```

```bash
# Filtrar por labels
kubectl get pods -l app=nginx
kubectl get pods -l environment=production,tier=frontend
kubectl get pods -l 'environment in (prod,staging)'
kubectl get pods -l environment!=dev
```

---

## 📊 Monitoring con Kubernetes Metrics

### Métricas Clave (con Prometheus)

```promql
# Pod CPU usage
sum(rate(container_cpu_usage_seconds_total{pod!=""}[5m])) by (pod)

# Pod Memory usage
sum(container_memory_usage_bytes{pod!=""}) by (pod)

# Pod restarts
sum(kube_pod_container_status_restarts_total) by (pod)

# Pods not ready
kube_pod_status_ready{condition="false"} == 1

# Node capacity
kube_node_status_capacity{resource="cpu"}
kube_node_status_capacity{resource="memory"}
```

---

## 🎓 Ejercicios Prácticos

### Ejercicio 1: Desplegar una aplicación completa

```bash
# 1. Crear namespace
kubectl create namespace my-app

# 2. Crear ConfigMap
kubectl create configmap app-config \
  --from-literal=DB_HOST=postgres \
  --from-literal=DB_NAME=mydb \
  -n my-app

# 3. Crear Secret
kubectl create secret generic db-secret \
  --from-literal=DB_PASSWORD=secretpass \
  -n my-app

# 4. Crear Deployment
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: nginx:1.21
        ports:
        - containerPort: 80
        env:
        - name: DB_HOST
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: DB_HOST
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: DB_PASSWORD
EOF

# 5. Crear Service
kubectl expose deployment web-app --port=80 --type=NodePort -n my-app

# 6. Verificar
kubectl get all -n my-app
```

---

## ❓ Preguntas de TestGorilla

### Pregunta 1: ¿Qué pasa si un Pod excede su memory limit?
- A) Se ralentiza
- B) Se reinicia (OOMKilled) ✅
- C) Se migra a otro nodo
- D) Nada, el límite es sugerido

### Pregunta 2: ¿Qué comando usarías para ver logs del contenedor anterior (crasheado)?
- A) `kubectl logs <pod> --tail=100`
- B) `kubectl logs <pod> --previous` ✅
- C) `kubectl logs <pod> --last`
- D) `kubectl describe pod <pod>`

### Pregunta 3: ¿Cuál es la diferencia entre ClusterIP y NodePort?
- A) ClusterIP es externo, NodePort interno
- B) ClusterIP solo interno, NodePort expone puerto en nodos ✅
- C) No hay diferencia
- D) NodePort es más seguro

---

## ✅ Checklist de Dominio

- [ ] Puedo explicar la arquitectura de K8s (control plane + nodes)
- [ ] Entiendo la diferencia entre Pod, Deployment, ReplicaSet
- [ ] Sé crear y gestionar Deployments
- [ ] Entiendo cómo funcionan los Services y sus tipos
- [ ] Puedo usar ConfigMaps y Secrets correctamente
- [ ] Sé debuggear pods en CrashLoopBackOff
- [ ] Entiendo requests vs limits
- [ ] Puedo configurar liveness y readiness probes
- [ ] Sé hacer rollback de deployments
- [ ] Puedo troubleshootear issues de networking
- [ ] Entiendo namespaces y su uso
- [ ] Sé usar labels y selectors efectivamente

---

## 📚 Para Profundizar

- [Kubernetes Official Docs](https://kubernetes.io/docs/)
- [Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- [Play with Kubernetes](https://labs.play-with-k8s.com/)
