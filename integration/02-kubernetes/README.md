# ☸️ Kubernetes - Guía Completa

## 📚 Índice
1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [Arquitectura de Kubernetes](#arquitectura-de-kubernetes)
3. [Pods y Contenedores](#pods-y-contenedores)
4. [Deployments y ReplicaSets](#deployments-y-replicasets)
5. [Services y Networking](#services-y-networking)
6. [Volumes y Storage](#volumes-y-storage)
7. [ConfigMaps y Secrets](#configmaps-y-secrets)
8. [Probes y Health Checks](#probes-y-health-checks)
9. [Init Containers](#init-containers)
10. [Debugging y Troubleshooting](#debugging-y-troubleshooting)
11. [Helm](#helm)
12. [Ejercicios Prácticos](#ejercicios-prácticos)

---

## 1. Conceptos Fundamentales

### 🎯 ¿Qué es Kubernetes?

Kubernetes (K8s) es un sistema de orquestación de contenedores open-source que automatiza el despliegue, escalado y gestión de aplicaciones en contenedores.

**Características principales:**
- 🔄 Auto-healing: Reinicia contenedores fallidos
- 📊 Load balancing: Distribuye tráfico
- 🔐 Secret management: Gestiona información sensible
- 📦 Storage orchestration: Monta sistemas de archivos
- 🚀 Rolling updates: Actualizaciones sin downtime
- 📈 Horizontal scaling: Escala automáticamente

### 📖 Terminología Esencial

| Término | Descripción |
|---------|-------------|
| **Cluster** | Conjunto de nodos que ejecutan aplicaciones containerizadas |
| **Node** | Máquina (física o virtual) que ejecuta pods |
| **Pod** | Unidad mínima de despliegue, contiene uno o más contenedores |
| **Deployment** | Declara el estado deseado de pods y ReplicaSets |
| **Service** | Abstracción que define acceso a un conjunto de pods |
| **Namespace** | Aislamiento lógico de recursos en el cluster |
| **Label** | Par clave-valor para identificar y seleccionar objetos |

---

## 2. Arquitectura de Kubernetes

### 🏗️ Componentes del Control Plane

```
┌─────────────────────────────────────────┐
│         Control Plane (Master)          │
├─────────────────────────────────────────┤
│  ┌──────────┐  ┌───────────────────┐   │
│  │ API      │  │ Controller        │   │
│  │ Server   │  │ Manager           │   │
│  └──────────┘  └───────────────────┘   │
│  ┌──────────┐  ┌───────────────────┐   │
│  │ Scheduler│  │ etcd (Key-Value   │   │
│  │          │  │ Store)            │   │
│  └──────────┘  └───────────────────┘   │
└─────────────────────────────────────────┘
            │
            ├─────────────┬─────────────┐
            ▼             ▼             ▼
┌───────────────┐ ┌───────────────┐ ┌──────────────┐
│   Node 1      │ │   Node 2      │ │   Node 3     │
├───────────────┤ ├───────────────┤ ├──────────────┤
│ Kubelet       │ │ Kubelet       │ │ Kubelet      │
│ Kube-proxy    │ │ Kube-proxy    │ │ Kube-proxy   │
│ Container     │ │ Container     │ │ Container    │
│ Runtime       │ │ Runtime       │ │ Runtime      │
│  ┌────┐┌────┐ │ │  ┌────┐┌────┐ │ │  ┌────┐      │
│  │Pod ││Pod │ │ │  │Pod ││Pod │ │ │  │Pod │      │
│  └────┘└────┘ │ │  └────┘└────┘ │ │  └────┘      │
└───────────────┘ └───────────────┘ └──────────────┘
```

**Control Plane:**
- **API Server**: Frontend del control plane, expone la API de K8s
- **etcd**: Almacén de datos distribuido para el estado del cluster
- **Scheduler**: Asigna pods a nodos
- **Controller Manager**: Ejecuta controladores (Deployment, ReplicaSet, etc.)

**Worker Nodes:**
- **Kubelet**: Agente que se ejecuta en cada nodo
- **Kube-proxy**: Mantiene reglas de red
- **Container Runtime**: Docker, containerd, CRI-O

---

## 3. Pods y Contenedores

### 🚀 Crear y Gestionar Pods

```bash
# Comandos básicos
kubectl get pods                           # Listar pods
kubectl get pods -A                        # Todos los namespaces
kubectl get pods -o wide                   # Info adicional (IP, nodo)
kubectl get pods --watch                   # Watch mode
kubectl get pods -l app=nginx              # Filtrar por label

# Describir pod (info detallada)
kubectl describe pod nginx-pod

# Ver logs
kubectl logs nginx-pod                     # Logs del pod
kubectl logs nginx-pod -f                  # Follow logs
kubectl logs nginx-pod -c container-name   # Logs de contenedor específico
kubectl logs nginx-pod --previous          # Logs del contenedor anterior

# Ejecutar comandos en pod
kubectl exec nginx-pod -- ls /usr/share/nginx/html
kubectl exec -it nginx-pod -- /bin/bash    # Shell interactivo

# Eliminar pod
kubectl delete pod nginx-pod
kubectl delete pod --all                   # Eliminar todos
```

### 📝 Pod YAML Básico

```yaml
# pod-simple.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
    env: production
spec:
  containers:
  - name: nginx
    image: nginx:1.21
    ports:
    - containerPort: 80
```

```bash
# Crear pod desde YAML
kubectl apply -f pod-simple.yaml

# Ver YAML de pod existente
kubectl get pod nginx-pod -o yaml
```

### 🔧 Pod Multi-Container

```yaml
# pod-multi-container.yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
spec:
  containers:
  - name: web
    image: nginx:1.21
    ports:
    - containerPort: 80
    volumeMounts:
    - name: shared-data
      mountPath: /usr/share/nginx/html
  
  - name: content-updater
    image: busybox:1.34
    command: ["/bin/sh"]
    args:
      - -c
      - >
        while true; do
          echo "Updated at $(date)" > /data/index.html;
          sleep 60;
        done
    volumeMounts:
    - name: shared-data
      mountPath: /data
  
  volumes:
  - name: shared-data
    emptyDir: {}
```

### 🎯 Recursos y Límites

```yaml
# pod-resources.yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-pod
spec:
  containers:
  - name: app
    image: nginx:1.21
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"        # 0.25 CPU
      limits:
        memory: "128Mi"
        cpu: "500m"        # 0.5 CPU
```

---

## 4. Deployments y ReplicaSets

### 🚀 Deployments

Los Deployments gestionan el estado deseado de los pods y permiten actualizaciones declarativas.

```yaml
# deployment-nginx.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3                    # Número de pods
  selector:
    matchLabels:
      app: nginx
  template:                      # Template del Pod
    metadata:
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
            cpu: "100m"
          limits:
            memory: "128Mi"
            cpu: "200m"
```

```bash
# Gestionar Deployments
kubectl apply -f deployment-nginx.yaml
kubectl get deployments
kubectl get rs                             # Ver ReplicaSets
kubectl describe deployment nginx-deployment

# Escalar
kubectl scale deployment nginx-deployment --replicas=5
kubectl autoscale deployment nginx-deployment --min=2 --max=10 --cpu-percent=80

# Ver historial de rollouts
kubectl rollout history deployment nginx-deployment
kubectl rollout status deployment nginx-deployment

# Actualizar imagen
kubectl set image deployment/nginx-deployment nginx=nginx:1.22

# Rollback
kubectl rollout undo deployment nginx-deployment
kubectl rollout undo deployment nginx-deployment --to-revision=2

# Pausar/Reanudar rollout
kubectl rollout pause deployment nginx-deployment
kubectl rollout resume deployment nginx-deployment
```

### 🔄 Estrategias de Actualización

```yaml
# deployment-strategies.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deployment
spec:
  replicas: 4
  strategy:
    type: RollingUpdate           # o Recreate
    rollingUpdate:
      maxSurge: 1                 # Máximo de pods adicionales
      maxUnavailable: 1           # Máximo de pods no disponibles
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: app
        image: myapp:v1
```

**Tipos de estrategias:**
- **RollingUpdate**: Actualización gradual (default)
- **Recreate**: Elimina todos los pods antes de crear nuevos

---

## 5. Services y Networking

### 🌐 Tipos de Services

```yaml
# service-clusterip.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: ClusterIP              # Default, solo accesible dentro del cluster
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80                   # Puerto del service
    targetPort: 80             # Puerto del contenedor
```

```yaml
# service-nodeport.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
spec:
  type: NodePort               # Accesible desde fuera por IP del nodo
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30080            # Puerto en los nodos (30000-32767)
```

```yaml
# service-loadbalancer.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-lb
spec:
  type: LoadBalancer           # Crea un LB externo (cloud provider)
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

```bash
# Comandos de Services
kubectl get services
kubectl get svc                            # Alias
kubectl describe service nginx-service
kubectl get endpoints                      # Ver endpoints del service

# Exponer deployment como service
kubectl expose deployment nginx-deployment --type=LoadBalancer --port=80
```

### 🔗 Ingress

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx-service
            port:
              number: 80
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 8080
```

---

## 6. Volumes y Storage

### 💾 Tipos de Volumes

```yaml
# pod-emptydir.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-emptydir
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: cache
      mountPath: /cache
  volumes:
  - name: cache
    emptyDir: {}                # Directorio temporal, se pierde al eliminar pod
```

```yaml
# pod-hostpath.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-hostpath
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: data
      mountPath: /data
  volumes:
  - name: data
    hostPath:
      path: /mnt/data           # Path en el nodo
      type: DirectoryOrCreate
```

### 📦 PersistentVolume y PersistentVolumeClaim

```yaml
# pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-data
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce            # RWO, ROX, RWX
  persistentVolumeReclaimPolicy: Retain  # Retain, Delete, Recycle
  storageClassName: standard
  hostPath:
    path: /mnt/data
```

```yaml
# pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-data
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard
```

```yaml
# pod-with-pvc.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-storage
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: data
      mountPath: /data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: pvc-data
```

```bash
# Comandos de storage
kubectl get pv                             # PersistentVolumes
kubectl get pvc                            # PersistentVolumeClaims
kubectl describe pv pv-data
kubectl describe pvc pvc-data
```

### 🗄️ StorageClass

```yaml
# storageclass.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-storage
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
  fsType: ext4
reclaimPolicy: Delete
allowVolumeExpansion: true
```

---

## 7. ConfigMaps y Secrets

### ⚙️ ConfigMaps

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  app.properties: |
    database.host=mysql
    database.port=3306
    log.level=INFO
  nginx.conf: |
    server {
        listen 80;
        server_name localhost;
    }
```

```bash
# Crear ConfigMap desde comando
kubectl create configmap app-config --from-literal=key1=value1 --from-literal=key2=value2
kubectl create configmap app-config --from-file=config.properties
kubectl create configmap nginx-config --from-file=nginx.conf

# Ver ConfigMaps
kubectl get configmaps
kubectl describe configmap app-config
kubectl get configmap app-config -o yaml
```

**Usar ConfigMap en Pod:**

```yaml
# pod-with-configmap.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-configmap
spec:
  containers:
  - name: app
    image: nginx
    envFrom:
    - configMapRef:
        name: app-config         # Todas las keys como env vars
    env:
    - name: DATABASE_HOST        # Key específica
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: database.host
    volumeMounts:
    - name: config
      mountPath: /etc/config
  volumes:
  - name: config
    configMap:
      name: app-config           # Montar como archivos
```

### 🔐 Secrets

```yaml
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  username: YWRtaW4=             # base64 encoded: admin
  password: cGFzc3dvcmQxMjM=     # base64 encoded: password123
```

```bash
# Crear Secret
kubectl create secret generic db-secret \
  --from-literal=username=admin \
  --from-literal=password=password123

# Desde archivo
kubectl create secret generic tls-secret \
  --from-file=tls.crt=cert.crt \
  --from-file=tls.key=cert.key

# Ver Secrets (sin decodificar)
kubectl get secrets
kubectl describe secret db-secret

# Ver valor decodificado
kubectl get secret db-secret -o jsonpath='{.data.password}' | base64 -d
```

**Usar Secret en Pod:**

```yaml
# pod-with-secret.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-secret
spec:
  containers:
  - name: app
    image: myapp
    env:
    - name: DB_USERNAME
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: username
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: password
    volumeMounts:
    - name: secret
      mountPath: /etc/secret
      readOnly: true
  volumes:
  - name: secret
    secret:
      secretName: db-secret
```

---

## 8. Probes y Health Checks

### 🏥 Liveness, Readiness y Startup Probes

```yaml
# pod-with-probes.yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-probes
spec:
  containers:
  - name: app
    image: myapp:v1
    ports:
    - containerPort: 8080
    
    # Liveness Probe: ¿Está vivo el contenedor?
    # Si falla, Kubernetes reinicia el contenedor
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 3
      periodSeconds: 3
      timeoutSeconds: 1
      failureThreshold: 3
    
    # Readiness Probe: ¿Está listo para recibir tráfico?
    # Si falla, se quita del Service
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 5
      timeoutSeconds: 1
      successThreshold: 1
      failureThreshold: 3
    
    # Startup Probe: Para apps de arranque lento
    # Deshabilita liveness/readiness hasta que pase
    startupProbe:
      httpGet:
        path: /startup
        port: 8080
      initialDelaySeconds: 0
      periodSeconds: 10
      failureThreshold: 30      # 300s máximo de arranque
```

**Tipos de Probes:**

```yaml
# HTTP Probe
livenessProbe:
  httpGet:
    path: /health
    port: 8080
    httpHeaders:
    - name: Custom-Header
      value: Awesome

# TCP Probe
livenessProbe:
  tcpSocket:
    port: 8080

# Exec Probe (ejecuta comando)
livenessProbe:
  exec:
    command:
    - cat
    - /tmp/healthy
```

---

## 9. Init Containers

Init containers se ejecutan antes que los contenedores de la aplicación y deben completarse exitosamente.

```yaml
# pod-with-init-containers.yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  initContainers:
  - name: init-db
    image: busybox:1.34
    command: ['sh', '-c', 'until nslookup mydb; do echo waiting for mydb; sleep 2; done']
  
  - name: init-config
    image: busybox:1.34
    command: ['sh', '-c', 'echo "Config initialized" > /work-dir/config.txt']
    volumeMounts:
    - name: workdir
      mountPath: /work-dir
  
  containers:
  - name: myapp
    image: myapp:v1
    volumeMounts:
    - name: workdir
      mountPath: /app/config
  
  volumes:
  - name: workdir
    emptyDir: {}
```

**Casos de uso:**
- Esperar a que un servicio esté disponible
- Registrar el pod en un sistema externo
- Descargar configuración o datos
- Preparar el sistema de archivos

---

## 10. Debugging y Troubleshooting

### 🔍 Comandos de Debugging

```bash
# Ver estado de recursos
kubectl get all
kubectl get pods --all-namespaces
kubectl get events --sort-by='.lastTimestamp'

# Describir recursos (info detallada + eventos)
kubectl describe pod pod-name
kubectl describe deployment deployment-name
kubectl describe node node-name

# Logs
kubectl logs pod-name
kubectl logs pod-name -c container-name     # Multi-container
kubectl logs pod-name --previous            # Logs del contenedor anterior
kubectl logs -f pod-name                    # Follow
kubectl logs --tail=100 pod-name            # Últimas 100 líneas
kubectl logs --since=1h pod-name            # Última hora

# Ejecutar comandos en contenedor
kubectl exec pod-name -- ls /app
kubectl exec -it pod-name -- /bin/bash
kubectl exec -it pod-name -c container-name -- /bin/sh

# Port forwarding (acceder a pod desde localhost)
kubectl port-forward pod-name 8080:80
kubectl port-forward svc/service-name 8080:80

# Copiar archivos
kubectl cp pod-name:/path/to/file ./local-file
kubectl cp ./local-file pod-name:/path/to/file

# Debug interactivo (crea pod temporal)
kubectl run -it debug --image=busybox --rm -- /bin/sh
kubectl debug pod-name -it --image=busybox

# Ver recursos del cluster
kubectl top nodes                           # Uso de recursos por nodo
kubectl top pods                            # Uso de recursos por pod
kubectl top pods --containers               # Por contenedor

# Ver configuración
kubectl config view
kubectl config get-contexts
kubectl config use-context context-name

# Editar recursos en vivo
kubectl edit deployment deployment-name
kubectl edit pod pod-name
```

### 🐛 Troubleshooting Común

**1. Pod en estado Pending:**
```bash
kubectl describe pod pod-name
# Verificar:
# - Recursos insuficientes en nodos
# - PVC sin PV disponible
# - Nodo con taints que el pod no tolera
```

**2. Pod en CrashLoopBackOff:**
```bash
kubectl logs pod-name --previous
kubectl describe pod pod-name
# Verificar:
# - Errores en logs
# - Liveness probe fallando
# - Comando de inicio incorrecto
```

**3. ImagePullBackOff:**
```bash
kubectl describe pod pod-name
# Verificar:
# - Nombre de imagen correcto
# - Image pull secrets configurados
# - Registry accesible
```

**4. Pod Running pero no responde:**
```bash
kubectl exec -it pod-name -- /bin/sh
# Dentro del pod:
netstat -tulpn                              # Ver puertos
ps aux                                      # Ver procesos
curl localhost:8080/health                  # Test local

# Verificar readiness probe
kubectl describe pod pod-name | grep -A 5 Readiness
```

### 📊 Debugging Avanzado

```yaml
# pod-debug.yaml - Pod con herramientas de debugging
apiVersion: v1
kind: Pod
metadata:
  name: debug-pod
spec:
  containers:
  - name: debug
    image: nicolaka/netshoot                # Imagen con herramientas de red
    command: ["sleep", "3600"]
```

```bash
# Desde el debug pod:
kubectl exec -it debug-pod -- /bin/bash

# Herramientas disponibles:
ping 10.0.0.1
nslookup service-name
curl http://service-name:80
tcpdump -i eth0
iperf3 -s                                   # Test de ancho de banda
```

---

## 11. Helm

Helm es el gestor de paquetes de Kubernetes.

### 📦 Comandos Básicos de Helm

```bash
# Añadir repositorio
helm repo add stable https://charts.helm.sh/stable
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Buscar charts
helm search repo nginx
helm search hub wordpress

# Instalar chart
helm install my-release bitnami/nginx
helm install my-release bitnami/nginx --namespace my-namespace --create-namespace
helm install my-release ./my-chart          # Desde directorio local

# Listar releases
helm list
helm list -A                                # Todos los namespaces

# Ver estado
helm status my-release
helm get values my-release                  # Ver valores configurados
helm get manifest my-release                # Ver manifiestos generados

# Actualizar release
helm upgrade my-release bitnami/nginx --set replicaCount=3
helm upgrade my-release bitnami/nginx -f values.yaml

# Rollback
helm rollback my-release 1                  # A versión específica
helm history my-release                     # Ver historial

# Desinstalar
helm uninstall my-release

# Crear chart propio
helm create my-chart
```

### 📋 Estructura de un Helm Chart

```
my-chart/
├── Chart.yaml              # Metadata del chart
├── values.yaml             # Valores por defecto
├── templates/              # Templates de K8s
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── _helpers.tpl        # Helpers/funciones
│   └── NOTES.txt           # Notas post-instalación
└── charts/                 # Charts dependientes
```

**Chart.yaml:**
```yaml
apiVersion: v2
name: my-app
description: A Helm chart for my application
version: 1.0.0
appVersion: "1.0"
```

**values.yaml:**
```yaml
replicaCount: 3

image:
  repository: nginx
  tag: "1.21"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

resources:
  limits:
    cpu: 100m
    memory: 128Mi
  requests:
    cpu: 100m
    memory: 128Mi
```

**templates/deployment.yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-chart.fullname" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "my-chart.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "my-chart.selectorLabels" . | nindent 8 }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: 80
        resources:
          {{- toYaml .Values.resources | nindent 12 }}
```

---

## 12. Ejercicios Prácticos

### 🎯 Ejercicio 1: Deploy Completo

Despliega una aplicación web con:
- Deployment de 3 réplicas
- Service type LoadBalancer
- ConfigMap para configuración
- Secret para credenciales
- PVC de 1GB
- Readiness y liveness probes

```bash
# Ver solución en: ejercicios/01-web-app/
```

### 🎯 Ejercicio 2: Debugging

Se tiene un pod que no arranca. Encuentra y soluciona el problema:
- Pod en CrashLoopBackOff
- Revisa logs
- Verifica configuración
- Corrige el issue

### 🎯 Ejercicio 3: Helm Chart

Crea un Helm chart para desplegar:
- Aplicación web
- Base de datos
- Redis cache
- Configuración parametrizable

---

## 📝 Comandos Esenciales para el Test

```bash
# Top 30 comandos críticos
kubectl get pods
kubectl describe pod <name>
kubectl logs <pod>
kubectl exec -it <pod> -- /bin/bash
kubectl apply -f <file>
kubectl delete -f <file>
kubectl get deployments
kubectl scale deployment <name> --replicas=5
kubectl rollout status deployment/<name>
kubectl rollout undo deployment/<name>
kubectl get services
kubectl expose deployment <name>
kubectl port-forward <pod> 8080:80
kubectl get pv
kubectl get pvc
kubectl get configmaps
kubectl get secrets
kubectl create configmap <name> --from-literal=key=value
kubectl create secret generic <name> --from-literal=key=value
kubectl top nodes
kubectl top pods
kubectl get events
kubectl get all
kubectl edit deployment <name>
kubectl set image deployment/<name> container=image:tag
```

---

## 🎓 Preguntas Típicas del Test

1. **¿Cuál es la diferencia entre Deployment y ReplicaSet?**
   - Deployment gestiona ReplicaSets y permite rolling updates
   - ReplicaSet solo mantiene el número deseado de pods

2. **¿Qué hace el Liveness Probe?**
   - Verifica si el contenedor está vivo
   - Si falla, Kubernetes lo reinicia

3. **¿Cuándo usar emptyDir vs PersistentVolume?**
   - emptyDir: datos temporales, se pierden al eliminar pod
   - PersistentVolume: datos persistentes

4. **¿Qué tipos de Services existen?**
   - ClusterIP: interno al cluster
   - NodePort: accesible por IP del nodo
   - LoadBalancer: crea LB externo

5. **¿Para qué sirven los Init Containers?**
   - Se ejecutan antes que los contenedores principales
   - Útiles para inicialización, wait de dependencias

---

## 🔗 Recursos

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubernetes Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Interactive Tutorial](https://kubernetes.io/docs/tutorials/)
- [Helm Documentation](https://helm.sh/docs/)

---

**💡 Consejo:** Instala minikube y practica todos los comandos. El test evaluará tu capacidad de troubleshooting y entendimiento de ciclo de vida de pods.
