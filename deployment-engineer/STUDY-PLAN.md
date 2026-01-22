# Plan de Estudio Completo - 4 Semanas

## 📅 Estructura General

**Duración Total**: 4 semanas  
**Tiempo de Estudio Diario**: 2-3 horas  
**Total Horas**: 50-60 horas

---

## 📖 SEMANA 1: Fundamentos Linux y Networking

### Días 1-2: Administración de Sistemas Linux
**Lectura**: [Administración de Sistemas](01-linux-fundamentals/administracion-sistemas.md)
- Usuarios y grupos
- Permisos y propiedad
- Procesos y demonios
- Servicios (systemd)
- SSH y acceso remoto

**Ejercicios**:
1. Crear 3 usuarios con diferentes permisos
2. Configurar SSH seguro
3. Monitorear procesos activos
4. Crear cron job

**Duración**: 4-5 horas

---

### Días 3-4: Networking Nivel Intermedio
**Lectura**: [Networking Linux](02-networking/networking-linux.md)
- Netplan y configuración IP
- VLANs
- Bonding
- Enrutamiento
- DNS y resolución

**Ejercicios**:
1. Configurar IP estática con netplan
2. Crear bond entre dos interfaces
3. Crear VLAN y probar conectividad
4. Configurar rutas persistentes
5. Setup de DNS

**Duración**: 5-6 horas

---

### Día 5: Gestión de Discos
**Lectura**: [Gestión de Discos](04-disk-management/disk-management.md)
- Particionamiento
- Formateo
- Montaje persistente
- Expansión de volúmenes
- LVM

**Ejercicios**:
1. Particionar disco con fdisk/parted
2. Crear filesystem ext4
3. Montar disco persistentemente
4. Expandir volumen LVM

**Duración**: 3-4 horas

**Repaso Semana 1**: 
- Quiz: 10 preguntas sobre Linux y Networking
- Ejercicio integrador: Configurar servidor con red, usuarios y permisos

---

## 🔧 SEMANA 2: Scripting y Automatización

### Días 6-7: Bash Scripting
**Lectura**: [Bash Scripting](03-bash-scripting/bash-scripting.md)
- Variables y operadores
- Condicionales
- Bucles
- Funciones
- Procesamiento de texto

**Ejercicios**:
1. Script de backup automático
2. Monitor de sistema
3. Procesamiento de logs con grep/sed/awk
4. Loop sobre lista de servidores

**Duración**: 4-5 horas

---

### Día 8: Docker Básico
**Lectura**: [Docker Basics](06-docker/docker-basics.md)
- Conceptos: imágenes, contenedores
- Dockerfile
- Volúmenes y redes
- Docker Compose básico

**Ejercicios**:
1. Ejecutar contenedor Nginx
2. Crear Dockerfile personalizado
3. Usar volúmenes persistentes
4. Conectar múltiples contenedores

**Duración**: 3-4 horas

---

### Día 9: Ansible Básico-Intermedio
**Lectura**: [Ansible Basics](05-ansible/ansible-basics.md)
- Inventarios
- Ad-hoc commands
- Playbooks
- Roles
- Handlers

**Ejercicios**:
1. Crear inventario con múltiples hosts
2. Ejecutar ad-hoc commands
3. Playbook para instalar y configurar servicios
4. Crear rol reutilizable

**Duración**: 4-5 horas

---

### Día 10: Git Esenciales
**Lectura**: [Git Essentials](07-git/git-essentials.md)
- Repo básico
- Branches y merge
- Remote repositories
- Flujo de trabajo

**Ejercicios**:
1. Clonar y configurar repo
2. Crear rama, hacer cambios, mergear
3. Resolver conflictos
4. Push/Pull con repositorio remoto

**Duración**: 2-3 horas

**Repaso Semana 2**:
- Quiz: 15 preguntas sobre Bash, Ansible, Docker, Git
- Ejercicio: Crear playbook Ansible que instale y configure aplicación en contenedor Docker

---

## 🐍 SEMANA 3: Python y Niveles Avanzados

### Días 11-12: Python Scripting para Automatización
**Lectura**: [Python Scripting](08-python-automation/python-scripting.md)
- Sintaxis básica
- Módulos útiles (os, subprocess, socket, json)
- Manejo de archivos
- Paramiko para SSH remoto
- Fabric para tareas

