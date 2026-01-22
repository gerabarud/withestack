# Preguntas de Práctica - SysAdmin Level 1 & 2

## SysAdmin Level 1 (15 preguntas)

### 1. **Gestión de Usuarios**
¿Cuál es el comando correcto para crear un usuario con directorio home y shell /bin/bash?

A) `useradd user1`
B) `useradd -m -s /bin/bash user1`
C) `adduser user1 /bin/bash`
D) `usermod -m user1`

**Respuesta**: B
**Explicación**: `-m` crea directorio home, `-s` especifica el shell

---

### 2. **Permisos de Archivos**
¿Cuál es el resultado de los permisos 755 en octal?

A) rw-r--r--
B) rwxr-xr-x
C) rwx------
D) rw-rw-rw-

**Respuesta**: B
**Explicación**: 7=rwx, 5=r-x, 5=r-x

---

### 3. **Procesos**
¿Qué comando te muestra todos los procesos en formato árbol?

A) `ps aux`
B) `ps -ef --forest`
C) `ps -tree`
D) `pstree -a`

**Respuesta**: B (o D)
**Explicación**: Ambas opciones son válidas

---

### 4. **Servicios**
¿Cómo habilitas un servicio para que inicie al boot?

A) `systemctl start nginx`
B) `systemctl enable nginx`
C) `systemctl auto nginx`
D) `systemctl boot nginx`

**Respuesta**: B
**Explicación**: `enable` hace que inicie automáticamente

---

### 5. **Networking - Interfaces**
¿Cuál es el comando para ver todas las interfaces de red actualmente?

A) `ifconfig`
B) `ip addr show`
C) `ip link show`
D) B y C son correctas

**Respuesta**: D
**Explicación**: Ambos comandos funcionan, aunque `ip` es más moderno

---

### 6. **SSH**
¿Cuál es el puerto por defecto de SSH?

A) 21
B) 22
C) 23
D) 2222

**Respuesta**: B

---

### 7. **Firewall**
¿Cuál es el comando para permitir el puerto 80 en UFW?

A) `ufw allow 80`
B) `ufw allow http`
C) `ufw accept 80`
D) A y B son correctas

**Respuesta**: D

---

### 8. **Logs**
¿Dónde se encuentran típicamente los logs del sistema en Linux?

A) `/var/log/`
B) `/etc/logs/`
C) `/home/logs/`
D) `/tmp/logs/`

**Respuesta**: A

---

### 9. **Package Management**
¿Cuál es el comando para actualizar la lista de paquetes en Ubuntu?

A) `apt upgrade`
B) `apt update`
C) `apt-get update`
D) B y C son correctas

**Respuesta**: D

---

### 10. **Discos**
¿Cuál es el comando para ver el espacio disponible en disco?

A) `du -h`
B) `df -h`
C) `disk -free`
D) `fdisk -l`

**Respuesta**: B
**Explicación**: `df` muestra espacio disponible, `du` muestra uso

---

### 11. **Bash Scripting**
¿Cuál es el resultado de este script?
```bash
i=5
if [ $i -lt 10 ]; then
  echo "Menor"
fi
```

A) "Menor" se imprime
B) "Menor" no se imprime
C) Error de sintaxis
D) Ninguno

**Respuesta**: A
**Explicación**: 5 es menor que 10

---

### 12. **Variables de Entorno**
¿Cuál es la variable que contiene el directorio actual del usuario?

A) `$PWD`
B) `$HOME`
C) `$USER`
D) `$SHELL`

**Respuesta**: A (para directorio actual)
**Nota**: `$HOME` es para home, `$USER` es usuario actual

---

### 13. **Conectividad**
¿Cuál es el comando para verificar si un host es alcanzable?

A) `ping hostname`
B) `nslookup hostname`
C) `traceroute hostname`
D) `ssh hostname`

**Respuesta**: A

---

### 14. **Cron**
¿Qué significa `*/5` en una línea de cron?

A) Cada 5 segundos
B) Cada 5 minutos
C) Cada 5 horas
D) Cada 5 días

**Respuesta**: B

---

### 15. **Troubleshooting**
¿Cuál es el comando para ver los últimos 50 logs del sistema?

