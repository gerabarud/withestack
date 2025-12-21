# 🐧 Linux Essentials - Comandos y Conceptos para DevOps/SRE

## 🎯 Comandos Top 100 que DEBES Dominar

---

## 1️⃣ Navegación y Archivos

### Básicos
```bash
# Directorio actual
pwd

# Listar archivos
ls
ls -la              # detallado + ocultos
ls -lh              # tamaños human-readable
ls -lt              # ordenado por tiempo
ls -lS              # ordenado por tamaño
ls -R               # recursivo

# Cambiar directorio
cd /path/to/dir
cd ..               # directorio padre
cd ~                # home
cd -                # directorio anterior

# Crear directorio
mkdir mydir
mkdir -p path/to/nested/dir   # crear toda la ruta

# Eliminar
rm file.txt
rm -r directory/              # recursivo
rm -rf directory/             # forzar sin confirmación
rmdir empty_directory/        # solo directorios vacíos

# Copiar
cp file.txt file_backup.txt
cp -r dir1/ dir2/             # recursivo
cp -p file.txt backup/        # preservar permisos/timestamps

# Mover/Renombrar
mv old_name.txt new_name.txt
mv file.txt /other/path/

# Crear archivo vacío / actualizar timestamp
touch file.txt
```

---

### Búsqueda de Archivos

```bash
# Find - buscar archivos
find /path -name "*.log"                    # por nombre
find /var/log -name "*.log" -mtime -7       # modificados últimos 7 días
find . -type f -size +100M                  # archivos >100MB
find . -type f -name "*.txt" -exec rm {} \; # ejecutar comando en resultados
find /tmp -mtime +30 -delete                # eliminar archivos viejos

# Ejemplos útiles
find . -name "*.pyc" -delete                # limpiar Python cache
find /var/log -name "*.gz" -mtime +30 -delete  # limpiar logs viejos
find . -type f -perm 0777                   # archivos con permisos 777

# Locate - búsqueda rápida (usa DB)
locate nginx.conf
sudo updatedb             # actualizar DB

# Which - ubicación de ejecutable
which python3
which docker

# Whereis - ubicación de binario, source, manual
whereis nginx
```

---

## 2️⃣ Visualización de Archivos

```bash
# Cat - mostrar contenido completo
cat file.txt
cat file1.txt file2.txt > combined.txt

# Less - paginador (recomendado para archivos grandes)
less /var/log/syslog
# Controles: space (página), q (salir), /palabra (buscar)

# Head - primeras líneas
head file.txt           # primeras 10 líneas
head -n 20 file.txt     # primeras 20 líneas

# Tail - últimas líneas
tail file.txt           # últimas 10 líneas
tail -n 50 file.txt     # últimas 50 líneas
tail -f /var/log/syslog # follow (tiempo real) ⭐

# More - paginador simple
more file.txt

# Bat - cat con syntax highlighting (si está instalado)
bat app.py
```

---

## 3️⃣ Procesamiento de Texto

### Grep - Búsqueda de Patrones

```bash
# Búsqueda básica
grep "error" /var/log/syslog
grep "ERROR" app.log

# Case insensitive
grep -i "error" app.log

# Recursivo en directorio
grep -r "TODO" .
grep -r "import" src/

# Mostrar líneas antes/después del match
grep -A 5 "error" log.txt    # 5 líneas After
grep -B 5 "error" log.txt    # 5 líneas Before
grep -C 5 "error" log.txt    # 5 líneas Context (antes y después)

# Invertir match (líneas que NO coinciden)
grep -v "DEBUG" app.log

# Contar ocurrencias
grep -c "error" app.log

# Mostrar solo nombres de archivo
grep -l "error" *.log

# Números de línea
grep -n "error" app.log

# Regex extendido
grep -E "error|warning|critical" app.log

# Ejemplos útiles
grep -i "error" /var/log/syslog | tail -20
grep -r "FIXME" . --include="*.py"
grep -r "password" . --exclude-dir=node_modules
```

