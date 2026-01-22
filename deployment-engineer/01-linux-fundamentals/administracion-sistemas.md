# Administración de Sistemas Linux - Nivel Intermedio

## 1. Administración de Usuarios y Grupos

### Crear Usuario
```bash
sudo useradd -m -s /bin/bash -c "Nombre Usuario" username
sudo usermod -aG sudo username  # Añadir a grupo sudo
```

### Gestionar Contraseñas
```bash
sudo passwd username            # Cambiar contraseña
sudo passwd -l username         # Bloquear usuario
sudo passwd -u username         # Desbloquear usuario
sudo passwd -e username         # Forzar cambio en próximo login
```

### Grupos
```bash
sudo groupadd groupname
sudo usermod -aG groupname username
id username                      # Ver grupos de usuario
groups username                  # Listar grupos del usuario
```

## 2. Permisos y Propiedad de Archivos

### Cambiar Permisos
```bash
chmod 755 file                   # rwxr-xr-x
chmod 644 file                   # rw-r--r--
chmod -R 755 directory/          # Recursivo
chmod u+x file                   # Añadir ejecución al propietario
```

### Cambiar Propietario
```bash
sudo chown user:group file
sudo chown -R user:group directory/
```

### Permisos Especiales
```bash
chmod u+s file                   # SUID (set user ID)
chmod g+s directory/             # SGID (set group ID)
chmod +t directory/              # Sticky bit
```

## 3. Gestión de Procesos

### Listar y Monitorizar
```bash
ps aux                           # Todos los procesos
ps aux | grep nombre_proceso
top                              # Monitor dinámico
htop                             # top mejorado
ps -ef --forest                  # Árbol de procesos
```

### Señales y Control
```bash
kill -9 PID                      # SIGKILL (no ignorable)
kill -15 PID                     # SIGTERM (terminar gracefully)
kill -1 PID                      # SIGHUP (recargar)
pkill nombre_proceso             # Matar por nombre
```

### Background y Foreground
```bash
command &                        # Ejecutar en background
bg                               # Enviar a background
fg                               # Traer a foreground
jobs                             # Listar trabajos
```

## 4. Servicios y Demonios

### SystemD
```bash
sudo systemctl start service_name
sudo systemctl stop service_name
sudo systemctl restart service_name
sudo systemctl status service_name
sudo systemctl enable service_name   # Iniciar al boot
sudo systemctl disable service_name  # No iniciar al boot
sudo systemctl list-units --type=service
```

### Ver Logs
```bash
sudo journalctl -u service_name      # Logs del servicio
sudo journalctl -u service_name -f   # Logs en tiempo real
sudo journalctl -n 50                # Últimas 50 líneas
```

## 5. Instalación de Paquetes

### APT (Debian/Ubuntu)
```bash
sudo apt update                  # Actualizar índice
sudo apt upgrade                 # Actualizar paquetes
sudo apt install package_name
sudo apt remove package_name
sudo apt search keyword
apt-cache show package_name      # Info del paquete
```

### YUM/DNF (RHEL/CentOS)
```bash
sudo yum update
sudo yum install package_name
sudo yum remove package_name
```

## 6. Monitoreo de Recursos

### CPU, Memoria, Disco
```bash
free -h                         # Memoria RAM
df -h                           # Espacio disco
du -sh directory/               # Tamaño de directorio
vmstat 1                        # Estadísticas virtuales
iostat                          # I/O estadísticas
```

### Logs del Sistema
```bash
tail -f /var/log/syslog         # Logs en tiempo real
dmesg                           # Mensajes del kernel
journalctl                      # Logs systemd
```

## 7. SSH y Acceso Remoto

### Configuración SSH
```bash
sudo nano /etc/ssh/sshd_config
sudo systemctl restart ssh       # Reiniciar SSH

# Configuraciones comunes:
Port 22
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```

### Claves SSH
```bash
ssh-keygen -t rsa -b 4096       # Generar clave
ssh-copy-id -i ~/.ssh/id_rsa.pub user@host
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
```

### Conectar
```bash
ssh user@hostname
ssh -p 2222 user@hostname
ssh -i /path/to/key user@hostname
```

## 8. Cron y Tareas Programadas

### Ver Crontab
```bash
crontab -l                      # Ver tareas actuales
crontab -e                      # Editar tareas
```

### Sintaxis Cron
```
# min hora día mes día-semana comando
0 2 * * * /ruta/script.sh       # Diario a las 2:00 AM
*/5 * * * * /ruta/script.sh     # Cada 5 minutos
0 * * * * /ruta/script.sh       # Cada hora
0 0 * * 0 /ruta/script.sh       # Cada domingo medianoche
```

## 9. Troubleshooting Común

### Verificar Conectividad
```bash
ping hostname
traceroute hostname
netstat -tulpn                  # Puertos activos
ss -tulpn                       # Alternativa moderna a netstat
```

### Buscar Problemas
```bash
dmesg | tail -20                # Errores del kernel
sudo journalctl -p err          # Solo errores
ps aux | grep zombie            # Procesos zombie
```

## 10. Comandos Esenciales de Administración

```bash
whoami                          # Usuario actual
hostname                        # Nombre del host
uname -a                        # Info del sistema
lsb_release -a                  # Versión Linux
uptime                          # Tiempo encendido
w                               # Usuarios conectados
lastlog                         # Últimos logins
sudo visudo                     # Editar sudoers
```

---
**Nivel**: Intermedio
**Tiempo estimado de estudio**: 4-5 horas
