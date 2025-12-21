# 🚀 Preparación para Test TestGorilla - Cloud Integration Engineer @ Whitestack

Este proyecto contiene todo el material de estudio necesario para prepararte para el test de TestGorilla para el puesto de **Cloud Integration Engineer** en Whitestack.

## 📋 Sobre el Puesto

**Empresa:** Whitestack - Líder en soluciones cloud open source en Latinoamérica
**Posición:** Cloud Integration Engineer
**Modalidad:** Remoto 100%
**Link:** https://careers.whitestack.com/jobs/302532-cloud-integration-engineer

## 🎯 Requisitos Clave del Puesto

### Experiencia Requerida
- ✅ +2 años en Cloud Engineering
- ✅ Despliegue e integración de tecnologías cloud open source (OpenStack, Kubernetes)
- ✅ Troubleshooting de infraestructura cloud
- ✅ Configuración de redes en Linux
- ✅ Metodologías ágiles

### Conocimientos Técnicos Principales

#### 🐧 Linux (Intermedio-Avanzado) - **CRÍTICO**
- Comandos básicos y avanzados
- Manipulación de archivos y sistemas
- Configuración de red (interfaces, VLAN, iptables, routing, bonding)
- Shell scripting (Bash)

#### ☸️ Kubernetes (Intermedio-Avanzado) - **CRÍTICO**
- Ciclo de vida de pods
- Tipos de deployments
- PersistentVolumeClaims, Volumes, StorageClasses
- Debugging de pods
- Probes, init-containers
- Deployments con YAML y Helm

#### 🐳 Docker/Containerd - **IMPORTANTE**
- Ciclo de vida de containers
- Volúmenes
- Comandos: exec, attach, logs
- Troubleshooting

#### 🌐 Networking (Intermedio-Avanzado) - **CRÍTICO**
- Interfaces y VLANs
- IPTables
- Enrutamiento
- Bonding

#### 🤖 Ansible (Intermedio) - **IMPORTANTE**
- Ejecución de playbooks
- Roles y estructura
- Inventarios y variables

#### 🏗️ Terraform (Intermedio) - **IMPORTANTE**
- Despliegue de IaC
- Troubleshooting
- Providers y recursos

#### 🔧 Git (Intermedio) - **IMPORTANTE**
- Flujo add, commit, push
- Rebase y cherry-pick
- GitOps workflows

#### ☁️ OpenStack - **DESEABLE**
- Componentes principales
- Despliegue y configuración

#### 📊 Monitoreo - **DESEABLE**
- Grafana, Kibana, Zabbix, Nagios

## 📚 Plan de Estudio Recomendado

### Semana 1: Fundamentos Linux y Networking
- [ ] Días 1-3: [01-linux-avanzado](./01-linux-avanzado/)
- [ ] Días 4-5: [04-networking](./04-networking/)
- [ ] Día 6-7: Práctica y ejercicios

### Semana 2: Kubernetes y Docker
- [ ] Días 1-4: [02-kubernetes](./02-kubernetes/)
- [ ] Días 5-6: [03-docker](./03-docker/)
- [ ] Día 7: Práctica integrada

### Semana 3: IaC y Automatización
- [ ] Días 1-3: [05-ansible](./05-ansible/)
- [ ] Días 4-5: [06-terraform](./06-terraform/)
- [ ] Días 6-7: [07-git-avanzado](./07-git-avanzado/)

### Semana 4: OpenStack y Simulaciones
- [ ] Días 1-2: [08-openstack](./08-openstack/)
- [ ] Días 3-4: [09-monitoreo](./09-monitoreo/)
- [ ] Días 5-7: [10-ejercicios-practicos](./10-ejercicios-practicos/)

## 🎓 Qué Esperar en el Test TestGorilla

TestGorilla típicamente evalúa:

1. **Preguntas de Selección Múltiple** (40%)
   - Conceptos teóricos
   - Mejores prácticas
   - Comandos y sintaxis

2. **Ejercicios Prácticos** (30%)
   - Debugging de código/configuraciones
   - Lectura de logs
   - Identificación de problemas

3. **Escenarios de Resolución de Problemas** (20%)
   - Troubleshooting
   - Análisis de situaciones
   - Toma de decisiones técnicas

4. **Evaluación Cognitiva** (10%)
   - Razonamiento lógico
   - Resolución de problemas
   - Pensamiento crítico

## 📖 Estructura del Proyecto

```
integration/
├── 01-linux-avanzado/          # Linux intermedio-avanzado
├── 02-kubernetes/              # Kubernetes completo
├── 03-docker/                  # Docker y Containerd
├── 04-networking/              # Networking avanzado
├── 05-ansible/                 # Automatización con Ansible
├── 06-terraform/               # Infrastructure as Code
├── 07-git-avanzado/            # Git workflows avanzados
├── 08-openstack/               # OpenStack fundamentals
├── 09-monitoreo/               # Sistemas de monitoreo
├── 10-ejercicios-practicos/    # Ejercicios y simulaciones
└── README.md                   # Este archivo
```

## 🎯 Prioridades de Estudio (Orden de Importancia)

### ALTA PRIORIDAD ⭐⭐⭐
1. Linux avanzado (comandos, networking, bash scripting)
2. Kubernetes (deployments, pods, debugging, helm)
3. Networking (VLANs, routing, iptables)
4. Docker (lifecycle, troubleshooting)

### MEDIA PRIORIDAD ⭐⭐
5. Ansible (playbooks, roles)
6. Terraform (IaC, providers)
7. Git avanzado (rebase, cherry-pick)

### BAJA PRIORIDAD ⭐
8. OpenStack (conceptos básicos)
9. Monitoreo (Grafana, Kibana)

## 💡 Consejos para el Test

1. **Practica en un entorno real**: Usa minikube, docker, y una VM Linux
2. **Lee la documentación oficial**: Kubernetes, Docker, Terraform docs
3. **Cronometra tu tiempo**: TestGorilla tiene límites de tiempo
4. **No te quedes atascado**: Si no sabes una respuesta, márcala y continúa
5. **Revisa los logs**: Muchas preguntas se basan en análisis de logs
6. **Entiende los conceptos**: No solo memorices comandos

## 🔗 Recursos Adicionales

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Terraform Documentation](https://www.terraform.io/docs/)
- [Linux Command Line Basics](https://linuxcommand.org/)
- [Ansible Documentation](https://docs.ansible.com/)
- [OpenStack Documentation](https://docs.openstack.org/)

## 🎬 Cómo Empezar

1. **Evalúa tu nivel actual**: Revisa cada carpeta y marca qué ya conoces
2. **Sigue el plan de estudio**: Dedica 2-3 horas diarias
3. **Practica constantemente**: Cada día ejecuta comandos y crea recursos
4. **Toma notas**: Anota comandos y conceptos clave
5. **Haz los ejercicios**: La carpeta 10-ejercicios-practicos tiene simulaciones

## 📞 Sobre Whitestack

- Empresa líder en Latinoamérica
- Especializada en cloud open source
- Trabajan con operadores de telecomunicaciones
- Great Place to Work certificado
- Proyectos internacionales

---

**¡Mucha suerte en tu test! 🍀**

*Última actualización: Diciembre 2025*
