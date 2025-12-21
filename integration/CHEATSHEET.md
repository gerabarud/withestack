# ⚡ Cheat Sheet - Comandos Rápidos

## 🐧 Linux

```bash
# Sistema
systemctl status|start|stop|restart service
journalctl -u service -f
ps aux | grep process
top / htop
df -h / du -sh
free -h

# Red
ip addr show
ip route show
ss -tulpn / netstat -tulpn
iptables -L -n -v
ping / traceroute / mtr

# Archivos
find / -name "*.log"
grep -r "pattern" /path
chmod 755 / chown user:group
tar -czf archive.tar.gz /path
```

## ☸️ Kubernetes

```bash
# Básicos
kubectl get pods
kubectl describe pod <name>
kubectl logs <pod> -f
kubectl exec -it <pod> -- /bin/bash

# Deployments
kubectl create deployment <name> --image=<image>
kubectl scale deployment <name> --replicas=3
kubectl rollout status deployment/<name>
kubectl rollout undo deployment/<name>

# Services
kubectl expose deployment <name> --port=80
kubectl get svc

# Apply/Delete
kubectl apply -f file.yaml
kubectl delete -f file.yaml
```

## 🐳 Docker

```bash
# Contenedores
docker ps / docker ps -a
docker run -d -p 80:80 nginx
docker stop|start|restart <container>
docker rm <container>
docker logs -f <container>
docker exec -it <container> bash

# Imágenes
docker images
docker pull <image>
docker build -t <name>:<tag> .
docker rmi <image>

# Compose
docker-compose up -d
docker-compose down
docker-compose logs -f
```

## 🤖 Ansible

```bash
# Ejecución
ansible-playbook playbook.yml
ansible-playbook -i inventory.ini playbook.yml
ansible-playbook playbook.yml --check --diff
ansible all -m ping

# Roles
ansible-galaxy init <role>
ansible-galaxy install <role>
```

## 🏗️ Terraform

```bash
# Workflow
terraform init
terraform plan
terraform apply
terraform destroy

# State
terraform state list
terraform state show <resource>
terraform output

# Otros
terraform fmt
terraform validate
```

## 🔧 Git

```bash
# Básico
git add .
git commit -m "message"
git push origin main
git pull origin main

# Avanzado
git rebase main
git rebase -i HEAD~3
git cherry-pick <hash>
git stash / git stash pop

# Branches
git checkout -b feature
git merge feature
git branch -d feature
```

## ☁️ OpenStack

```bash
# Básicos
openstack server list
openstack network list
openstack image list

# Crear instancia
openstack server create \
  --flavor m1.small \
  --image ubuntu \
  --network private \
  --key-name mykey \
  myinstance
```

---

## 🎯 Diagnóstico Rápido

### Pod no inicia (K8s)
```bash
kubectl describe pod <pod>
kubectl logs <pod> --previous
kubectl get events --sort-by='.lastTimestamp'
```

### Contenedor crashea (Docker)
```bash
docker logs <container>
docker inspect <container>
docker stats <container>
```

### Servicio no responde (Linux)
```bash
systemctl status service
journalctl -u service -n 50
ss -tulpn | grep port
curl localhost:port
```

### Sin conectividad (Networking)
```bash
ip addr show
ip route show
ping gateway
ping 8.8.8.8
dig google.com
```

---

## 📊 Formato de Respuestas TestGorilla

**Tipo 1: Comando correcto**
```
¿Cómo ves logs de systemd service?
→ journalctl -u service-name
```

**Tipo 2: Concepto**
```
¿Qué hace liveness probe?
→ Verifica si contenedor está vivo, lo reinicia si falla
```

**Tipo 3: Troubleshooting**
```
Pod en CrashLoopBackOff, ¿qué hacer?
→ kubectl logs pod --previous
→ kubectl describe pod
```

**Tipo 4: Mejor práctica**
```
¿Cómo optimizar Dockerfile?
→ Multi-stage build
→ Usar imágenes alpine
→ Combinar RUN commands
```

---

## 🎓 Tips para el Test

1. **Lee bien la pregunta** - A veces hay trucos
2. **Busca palabras clave** - "troubleshoot", "optimizar", "seguro"
3. **Descarta opciones obvias** - Elimina las incorrectas primero
4. **Tiempo** - No te atasques, marca y continúa
5. **Práctica** - Ejecuta los comandos antes del test

---

## 🔑 Conceptos Clave por Tema

### Linux
- systemd y journalctl
- iptables (INPUT, OUTPUT, FORWARD)
- VLANs y bonding
- Permisos y ACLs

### Kubernetes
- Ciclo de vida de pods
- Deployments y ReplicaSets
- Services (ClusterIP, NodePort, LoadBalancer)
- ConfigMaps y Secrets
- Probes (liveness, readiness, startup)

### Docker
- Dockerfile (CMD vs ENTRYPOINT)
- Volumes vs Bind Mounts
- Networks
- Multi-stage builds

### Ansible
- Playbooks y roles
- Variables y templates
- Idempotencia
- Handlers

### Terraform
- State management
- Plan vs Apply
- Variables y outputs
- Providers

### Git
- Rebase vs Merge
- Cherry-pick
- Reset vs Revert
- GitOps workflows

---

**Última revisión:** 20 Diciembre 2025
