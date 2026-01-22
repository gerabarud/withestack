# Python para Automatización - Nivel Básico

> **Propósito General**: Python es el lenguaje de automatización por excelencia para DevOps y administración de sistemas. Permite crear scripts robustos para gestionar servidores, redes, discos, servicios y despliegues de forma más mantenible que Bash.

## 1. Sintaxis Básica

> **Definición**: Estructuras fundamentales del lenguaje Python para almacenar y manipular datos.
> 
> **Propósito**: Comprender cómo Python almacena información te permite escribir scripts de automatización efectivos. Los diccionarios son especialmente útiles para configuraciones de servidores y respuestas de APIs.

### Variables y Tipos
```python
# ===== STRINGS (Cadenas de texto) =====
# Propósito: Almacenar texto como nombres de host, rutas, comandos
nombre = "Juan"
print(f"Hola {nombre}")  # f-strings: forma moderna de interpolar variables

# ===== NÚMEROS =====
# Propósito: Contadores, puertos, PIDs, métricas de sistema
edad = 30              # int: números enteros (ej: puerto 8080, PID 1234)
altura = 1.75          # float: decimales (ej: uso de CPU 45.3%, espacio en disco 89.5GB)

# ===== LISTAS =====
# Propósito: Colecciones ordenadas - ideal para listas de servidores, IPs, archivos
servidores = ["web1", "web2", "db1"]
print(servidores[0])   # Acceso por índice (comienza en 0)
servidores.append("web3")  # Agregar elemento
servidores.remove("db1")   # Eliminar elemento

# ===== DICCIONARIOS =====
# Propósito: Pares clave-valor - perfecto para configs, respuestas JSON, metadatos
config = {
    "host": "localhost",      # Clave: valor
    "puerto": 8080,           # Usar para configuraciones de servicios
    "usuario": "admin"
}
print(config["host"])         # Acceso por clave
config["activo"] = True       # Agregar nueva clave
```

## 2. Condicionales

> **Definición**: Estructuras de control que ejecutan código basándose en condiciones.
> 
> **Propósito**: Tomar decisiones en scripts - verificar si un servicio está activo, si hay espacio en disco, si un puerto está abierto.
> 
> **Casos de uso**: Validar estados de sistema, comprobar umbrales (CPU > 80%, disco > 90%), decidir acciones según respuestas de comandos.

```python
# ===== IF/ELIF/ELSE: Estructura de decisión básica =====
# Ejemplo: Verificar estado de un servicio basado en código de retorno
codigo_retorno = 0

if codigo_retorno == 0:
    print("Servicio funcionando correctamente")
elif codigo_retorno == 1:
    print("Servicio con advertencias")
else:
    print("Servicio caído - requiere intervención")

# ===== ONE-LINER (Operador Ternario) =====
# Propósito: Asignaciones condicionales en una línea - más limpio para casos simples
disk_usage = 85
estado_disco = "CRÍTICO" if disk_usage > 90 else "OK"  # Condición compacta

# Ejemplo práctico: Determinar tipo de red según máscara
mascara = "255.255.255.0"
tipo_red = "Clase C" if mascara == "255.255.255.0" else "Otra clase"
```

## 3. Bucles

> **Definición**: Estructuras que repiten código múltiples veces.
> 
> **Propósito**: Iterar sobre listas de servidores, procesar líneas de archivos de log, ejecutar tareas en múltiples hosts, generar configuraciones repetitivas.
> 
> **Casos de uso**: Procesar salidas de comandos, verificar múltiples servicios, leer archivos de configuración línea por línea.

```python
# ===== FOR LOOP: Iterar sobre colecciones =====
# Propósito: Ejecutar la misma operación en múltiples elementos
servidores = ["web1", "web2", "db1"]

for servidor in servidores:
    print(f"Verificando servidor: {servidor}")
    # Aquí podrías hacer: ping, verificar servicio, copiar archivo, etc.

# ===== FOR con RANGE: Generar secuencias numéricas =====
# Propósito: Repetir N veces, generar IPs, iterar por índices
for i in range(5):                    # 0, 1, 2, 3, 4
    print(f"Puerto 808{i}")           # Genera puertos 8080-8084

for i in range(1, 255):               # Útil para escanear IPs
    ip = f"192.168.1.{i}"             # Genera 192.168.1.1 hasta 192.168.1.254
    # ping(ip)

# ===== WHILE LOOP: Repetir mientras se cumpla condición =====
# Propósito: Reintentos, esperar que un servicio inicie, polling
intentos = 0
max_intentos = 5

while intentos < max_intentos:
    print(f"Intento {intentos + 1} de conexión...")
    # resultado = conectar_servicio()
    # if resultado: break  # Salir si conecta exitosamente
    intentos += 1

# ===== LIST COMPREHENSION: Crear listas de forma concisa =====
# Propósito: Transformar/filtrar datos en una línea - muy común en Python
numeros = [x*2 for x in range(5)]              # [0, 2, 4, 6, 8]
puertos_web = [8080 + i for i in range(10)]    # [8080, 8081, ..., 8089]
servidores_activos = [s for s in servidores if "web" in s]  # Filtrar solo "web"
```

## 4. Funciones

> **Definición**: Bloques de código reutilizables que realizan una tarea específica.
> 
> **Propósito**: Modularizar código, evitar repetición, crear herramientas reutilizables (conectar SSH, verificar disco, parsear logs).
> 
> **Casos de uso**: Crear librerías de funciones de administración, parametrizar operaciones comunes, facilitar testing y mantenimiento.

```python
# ===== DEFINICIÓN DE FUNCIÓN =====
# Sintaxis: def nombre_funcion(parametros):
def conectar_servidor(host, puerto=22):
    """
    Conectar a servidor SSH.
    
    Args:
        host (str): IP o hostname del servidor
        puerto (int): Puerto SSH (default: 22)
    
    Returns:
        bool: True si conecta exitosamente
    
    Propósito: Abstrae la conexión SSH para reutilizar en múltiples scripts
    """
    print(f"Conectando a {host}:{puerto}")
    # Aquí iría la lógica real de conexión
    return True

# ===== LLAMAR FUNCIONES =====
conectar_servidor("192.168.1.1")          # Usa puerto por defecto (22)
conectar_servidor("192.168.1.1", 2222)    # Puerto personalizado

# ===== FUNCIÓN PARA VERIFICAR ESPACIO EN DISCO =====
# Ejemplo práctico de automatización
def verificar_espacio_disco(ruta="/", umbral=90):
    """
    Verifica si el uso de disco supera un umbral.
    
    Propósito: Monitoreo preventivo de espacio en disco
    Uso: Llamar en cron jobs o scripts de healthcheck
    """
    import shutil
    stats = shutil.disk_usage(ruta)
    porcentaje_usado = (stats.used / stats.total) * 100
    
    if porcentaje_usado > umbral:
        return False, f"ALERTA: Disco {ruta} al {porcentaje_usado:.1f}%"
    else:
        return True, f"OK: Disco {ruta} al {porcentaje_usado:.1f}%"

# Uso
estado, mensaje = verificar_espacio_disco("/var/log", 85)
print(mensaje)
```

## 5. Módulos Útiles para Administración