### Awk - Procesamiento de Columnas

```bash
# Imprimir columnas específicas
awk '{print $1}' file.txt              # primera columna
awk '{print $1, $3}' file.txt          # columnas 1 y 3

# Con delimitador custom
awk -F: '{print $1}' /etc/passwd       # usar : como separador

# Filtrar y procesar
awk '$3 > 100' file.txt                # líneas donde col3 > 100
awk '/error/ {print $1, $2}' app.log   # match pattern y mostrar cols

# Sumar columna
awk '{sum += $1} END {print sum}' file.txt

# Ejemplos útiles
# Mostrar usuarios y sus shells
awk -F: '{print $1, $7}' /etc/passwd

# Procesos usando más memoria
ps aux | awk '{print $4, $11}' | sort -n

# Analizar logs de Nginx/Apache
awk '{print $1}' access.log | sort | uniq -c | sort -rn  # IPs más frecuentes
```

### Sed - Editor de Stream

```bash
# Substituir (primera ocurrencia)
sed 's/old/new/' file.txt

# Substituir (todas las ocurrencias)
sed 's/old/new/g' file.txt

# Substituir e modificar archivo in-place
sed -i 's/old/new/g' file.txt

# Eliminar líneas
sed '/pattern/d' file.txt              # eliminar líneas con pattern
sed '5d' file.txt                      # eliminar línea 5
sed '1,10d' file.txt                   # eliminar líneas 1-10

# Reemplazar en múltiples archivos
sed -i 's/old/new/g' *.txt

# Ejemplos útiles
# Cambiar IPs en config
sed -i 's/192.168.1.1/10.0.0.1/g' config.ini

# Eliminar líneas vacías
sed '/^$/d' file.txt

# Agregar línea después de match
sed '/pattern/a\new line' file.txt
```

### Cut - Extraer Columnas

```bash
# Por delimitador
cut -d: -f1 /etc/passwd               # campo 1 (usuarios)
cut -d: -f1,7 /etc/passwd             # campos 1 y 7
cut -d',' -f2-4 data.csv              # campos 2 al 4

# Por posición de caracteres
cut -c1-10 file.txt                   # caracteres 1 al 10
```

### Sort - Ordenar

```bash
# Ordenar alfabéticamente
sort file.txt

# Ordenar numéricamente
sort -n numbers.txt

# Orden reverso
sort -r file.txt

# Ordenar por columna específica
sort -k2 file.txt                     # por columna 2
sort -t: -k3 -n /etc/passwd           # por campo 3, delim :, numérico

# Eliminar duplicados
sort -u file.txt

# Ejemplos
# Top 10 comandos más usados en history
history | awk '{print $2}' | sort | uniq -c | sort -rn | head -10
```

### Uniq - Eliminar Duplicados

```bash
# Eliminar líneas duplicadas consecutivas
uniq file.txt

# Contar ocurrencias
uniq -c file.txt

# Solo mostrar duplicados
uniq -d file.txt

# Solo mostrar únicos (no duplicados)
uniq -u file.txt

# Nota: uniq requiere entrada ordenada
sort file.txt | uniq -c
```

### Tr - Translate/Delete Characters

```bash
# Mayúsculas a minúsculas
tr '[:upper:]' '[:lower:]' < file.txt

# Eliminar caracteres
tr -d '0-9' < file.txt                # eliminar dígitos

# Replace espacios por guiones
echo "hello world" | tr ' ' '-'

# Eliminar saltos de línea
tr -d '\n' < file.txt
```

### Wc - Word Count

```bash
# Contar líneas, palabras, bytes
wc file.txt

# Solo líneas
wc -l file.txt

# Solo palabras
wc -w file.txt

# Solo bytes
wc -c file.txt

# Ejemplos
# Contar archivos en directorio
ls | wc -l

# Contar líneas de código Python
find . -name "*.py" | xargs wc -l
```