**Ejercicios**:
1. Script que ejecuta comandos remotos via SSH
2. Monitor de múltiples servidores
3. Procesar JSON y archivos de configuración
4. Script integrador con Paramiko

**Duración**: 4-5 horas

---

### Día 13: Seguridad y Hardening
**Lectura**: [Security Hardening](09-security/security-hardening.md)
- SSH seguro
- Firewall (UFW)
- SELinux/AppArmor
- Auditoría
- Análisis de vulnerabilidades
- Fail2ban

**Ejercicios**:
1. Configurar SSH seguro
2. Setup de firewall con UFW
3. Implementar Fail2ban
4. Auditar sistema

**Duración**: 3-4 horas

---

### Días 14-15: Ejercicios Integrados
**Lectura**: [Ejercicios Prácticos](10-practical-exercises/ejercicios-practicos.md)
- Ejercicio 1: Administración de usuarios y permisos
- Ejercicio 2: Bonding y VLANs
- Ejercicio 3: Despliegue Ansible
- Ejercicio 4: Docker + Python + SSH

**Duración**: 6-8 horas

**Repaso Semana 3**:
- Quiz: 20 preguntas (mezcla de temas)
- Ejercicio integrador: Desplegar aplicación Python en múltiples servidores via Ansible, con Docker, SSH seguro y monitoreo

---

## 🎯 SEMANA 4: Simulación y Repaso Final

### Días 16-17: Repaso Intensivo
- Repasar todos los comandos esenciales
- Revisar errores comunes
- Practicar problemas de troubleshooting
- Mock tests tipo TestGorilla

**Duración**: 4-5 horas

---

### Días 18-20: Simulación de Examen
- **Test 1**: SysAdmin Level 1 simulado (15 preguntas, 30 min)
- **Test 2**: SysAdmin Level 2 simulado (8 preguntas, 10 min)
- Ejercicio final integrador bajo presión de tiempo

**Duración**: 3-4 horas

---

## 📊 Distribución de Tiempo Sugerida

| Tema | Horas | % |
|------|-------|-----|
| Linux Fundamentals | 10 | 17% |
| Networking | 8 | 13% |
| Bash Scripting | 7 | 12% |
| Docker | 6 | 10% |
| Ansible | 8 | 13% |
| Python | 7 | 12% |
| Security | 6 | 10% |
| Git | 3 | 5% |
| Ejercicios Prácticos | 10 | 17% |
| **TOTAL** | **65** | **100%** |

---

## 🔍 Topics Críticos para TestGorilla

### SysAdmin Level 1 (Básico-Intermedio)
- Usuarios y permisos
- Procesos y servicios
- Networking básico
- Firewall
- SSH
- Package management
- Logs y troubleshooting

### SysAdmin Level 2 (Intermedio-Avanzado)
- Condicionales y scripting
- Automatización
- Análisis de problemas
- Optimización
- Seguridad avanzada
- Disaster recovery
- Monitoreo

---

## 📝 Checklist de Preparación

### Semana 1
- [ ] Dominar administración Linux
- [ ] Configurar networking (bonding, VLANs)
- [ ] Gestión de discos
- [ ] SSH seguro

### Semana 2
- [ ] Scripts Bash funcionales
- [ ] Docker containers ejecutándose
- [ ] Playbooks Ansible completos
- [ ] Git workflow dominado

### Semana 3
- [ ] Scripts Python para administración
- [ ] Seguridad implementada
- [ ] Troubleshooting prácticado
- [ ] Ejercicios integrados completados

### Semana 4
- [ ] 100% de comandos memorizados
- [ ] Simulacros de examen aprobados (80%+)
- [ ] Ejercicios prácticos fluidamente
- [ ] Confianza antes de examen

---

## 🎓 Recursos Adicionales

- **YouTube**: NetworkChuck, Linode, Atech Media (Linux administration)
- **Documentación Oficial**: man pages, Ansible docs, Docker docs
- **Sitios Prácticos**: HackTheBox, TryHackMe (secciones Linux)
- **Comunidades**: r/linux, Stack Exchange

---

## ✅ Criteria de Éxito

**Para considerarse listo para el examen:**
- Resolver el 80%+ de preguntas de practice tests
- Ejecutar todos los ejercicios prácticos sin ayuda
- Responder preguntas de conceptos sin dudas
- Troubleshoot problemas en menos de 5 minutos

---

**Última actualización**: 20 enero 2026  
**Próximo examen**: [Tu fecha aquí]
