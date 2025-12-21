# ☁️ OpenStack - Guía Básica

## 📚 Índice
1. [¿Qué es OpenStack?](#qué-es-openstack)
2. [Arquitectura y Componentes](#arquitectura-y-componentes)
3. [CLI Essentials](#cli-essentials)
4. [Conceptos Clave](#conceptos-clave)

---

## 1. ¿Qué es OpenStack?

OpenStack es una plataforma open source de cloud computing para crear y gestionar nubes públicas y privadas.

**Casos de uso:**
- Infraestructura como Servicio (IaaS)
- Nubes privadas empresariales
- NFV (Network Functions Virtualization)
- Plataformas de telecomunicaciones

---

## 2. Arquitectura y Componentes

### 🏗️ Componentes Principales

| Componente | Servicio | Función |
|------------|----------|---------|
| **Nova** | Compute | Gestión de instancias (VMs) |
| **Neutron** | Networking | Redes virtuales, routers, firewalls |
| **Cinder** | Block Storage | Volúmenes persistentes |
| **Swift** | Object Storage | Almacenamiento de objetos (S3-like) |
| **Glance** | Image | Gestión de imágenes (OS templates) |
| **Keystone** | Identity | Autenticación y autorización |
| **Horizon** | Dashboard | UI web |
| **Heat** | Orchestration | Templates de infraestructura (IaC) |

### 🔄 Flujo de Trabajo

```
User → Keystone (auth) → Horizon/CLI
                          ↓
        Nova (create VM) → Glance (get image)
                          ↓
                       Neutron (setup network)
                          ↓
                       Cinder (attach volume)
```

---

## 3. CLI Essentials

### 🔧 Configuración

```bash
# Instalar cliente
pip install python-openstackclient

# Variables de entorno (openrc)
export OS_AUTH_URL=http://controller:5000/v3
export OS_PROJECT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=secret
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_DOMAIN_NAME=Default
export OS_IDENTITY_API_VERSION=3

# Source el archivo
source openrc
```

### 📦 Comandos Básicos

```bash
# Ver información
openstack --version
openstack --help

# Autenticación
openstack token issue

# Listados generales
openstack catalog list          # Servicios disponibles
openstack endpoint list         # Endpoints de servicios
```

### 🖼️ Glance - Imágenes

```bash
# Listar imágenes
openstack image list
openstack image show <image-id>

# Crear imagen
openstack image create "Ubuntu 20.04" \
  --file ubuntu-20.04.qcow2 \
  --disk-format qcow2 \
  --container-format bare \
  --public

# Eliminar imagen
openstack image delete <image-id>
```

### 💻 Nova - Compute

```bash
# Listar instancias
openstack server list
openstack server list --all-projects
openstack server show <instance-id>

# Crear instancia
openstack server create \
  --flavor m1.small \
  --image ubuntu-20.04 \
  --network private \
  --key-name my-key \
  --security-group default \
  my-instance

# Gestionar instancia
openstack server start <instance>
openstack server stop <instance>
openstack server reboot <instance>
openstack server delete <instance>

# Flavor (tamaños de VM)
openstack flavor list
openstack flavor show m1.small

# Keypairs
openstack keypair create --public-key ~/.ssh/id_rsa.pub my-key
openstack keypair list
openstack keypair delete my-key

# Console
openstack console url show <instance>
openstack console log show <instance>
```

### 🌐 Neutron - Networking

```bash
# Redes
openstack network list
openstack network show <network>
openstack network create private-net

# Subnets
openstack subnet list
openstack subnet create private-subnet \
  --network private-net \
  --subnet-range 192.168.1.0/24 \
  --gateway 192.168.1.1 \
  --dns-nameserver 8.8.8.8

# Routers
openstack router list
openstack router create my-router
openstack router set --external-gateway public my-router
openstack router add subnet my-router private-subnet

# Security Groups
openstack security group list
openstack security group create web-sg
openstack security group rule create \
  --protocol tcp \
  --dst-port 80:80 \
  --remote-ip 0.0.0.0/0 \
  web-sg

# Floating IPs
openstack floating ip list
openstack floating ip create public
openstack server add floating ip <instance> <floating-ip>

# Ports
openstack port list
openstack port show <port-id>
```

### 💾 Cinder - Block Storage

```bash
# Volúmenes
openstack volume list
openstack volume show <volume-id>

# Crear volumen
openstack volume create \
  --size 10 \
  --type ssd \
  my-volume

# Attach/Detach
openstack server add volume <instance> <volume>
openstack server remove volume <instance> <volume>

# Snapshot
openstack volume snapshot create \
  --volume <volume-id> \
  my-snapshot

# Eliminar
openstack volume delete <volume-id>
```

### 👥 Keystone - Identity

```bash
# Proyectos
openstack project list
openstack project create --domain default dev-project

# Usuarios
openstack user list
openstack user create --project dev-project \
  --password secret123 \
  devuser

# Roles
openstack role list
openstack role add --project dev-project --user devuser member

# Domains
openstack domain list
```

---

## 4. Conceptos Clave

### 🎯 Flavors

Definen el tamaño de las instancias (vCPUs, RAM, disco).

```bash
openstack flavor list

# Crear flavor personalizado
openstack flavor create \
  --ram 2048 \
  --disk 20 \
  --vcpus 2 \
  custom.medium
```

### 🔐 Security Groups

Reglas de firewall para instancias.

```bash
# Regla SSH
openstack security group rule create \
  --protocol tcp \
  --dst-port 22 \
  --remote-ip 0.0.0.0/0 \
  default

# Regla HTTP
openstack security group rule create \
  --protocol tcp \
  --dst-port 80 \
  --remote-ip 0.0.0.0/0 \
  web-sg
```

### 🌍 Networking Concepts

**Network Types:**
- **Tenant/Private**: Redes aisladas por proyecto
- **Provider/External**: Redes físicas/públicas
- **Shared**: Compartidas entre proyectos

**Floating IPs:**
- IPs públicas asignables a instancias
- Permiten acceso desde internet

### 📊 Quotas

```bash
# Ver quotas
openstack quota show <project>

# Modificar quotas
openstack quota set --instances 20 <project>
openstack quota set --cores 40 <project>
openstack quota set --ram 51200 <project>
```

---

## 🎓 Preguntas Típicas

1. **¿Qué es Nova?**
   - Servicio de compute, gestiona VMs

2. **¿Diferencia entre Cinder y Swift?**
   - Cinder: block storage (volúmenes)
   - Swift: object storage (archivos)

3. **¿Para qué sirve Keystone?**
   - Autenticación y autorización
   - Gestión de usuarios, proyectos, roles

4. **¿Qué es un flavor?**
   - Plantilla de recursos para VMs
   - Define vCPUs, RAM, disco

5. **¿Cómo funciona Neutron?**
   - Redes virtuales, subnets, routers
   - Security groups, floating IPs

---

## 🔗 Recursos

- [OpenStack Docs](https://docs.openstack.org/)
- [OpenStack CLI Reference](https://docs.openstack.org/python-openstackclient/latest/)

---

**💡 Consejo:** Whitestack trabaja con OpenStack. Familiarízate con los componentes principales y CLI básico.