> **Definición**: Librerías estándar de Python para interactuar con el sistema operativo, procesos, red y archivos.
> 
> **Propósito**: Estas librerías son fundamentales para cualquier script de automatización - permiten ejecutar comandos, manipular archivos, conectar por red, gestionar discos.

### os - Sistema Operativo

> **Definición**: Módulo para interactuar con funciones del sistema operativo.
> 
> **Propósito**: Ejecutar comandos, navegar filesystem, crear/eliminar directorios, manejar variables de entorno.
> 
> **Casos de uso**: Verificar existencia de archivos antes de operaciones, crear estructuras de directorios, acceder a configuraciones del sistema.

```python
import os

# ===== EJECUTAR COMANDOS DEL SISTEMA =====
# Propósito: Ejecutar comandos shell simples (mejor usar subprocess para comandos complejos)
os.system("whoami")              # Ejecuta comando y devuelve código de retorno
os.system("df -h")               # Verificar espacio en disco

# ===== VERIFICAR EXISTENCIA DE ARCHIVOS/DIRECTORIOS =====
# Propósito: Validar antes de leer/escribir archivos, evitar errores
archivo_existe = os.path.exists("/tmp/file.txt")       # True/False
es_directorio = os.path.isdir("/tmp")                  # True si es directorio
es_archivo = os.path.isfile("/etc/hosts")              # True si es archivo regular

# ===== CREAR/ELIMINAR DIRECTORIOS =====
# Propósito: Preparar estructuras para logs, backups, datos temporales
os.mkdir("/tmp/nuevo")                   # Crear un directorio
os.makedirs("/tmp/a/b/c", exist_ok=True) # Crear estructura completa (como mkdir -p)
os.rmdir("/tmp/nuevo")                   # Eliminar directorio vacío

# ===== VARIABLES DE ENTORNO =====
# Propósito: Acceder a configs del sistema, PATH, HOME, variables personalizadas
home = os.environ.get("HOME")            # Obtener variable (None si no existe)
path = os.environ["PATH"]                # Leer PATH del sistema
os.environ["MI_VAR"] = "valor"           # Definir variable para el proceso

# ===== RUTAS Y FILESYSTEM =====
# Propósito: Construir rutas de forma multiplataforma
ruta_completa = os.path.join("/var", "log", "app.log")  # /var/log/app.log
directorio = os.path.dirname("/var/log/app.log")        # /var/log
archivo = os.path.basename("/var/log/app.log")          # app.log
```

### subprocess - Ejecutar Procesos

> **Definición**: Módulo moderno para ejecutar comandos del sistema y capturar su salida.
> 
> **Propósito**: Reemplaza os.system() con mayor control - capturar stdout/stderr, verificar códigos de retorno, manejar timeouts, ejecutar pipes.
> 
> **Casos de uso**: Ejecutar comandos de sistema (df, netstat, systemctl), obtener información de red/discos, integrar herramientas CLI en scripts.

```python
import subprocess

# ===== EJECUTAR COMANDO Y CAPTURAR SALIDA =====
# Propósito: Obtener output del comando para procesarlo en Python
resultado = subprocess.run(
    ["ls", "-la"],                    # Lista de argumentos (más seguro que string)
    capture_output=True,              # Capturar stdout y stderr
    text=True                         # Decodificar output a string (no bytes)
)

print(resultado.stdout)               # Salida estándar del comando
print(resultado.stderr)               # Errores del comando
print(resultado.returncode)           # Código de retorno (0 = éxito)

# ===== VERIFICAR ESPACIO EN DISCO =====
# Ejemplo práctico: Parsear salida de df para monitorear discos
resultado = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
for linea in resultado.stdout.split('\n')[1:]:  # Saltar encabezado
    if linea:
        partes = linea.split()
        filesystem, size, used, available, percent, mount = partes
        print(f"Disco {mount}: {percent} usado ({used}/{size})")

# ===== VERIFICAR CONEXIONES DE RED =====
# Propósito: Listar puertos abiertos y conexiones activas
resultado = subprocess.run(
    ["ss", "-tuln"],                  # Sockets TCP/UDP listening y numeric
    capture_output=True,
    text=True
)
# Procesar salida para verificar qué puertos están escuchando
for linea in resultado.stdout.split('\n'):
    if "LISTEN" in linea and "8080" in linea:
        print(f"Puerto 8080 detectado: {linea}")

# ===== EJECUTAR CON SHELL (usar con precaución) =====
# Propósito: Permitir pipes, redirects, wildcards - pero menos seguro
resultado = subprocess.run(
    "ps aux | grep python",           # Comando con pipe
    shell=True,                       # Habilita sintaxis de shell
    capture_output=True,
    text=True
)
print(resultado.stdout)

# ===== TIMEOUT Y MANEJO DE ERRORES =====
# Propósito: Evitar comandos colgados, manejar fallos gracefully
try:
    resultado = subprocess.run(
        ["ping", "-c", "3", "8.8.8.8"],
        capture_output=True,
        timeout=10,                   # Máximo 10 segundos
        check=True                    # Lanza excepción si returncode != 0
    )
    print("Ping exitoso")
except subprocess.TimeoutExpired:
    print("Comando excedió timeout")
except subprocess.CalledProcessError as e:
    print(f"Comando falló con código {e.returncode}")

# ===== SUBPROCESS.POPEN: Control avanzado =====
# Propósito: Para procesos de larga duración, comunicación bidireccional
proceso = subprocess.Popen(
    ["tail", "-f", "/var/log/syslog"], # Comando que corre continuamente
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# proceso.wait()                     # Esperar a que termine
# proceso.terminate()                # Terminar proceso
# proceso.kill()                     # Matar proceso forzosamente
```

### socket - Redes 🌐

> **Definición**: Módulo para programación de red de bajo nivel - crear conexiones TCP/UDP, resolver DNS, verificar conectividad.
> 
> **Propósito**: Verificar disponibilidad de servicios, escaneo de puertos, obtener información de red, crear servers/clients simples.
> 
> **Casos de uso**: Healthchecks de puertos, verificación de servicios antes de despliegue, diagnóstico de red, obtener IPs de hosts.

