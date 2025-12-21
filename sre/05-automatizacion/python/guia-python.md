# 🐍 Python para DevOps/SRE - Guía Completa

## 🎯 ¿Por qué Python en DevOps?

Python es el lenguaje preferido para automatización, scripting y herramientas DevOps por:
- ✅ Sintaxis clara y legible
- ✅ Librerías excelentes para system admin (psutil, requests, paramiko)
- ✅ Integración con APIs REST
- ✅ Procesamiento de datos (JSON, YAML, CSV)
- ✅ Amplia comunidad y documentación

---

## 📚 Conceptos Básicos

### Variables y Tipos de Datos

```python
# Variables (tipado dinámico)
name = "Juan"
age = 25
is_admin = True
salary = 50000.50

# None (equivalente a null)
config = None

# Type hints (Python 3.5+)
def greet(name: str) -> str:
    return f"Hola, {name}"

# Múltiples asignaciones
x, y, z = 1, 2, 3

# Swap
a, b = b, a
```

### Strings

```python
# Strings básicos
name = "DevOps Engineer"
company = 'Whitestack'

# Multi-línea
config = """
server:
  host: localhost
  port: 8080
"""

# f-strings (Python 3.6+) - RECOMENDADO
name = "Juan"
age = 25
print(f"Hola {name}, tienes {age} años")
print(f"El doble es {age * 2}")

# Métodos útiles
text = "  hello world  "
text.strip()           # "hello world"
text.upper()           # "  HELLO WORLD  "
text.lower()           # "  hello world  "
text.replace("world", "python")  # "  hello python  "
text.split()           # ["hello", "world"]

# Verificaciones
"hello" in text        # True
text.startswith("  ")  # True
text.endswith("  ")    # True

# Join
words = ["hello", "world"]
"-".join(words)        # "hello-world"
```

### Listas (Arrays)

```python
# Crear lista
servers = ["web1", "web2", "db1"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

# Acceder elementos
servers[0]           # "web1"
servers[-1]          # "db1" (último)
servers[0:2]         # ["web1", "web2"] (slice)

# Modificar
servers.append("cache1")      # Agregar al final
servers.insert(0, "lb1")      # Insertar en posición
servers.remove("db1")         # Eliminar por valor
servers.pop()                 # Eliminar último
servers.pop(0)                # Eliminar por índice

# Búsqueda
"web1" in servers            # True
servers.index("web2")        # 1
servers.count("web1")        # 1

# Ordenar
numbers.sort()               # Modifica lista
sorted(numbers)              # Retorna nueva lista
servers.reverse()            # Invertir

# List comprehension (muy usado!)
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Transformar
servers_upper = [s.upper() for s in servers]
```

### Diccionarios (Maps/Objects)

```python
# Crear diccionario
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

# Acceder
config["host"]              # "localhost"
config.get("host")          # "localhost"
config.get("missing", "default")  # "default"

# Modificar
config["timeout"] = 30      # Agregar/modificar
del config["debug"]         # Eliminar

# Verificar
"host" in config            # True
"missing" in config         # False

# Iterar
for key in config:
    print(key, config[key])

for key, value in config.items():
    print(f"{key}: {value}")

# Keys y values
config.keys()               # dict_keys(['host', 'port', ...])
config.values()             # dict_values(['localhost', 8080, ...])

# Dict comprehension
squared = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Sets (Conjuntos)

```python
# Crear set (elementos únicos)
servers = {"web1", "web2", "web3"}
numbers = {1, 2, 3, 3, 3}  # {1, 2, 3}

# Operaciones
servers.add("db1")
servers.remove("web1")
"web2" in servers          # True

# Operaciones de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1 | set2                # {1, 2, 3, 4, 5} - unión
set1 & set2                # {3} - intersección
set1 - set2                # {1, 2} - diferencia
```

---

## 🔄 Control de Flujo

### If-Elif-Else

```python
age = 25

if age < 18:
    print("Menor de edad")
elif age < 65:
    print("Adulto")
else:
    print("Senior")

# Ternario
status = "Mayor" if age >= 18 else "Menor"

# Múltiples condiciones
if age > 18 and age < 65:
    print("Adulto trabajador")