---

## 4️⃣ Procesos y Sistema

### Ver Procesos

```bash
# Lista de procesos
ps aux                                # todos los procesos
ps aux | grep nginx                   # filtrar por nombre
ps -ef                                # formato alternativo

# Tree de procesos
pstree
pstree -p                             # con PIDs

# Top - monitoreo interactivo
top
# Controles:
# - k: kill proceso
# - M: ordenar por memoria
# - P: ordenar por CPU
# - q: salir

# Htop - versión mejorada de top
htop

# Procesos de un usuario
ps -u username

# Procesos por uso de CPU (top 10)
ps aux --sort=-%cpu | head -11

# Procesos por uso de memoria (top 10)
ps aux --sort=-%mem | head -11
```

### Gestión de Procesos

```bash
# Kill proceso
kill <PID>
kill -9 <PID>                         # forzar (SIGKILL)
kill -15 <PID>                        # graceful (SIGTERM)

# Kill por nombre
killall nginx
pkill -f "python app.py"

# Ejecutar en background
command &

# Ver jobs en background
jobs

# Traer job al foreground
fg %1

# Enviar job actual al background
Ctrl+Z                                # suspender
bg                                    # continuar en background

# Nohup - ejecutar desconectado de terminal
nohup ./script.sh &

# Disown - desasociar proceso de shell
./long_process.sh &
disown

# Nice - ejecutar con prioridad
nice -n 10 ./script.sh                # menor prioridad
nice -n -10 ./script.sh               # mayor prioridad (requiere root)

# Renice - cambiar prioridad de proceso running
renice -n 5 -p <PID>
```

### Systemd (Servicios)

```bash
# Ver status de servicio
systemctl status nginx
systemctl status docker

# Iniciar servicio
sudo systemctl start nginx

# Detener servicio
sudo systemctl stop nginx

# Reiniciar servicio
sudo systemctl restart nginx

# Reload config (sin reiniciar)
sudo systemctl reload nginx

# Habilitar en boot
sudo systemctl enable nginx

# Deshabilitar en boot
sudo systemctl disable nginx

# Ver logs de servicio
journalctl -u nginx
journalctl -u nginx -f                # follow
journalctl -u nginx --since "1 hour ago"
journalctl -u nginx --since "2024-01-01"

# Listar servicios
systemctl list-units --type=service
systemctl list-units --state=running
systemctl list-units --state=failed

# Ver dependencias de servicio
systemctl list-dependencies nginx
```

---

## 5️⃣ Networking

```bash
# Ver interfaces de red
ip addr
ip a                                  # shorthand
ifconfig                              # legacy

# Ver rutas
ip route
route -n

# Ping
ping google.com
ping -c 4 google.com                  # solo 4 paquetes

# Traceroute
traceroute google.com
traceroute -n google.com              # sin DNS lookup

# Netstat - conexiones de red (legacy)
netstat -tulpn                        # listening ports
netstat -an                           # todas las conexiones

# SS - socket statistics (reemplazo de netstat)
ss -tulpn                             # listening TCP/UDP
ss -t                                 # solo TCP
ss -u                                 # solo UDP
ss -p                                 # mostrar proceso

# Ver procesos escuchando en puertos
sudo lsof -i -P -n
sudo lsof -i :80                      # puerto específico

# Curl - HTTP requests
curl http://example.com
curl -I http://example.com            # solo headers
curl -X POST -d '{"key":"value"}' http://api.com
curl -H "Authorization: Bearer token" http://api.com

# Wget - descargar archivos
wget http://example.com/file.zip
wget -c http://example.com/file.zip   # continuar descarga

# Nmap - escaneo de puertos
nmap localhost
nmap -p 80,443 example.com
nmap -sV example.com                  # detectar versiones

# Dig - DNS lookup
dig google.com
dig +short google.com
dig @8.8.8.8 google.com               # usar DNS server específico
dig google.com MX                     # records MX

# Nslookup
nslookup google.com

# Host
host google.com

# Telnet - test de conectividad TCP
telnet example.com 80

# Nc (netcat) - Swiss Army knife de networking
nc -zv example.com 80                 # test port
nc -l 8080                            # escuchar en puerto
echo "hello" | nc localhost 8080      # enviar data
```

