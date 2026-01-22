# Ansible - Automatización de Infraestructura

## 1. Conceptos Fundamentales

### ¿Qué es Ansible?
- Herramienta de automatización agentless
- Basada en YAML
- Gestión de configuración, despliegue y orquestación
- Usa SSH para comunicarse

### Instalación
```bash
sudo apt install ansible        # Debian/Ubuntu
sudo yum install ansible        # RHEL/CentOS
ansible --version
```

## 2. Inventario (Inventory)

### Archivo Hosts Estático
```ini
# /etc/ansible/hosts
[webservers]
web1.example.com ansible_user=admin
web2.example.com ansible_user=admin
192.168.1.10 ansible_user=root

[dbservers]
db1.example.com
db2.example.com

[all_servers:children]
webservers
dbservers
```

### Inventario YAML
```yaml
# inventory.yaml
all:
  children:
    webservers:
      hosts:
        web1:
          ansible_host: 192.168.1.10
        web2:
          ansible_host: 192.168.1.11
      vars:
        ansible_user: admin
    dbservers:
      hosts:
        db1:
          ansible_host: 192.168.1.20
```

## 3. Ad-Hoc Commands

### Ejecutar Comandos Directos
```bash
ansible all -i inventory.ini -m ping
ansible webservers -i inventory.ini -a "uptime"
ansible webservers -i inventory.ini -m shell -a "ps aux"
ansible all -i inventory.ini -m setup          # Recopilar hechos
```

## 4. Playbooks - Estructura Básica

### Playbook Simple
```yaml
---
- name: Configurar servidores web
  hosts: webservers
  gather_facts: yes
  vars:
    package_name: apache2
  
  tasks:
    - name: Actualizar cache APT
      apt:
        update_cache: yes
      become: yes
    
    - name: Instalar Apache2
      apt:
        name: "{{ package_name }}"
        state: present
      become: yes
    
    - name: Iniciar servicio Apache
      service:
        name: apache2
        state: started
        enabled: yes
      become: yes
    
    - name: Crear archivo test
      copy:
        content: "Hola desde {{ inventory_hostname }}"
        dest: /var/www/html/index.html
      become: yes
```

### Ejecutar Playbook
```bash
ansible-playbook playbook.yml
ansible-playbook playbook.yml -i inventory.ini
ansible-playbook playbook.yml --check    # Dry-run
ansible-playbook playbook.yml -v         # Verbose
ansible-playbook playbook.yml -vvv       # Muy verbose (debug)
```

## 5. Módulos Comunes

### Módulo APT/YUM
```yaml
- name: Instalar paquete
  apt:
    name: nginx
    state: present

- name: Instalar múltiples paquetes
  apt:
    name: 
      - nginx
      - curl
      - wget
    state: present
```

### Módulo Service
```yaml
- name: Reiniciar servicio
  service:
    name: nginx
    state: restarted
    enabled: yes
```

### Módulo Command/Shell
```yaml
- name: Ejecutar comando
  command: /usr/bin/uptime

- name: Ejecutar script shell
  shell: |
    #!/bin/bash
    echo "Ejecutando..."
    ls -la /tmp
```

### Módulo Copy/Template
```yaml
- name: Copiar archivo
  copy:
    src: /local/path/file.conf
    dest: /remote/path/file.conf
    owner: root
    group: root
    mode: '0644'

- name: Usar template
  template:
    src: config.j2
    dest: /etc/config.conf
    owner: root
    group: root
    mode: '0644'
```

### Módulo File
```yaml
- name: Crear directorio
  file:
    path: /var/www/html
    state: directory
    mode: '0755'

- name: Crear archivo vacío
  file:
    path: /tmp/myfile.txt
    state: touch

- name: Cambiar permisos
  file:
    path: /var/www/html
    mode: '0755'
    recurse: yes
```

### Módulo User
```yaml
- name: Crear usuario
  user:
    name: appuser
    shell: /bin/bash
    groups: sudo
    createhome: yes

- name: Eliminar usuario
  user:
    name: appuser
    state: absent
    remove: yes
```

## 6. Variables

### Variables en Playbook
```yaml
---
- name: Demo de variables
  hosts: all
  vars:
    web_port: 8080
    app_name: myapp
  
  tasks:
    - name: Mostrar variables
      debug:
        msg: "App {{ app_name }} corriendo en puerto {{ web_port }}"
```

### Variables Externas (Archivos)
```yaml
# vars/main.yml
---
web_port: 8080
app_name: myapp
```

```yaml
---
- name: Usar archivo de variables
  hosts: all
  vars_files:
    - vars/main.yml
  
  tasks:
    - debug: msg="{{ app_name }}"
```

### Variables de Línea de Comando
```bash
ansible-playbook playbook.yml -e "variable=valor"
ansible-playbook playbook.yml -e "@variables.json"
```

## 7. Condicionales

### When
```yaml
- name: Instalar en Ubuntu
  apt:
    name: nginx
  when: ansible_distribution == "Ubuntu"

- name: Instalar en CentOS
  yum:
    name: nginx
  when: ansible_os_family == "RedHat"

- name: Ejecutar si puerto está disponible
  debug:
    msg: "Puerto disponible"
  when: ansible_default_ipv4.address is defined
```

## 8. Loops

### Simple Loop
```yaml
- name: Instalar paquetes
  apt:
    name: "{{ item }}"
  loop:
    - nginx
    - curl
    - git

- name: Crear usuarios
  user:
    name: "{{ item }}"
    shell: /bin/bash
  loop:
    - user1
    - user2
    - user3
```

### Loop Dictionary
```yaml
- name: Crear usuarios con info
  user:
    name: "{{ item.name }}"
    groups: "{{ item.groups }}"
  loop:
    - { name: 'user1', groups: 'sudo' }
    - { name: 'user2', groups: 'admin' }
```

## 9. Roles - Estructura

### Crear Rol
```bash
ansible-galaxy role init my_role
```

### Estructura de Rol
```
my_role/
├── tasks/
│   └── main.yml
├── handlers/
│   └── main.yml
├── vars/
│   └── main.yml
├── defaults/
│   └── main.yml
├── files/
├── templates/
└── README.md
```

### Usar Rol en Playbook
```yaml
---
- name: Usar rol
  hosts: webservers
  roles:
    - my_role
```

## 10. Handlers (Manejadores de Eventos)

### Triggers y Handlers
```yaml
---
- name: Configurar Apache
  hosts: webservers
  
  tasks:
    - name: Instalar Apache
      apt:
        name: apache2
      become: yes
      notify: Reiniciar Apache
    
    - name: Copiar config
      copy:
        src: apache2.conf
        dest: /etc/apache2/apache2.conf
      become: yes
      notify: Reiniciar Apache
  
  handlers:
    - name: Reiniciar Apache
      service:
        name: apache2
        state: restarted
      become: yes
```

---
**Nivel**: Básico-Intermedio
**Tiempo estimado de estudio**: 5-6 horas