A) `tail -f /var/log/syslog`
B) `tail -50 /var/log/syslog`
C) `head -50 /var/log/syslog`
D) `tail -n 50 /var/log/syslog`

**Respuesta**: B o D

---

## SysAdmin Level 2 (8 preguntas - MÁS COMPLEJAS)

### 1. **Scripting Avanzado**
¿Cuál es la salida de este script?
```bash
arr=(1 2 3 4 5)
for i in "${arr[@]}"; do
  if [ $i -eq 3 ]; then
    break
  fi
  echo $i
done
```

A) 1 2 3 4 5
B) 1 2
C) 1 2 3
D) Error

**Respuesta**: B
**Explicación**: `break` sale del loop cuando i=3

---

### 2. **Networking Avanzado**
¿Cómo verificas la tabla de rutas en el sistema?

A) `ip route show`
B) `netstat -r`
C) `route -n`
D) Todas las anteriores

**Respuesta**: D

---

### 3. **Seguridad**
¿Cuál es la configuración correcta en `sshd_config` para deshabilitar login por contraseña?

A) `PasswordAuthentication yes`
B) `PasswordAuthentication no`
C) `PublicKeyAuthentication no`
D) `PermitRootLogin yes`

**Respuesta**: B

---

### 4. **LVM**
¿Cuál es el comando para expandir un volumen lógico 20GB?

A) `lvextend -L +20G /dev/vg0/lv_data`
B) `lvresize -L +20G /dev/vg0/lv_data`
C) `lvexpand -L +20G /dev/vg0/lv_data`
D) A y B son correctas

**Respuesta**: D (ambas funcionan)

---

### 5. **Ansible**
¿Cuál es la estructura correcta de un handler en Ansible?

A) 
```yaml
tasks:
  - name: task
    notify: handler_name
handlers:
  - name: handler_name
    action: command
```

B)
```yaml
tasks:
  - name: task
    call: handler_name
```

C) Ninguna

**Respuesta**: A

---

### 6. **Docker**
¿Cuál es el comando para ejecutar un contenedor en background exponiendo puerto 8080 al 80 interno?

A) `docker run -d -p 8080:80 nginx`
B) `docker run -d -P 8080:80 nginx`
C) `docker run -b -p 8080:80 nginx`
D) `docker run -d 8080:80 nginx`

**Respuesta**: A

---

### 7. **Análisis de Problemas**
Un servidor está lento. ¿Qué comandos ejecutarías PRIMERO para diagnosticar?

A) `top` y `df -h`
B) `netstat` solamente
C) `dmesg` solamente
D) `systemctl restart *`

**Respuesta**: A
**Explicación**: Ver procesos (top) y espacio disco (df) es lo primero

---

### 8. **Firewall Avanzado**
¿Cuál es el comando para permitir SSH solo desde 192.168.1.0/24?

A) `ufw allow from 192.168.1.0/24 to any port 22`
B) `ufw allow 192.168.1.0/24 22`
C) `ufw allow source 192.168.1.0/24 port 22`
D) Ninguna

**Respuesta**: A

---

## 📊 Respuestas Rápidas

| Pregunta | Respuesta |
|----------|-----------|
| L1.1 | B |
| L1.2 | B |
| L1.3 | B o D |
| L1.4 | B |
| L1.5 | D |
| L1.6 | B |
| L1.7 | D |
| L1.8 | A |
| L1.9 | D |
| L1.10 | B |
| L1.11 | A |
| L1.12 | A |
| L1.13 | A |
| L1.14 | B |
| L1.15 | B o D |
| L2.1 | B |
| L2.2 | D |
| L2.3 | B |
| L2.4 | D |
| L2.5 | A |
| L2.6 | A |
| L2.7 | A |
| L2.8 | A |

---

## 💡 Estrategia de Estudio

1. **Primera pasada**: Intenta sin mirar respuestas
2. **Segunda pasada**: Revisa respuestas y explicaciones
3. **Tercera pasada**: Simula examen con cronómetro
4. **Meta**: 85%+ en Level 1, 80%+ en Level 2

---

**Puedes practicar estos ejercicios múltiples veces para asegurar dominio de cada tema.**
