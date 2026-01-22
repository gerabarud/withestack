# Bash Scripting - Nivel Intermedio

## 1. Estructura Básica de Script

```bash
#!/bin/bash

# Comentarios con #
set -euo pipefail  # Salir en error, no permitir vars sin definir, fallar en pipe

# Tu código aquí
```

### Ejecutar Script
```bash
chmod +x script.sh
./script.sh
bash script.sh
```

## 2. Variables

### Declaración y Uso
```bash
VARIABLE="valor"
echo $VARIABLE
echo ${VARIABLE}                # Forma explícita

# Substitución de comando
RESULTADO=$(command)
RESULTADO=`command`             # Forma antigua

# Variables de entorno
export VARIABLE="valor"
```

### Variables Especiales
```bash
$0                              # Nombre del script
$1, $2, $3                      # Argumentos posicionales
$#                              # Número de argumentos
$@                              # Todos los argumentos
$?                              # Código de salida del último comando
$$                              # PID del script
$!                              # PID del último background
```

### Variables de Sistema
```bash
$HOME                           # Directorio home
$USER                           # Usuario actual
$PWD                            # Directorio actual
$HOSTNAME                       # Nombre del host
```

## 3. Operadores Comparación

### Números
```bash
-eq                             # Igual
-ne                             # No igual
-lt                             # Menor que
-le                             # Menor o igual
-gt                             # Mayor que
-ge                             # Mayor o igual
```

### Strings
```bash
=                               # Igual
!=                              # No igual
-z                              # String vacío
-n                              # String no vacío
```

### Archivos
```bash
-f                              # Es archivo regular
-d                              # Es directorio
-e                              # Existe
-r                              # Readable
-w                              # Writable
-x                              # Executable
-s                              # No está vacío
```

## 4. Condicionales

### If-Else
```bash
if [ $1 -eq 5 ]; then
    echo "Es igual a 5"
elif [ $1 -gt 5 ]; then
    echo "Mayor que 5"
else
    echo "Menor que 5"
fi
```

### Case
```bash
case $1 in
    start)
        echo "Iniciando..."
        ;;
    stop)
        echo "Deteniendo..."
        ;;
    *)
        echo "Uso: $0 {start|stop}"
        exit 1
        ;;
esac
```

## 5. Bucles

### For Loop
```bash
for i in 1 2 3 4 5; do
    echo $i
done

for i in {1..10}; do
    echo $i
done

for file in *.txt; do
    echo "Procesando $file"
done

for ((i=1; i<=10; i++)); do
    echo $i
done
```

### While Loop
```bash
while [ $contador -lt 10 ]; do
    echo $contador
    contador=$((contador + 1))
done
```

### Until Loop
```bash
until [ $contador -eq 10 ]; do
    echo $contador
    contador=$((contador + 1))
done
```

## 6. Funciones

### Definición y Uso
```bash
# Forma 1
function saludar() {
    echo "Hola, $1"
}

# Forma 2
saludar() {
    echo "Hola, $1"
    return 0
}

# Llamar función
saludar "Juan"
```

### Retorno de Valores
```bash
obtener_suma() {
    echo $((2 + 3))
}

resultado=$(obtener_suma)
echo "Suma: $resultado"
```

## 7. Procesamiento de Texto

### grep
```bash
grep "patrón" archivo.txt
grep -i "patrón" archivo.txt    # Case insensitive
grep -n "patrón" archivo.txt    # Mostrar número línea
grep -v "patrón" archivo.txt    # Invertir (excluir)
grep -E "patron|alternativa" archivo.txt  # Regex extendida
```

### sed (Stream Editor)
```bash
sed 's/viejo/nuevo/g' archivo.txt     # Reemplazar
sed '5d' archivo.txt                  # Borrar línea 5
sed -n '1,5p' archivo.txt             # Mostrar líneas 1-5
sed 's/  */ /g' archivo.txt           # Collapsar espacios
```

### awk
```bash
awk '{print $1}' archivo.txt          # Primer campo
awk -F: '{print $1}' /etc/passwd      # Cambiar separador
awk '{sum+=$1} END {print sum}' archivo.txt  # Suma
awk 'NR==5' archivo.txt               # Línea 5
```

### cut
```bash
cut -d: -f1 /etc/passwd               # Primer campo (delimitador :)
cut -c1-10 archivo.txt                # Primeros 10 caracteres
```

## 8. Entrada y Salida

### Read de Usuario
```bash
read -p "Ingrese nombre: " nombre
echo "Hola $nombre"

read -s -p "Contraseña: " password    # Sin mostrar
read -t 10 variable                   # Timeout 10 segundos
```

### Redirección
```bash
comando > archivo.txt                 # Stdout a archivo
comando >> archivo.txt                # Append
comando 2> error.txt                  # Stderr a archivo
comando &> todo.txt                   # Stdout y stderr
comando < entrada.txt                 # Stdin desde archivo
comando1 | comando2                   # Pipe
```

## 9. Arrays

### Declaración y Uso
```bash
arr=(1 2 3 4 5)
echo ${arr[0]}                        # Primer elemento
echo ${arr[@]}                        # Todos elementos
echo ${#arr[@]}                       # Longitud

# Iterar
for elemento in "${arr[@]}"; do
    echo $elemento
done

# Añadir
arr+=(6 7)
```

## 10. Scripts Prácticos Comunes

### Verificar si archivo existe
```bash
if [ -f "$1" ]; then
    echo "Archivo existe"
else
    echo "Archivo no existe"
    exit 1
fi
```

### Backup automático
```bash
#!/bin/bash
ORIGEN="/home/usuario/datos"
DESTINO="/backup/$(date +%Y-%m-%d)"

mkdir -p "$DESTINO"
cp -r "$ORIGEN" "$DESTINO"
echo "Backup completado en $DESTINO"
```

### Monitorear proceso
```bash
#!/bin/bash
PROCESO="apache2"

if pgrep -x "$PROCESO" > /dev/null; then
    echo "$PROCESO está activo"
else
    echo "Iniciando $PROCESO"
    sudo systemctl start $PROCESO
fi
```

### Loop sobre lista de servidores
```bash
#!/bin/bash
servidores=("server1" "server2" "server3")

for servidor in "${servidores[@]}"; do
    echo "Conectando a $servidor..."
    ssh user@$servidor "uptime"
done
```

---
**Nivel**: Intermedio
**Tiempo estimado de estudio**: 5 horas
