# 📌 Cheatsheet Rápido - Comandos Más Importantes

## 👤 Usuarios y Permisos

```bash
sudo useradd -m -s /bin/bash username        # Crear usuario
sudo usermod -aG sudo username               # Añadir a sudoers
id username                                  # Ver usuario
chmod 755 file                               # Permisos: rwxr-xr-x
chown user:group file                        # Cambiar propietario
sudo visudo                                  # Editar sudoers
```

## 🔧 Servicios

```bash
sudo systemctl start nginx                   # Iniciar
sudo systemctl stop nginx                    # Detener
sudo systemctl restart nginx                 # Reiniciar
sudo systemctl status nginx                  # Ver estado
sudo systemctl enable nginx                  # Auto-iniciar
sudo systemctl disable nginx                 # No auto-iniciar
sudo journalctl -u nginx -f                  # Ver logs
```

## 🌐 Networking

```bash
ip addr show                                 # Ver IPs
ip link show                                 # Ver interfaces
netstat -tulpn                               # Puertos activos (deprecated)
ss -tulpn                                    # Puertos activos (moderno)
ping -c 4 8.8.8.8                           # Verificar conectividad
cat /etc/netplan/01-netcfg.yaml             # Ver configuración netplan
sudo netplan apply                           # Aplicar cambios netplan
```

## 🔒 Firewall

```bash
sudo ufw status                              # Ver estado
sudo ufw enable                              # Activar
sudo ufw allow 22/tcp                        # Permitir puerto
sudo ufw deny 23/tcp                         # Bloquear puerto
sudo ufw delete allow 22/tcp                 # Eliminar regla
```

## 🔐 SSH

```bash
ssh-keygen -t ed25519 -C "comment"          # Generar clave
ssh-copy-id -i ~/.ssh/id_rsa.pub user@host # Copiar clave pública
ssh user@host                                # Conectar SSH
ssh -p 2222 user@host                        # Puerto personalizado
scp file user@host:/path/                   # Copiar archivo remoto
ssh user@host 'command'                      # Ejecutar comando remoto
```

## 📦 Package Management

```bash
sudo apt update                              # Actualizar índice (Debian)
sudo apt upgrade                             # Actualizar paquetes
sudo apt install package                    # Instalar paquete
sudo apt remove package                     # Desinstalar
apt search keyword                           # Buscar paquete
apt show package                             # Info del paquete
```

## 🖥️ Procesos

```bash
ps aux                                       # Ver todos los procesos
top                                          # Monitor dinámico
htop                                         # Monitor mejorado
kill -9 PID                                  # Matar proceso
pkill name                                   # Matar por nombre
bg                                           # Enviar a background
fg                                           # Traer a foreground
```

## 💾 Discos

```bash
df -h                                        # Espacio disponible
du -sh /path                                 # Tamaño de directorio
lsblk                                        # Ver discos
sudo fdisk -l                                # Listar particiones
sudo mkfs.ext4 /dev/sdb1                    # Crear filesystem
sudo mount /dev/sdb1 /mnt/disco             # Montar disco
sudo umount /mnt/disco                       # Desmontar
```

## 🔍 Logs

```bash
tail -f /var/log/syslog                      # Logs en tiempo real
tail -50 /var/log/syslog                     # Últimas 50 líneas
grep "ERROR" /var/log/syslog                # Buscar en logs
sudo journalctl -u service -f               # Logs de servicio
dmesg                                        # Mensajes del kernel
```

## 🐚 Bash Scripting

```bash
#!/bin/bash                                  # Shebang
if [ $1 -eq 5 ]; then echo "Yes"; fi        # Condicional
for i in {1..10}; do echo $i; done          # Loop
while [ $i -lt 5 ]; do ((i++)); done        # While
arr=(1 2 3)                                  # Array
${arr[@]}                                    # Expandir array
command $(other_command)                    # Sustitución de comando
```

## 🐋 Docker

```bash
docker run -d -p 8080:80 nginx              # Ejecutar contenedor
docker ps                                    # Listar contenedores
docker ps -a                                 # Todos los contenedores
docker stop container                        # Detener
docker rm container                          # Eliminar
docker logs container                        # Ver logs
docker exec -it container bash              # Entrar en contenedor
docker build -t myimage:1.0 .               # Construir imagen
```

## 🤖 Ansible

```bash
ansible all -i inventory -m ping            # Test conectividad
ansible-playbook playbook.yml               # Ejecutar playbook
ansible-playbook -i inventory playbook.yml  # Con inventario
ansible-playbook playbook.yml --check       # Dry-run
ansible webservers -a "uptime"              # Ad-hoc command
```

## 🐍 Python

```python
import subprocess
resultado = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(resultado.stdout)

import paramiko
ssh = paramiko.SSHClient()
ssh.connect("host", username="user", password="pass")
stdin, stdout, stderr = ssh.exec_command("uptime")
```

## 🌳 Git

```bash
git clone https://github.com/user/repo.git  # Clonar repo
git status                                   # Ver estado
git add file                                 # Agregar cambios
git commit -m "mensaje"                      # Hacer commit
git push origin main                         # Enviar cambios
git pull origin main                         # Descargar cambios
git branch nueva-rama                        # Crear rama
git checkout nueva-rama                      # Cambiar rama
git merge otra-rama                          # Mergear rama
```

## 🧪 Troubleshooting Rápido

```bash
# Sistema lento?
top                                          # Ver CPU/Memoria
df -h                                        # Ver disco

# Red no funciona?
ping 8.8.8.8                                 # Conectividad
ss -tulpn                                    # Puertos escuchando
sudo systemctl status networking             # Estado red

# Servicio no inicia?
sudo systemctl status nginx                  # Ver error
sudo journalctl -u nginx -n 50              # Últimos 50 logs
sudo tail -f /var/log/nginx/error.log        # Log de error

# Permiso denegado?
ls -la archivo                               # Ver permisos
chmod 755 archivo                            # Cambiar permiso
sudo chown user:group archivo                # Cambiar propietario
```

---

## 📊 Tabla Rápida: Comparaciones

| Tarea | Comando |
|-------|---------|
| Ver procesos | `ps aux` |
| Monitorear recursos | `top` |
| Ver discos | `lsblk` o `df -h` |
| Ver red | `ip addr show` |
| Ver puertos | `ss -tulpn` |
| Editar archivo | `nano` o `vim` |
| Buscar texto | `grep pattern file` |
| Procesar texto | `sed 's/old/new/' file` |
| Extraer campos | `awk '{print $1}' file` |
| Ver últimas líneas | `tail file` |

---

## 🎯 Orden de Troubleshooting (GOLDEN)

1. **Ver estado del servicio**: `systemctl status`
2. **Ver logs**: `journalctl -u servicio -f`
3. **Ver procesos**: `ps aux | grep`
4. **Ver conectividad**: `ping`, `ss -tulpn`
5. **Ver recursos**: `top`, `df -h`
6. **Ver permisos**: `ls -la`, `id usuario`

---

Este cheatsheet te ahorrerá tiempo. **Memoriza estos comandos.**

**Última actualización**: 20 enero 2026
