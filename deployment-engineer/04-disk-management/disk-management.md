# Gestión de Discos en Linux

## 1. Ver Dispositivos de Disco

### Listar Discos
```bash
lsblk                           # Vista de árbol (recomendado)
fdisk -l                        # Listar todas particiones
parted -l                       # Particiones detalladas
ls -l /dev/sd*                  # Dispositivos SCSI/SATA
```

### Info de Uso
```bash
df -h                           # Espacio disco (por mount point)
df -i                           # Inodos disponibles
du -sh /path/to/dir             # Tamaño de directorio
du -sh /*                       # Tamaño por directorio raíz
```

## 2. Particionamiento con fdisk

### Crear Partición
```bash
sudo fdisk /dev/sdb             # Entrar en fdisk

# Dentro de fdisk:
n                               # Nueva partición
p                               # Partición primaria (o e - extendida)
1                               # Número de partición
ENTER                           # Usar sector por defecto
+10G                            # Tamaño 10GB
t                               # Cambiar tipo
83                              # Linux (o L para listar tipos)
w                               # Escribir cambios
```

### Ver Particiones
```bash
sudo fdisk -l /dev/sdb
sudo parted /dev/sdb print
```

## 3. Particionamiento con parted

### Crear Partición GPT
```bash
sudo parted /dev/sdb            # Entrar en parted
mklabel gpt                     # Crear tabla GPT
mkpart primary ext4 0% 100%     # Crear partición completa
quit                            # Salir
```

### Operaciones
```bash
sudo parted /dev/sdb print      # Ver particiones
sudo parted /dev/sdb resizepart 1 50GB  # Redimensionar
```

## 4. Formateo de Particiones

### Sistemas de Archivos Comunes
```bash
sudo mkfs.ext4 /dev/sdb1       # Crear ext4
sudo mkfs.xfs /dev/sdb1        # Crear XFS
sudo mkfs.vfat /dev/sdb1       # FAT32
```

### Opciones de Formateo
```bash
sudo mkfs.ext4 -L "MiDisco" /dev/sdb1      # Con etiqueta
sudo mkfs.ext4 -b 4096 /dev/sdb1           # Tamaño bloque
sudo mkfs.ext4 -m 1 /dev/sdb1              # Reservar 1% (no 5%)
```

## 5. Montaje de Disco

### Montaje Manual
```bash
sudo mkdir /mnt/disco
sudo mount /dev/sdb1 /mnt/disco
mount                            # Ver montes actuales
sudo umount /mnt/disco           # Desmontar
```

### Montaje Persistente (fstab)
```bash
# Editar /etc/fstab
sudo nano /etc/fstab

# Añadir línea (Por UUID es más seguro):
/dev/sdb1               /mnt/disco    ext4    defaults    0 2
UUID=xxxx-xxxx-xxxx     /mnt/disco    ext4    defaults    0 2

# Obtener UUID
sudo blkid
lsblk -o +UUID

# Validar antes de reboot
sudo mount -a
```

### Opciones de Mount
```bash
defaults                        # rw, suid, dev, exec, auto, nouser, async
ro                              # Solo lectura
rw                              # Lectura-escritura
noexec                          # No ejecutar binarios
nouser                          # Solo root puede desmontar
nofail                          # No fallar si no existe
```

## 6. Gestión de Espacio

### Expandir Partición

#### Con LVM (Logical Volume Management)
```bash
# Ver volúmenes lógicos
sudo lvdisplay
sudo lvs

# Expandir LV
sudo lvextend -L +10G /dev/vg0/lv_data
sudo resize2fs /dev/vg0/lv_data     # Para ext4
sudo xfs_growfs /dev/vg0/lv_data    # Para XFS
```

#### Expandir ext4 sin LVM
```bash
sudo resize2fs /dev/sdb1           # Después de expandir con parted
```

### Verificar y Reparar Sistemas de Archivos
```bash
sudo fsck -n /dev/sdb1             # Dry-run (sin reparar)
sudo fsck.ext4 -f /dev/sdb1        # Forzar verificación
sudo e2fsck -f /dev/sdb1           # Alternativa ext4

# XFS
sudo xfs_repair /dev/sdb1          # Reparar XFS
```

## 7. RAID (Redundant Array)

### Ver RAID
```bash
cat /proc/mdstat                    # Estado de RAID
sudo mdadm --detail /dev/md0        # Detalle RAID
```

### Crear RAID 1
```bash
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1
sudo mdadm --stop /dev/md0          # Detener
```

## 8. Cuotas de Disco (Disk Quotas)

### Habilitar Cuotas
```bash
# Editar /etc/fstab - añadir usrquota,grpquota
/dev/sdb1 /mnt/disco ext4 defaults,usrquota,grpquota 0 2

sudo mount -o remount /mnt/disco
sudo quotacheck -cug /mnt/disco
sudo quotaon /mnt/disco
```

### Configurar Cuota de Usuario
```bash
sudo edquota -u username           # Editar cuota
```

## 9. LVM (Logical Volume Management)

### Crear Volumen Lógico
```bash
# 1. Crear Physical Volume
sudo pvcreate /dev/sdb1

# 2. Crear Volume Group
sudo vgcreate vg_datos /dev/sdb1

# 3. Crear Logical Volume
sudo lvcreate -L 50G -n lv_datos vg_datos

# 4. Formatear
sudo mkfs.ext4 /dev/vg_datos/lv_datos

# 5. Montar
sudo mount /dev/vg_datos/lv_datos /mnt/datos
```

### Expandir Volumen LVM
```bash
sudo lvextend -L +20G /dev/vg_datos/lv_datos
sudo resize2fs /dev/vg_datos/lv_datos
```

## 10. Monitoreo Continuo

### Alertas de Espacio
```bash
# Crear script que chequee espacio
#!/bin/bash
LIMITE=80  # Porcentaje

df -h | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{ print $5 " " $1 }' | while read output;
do
  usage=$(echo $output | awk '{ print $1}' | cut -d'%' -f1)
  partition=$(echo $output | awk '{ print $2 }')
  if [ $usage -ge $LIMITE ]; then
    echo "Alerta: $partition está al $usage%"
  fi
done
```

---
**Nivel**: Intermedio
**Tiempo estimado de estudio**: 4-5 horas