```python
import socket

# ===== OBTENER INFORMACIÓN DEL HOST LOCAL =====
# Propósito: Conocer IP local, hostname - útil en scripts de configuración
hostname = socket.gethostname()        # Nombre del host local
ip_local = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"IP Local: {ip_local}")

# ===== RESOLVER DNS =====
# Propósito: Convertir hostname a IP, verificar resolución DNS
try:
    ip = socket.gethostbyname("google.com")
    print(f"google.com resuelve a: {ip}")
except socket.gaierror:
    print("No se pudo resolver el hostname")

# Resolución inversa (IP a hostname)
try:
    hostname = socket.gethostbyaddr("8.8.8.8")
    print(f"8.8.8.8 es: {hostname}")
except socket.herror:
    print("No se pudo resolver la IP")

# ===== VERIFICAR PUERTO ABIERTO (Port Scanning) =====
# Propósito: Healthcheck de servicios - verificar que puertos estén escuchando
def puerto_abierto(host, puerto, timeout=1):
    """
    Verifica si un puerto está abierto en un host.
    
    Args:
        host: IP o hostname (ej: "192.168.1.1", "google.com")
        puerto: Número de puerto (ej: 80, 443, 22, 8080)
        timeout: Segundos de espera antes de considerar cerrado
    
    Returns:
        bool: True si el puerto está abierto/accesible
    
    Casos de uso:
        - Verificar que web server esté escuchando en puerto 80/443
        - Confirmar que SSH esté disponible (puerto 22)
        - Validar que base de datos acepte conexiones (3306, 5432)
    """
    try:
        socket.create_connection((host, puerto), timeout=timeout)
        return True
    except (socket.timeout, socket.error):
        return False

# Ejemplos de uso en administración
print(f"Web: {puerto_abierto('google.com', 80)}")      # HTTP
print(f"HTTPS: {puerto_abierto('google.com', 443)}")   # HTTPS
print(f"SSH: {puerto_abierto('192.168.1.1', 22)}")     # SSH
print(f"MySQL: {puerto_abierto('localhost', 3306)}")   # MySQL
print(f"PostgreSQL: {puerto_abierto('localhost', 5432)}") # PostgreSQL

# ===== ESCANEAR MÚLTIPLES PUERTOS =====
# Propósito: Descubrir qué servicios están corriendo en un servidor
def escanear_puertos(host, puertos):
    """Escanea lista de puertos y devuelve los que están abiertos."""
    puertos_abiertos = []
    for puerto in puertos:
        if puerto_abierto(host, puerto, timeout=0.5):
            puertos_abiertos.append(puerto)
            print(f"✓ Puerto {puerto} ABIERTO")
        else:
            print(f"✗ Puerto {puerto} cerrado")
    return puertos_abiertos

# Puertos comunes para verificar
puertos_comunes = [22, 80, 443, 3306, 5432, 6379, 8080, 9090]
abiertos = escanear_puertos("localhost", puertos_comunes)

# ===== OBTENER IP DE INTERFACE ESPECÍFICA =====
# Propósito: En servidores con múltiples NICs, obtener IP específica
def obtener_ip_interface():
    """Obtiene la IP que usaría para conectar a internet."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No necesita conectar realmente - solo determinar ruta
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

ip_principal = obtener_ip_interface()
print(f"IP principal: {ip_principal}")

# ===== OBTENER INFORMACIÓN DETALLADA DEL SOCKET =====
# Propósito: Debugging de conexiones, conocer familia de direcciones
info = socket.getaddrinfo("google.com", 443, socket.AF_INET, socket.SOCK_STREAM)
for item in info:
    family, socktype, proto, canonname, sockaddr = item
    print(f"Familia: {family}, Tipo: {socktype}, Dirección: {sockaddr}")
```

### json - Trabajar con JSON

> **Definición**: Módulo para parsear (leer) y serializar (escribir) datos en formato JSON.
> 
> **Propósito**: JSON es el formato estándar para APIs, archivos de configuración, respuestas HTTP. Este módulo permite convertir entre Python (dicts/listas) y JSON (strings).
> 
> **Casos de uso**: Leer configs de aplicaciones, consumir APIs REST, guardar resultados de scripts, intercambiar datos con otros sistemas.

```python
import json

# ===== DATOS DE EJEMPLO: Configuración de servidor =====
datos = {
    "nombre": "servidor-web-01",
    "ip": "192.168.1.100",
    "puerto": 8080,
    "servicios": ["nginx", "mysql", "redis"],
    "recursos": {
        "cpu": "4 cores",
        "ram": "16GB",
        "disco": "500GB SSD"
    },
    "activo": True
}

# ===== SERIALIZAR: Python → JSON String =====
# Propósito: Convertir objetos Python a texto JSON para enviar/guardar
json_str = json.dumps(datos, indent=2)       # indent=2 hace el JSON legible
print(json_str)
# Resultado:
# {
#   "nombre": "servidor-web-01",
#   "ip": "192.168.1.100",
#   ...
# }

# Sin formato (compacto - útil para logs o transmisión)
json_compacto = json.dumps(datos)
print(json_compacto)  # {"nombre":"servidor-web-01","ip":"192.168.1.100",...}

# ===== PARSEAR: JSON String → Python =====
# Propósito: Convertir JSON recibido (de API o archivo) a objetos Python
datos_parseados = json.loads(json_str)
print(datos_parseados["nombre"])              # servidor-web-01
print(datos_parseados["servicios"][0])        # nginx
print(datos_parseados["recursos"]["ram"])     # 16GB

# ===== GUARDAR JSON EN ARCHIVO =====
# Propósito: Persistir configuraciones, resultados de inventarios, caches
with open("/tmp/config.json", "w") as f:
    json.dump(datos, f, indent=2)             # dump() escribe directo a archivo
    
# Guardar múltiples servidores (inventario)
inventario = [
    {"host": "web1", "ip": "192.168.1.10", "role": "web"},
    {"host": "db1", "ip": "192.168.1.20", "role": "database"},
    {"host": "cache1", "ip": "192.168.1.30", "role": "redis"}
]
with open("/tmp/inventario.json", "w") as f:
    json.dump(inventario, f, indent=2)

# ===== LEER JSON DESDE ARCHIVO =====
# Propósito: Cargar configuraciones, leer respuestas cacheadas
with open("/tmp/config.json", "r") as f:
    datos_cargados = json.load(f)            # load() lee desde archivo
    print(f"Servidor: {datos_cargados['nombre']}")
    print(f"IP: {datos_cargados['ip']}")

# ===== CASO PRÁCTICO: Procesar respuesta de API =====
# Simula respuesta de una API de monitoreo
respuesta_api = '''
{
    "status": "healthy",
    "servers": [
        {"name": "web1", "cpu": 45.2, "memory": 62.1, "disk": 78.5},
        {"name": "db1", "cpu": 72.8, "memory": 81.3, "disk": 92.7}
    ]
}
'''

# Parsear y procesar
data = json.loads(respuesta_api)
print(f"Estado general: {data['status']}")

# Verificar umbrales de alerta
for server in data['servers']:
    nombre = server['name']
    disco = server['disk']
    if disco > 90:
        print(f"⚠️  ALERTA: {nombre} con disco al {disco}%")
    else:
        print(f"✓ {nombre} OK - disco al {disco}%")

# ===== MANEJAR ERRORES DE JSON =====
# Propósito: JSON mal formado puede causar crashes - siempre validar
json_invalido = '{"nombre": "servidor", "ip": "192.168.1.1"'  # Falta }

try:
    datos = json.loads(json_invalido)
except json.JSONDecodeError as e:
    print(f"Error parseando JSON: {e}")
    print(f"Posición del error: línea {e.lineno}, columna {e.colno}")
```

## 6. Manejo de Archivos 📁