if status == "admin" or status == "root":
    print("Acceso total")

# Verificar None
config = None
if config is None:
    print("Config no definido")

# Verificar vacío
if not servers:  # Lista vacía
    print("No hay servers")

if servers:  # Lista con elementos
    print("Hay servers")
```

### Loops

```python
# For loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Iterar lista
servers = ["web1", "web2", "db1"]
for server in servers:
    print(server)

# Con índice
for i, server in enumerate(servers):
    print(f"{i}: {server}")

# Iterar diccionario
config = {"host": "localhost", "port": 8080}
for key, value in config.items():
    print(f"{key} = {value}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break y continue
for i in range(10):
    if i == 3:
        continue  # Saltar esta iteración
    if i == 7:
        break     # Salir del loop
    print(i)

# Else en loops (raramente usado)
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completado sin break")
```

---

## 🔧 Funciones

### Funciones Básicas

```python
# Función simple
def greet(name):
    return f"Hola, {name}"

result = greet("Juan")

# Con valor por defecto
def greet(name="Usuario"):
    return f"Hola, {name}"

greet()          # "Hola, Usuario"
greet("Juan")    # "Hola, Juan"

# Múltiples parámetros
def add(a, b):
    return a + b

# Type hints
def add(a: int, b: int) -> int:
    return a + b

# Múltiples returns
def get_stats():
    return 100, 200, 300

cpu, memory, disk = get_stats()

# *args - argumentos variables
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4, 5)  # 15

# **kwargs - argumentos con nombre
def print_config(**config):
    for key, value in config.items():
        print(f"{key}: {value}")

print_config(host="localhost", port=8080, debug=True)

# Docstrings
def calculate_cpu(usage: float, cores: int) -> float:
    """
    Calcula el uso de CPU en %.
    
    Args:
        usage: Uso actual de CPU
        cores: Número de cores
    
    Returns:
        Porcentaje de uso
    """
    return (usage / cores) * 100
```

### Lambda Functions

```python
# Lambda (funciones anónimas)
square = lambda x: x ** 2
square(5)  # 25

# Con map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Con filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# Con sorted
servers = [{"name": "web1", "cpu": 80}, {"name": "db1", "cpu": 60}]
sorted_servers = sorted(servers, key=lambda x: x["cpu"])
```

---

## 📦 Módulos y Imports

```python
# Import completo
import os
import sys
import json

os.path.exists("/tmp")
json.loads('{"key": "value"}')

# Import específico
from os import path, environ
from datetime import datetime, timedelta

path.exists("/tmp")
now = datetime.now()

# Import con alias
import requests as req
import pandas as pd
import numpy as np

response = req.get("http://example.com")

# Import todo (no recomendado)
from os import *

# Import relativo (mismo package)
from .module import function
from ..parent import something
```

### Módulos Útiles para DevOps

```python
# OS y Sistema
import os
import sys
import subprocess
import shutil
import glob

# Archivos y paths
from pathlib import Path
import tempfile

# Tiempo
import time
from datetime import datetime, timedelta

# Networking
import socket
import requests
import urllib

# Datos
import json
import yaml
import csv
import configparser

# System monitoring
import psutil

# Regex
import re

# Logging
import logging

# Argumentos CLI
import argparse

# Variables de entorno
from dotenv import load_dotenv
```

---

## 📁 Trabajar con Archivos

### Leer y Escribir

```python
# Leer archivo completo
with open("file.txt", "r") as f:
    content = f.read()

# Leer línea por línea
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Leer todas las líneas en lista
with open("file.txt", "r") as f:
    lines = f.readlines()

