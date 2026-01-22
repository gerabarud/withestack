# Seguridad y Hardening en Linux

## 1. Gestión de Usuarios y Acceso

### Principio del Menor Privilegio
```bash
# Crear usuario sin permisos sudo
sudo useradd -m -s /bin/bash -c "App User" appuser

# Crear usuario solo para servicio específico
sudo useradd -r -s /bin/false -m -d /var/lib/appuser appuser

# Sudoers - acceso limitado
sudo visudo
# Añadir línea:
# appuser ALL=(ALL) NOPASSWD: /usr/bin/service
```

### Gestión de Contraseñas
```bash
# Política de contraseñas
sudo apt install libpam-pwquality

# /etc/pam.d/common-password
password requisite pam_pwquality.so minlen=12 dcredit=-1 ucredit=-1 ocredit=-1

# /etc/login.defs
PASS_MAX_DAYS 90
PASS_MIN_DAYS 1
PASS_WARN_AGE 14

# Aplicar a usuarios existentes
sudo chage -M 90 -m 1 -W 14 username
```

## 2. SSH Hardening

### Configuración Segura de SSH
```bash
# /etc/ssh/sshd_config
Port 22
AddressFamily inet
ListenAddress 0.0.0.0

# Autenticación
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
StrictModes yes
MaxAuthTries 3

# Acceso
AllowUsers user1 user2
DenyUsers baduser
AllowGroups ssh-users

# Seguridad de sesión
ClientAliveInterval 300
ClientAliveCountMax 3
X11Forwarding no
PrintMotd no

# Criptografía
KexAlgorithms curve25519-sha256
Ciphers chacha20-poly1305@openssh.com
MACs hmac-sha2-256

# Reiniciar SSH
sudo systemctl restart ssh
```

### Configuración de Claves
```bash
# Generar clave segura
ssh-keygen -t ed25519 -C "user@host" -f ~/.ssh/id_ed25519

# Permisos correctos
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/id_ed25519

# Desactivar acceso por contraseña en servidor
sudo nano /etc/ssh/sshd_config
# PasswordAuthentication no
```

## 3. Firewall - UFW

### Configuración Básica
```bash
# Habilitar
sudo ufw enable
sudo ufw status verbose

# Política por defecto
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Permitir SSH (importante!)
sudo ufw allow 22/tcp
sudo ufw allow ssh

# Permitir servicios
sudo ufw allow 80/tcp           # HTTP
sudo ufw allow 443/tcp          # HTTPS
sudo ufw allow 8080/tcp         # Puerto personalizado

# Denegar específicos
sudo ufw deny 23/tcp            # Telnet

# Reglas por IP
sudo ufw allow from 192.168.1.0/24
sudo ufw allow from 192.168.1.100 to any port 3306

# Ver reglas detalladas
sudo ufw show added
sudo ufw status numbered

# Eliminar regla
sudo ufw delete allow 23/tcp
```

## 4. SELinux (Red Hat/CentOS)

### Verificar y Configurar
```bash
getenforce                      # Ver estado
sudo setenforce 0               # Deshabilitar temporalmente
sudo setenforce 1               # Habilitar

# Modo permanente
sudo nano /etc/selinux/config
SELINUX=enforcing

# Ver violaciones
sudo sealert -a /var/log/audit/audit.log
```

## 5. AppArmor (Ubuntu/Debian)

### Perfiles
```bash
aa-enabled                      # Verificar si está activo
sudo aa-status                  # Ver perfiles
sudo aa-enforce /etc/apparmor.d/usr.bin.nginx
sudo aa-complain /etc/apparmor.d/usr.bin.nginx
```

## 6. Auditoría y Logging

### auditd - Sistema de Auditoría
```bash
sudo apt install auditd
sudo systemctl start auditd

# Ver reglas
sudo auditctl -l

# Crear reglas
sudo auditctl -w /etc/shadow -p wa -k shadow_changes
sudo auditctl -w /etc/sudoers -p wa -k sudoers_changes

# Ver eventos
sudo ausearch -k shadow_changes
sudo aureport
```

### Logs del Sistema
```bash
# Ver logs de inicio de sesión
sudo lastlog
sudo last

# Logs de sudoers
sudo grep sudo /var/log/auth.log

# Ver intentos fallidos
sudo grep "Failed password" /var/log/auth.log
```

## 7. Análisis de Vulnerabilidades

### Verificar Puertos Abiertos
```bash
netstat -tulpn
ss -tulpn

# Escanear vulnerabilidades
sudo nmap -sV localhost
sudo nmap -O localhost            # Detectar OS
```

### Verificar Servicios
```bash
# Servicios activos
sudo systemctl list-units --type=service --state=running

# Servicios que se inician
sudo systemctl list-unit-files --state=enabled

# Desactivar servicios no necesarios
sudo systemctl disable avahi-daemon
sudo systemctl stop avahi-daemon
```

## 8. Permisos de Archivos

### Umask
```bash
# Ver umask actual
umask

# Cambiar umask (archivos 644, directorios 755)
umask 0022

# Hacer permanente
echo "umask 0022" >> ~/.bashrc
```

### SETUID/SETGID
```bash
# Ver archivos con SUID (ejecutables como propietario)
sudo find / -perm -4000 -type f 2>/dev/null

# Ver archivos con SGID (ejecutables como grupo)
sudo find / -perm -2000 -type f 2>/dev/null

# Sticky bit en /tmp
ls -ld /tmp              # Ver d...t
```

### Cambiar Propietarios Seguros
```bash
# Archivos sensibles solo lectura propietario
sudo chmod 600 /etc/shadow
sudo chmod 600 /etc/gshadow
sudo chmod 644 /etc/passwd
sudo chmod 644 /etc/group
```

## 9. Criptografía y LUKS

### Encriptación de Disco
```bash
# Crear volumen encriptado LUKS
sudo cryptsetup luksFormat /dev/sdb1

# Abrir volumen
sudo cryptsetup luksOpen /dev/sdb1 encrypted_drive

# Formatear
sudo mkfs.ext4 /dev/mapper/encrypted_drive

# Montar
sudo mount /dev/mapper/encrypted_drive /mnt/encrypted

# Cerrar
sudo umount /mnt/encrypted
sudo cryptsetup luksClose encrypted_drive
```

## 10. Fail2ban - Protección contra Ataques

### Instalación y Configuración
```bash
sudo apt install fail2ban
sudo systemctl start fail2ban

# Configuración
sudo nano /etc/fail2ban/jail.local

[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 5

[sshd]
enabled = true
port = ssh
maxretry = 3

# Ver bans activos
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

## 11. Checklist de Hardening Básico

```bash
# 1. Actualizar sistema
sudo apt update && sudo apt upgrade

# 2. Desactivar servicios innecesarios
sudo systemctl disable cups
sudo systemctl disable bluetooth

# 3. Habilitar firewall
sudo ufw enable

# 4. Configurar SSH seguro
sudo nano /etc/ssh/sshd_config
# PermitRootLogin no
# PasswordAuthentication no

# 5. Habilitar auditoría
sudo systemctl enable auditd

# 6. Configurar fail2ban
sudo systemctl enable fail2ban

# 7. Permisos correctos
sudo chmod 600 /etc/shadow
sudo chmod 600 /etc/gshadow

# 8. Verificar ejecuciones remotas
sudo netstat -tulpn | grep LISTEN
```

---
**Nivel**: Intermedio
**Tiempo estimado de estudio**: 4-5 horas