> **Definición**: Operaciones de lectura y escritura de archivos - fundamental para procesar logs, configs, datos.
> 
> **Propósito**: Leer archivos de configuración del sistema (/etc/hosts, /etc/fstab), procesar logs (/var/log/*), escribir reportes, crear backups de configs.
> 
> **Casos de uso**: Parsear logs de aplicaciones, modificar configs automaticamente, generar reportes de auditoría, procesar salidas de comandos guardadas.

```python
# ===== LEER ARCHIVO COMPLETO =====
# Propósito: Cargar archivo pequeño completamente en memoria
# Ejemplo: Leer /etc/hosts para verificar entradas
with open("/etc/hosts", "r") as f:
    contenido = f.read()              # Lee todo el archivo como string
    print(contenido)

# ===== LEER LÍNEA POR LÍNEA =====
# Propósito: Procesar archivos grandes (logs) sin cargar todo en memoria
# Ejemplo: Parsear /etc/fstab (información de montajes de disco)
with open("/etc/fstab", "r") as f:
    for linea in f:
        linea = linea.strip()         # Quitar \n y espacios
        if linea and not linea.startswith("#"):  # Ignorar vacías y comentarios
            campos = linea.split()
            if len(campos) >= 6:
                dispositivo, punto_montaje, tipo_fs, opciones, dump, pase = campos
                print(f"Disco: {dispositivo} → {punto_montaje} (tipo: {tipo_fs})")

# ===== LEER COMO LISTA DE LÍNEAS =====
# Propósito: Cuando necesitas procesar líneas múltiples veces
with open("/etc/hosts", "r") as f:
    lineas = f.readlines()            # Lista donde cada elemento es una línea
    for linea in lineas:
        if "localhost" in linea:
            print(f"Encontrado: {linea.strip()}")

# ===== ESCRIBIR ARCHIVO (SOBRESCRIBE) =====
# Propósito: Crear archivo nuevo o reemplazar contenido existente
# Ejemplo: Guardar reporte de verificación de discos
with open("/tmp/disk_report.txt", "w") as f:
    f.write("=== Reporte de Discos ===\n")
    f.write("Fecha: 2026-01-22\n")
    f.write("Filesystem: /dev/sda1\n")
    f.write("Uso: 78%\n")

# Escribir múltiples líneas de una vez
lineas_reporte = [
    "=== Health Check ===\n",
    "CPU: 45%\n",
    "RAM: 62%\n",
    "Disco: 78%\n"
]
with open("/tmp/healthcheck.txt", "w") as f:
    f.writelines(lineas_reporte)

# ===== APPEND (AÑADIR AL FINAL) =====
# Propósito: Agregar a archivo existente sin borrar contenido (ideal para logs)
# Ejemplo: Log personalizado de eventos
with open("/tmp/eventos.log", "a") as f:
    f.write("2026-01-22 10:30:15 - Backup completado\n")
    f.write("2026-01-22 10:31:20 - Servicio reiniciado\n")

# ===== CASO PRÁCTICO: Analizar logs de red =====
# Propósito: Encontrar errores de conexión en logs
def analizar_log_red(archivo_log):
    """
    Busca problemas de red en logs.
    
    Busca patrones como: connection refused, timeout, network unreachable
    """
    errores = []
    with open(archivo_log, "r") as f:
        for numero_linea, linea in enumerate(f, 1):
            linea_lower = linea.lower()
            if any(error in linea_lower for error in 
                   ["connection refused", "timeout", "network unreachable", "host down"]):
                errores.append((numero_linea, linea.strip()))
    
    return errores

# Uso
# errores = analizar_log_red("/var/log/app.log")
# for num, linea in errores:
#     print(f"Línea {num}: {linea}")

# ===== CASO PRÁCTICO: Procesar archivo de discos =====
# Propósito: Leer salida de 'df' guardada y encontrar discos llenos
def encontrar_discos_llenos(archivo_df, umbral=80):
    """
    Procesa salida de 'df -h' guardada en archivo.
    
    Ejemplo de línea:
    /dev/sda1       100G   78G   22G  78% /
    """
    discos_llenos = []
    with open(archivo_df, "r") as f:
        for linea in f:
            if linea.startswith("Filesystem"):  # Saltar header
                continue
            campos = linea.split()
            if len(campos) >= 6:
                filesystem = campos[0]
                size = campos[1]
                usado = campos[2]
                disponible = campos[3]
                porcentaje_str = campos[4]      # "78%"
                punto_montaje = campos[5]
                
                # Extraer número del porcentaje
                if porcentaje_str.endswith("%"):
                    porcentaje = int(porcentaje_str[:-1])
                    if porcentaje >= umbral:
                        discos_llenos.append({
                            "filesystem": filesystem,
                            "montaje": punto_montaje,
                            "uso": porcentaje,
                            "usado": usado,
                            "total": size
                        })
    return discos_llenos

# ===== LEER Y ESCRIBIR BINARIOS =====
# Propósito: Para archivos no texto (imágenes, ejecutables, dumps)
with open("/tmp/archivo.bin", "rb") as f:  # 'rb' = read binary
    datos_binarios = f.read()

with open("/tmp/copia.bin", "wb") as f:    # 'wb' = write binary
    f.write(datos_binarios)
```

## 7. Librerías de Automatización - Paramiko 🔐

> **Definición**: Librería de Python para SSH y SFTP - permite conectar remotamente a servidores y ejecutar comandos.
> 
> **Propósito**: Automatizar tareas en múltiples servidores remotos sin necesidad de shell scripts - ejecutar comandos, transferir archivos, gestionar configs.
> 
> **Instalación**: `pip install paramiko`
> 
> **Casos de uso**: Despliegues automatizados, recolección de información de múltiples servidores, backups remotos, ejecución de comandos en paralelo.

### SSH Remoto con Paramiko

```python
import paramiko

# ===== CONEXIÓN SSH BÁSICA CON PASSWORD =====
# Propósito: Conectar a servidor remoto para ejecutar comandos
ssh = paramiko.SSHClient()

# Aceptar automáticamente host keys (PRECAUCIÓN: solo en entornos confiables)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Conectar al servidor
ssh.connect(
    hostname="192.168.1.100",        # IP o hostname del servidor
    port=22,                          # Puerto SSH (default 22)
    username="admin",                 # Usuario remoto
    password="password123"            # Password (mejor usar keys)
)

# ===== EJECUTAR COMANDO REMOTO =====
# Propósito: Ejecutar cualquier comando como si estuvieras en terminal SSH
stdin, stdout, stderr = ssh.exec_command("uptime")

# Leer resultados
salida = stdout.read().decode()      # Salida estándar
errores = stderr.read().decode()     # Errores (si hay)
codigo_retorno = stdout.channel.recv_exit_status()

print(f"Salida: {salida}")
print(f"Código de retorno: {codigo_retorno}")

# ===== MÚLTIPLES COMANDOS =====
# Propósito: Recolectar información del sistema remoto
comandos = [
    "hostname",                       # Nombre del servidor
    "df -h | grep '^/dev'",          # Uso de discos
    "free -h",                        # Memoria disponible
    "ss -tuln | grep LISTEN"         # Puertos escuchando
]

for cmd in comandos:
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(f"\n=== {cmd} ===")
    print(stdout.read().decode())

# ===== TRANSFERIR ARCHIVOS CON SFTP =====
# Propósito: Copiar archivos hacia/desde servidor remoto
sftp = ssh.open_sftp()

# UPLOAD: Local → Remoto (subir archivo)
# Ejemplo: Subir script de backup al servidor
sftp.put("/home/admin/backup.sh", "/opt/scripts/backup.sh")
print("Archivo subido: backup.sh")

# DOWNLOAD: Remoto → Local (descargar archivo)
# Ejemplo: Traer logs del servidor remoto
sftp.get("/var/log/app.log", "/tmp/app.log")
print("Archivo descargado: app.log")

# Listar archivos remotos
archivos = sftp.listdir("/var/log")
for archivo in archivos:
    print(f"Archivo remoto: {archivo}")

sftp.close()
ssh.close()

# ===== CASO PRÁCTICO: Verificar discos en múltiples servidores =====
def verificar_discos_remotos(servidores):
    """
    Conecta a múltiples servidores y verifica uso de disco.
    
    Args:
        servidores: Lista de dicts con {host, user, password}
    
    Returns:
        Dict con resultados por servidor
    """
    resultados = {}
    
    for srv in servidores:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(srv['host'], username=srv['user'], password=srv['password'])
            
            # Ejecutar df para obtener uso de discos
            stdin, stdout, stderr = ssh.exec_command("df -h | grep '^/dev' | awk '{print $5,$6}'")
            salida = stdout.read().decode()
            
            discos = []
            for linea in salida.strip().split('\n'):
                if linea:
                    uso, montaje = linea.split()
                    uso_num = int(uso.replace('%', ''))
                    discos.append({
                        'montaje': montaje,
                        'uso': uso_num,
                        'alerta': uso_num > 80
                    })
            
            resultados[srv['host']] = {
                'estado': 'ok',
                'discos': discos
            }
            
            ssh.close()
            
        except Exception as e:
            resultados[srv['host']] = {
                'estado': 'error',
                'mensaje': str(e)
            }
    
    return resultados

# Uso
# servidores = [
#     {'host': '192.168.1.10', 'user': 'admin', 'password': 'pass1'},
#     {'host': '192.168.1.11', 'user': 'admin', 'password': 'pass2'}
# ]
# resultados = verificar_discos_remotos(servidores)
```

### SSH con Clave Privada (Recomendado) 🔑

> **Definición**: Autenticación SSH usando par de claves pública/privada en lugar de password.
> 
> **Propósito**: Método más seguro y automatizable - no expone passwords en código, permite autenticación sin interacción.
> 
> **Cuándo usar**: Producción, scripts automatizados en cron, CI/CD pipelines, cuando se gestionan múltiples servidores.

```python
import paramiko

# ===== CONECTAR CON CLAVE SSH PRIVADA =====
# Propósito: Autenticación segura sin passwords en el código
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Usar clave privada SSH (igual que ssh -i)
ssh.connect(
    hostname="192.168.1.100",
    port=22,
    username="admin",
    key_filename="/home/user/.ssh/id_rsa"    # Ruta a tu private key
)

# Ejecutar comando
stdin, stdout, stderr = ssh.exec_command("df -h")
print(stdout.read().decode())

ssh.close()

# ===== CON CLAVE PRIVADA PROTEGIDA POR PASSPHRASE =====
# Propósito: Si tu clave SSH tiene passphrase (password adicional)
from paramiko import RSAKey

# Cargar clave con passphrase
private_key = RSAKey.from_private_key_file(
    "/home/user/.ssh/id_rsa",
    password="mi_passphrase_secreta"
)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname="192.168.1.100",
    username="admin",
    pkey=private_key                          # Usar objeto de clave
)

# ===== CASO PRÁCTICO: Backup de configs remotas =====
def backup_configs_remotas(servidores, destino_local):
    """
    Descarga archivos de configuración de múltiples servidores.
    
    Args:
        servidores: Lista con [{host, user, key_file, configs_remotas}]
        destino_local: Directorio donde guardar backups
    
    Ejemplo de configs_remotas: ['/etc/nginx/nginx.conf', '/etc/hosts']
    """
    import os
    from datetime import datetime
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for srv in servidores:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                hostname=srv['host'],
                username=srv['user'],
                key_filename=srv['key_file']
            )
            
            sftp = ssh.open_sftp()
            
            # Crear directorio por servidor
            dir_servidor = os.path.join(destino_local, f"{srv['host']}_{timestamp}")
            os.makedirs(dir_servidor, exist_ok=True)
            
            # Descargar cada config
            for config_remota in srv['configs_remotas']:
                nombre_archivo = config_remota.replace("/", "_")
                ruta_local = os.path.join(dir_servidor, nombre_archivo)
                
                try:
                    sftp.get(config_remota, ruta_local)
                    print(f"✓ Backup {srv['host']}: {config_remota}")
                except Exception as e:
                    print(f"✗ Error en {srv['host']}: {config_remota} - {e}")
            
            sftp.close()
            ssh.close()
            
        except Exception as e:
            print(f"✗ Error conectando a {srv['host']}: {e}")

# Uso
# servidores = [
#     {
#         'host': '192.168.1.10',
#         'user': 'admin',
#         'key_file': '/home/user/.ssh/id_rsa',
#         'configs_remotas': ['/etc/nginx/nginx.conf', '/etc/hosts', '/etc/fstab']
#     }
# ]
# backup_configs_remotas(servidores, '/backup/configs')
```

## 8. Librerías de Automatización - Fabric

> **Definición**: Librería de alto nivel construida sobre Paramiko - simplifica ejecución de comandos remotos y despliegues.
> 
> **Propósito**: Automatizar tareas en múltiples servidores con sintaxis más simple que Paramiko crudo - ideal para deployments, configuración masiva.
> 
> **Instalación**: `pip install fabric`
> 
> **Ventaja sobre Paramiko**: Menos código, manejo automático de conexiones, soporte para tareas decoradas, ejecución en paralelo.

### Fabric para Tareas Remotas

```python
from fabric import Connection, task

# ===== CONEXIÓN SIMPLE =====
# Propósito: Ejecutar comandos remotos con sintaxis limpia
c = Connection(
    host="192.168.1.100",
    user="admin",
    connect_kwargs={
        "key_filename": "/home/user/.ssh/id_rsa"
    }
)

# Ejecutar comando - más simple que Paramiko
resultado = c.run("uptime", hide=False)      # hide=False muestra output
print(f"Código de retorno: {resultado.return_code}")
print(f"Salida: {resultado.stdout}")

# ===== TAREAS CON DECORADOR @task =====
# Propósito: Definir tareas reutilizables que pueden llamarse desde CLI
@task
def verificar_disco(c):
    """
    Verifica uso de disco en servidor remoto.
    
    Uso desde terminal: fab -H servidor.com verificar-disco
    """
    resultado = c.run("df -h | grep '^/dev'", hide=False)
    
    for linea in resultado.stdout.strip().split('\n'):
        campos = linea.split()
        if len(campos) >= 5:
            filesystem = campos[0]
            uso = campos[4]
            montaje = campos[5]
            
            uso_num = int(uso.replace('%', ''))
            if uso_num > 80:
                print(f"⚠️  ALERTA: {montaje} al {uso}% en {filesystem}")

@task
def deploy(c):
    """
    Despliega aplicación en servidor remoto.
    
    Uso: fab -H servidor.com deploy
    """
    # Actualizar código desde Git
    c.run("cd /app && git pull origin main")
    
    # Instalar dependencias
    c.run("cd /app && pip install -r requirements.txt")
    
    # Reiniciar servicio
    c.sudo("systemctl restart myapp")         # .sudo() ejecuta con sudo
    
    print("✓ Despliegue completado")

@task
def healthcheck(c):
    """
    Verifica salud del servidor (CPU, RAM, Disco, Servicios).
    
    Uso: fab -H servidor1,servidor2 healthcheck
    """
    print(f"\n{'='*50}")
    print(f"Health Check - {c.host}")
    print(f"{'='*50}")
    
    # CPU Load
    resultado = c.run("uptime | awk -F'load average:' '{print $2}'", hide=True)
    print(f"CPU Load: {resultado.stdout.strip()}")
    
    # Memoria
    resultado = c.run("free -h | grep Mem | awk '{print $3\"/\"$2}'", hide=True)
    print(f"Memoria usada: {resultado.stdout.strip()}")
    
    # Disco
    resultado = c.run("df -h / | tail -1 | awk '{print $5}'", hide=True)
    print(f"Disco raíz usado: {resultado.stdout.strip()}")
    
    # Servicios críticos
    servicios = ["nginx", "mysql", "redis"]
    for servicio in servicios:
        resultado = c.run(f"systemctl is-active {servicio}", warn=True, hide=True)
        estado = "✓ Activo" if resultado.return_code == 0 else "✗ Inactivo"
        print(f"{servicio}: {estado}")

# ===== EJECUTAR EN MÚLTIPLES SERVIDORES =====
# Propósito: Automatización masiva - ejecutar en todo un cluster
from fabric import SerialGroup, ThreadingGroup

def desplegar_cluster(servidores):
    """
    Despliega en múltiples servidores en paralelo.
    
    Args:
        servidores: Lista de hostnames/IPs ['web1.com', 'web2.com']
    """
    # ThreadingGroup ejecuta en paralelo
    grupo = ThreadingGroup(
        *servidores,
        user="admin",
        connect_kwargs={"key_filename": "/home/user/.ssh/id_rsa"}
    )
    
    # Ejecutar comando en todos los servidores simultáneamente
    resultados = grupo.run("cd /app && git pull")
    
    for conexion, resultado in resultados.items():
        print(f"{conexion.host}: código {resultado.return_code}")

# ===== TRANSFERIR ARCHIVOS =====
# Propósito: Copiar configs, scripts, binarios a servidores remotos
@task
def subir_config(c):
    """Sube archivo de configuración al servidor."""
    # Upload
    c.put("/local/nginx.conf", "/tmp/nginx.conf")
    c.sudo("mv /tmp/nginx.conf /etc/nginx/nginx.conf")
    c.sudo("systemctl reload nginx")
    print("✓ Configuración actualizada")

# ===== CASO PRÁCTICO: Actualizar /etc/hosts en múltiples servidores =====
@task
def actualizar_hosts(c, nueva_entrada):
    """
    Agrega entrada a /etc/hosts en servidor remoto.
    
    Uso: fab -H servidor1,servidor2 actualizar-hosts --nueva-entrada="192.168.1.50 newserver.local"
    """
    # Verificar si entrada ya existe
    resultado = c.run(f"grep '{nueva_entrada}' /etc/hosts", warn=True, hide=True)
    
    if resultado.return_code != 0:  # No existe
        c.sudo(f"echo '{nueva_entrada}' >> /etc/hosts")
        print(f"✓ Entrada agregada a /etc/hosts en {c.host}")
    else:
        print(f"⚠️  Entrada ya existe en {c.host}")

# ===== GUARDAR EN fabfile.py =====
# Para usar estas tareas desde línea de comandos:
# 1. Guarda este código en un archivo llamado "fabfile.py"
# 2. Ejecuta: fab -H servidor.com nombre-de-tarea
# 3. Para múltiples hosts: fab -H servidor1,servidor2,servidor3 healthcheck
```

## 9. Excepciones y Manejo de Errores ⚠️

> **Definición**: Mecanismo para capturar y manejar errores sin que el script se caiga completamente.
> 
> **Propósito**: Scripts robustos que no se rompen ante errores - manejar fallos de red, archivos no encontrados, comandos que fallan, timeouts.
> 
> **Casos de uso**: Scripts de producción que deben seguir corriendo aunque un servidor no responda, retry logic, logging de errores, rollback de operaciones.

```python
import subprocess
import time

# ===== ESTRUCTURA TRY/EXCEPT BÁSICA =====
# Propósito: Capturar errores específicos y continuar ejecución
try:
    resultado = subprocess.run(
        ["ping", "-c", "1", "servidor-inexistente.local"],
        capture_output=True,
        timeout=5,
        check=True                               # Lanza excepción si falla
    )
    print("✓ Ping exitoso")
    
except subprocess.TimeoutExpired:
    # Error específico: comando tardó mucho
    print("✗ Timeout: Servidor no responde en tiempo esperado")
    
except subprocess.CalledProcessError as e:
    # Error específico: comando falló (returncode != 0)
    print(f"✗ Comando falló con código {e.returncode}")
    print(f"Error: {e.stderr}")
    
except FileNotFoundError:
    # Error específico: comando 'ping' no encontrado
    print("✗ Comando 'ping' no existe en el sistema")
    
except Exception as e:
    # Catch-all para errores no anticipados
    print(f"✗ Error inesperado: {type(e).__name__}: {e}")
    
else:
    # Se ejecuta SOLO si no hubo ninguna excepción
    print("✓ Todo ejecutado exitosamente")
    
finally:
    # Se ejecuta SIEMPRE, haya o no error - para limpieza
    print("→ Limpiando recursos temporales...")

# ===== CASO PRÁCTICO: Verificar múltiples servidores con retry =====
def verificar_servidor_con_retry(host, puerto, max_intentos=3):
    """
    Intenta conectar a servidor, reintentando si falla.
    
    Propósito: Manejar fallos transitorios de red
    """
    import socket
    
    for intento in range(1, max_intentos + 1):
        try:
            print(f"Intento {intento}/{max_intentos} - Conectando a {host}:{puerto}")
            socket.create_connection((host, puerto), timeout=2)
            print(f"✓ {host}:{puerto} está accesible")
            return True
            
        except socket.timeout:
            print(f"✗ Timeout en {host}:{puerto}")
            if intento < max_intentos:
                print(f"  Reintentando en 2 segundos...")
                time.sleep(2)
                
        except socket.error as e:
            print(f"✗ Error de conexión: {e}")
            if intento < max_intentos:
                time.sleep(2)
                
        except Exception as e:
            print(f"✗ Error inesperado: {e}")
            break
    
    print(f"✗ Fallo después de {max_intentos} intentos")
    return False

# ===== CASO PRÁCTICO: Operación con rollback en disco =====
def operacion_disco_segura(archivo_config):
    """
    Modifica archivo de configuración con backup automático.
    
    Propósito: Si algo falla, restaurar estado anterior
    """
    import shutil
    
    backup = f"{archivo_config}.backup"
    
    try:
        # 1. Hacer backup
        shutil.copy2(archivo_config, backup)
        print(f"✓ Backup creado: {backup}")
        
        # 2. Modificar archivo (operación riesgosa)
        with open(archivo_config, "a") as f:
            f.write("\n# Nueva configuración\n")
            f.write("max_connections = 1000\n")
        
        # 3. Validar la configuración (ejemplo: parsear)
        with open(archivo_config, "r") as f:
            contenido = f.read()
            if "max_connections" not in contenido:
                raise ValueError("Configuración no se aplicó correctamente")
        
        print("✓ Configuración actualizada exitosamente")
        
    except IOError as e:
        print(f"✗ Error de I/O: {e}")
        print(f"→ Restaurando backup...")
        shutil.copy2(backup, archivo_config)
        
    except ValueError as e:
        print(f"✗ Validación falló: {e}")
        print(f"→ Restaurando backup...")
        shutil.copy2(backup, archivo_config)
        
    except Exception as e:
        print(f"✗ Error inesperado: {e}")
        print(f"→ Restaurando backup...")
        shutil.copy2(backup, archivo_config)
        
    finally:
        # Limpiar backup si todo salió bien
        import os
        if os.path.exists(backup):
            # Opcionalmente eliminar backup o dejarlo como respaldo
            pass

# ===== LOGGING DE ERRORES =====
# Propósito: Registrar errores para debugging posterior
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/mi_script.log'),
        logging.StreamHandler()                    # También a consola
    ]
)

def operacion_con_logging():
    """Ejemplo de operación que logguea errores."""
    try:
        resultado = subprocess.run(["df", "-h"], capture_output=True, check=True, text=True)
        logging.info("✓ Comando df ejecutado exitosamente")
        return resultado.stdout
        
    except subprocess.CalledProcessError as e:
        logging.error(f"✗ Error ejecutando df: {e}")
        logging.error(f"  stderr: {e.stderr}")
        return None
        
    except Exception as e:
        logging.exception(f"✗ Error inesperado: {e}")  # .exception() incluye traceback
        return None

# ===== EXCEPCIONES PERSONALIZADAS =====
# Propósito: Crear tus propios tipos de error para casos específicos
class DiscoLlenoError(Exception):
    """Se lanza cuando un disco supera umbral de uso."""
    pass

class ServicioInactivoError(Exception):
    """Se lanza cuando un servicio crítico no está corriendo."""
    pass

def verificar_sistema():
    """Verifica estado del sistema y lanza excepciones personalizadas."""
    import shutil
    
    # Verificar disco
    stats = shutil.disk_usage("/")
    porcentaje_usado = (stats.used / stats.total) * 100
    
    if porcentaje_usado > 90:
        raise DiscoLlenoError(f"Disco raíz al {porcentaje_usado:.1f}% - crítico")
    
    # Verificar servicio
    resultado = subprocess.run(
        ["systemctl", "is-active", "nginx"],
        capture_output=True
    )
    
    if resultado.returncode != 0:
        raise ServicioInactivoError("nginx no está activo")
    
    return True

# Uso
try:
    verificar_sistema()
    print("✓ Sistema OK")
except DiscoLlenoError as e:
    logging.critical(f"CRÍTICO: {e}")
    # Aquí ejecutar limpieza de disco, enviar alerta, etc.
except ServicioInactivoError as e:
    logging.error(f"ERROR: {e}")
    # Aquí intentar reiniciar servicio
```

## 10. Script Práctico - Monitor de Servidores 🖥️

> **Propósito del Script**: Ejemplo completo y funcional que combina todos los conceptos - verifica múltiples servidores (red), guarda resultados en JSON, maneja errores.
> 
> **Qué hace**: Verifica disponibilidad de servidores mediante ping, detecta servicios caídos, genera timestamps, guarda log JSON para posterior análisis.
> 
> **Casos de uso**: Monitoring básico, healthchecks en cron jobs, verificación pre-despliegue, alertas de disponibilidad.

```python
#!/usr/bin/env python3
"""
Monitor de Servidores - Script de Healthcheck

Descripción:
    Verifica conectividad a múltiples servidores mediante ping.
    Genera reporte con timestamps y guarda resultados en JSON.

Uso:
    ./monitor_servidores.py
    
Salida:
    - Imprime estado de cada servidor en consola
    - Guarda resultados en monitor_results.json para análisis posterior
    
Requiere:
    - Python 3.6+
    - Permisos para ejecutar ping (sudo en algunos sistemas)
"""

import subprocess
import json
from datetime import datetime
import sys

def check_servidor(host, timeout=2):
    """
    Verifica estado de servidor mediante ping.
    
    Args:
        host (str): IP o hostname del servidor (ej: "8.8.8.8", "google.com")
        timeout (int): Segundos máximos de espera para respuesta
    
    Returns:
        dict: {
            'host': str,              # Host verificado
            'activo': bool,           # True si responde al ping
            'timestamp': str,         # Momento de la verificación (ISO format)
            'latencia_ms': float,     # Latencia en milisegundos (si activo)
            'error': str              # Mensaje de error (si falló)
        }
    
    Propósito:
        Función reutilizable para verificar disponibilidad de red.
        Útil para pre-checks antes de operaciones remotas.
    """
    try:
        # Ejecutar ping (-c 1 = 1 paquete, -W timeout en segundos)
        resultado = subprocess.run(
            ["ping", "-c", "1", "-W", str(timeout), host],
            capture_output=True,
            text=True,
            timeout=timeout + 1      # Timeout del proceso Python
        )
        
        # Parsear latencia de la salida del ping
        latencia = None
        if resultado.returncode == 0:
            # Buscar línea con "time=XX.X ms"
            for linea in resultado.stdout.split('\n'):
                if 'time=' in linea:
                    # Extraer valor de latencia
                    import re
                    match = re.search(r'time=([\d.]+)', linea)
                    if match:
                        latencia = float(match.group(1))
                    break
        
        return {
            "host": host,
            "activo": resultado.returncode == 0,
            "timestamp": datetime.now().isoformat(),
            "latencia_ms": latencia,
            "codigo_retorno": resultado.returncode
        }
        
    except subprocess.TimeoutExpired:
        return {
            "host": host,
            "activo": False,
            "timestamp": datetime.now().isoformat(),
            "error": f"Timeout después de {timeout} segundos"
        }
        
    except FileNotFoundError:
        return {
            "host": host,
            "activo": False,
            "timestamp": datetime.now().isoformat(),
            "error": "Comando 'ping' no encontrado en el sistema"
        }
        
    except Exception as e:
        return {
            "host": host,
            "activo": False,
            "timestamp": datetime.now().isoformat(),
            "error": f"{type(e).__name__}: {str(e)}"
        }

def generar_reporte(resultados):
    """
    Genera reporte legible de los resultados.
    
    Propósito: Mostrar resumen visual de estado de servidores.
    """
    print("\n" + "="*60)
    print("REPORTE DE MONITOREO DE SERVIDORES")
    print("="*60)
    print(f"Fecha/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total servidores verificados: {len(resultados)}")
    
    activos = sum(1 for r in resultados if r['activo'])
    inactivos = len(resultados) - activos
    
    print(f"✓ Activos: {activos}")
    print(f"✗ Inactivos: {inactivos}")
    print("-"*60)
    
    for resultado in resultados:
        host = resultado['host']
        if resultado['activo']:
            latencia = resultado.get('latencia_ms', 'N/A')
            print(f"✓ {host:<30} ACTIVO  (latencia: {latencia}ms)")
        else:
            error = resultado.get('error', 'No responde al ping')
            print(f"✗ {host:<30} INACTIVO ({error})")
    
    print("="*60 + "\n")

def main():
    """
    Función principal del script.
    
    Propósito: Orquestar verificación de múltiples servidores.
    """
    # ===== CONFIGURACIÓN =====
    # Lista de servidores a verificar (agregar los tuyos aquí)
    servidores = [
        "8.8.8.8",              # Google DNS
        "1.1.1.1",              # Cloudflare DNS
        "192.168.1.1",          # Gateway típico (reemplazar con tu red)
        "google.com",           # Test de resolución DNS + conectividad
        "github.com",           # Test de acceso a internet
        "servidor-inexistente-test.local"  # Test de servidor caído
    ]
    
    # Archivo de salida para resultados JSON
    archivo_salida = "monitor_results.json"
    
    print("🔍 Iniciando verificación de servidores...")
    print(f"   Servidores a verificar: {len(servidores)}")
    print()
    
    # ===== VERIFICACIÓN =====
    resultados = []
    
    for i, servidor in enumerate(servidores, 1):
        print(f"[{i}/{len(servidores)}] Verificando {servidor}...", end=" ")
        estado = check_servidor(servidor, timeout=2)
        resultados.append(estado)
        
        # Feedback inmediato
        if estado['activo']:
            latencia = estado.get('latencia_ms', 'N/A')
            print(f"✓ ACTIVO ({latencia}ms)")
        else:
            print(f"✗ INACTIVO")
    
    # ===== GENERAR REPORTE =====
    generar_reporte(resultados)
    
    # ===== GUARDAR RESULTADOS EN JSON =====
    try:
        with open(archivo_salida, "w") as f:
            json.dump({
                "fecha_verificacion": datetime.now().isoformat(),
                "total_servidores": len(servidores),
                "servidores_activos": sum(1 for r in resultados if r['activo']),
                "servidores_inactivos": sum(1 for r in resultados if not r['activo']),
                "resultados": resultados
            }, f, indent=2)
        
        print(f"✓ Resultados guardados en: {archivo_salida}")
        
    except Exception as e:
        print(f"✗ Error guardando resultados: {e}", file=sys.stderr)
        return 1
    
    # ===== CÓDIGO DE SALIDA =====
    # Retornar código de error si hay servidores inactivos (útil en scripts)
    servidores_inactivos = sum(1 for r in resultados if not r['activo'])
    
    if servidores_inactivos > 0:
        print(f"⚠️  Advertencia: {servidores_inactivos} servidor(es) inactivo(s)")
        return 1  # Código de error
    else:
        print("✓ Todos los servidores están activos")
        return 0  # Éxito

# ===== PUNTO DE ENTRADA =====
if __name__ == "__main__":
    sys.exit(main())

"""
EXTENSIONES POSIBLES:

1. Agregar verificación de puertos específicos:
   - Usar socket.create_connection() para verificar HTTP/HTTPS/SSH
   
2. Enviar alertas:
   - Integrar con email (smtplib) o Slack cuando servidor caiga
   
3. Verificar múltiples veces:
   - Hacer 3 pings antes de declarar servidor caído (evitar falsos positivos)
   
4. Verificar servicios específicos:
   - SSH (puerto 22), HTTP (80), HTTPS (443), MySQL (3306)
   
5. Agregar verificación de disco remoto:
   - Usar Paramiko para ejecutar 'df -h' en servidores SSH

6. Historico de estados:
   - Guardar cada ejecución con timestamp para analizar tendencias
   
7. Dashboard simple:
   - Generar HTML con estado visual de servidores
"""
```

---

## 📚 Módulos Adicionales Útiles

### shutil - Operaciones de Alto Nivel con Archivos y Discos

> **Definición**: Módulo para operaciones de filesystem de alto nivel - copiar, mover, eliminar archivos/directorios, obtener info de discos.
> 
> **Propósito**: Complementa `os` con operaciones más complejas - gestión de discos, backups de archivos, operaciones recursivas.

```python
import shutil

# ===== INFORMACIÓN DE DISCO =====
# Propósito: Obtener estadísticas de uso de disco (más fácil que parsear df)
stats = shutil.disk_usage("/")
print(f"Total: {stats.total / (1024**3):.1f} GB")      # Total en GB
print(f"Usado: {stats.used / (1024**3):.1f} GB")       # Usado en GB
print(f"Libre: {stats.free / (1024**3):.1f} GB")       # Libre en GB

porcentaje = (stats.used / stats.total) * 100
print(f"Uso: {porcentaje:.1f}%")

# ===== COPIAR ARCHIVOS =====
# Propósito: Backups, distribución de configs
shutil.copy2("/etc/nginx/nginx.conf", "/backup/nginx.conf.bak")  # Preserva metadata
shutil.copy("/source/file.txt", "/dest/")                         # Copia simple

# ===== COPIAR DIRECTORIOS COMPLETOS =====
# Propósito: Backup de directorios enteros
shutil.copytree("/var/www/html", "/backup/html_backup")           # Copia recursiva

# ===== MOVER/RENOMBRAR =====
shutil.move("/tmp/old.txt", "/tmp/new.txt")                       # Mover o renombrar

# ===== ELIMINAR DIRECTORIOS =====
shutil.rmtree("/tmp/directorio_temporal")                         # Elimina dir y contenido
```

### psutil - Información de Sistema y Procesos

> **Definición**: Librería multiplataforma para obtener información del sistema - CPU, RAM, discos, red, procesos.
> 
> **Propósito**: Monitoreo de recursos, identificar procesos problemáticos, obtener métricas de sistema.
> 
> **Instalación**: `pip install psutil`

```python
import psutil

# ===== CPU =====
cpu_percent = psutil.cpu_percent(interval=1)         # % uso CPU (1 seg)
print(f"CPU: {cpu_percent}%")

cpu_count = psutil.cpu_count()                       # Cantidad de cores
print(f"CPUs: {cpu_count}")

# ===== MEMORIA =====
mem = psutil.virtual_memory()
print(f"RAM Total: {mem.total / (1024**3):.1f} GB")
print(f"RAM Usada: {mem.used / (1024**3):.1f} GB ({mem.percent}%)")
print(f"RAM Disponible: {mem.available / (1024**3):.1f} GB")

# ===== DISCO =====
# Listar todas las particiones
for particion in psutil.disk_partitions():
    print(f"\nPartición: {particion.device}")
    print(f"  Punto de montaje: {particion.mountpoint}")
    print(f"  Filesystem: {particion.fstype}")
    
    # Obtener uso de cada partición
    try:
        uso = psutil.disk_usage(particion.mountpoint)
        print(f"  Total: {uso.total / (1024**3):.1f} GB")
        print(f"  Usado: {uso.used / (1024**3):.1f} GB ({uso.percent}%)")
    except PermissionError:
        print(f"  Sin permisos para acceder")

# ===== RED =====
# Estadísticas de interfaces de red
net_io = psutil.net_io_counters()
print(f"\nBytes enviados: {net_io.bytes_sent / (1024**2):.1f} MB")
print(f"Bytes recibidos: {net_io.bytes_recv / (1024**2):.1f} MB")

# Conexiones de red activas
conexiones = psutil.net_connections(kind='inet')
print(f"\nConexiones activas: {len(conexiones)}")

# ===== PROCESOS =====
# Listar todos los procesos
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    print(f"PID: {proc.info['pid']}, Nombre: {proc.info['name']}")

# Información de proceso específico
proceso = psutil.Process(1234)  # PID
print(f"Nombre: {proceso.name()}")
print(f"CPU: {proceso.cpu_percent()}%")
print(f"Memoria: {proceso.memory_info().rss / (1024**2):.1f} MB")
```

---
**Nivel**: Básico
**Tiempo estimado de estudio**: 6-8 horas
**Próximos pasos**: Practicar combinando módulos, crear scripts propios, estudiar requests para APIs REST