---

## 6️⃣ Permisos y Usuarios

### Permisos

```bash
# Ver permisos
ls -l file.txt
# -rw-r--r-- 1 user group 1234 Jan 01 12:00 file.txt
# │││││││││
# ││││││││└─ otros: read
# │││││││└── grupo: read
# ││││││└─── owner: read, write
# │││││└──── enlaces
# ││││└───── owner
# │││└────── group
# ││└─────── size
# │└──────── date
# └───────── tipo (- = file, d = dir, l = link)

# Cambiar permisos (método octal)
chmod 644 file.txt                    # rw-r--r--
chmod 755 script.sh                   # rwxr-xr-x
chmod 600 secret.txt                  # rw-------

# Cambiar permisos (método simbólico)
chmod u+x script.sh                   # agregar execute al user
chmod g-w file.txt                    # quitar write al group
chmod o+r file.txt                    # agregar read a others
chmod a+x script.sh                   # agregar execute a all

# Recursivo
chmod -R 755 directory/

# Cambiar owner
chown user:group file.txt
chown user file.txt
chown -R user:group directory/

# Solo cambiar group
chgrp group file.txt

# Permisos especiales
chmod u+s file                        # setuid
chmod g+s directory                   # setgid
chmod +t directory                    # sticky bit
```

**Permisos octales comunes:**
- `644` - archivos normales (rw-r--r--)
- `755` - directorios/scripts (rwxr-xr-x)
- `600` - archivos privados (rw-------)
- `700` - directorios privados (rwx------)

### Usuarios y Grupos

```bash
# Ver usuario actual
whoami
id

# Ver usuarios logueados
who
w

# Cambiar a otro usuario
su - username
su -                                  # cambiar a root

# Ejecutar comando como root
sudo command

# Editar sudoers
sudo visudo

# Agregar usuario
sudo useradd -m username              # -m crea home dir
sudo useradd -m -s /bin/bash username

# Establecer password
sudo passwd username

# Eliminar usuario
sudo userdel username
sudo userdel -r username              # también eliminar home

# Modificar usuario
sudo usermod -aG docker username      # agregar a grupo
sudo usermod -s /bin/bash username    # cambiar shell

# Ver grupos de usuario
groups username

# Agregar grupo
sudo groupadd groupname

# Ver todos los usuarios
cat /etc/passwd

# Ver todos los grupos
cat /etc/group

# Último login
lastlog
last
```

---

## 7️⃣ Disk Usage

```bash
# Espacio en discos
df -h                                 # human-readable
df -h /                               # solo root partition

# Uso de directorio
du -sh /var/log                       # summary
du -h --max-depth=1 /var              # primer nivel
du -h | sort -h                       # ordenado por tamaño

# Top directorios más grandes
du -h /var | sort -rh | head -20

# Encontrar archivos grandes
find / -type f -size +100M -exec ls -lh {} \;

# Inodes
df -i                                 # ver uso de inodes
```

---

## 8️⃣ Compresión y Archiving

```bash
# Tar - archiving
tar -czf archive.tar.gz directory/    # crear tar.gz
tar -xzf archive.tar.gz               # extraer tar.gz
tar -tzf archive.tar.gz               # listar contenido
tar -xzf archive.tar.gz -C /target/   # extraer en directorio específico

# Gzip
gzip file.txt                         # comprime y reemplaza
gunzip file.txt.gz                    # descomprime

# Bzip2 (mayor compresión)
bzip2 file.txt
bunzip2 file.txt.bz2

# Zip
zip archive.zip file1 file2
zip -r archive.zip directory/
unzip archive.zip
unzip -l archive.zip                  # listar contenido

# Ejemplos útiles
# Backup de directorio
tar -czf backup-$(date +%Y%m%d).tar.gz /var/www/

# Extraer solo un archivo
tar -xzf archive.tar.gz path/to/file
```