# Escribir archivo
with open("output.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

# Append
with open("log.txt", "a") as f:
    f.write(f"[{datetime.now()}] Log entry\n")

# Escribir lista de líneas
lines = ["line1\n", "line2\n", "line3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# Pathlib (moderno)
from pathlib import Path

file = Path("data.txt")
content = file.read_text()
file.write_text("nuevo contenido")

# Verificar existencia
if file.exists():
    print("Archivo existe")

if file.is_file():
    print("Es un archivo")

if file.is_dir():
    print("Es un directorio")
```

### JSON

```python
import json

# Leer JSON
with open("config.json", "r") as f:
    config = json.load(f)

# Escribir JSON
data = {"name": "server1", "port": 8080}
with open("config.json", "w") as f:
    json.dump(data, f, indent=2)

# String to dict
json_string = '{"key": "value"}'
data = json.loads(json_string)

# Dict to string
json_string = json.dumps(data, indent=2)

# Pretty print
print(json.dumps(data, indent=2))
```

### YAML

```python
import yaml

# Leer YAML
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Escribir YAML
data = {
    "server": {
        "host": "localhost",
        "port": 8080
    }
}
with open("config.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)
```

### CSV

```python
import csv

# Leer CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # Lista de valores

# Leer CSV con dict
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# Escribir CSV
data = [
    ["Name", "Age", "City"],
    ["Juan", 25, "Madrid"],
    ["María", 30, "Barcelona"]
]
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Escribir dict a CSV
data = [
    {"name": "Juan", "age": 25},
    {"name": "María", "age": 30}
]
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)
```

---

## 🌐 Trabajar con APIs (Requests)

```python
import requests

# GET request
response = requests.get("https://api.example.com/data")
print(response.status_code)  # 200
print(response.text)         # Response body
data = response.json()       # Parse JSON

# Con headers
headers = {
    "Authorization": "Bearer token123",
    "Content-Type": "application/json"
}
response = requests.get("https://api.example.com/data", headers=headers)

# Con query parameters
params = {"limit": 10, "offset": 0}
response = requests.get("https://api.example.com/data", params=params)
# URL: https://api.example.com/data?limit=10&offset=0

# POST request
data = {"name": "server1", "type": "web"}
response = requests.post("https://api.example.com/servers", json=data)

# PUT request
response = requests.put("https://api.example.com/servers/1", json=data)

# DELETE request
response = requests.delete("https://api.example.com/servers/1")

# Timeout
response = requests.get("https://api.example.com/data", timeout=5)

# Error handling
try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # Raise exception si status >= 400
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timeout")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# Session (mantiene cookies, headers)
session = requests.Session()
session.headers.update({"Authorization": "Bearer token"})
response = session.get("https://api.example.com/data")
```

---

## 🖥️ System Administration (psutil)

```python
import psutil
import os

# CPU
cpu_percent = psutil.cpu_percent(interval=1)
cpu_count = psutil.cpu_count()
cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)

# Memory
memory = psutil.virtual_memory()
print(f"Total: {memory.total / (1024**3):.2f} GB")
print(f"Used: {memory.used / (1024**3):.2f} GB")
print(f"Percent: {memory.percent}%")

# Disk
disk = psutil.disk_usage('/')
print(f"Total: {disk.total / (1024**3):.2f} GB")
print(f"Used: {disk.used / (1024**3):.2f} GB")
print(f"Free: {disk.free / (1024**3):.2f} GB")
print(f"Percent: {disk.percent}%")

# Disk I/O
disk_io = psutil.disk_io_counters()
print(f"Read: {disk_io.read_bytes / (1024**2):.2f} MB")
print(f"Write: {disk_io.write_bytes / (1024**2):.2f} MB")

# Network
net_io = psutil.net_io_counters()
print(f"Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
print(f"Recv: {net_io.bytes_recv / (1024**2):.2f} MB")

# Procesos
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
    print(proc.info)

# Proceso específico
proc = psutil.Process(os.getpid())
print(f"CPU: {proc.cpu_percent()}")
print(f"Memory: {proc.memory_info().rss / (1024**2):.2f} MB")
print(f"Threads: {proc.num_threads()}")
print(f"Files: {len(proc.open_files())}")

# Boot time
import datetime
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
print(f"Boot time: {boot_time}")
```

---

## 🐚 Ejecutar Comandos Shell

```python
import subprocess
import os

# Run simple command
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
print(result.returncode)

# Con shell (cuidado con seguridad!)
result = subprocess.run("ls -la | grep .txt", shell=True, capture_output=True, text=True)

# Check si comando exitoso
try:
    subprocess.run(["ls", "/nonexistent"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with code {e.returncode}")

# Capturar output
output = subprocess.check_output(["date"])
print(output.decode())

# Con timeout
try:
    subprocess.run(["sleep", "10"], timeout=5)
except subprocess.TimeoutExpired:
    print("Command timeout")

# Input a comando
result = subprocess.run(
    ["grep", "error"],
    input="line1\nerror in line2\nline3",
    text=True,
    capture_output=True
)
print(result.stdout)  # "error in line2"

# Pipe entre comandos (método correcto)
ps = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
grep = subprocess.Popen(["grep", "python"], stdin=ps.stdout, stdout=subprocess.PIPE)
ps.stdout.close()
output = grep.communicate()[0]

# Alternativa con os.system (legacy, evitar)
os.system("ls -la")
```

---

## 🔍 Regular Expressions (Regex)

```python
import re

text = "Server: web1, IP: 192.168.1.100, Port: 8080"

# Buscar
match = re.search(r"IP: ([\d.]+)", text)
if match:
    print(match.group(1))  # "192.168.1.100"

# Buscar todas las ocurrencias
ips = re.findall(r"\d+\.\d+\.\d+\.\d+", text)
# ["192.168.1.100"]

# Replace
new_text = re.sub(r"\d+\.\d+\.\d+\.\d+", "10.0.0.1", text)

# Split
parts = re.split(r",\s*", text)

# Match completo
if re.match(r"Server:", text):
    print("Empieza con 'Server:'")

# Compiled regex (mejor performance si se usa múltiples veces)
ip_pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")
ips = ip_pattern.findall(text)

# Grupos nombrados
match = re.search(r"IP: (?P<ip>[\d.]+)", text)
if match:
    print(match.group("ip"))

# Ejemplos útiles para DevOps
log_line = "2024-01-15 10:30:45 ERROR Failed to connect"
match = re.search(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)", log_line)
if match:
    date, time, level, message = match.groups()
```

---

## 📝 Logging

```python
import logging

# Configuración básica
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()  # También en consola
    ]
)

logger = logging.getLogger(__name__)

# Niveles de log
logger.debug("Debug message")      # Desarrollo
logger.info("Info message")        # Info general
logger.warning("Warning message")  # Advertencia
logger.error("Error message")      # Error
logger.critical("Critical!")       # Crítico

# Con variables
user = "admin"
logger.info(f"User {user} logged in")

# Con exception
try:
    1 / 0
except Exception as e:
    logger.error("Error occurred", exc_info=True)  # Incluye traceback
    # O más corto:
    logger.exception("Error occurred")

# Logger avanzado
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Usar
logger.info("Application started")
```

---

## 🎯 CLI Arguments (argparse)

```python
import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Monitor de servicios',
        epilog='Ejemplo: python monitor.py --host localhost --port 8080'
    )
    
    # Argumentos posicionales
    parser.add_argument('action', choices=['start', 'stop', 'status'])
    
    # Argumentos opcionales
    parser.add_argument(
        '--host',
        default='localhost',
        help='Host to monitor'
    )
    
    parser.add_argument(
        '-p', '--port',
        type=int,
        default=8080,
        help='Port number'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',  # Flag boolean
        help='Verbose output'
    )
    
    parser.add_argument(
        '--config',
        type=argparse.FileType('r'),
        help='Config file'
    )
    
    # Parse
    args = parser.parse_args()
    
    # Usar
    print(f"Action: {args.action}")
    print(f"Host: {args.host}")
    print(f"Port: {args.port}")
    
    if args.verbose:
        print("Verbose mode enabled")
    
    if args.config:
        content = args.config.read()

if __name__ == '__main__':
    main()

# Uso:
# python script.py start --host example.com -p 9000 -v
```

---

## 🔐 Variables de Entorno

```python
import os
from dotenv import load_dotenv

# Leer variable de entorno
db_host = os.environ.get('DB_HOST', 'localhost')  # Con default
api_key = os.environ['API_KEY']  # Sin default (error si no existe)

# Establecer variable
os.environ['MY_VAR'] = 'value'

# .env file (requiere python-dotenv)
# .env:
# DB_HOST=localhost
# DB_PORT=5432
# DB_PASSWORD=secret

load_dotenv()  # Cargar .env
db_host = os.environ['DB_HOST']
```

---

## 🚨 Error Handling

```python
# Try-except básico
try:
    result = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")

# Múltiples excepciones
try:
    # código
    pass
except ValueError:
    print("Error de valor")
except KeyError:
    print("Key no encontrada")
except (TypeError, AttributeError) as e:
    print(f"Error de tipo o atributo: {e}")

# Capturar todas las excepciones
try:
    # código
    pass
except Exception as e:
    print(f"Error: {e}")

# Finally (siempre se ejecuta)
try:
    f = open("file.txt")
    # código
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    f.close()  # Siempre se ejecuta

# Else (se ejecuta si no hay excepción)
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print(f"Resultado: {result}")

# Raise exception
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# Custom exception
class ConfigError(Exception):
    pass

def load_config():
    raise ConfigError("Config file missing")
```

---

## 🎓 Scripts Útiles para DevOps

### 1. Health Check de URLs

```python
#!/usr/bin/env python3
import requests
import sys

urls = [
    "https://api.example.com/health",
    "https://web.example.com",
    "https://db.example.com:5432"
]

failed = []

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✓ {url}")
        else:
            print(f"✗ {url} - Status {response.status_code}")
            failed.append(url)
    except requests.exceptions.RequestException as e:
        print(f"✗ {url} - Error: {e}")
        failed.append(url)

if failed:
    print(f"\n{len(failed)} checks failed")
    sys.exit(1)
else:
    print("\nAll checks passed")
    sys.exit(0)
```

### 2. Limpiar Logs Viejos

```python
#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timedelta

log_dir = Path("/var/log/myapp")
days_to_keep = 7
cutoff = datetime.now() - timedelta(days=days_to_keep)

for log_file in log_dir.glob("*.log*"):
    mtime = datetime.fromtimestamp(log_file.stat().st_mtime)
    if mtime < cutoff:
        print(f"Deleting {log_file}")
        log_file.unlink()
```

### 3. Parse de Logs

```python
#!/usr/bin/env python3
import re
from collections import Counter

log_file = "/var/log/nginx/access.log"
ip_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')

ips = []
with open(log_file) as f:
    for line in f:
        match = ip_pattern.search(line)
        if match:
            ips.append(match.group(1))

# Top 10 IPs
top_ips = Counter(ips).most_common(10)
for ip, count in top_ips:
    print(f"{ip}: {count} requests")
```

---

## ✅ Best Practices

1. **Use virtual environments**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Type hints**
```python
def process_data(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}
```

3. **Docstrings**
```python
def calculate(x: int, y: int) -> int:
    """Calculate sum of two numbers.
    
    Args:
        x: First number
        y: Second number
    
    Returns:
        Sum of x and y
    """
    return x + y
```

4. **Context managers**
```python
# Siempre usar with para archivos
with open("file.txt") as f:
    content = f.read()
# Archivo se cierra automáticamente
```

5. **List comprehensions > loops**
```python
# ✅ Pythonic
squares = [x**2 for x in range(10)]

# ❌ No pythonic
squares = []
for x in range(10):
    squares.append(x**2)
```

---

## 📚 Librerías Esenciales DevOps

```bash
# Instalar con pip
pip install psutil          # System monitoring
pip install requests        # HTTP requests
pip install pyyaml          # YAML
pip install python-dotenv   # .env files
pip install paramiko        # SSH
pip install fabric          # Deployment
pip install ansible         # Automation
pip install docker          # Docker API
pip install kubernetes      # K8s API
pip install prometheus-client  # Prometheus
pip install click           # CLI apps (alternativa a argparse)
```

---

## ✅ Checklist

- [ ] Entiendo tipos de datos básicos (str, int, list, dict)
- [ ] Sé usar list/dict comprehensions
- [ ] Puedo leer/escribir archivos (text, JSON, YAML)
- [ ] Entiendo try-except para error handling
- [ ] Sé usar requests para APIs
- [ ] Puedo ejecutar comandos shell con subprocess
- [ ] Entiendo logging
- [ ] Sé usar argparse para CLI
- [ ] Puedo monitorear sistema con psutil
- [ ] Conozco pathlib para archivos/directorios