---

## 9️⃣ Variables de Entorno y Bash

```bash
# Ver variables de entorno
env
printenv
echo $PATH
echo $HOME

# Establecer variable (sesión actual)
export MY_VAR="value"

# Agregar al PATH
export PATH=$PATH:/new/path

# Variables permanentes (agregar a ~/.bashrc o ~/.profile)
echo 'export MY_VAR="value"' >> ~/.bashrc
source ~/.bashrc                      # recargar

# History
history                               # ver historial de comandos
!123                                  # ejecutar comando 123 del history
!!                                    # ejecutar último comando
!$                                    # último argumento del comando anterior

# Alias
alias ll='ls -la'
alias gs='git status'
# Permanentes: agregar a ~/.bashrc

# Command substitution
echo "Today is $(date)"
FILES=$(ls *.txt)
```

---

## 🔟 Shortcuts y Tips

```bash
# Navigation
Ctrl + A                              # inicio de línea
Ctrl + E                              # fin de línea
Ctrl + U                              # borrar desde cursor al inicio
Ctrl + K                              # borrar desde cursor al final
Ctrl + W                              # borrar palabra anterior
Ctrl + L                              # limpiar pantalla
Ctrl + R                              # buscar en history (reverse search)

# Control de procesos
Ctrl + C                              # kill proceso
Ctrl + Z                              # suspender proceso
Ctrl + D                              # EOF / logout

# Pipes y Redirection
command > file                        # redirect stdout (sobrescribe)
command >> file                       # redirect stdout (append)
command 2> file                       # redirect stderr
command &> file                       # redirect stdout y stderr
command1 | command2                   # pipe
command < file                        # redirect stdin

# Logical operators
command1 && command2                  # command2 solo si command1 exitoso
command1 || command2                  # command2 solo si command1 falla
command1 ; command2                   # ejecutar ambos secuencialmente
```

---

## 📚 Comandos Especializados

### System Info

```bash
# Hostname
hostname
hostname -I                           # IPs

# Uptime
uptime

# Kernel version
uname -a
uname -r

# OS info
cat /etc/os-release
lsb_release -a

# Hardware info
lscpu                                 # CPU
lsmem                                 # Memory
lsblk                                 # Block devices
lspci                                 # PCI devices
lsusb                                 # USB devices

# Free memory
free -h
```

### Cron (Scheduled Tasks)

```bash
# Editar crontab
crontab -e

# Ver crontab actual
crontab -l

# Formato crontab:
# * * * * * command
# │ │ │ │ │
# │ │ │ │ └─── día de semana (0-7, 0=domingo)
# │ │ │ └───── mes (1-12)
# │ │ └─────── día del mes (1-31)
# │ └───────── hora (0-23)
# └─────────── minuto (0-59)

# Ejemplos:
# 0 2 * * * /backup.sh          # 2am diario
# */5 * * * * /check.sh          # cada 5 minutos
# 0 0 * * 0 /weekly.sh           # domingo a medianoche
```

---

## ✅ Checklist de Dominio

- [ ] Navegación fluida (cd, ls, pwd)
- [ ] Crear/eliminar archivos y directorios
- [ ] Usar grep para búsquedas complejas
- [ ] Procesar texto con awk/sed/cut
- [ ] Gestionar procesos (ps, top, kill)
- [ ] Trabajar con systemd/journalctl
- [ ] Diagnosticar networking (ss, curl, dig)
- [ ] Entender permisos (chmod, chown)
- [ ] Usar pipes y redirections
- [ ] Comprimir/descomprimir archivos
- [ ] Monitorear recursos (df, du, free, top)
