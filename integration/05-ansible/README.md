# 🤖 Ansible - Guía de Automatización

## 📚 Índice
1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [Inventarios](#inventarios)
3. [Playbooks](#playbooks)
4. [Roles](#roles)
5. [Variables](#variables)
6. [Módulos Importantes](#módulos-importantes)
7. [Troubleshooting](#troubleshooting)

---

## 1. Conceptos Fundamentales

### 🎯 ¿Qué es Ansible?

Ansible es una herramienta de automatización IT que permite:
- Configurar sistemas
- Desplegar aplicaciones
- Orquestar tareas complejas
- Sin necesidad de agentes (usa SSH)

**Características:**
- ✅ Agentless (sin agentes en nodos)
- ✅ Declarativo (describe el estado deseado)
- ✅ Idempotente (se puede ejecutar múltiples veces)
- ✅ YAML (fácil de leer y escribir)

**Componentes:**
- **Control Node**: Máquina donde se ejecuta Ansible
- **Managed Nodes**: Servidores gestionados
- **Inventory**: Lista de hosts
- **Playbook**: Archivo de automatización
- **Roles**: Forma de organizar playbooks
- **Modules**: Unidades de código ejecutables

---

## 2. Inventarios

### 📝 Formato INI

```ini
# inventory.ini
[webservers]
web1.example.com
web2.example.com ansible_host=192.168.1.10
web3.example.com ansible_port=2222

[databases]
db1.example.com
db2.example.com

[databases:vars]
ansible_user=dbadmin
ansible_ssh_private_key_file=~/.ssh/db_key

[production:children]
webservers
databases

[production:vars]
env=production
```

### 📝 Formato YAML

```yaml
# inventory.yml
all:
  children:
    webservers:
      hosts:
        web1.example.com:
        web2.example.com:
          ansible_host: 192.168.1.10
        web3.example.com:
          ansible_port: 2222
    
    databases:
      hosts:
        db1.example.com:
        db2.example.com:
      vars:
        ansible_user: dbadmin
        ansible_ssh_private_key_file: ~/.ssh/db_key
    
    production:
      children:
        webservers:
        databases:
      vars:
        env: production
```

### 🔧 Comandos de Inventario

```bash
# Listar hosts
ansible-inventory -i inventory.ini --list
ansible-inventory -i inventory.ini --graph
ansible all --list-hosts
ansible webservers --list-hosts

# Ping a hosts
ansible all -m ping
ansible webservers -m ping -i inventory.ini

# Variables de host
ansible-inventory -i inventory.ini --host web1.example.com
```

---

## 3. Playbooks

### 📜 Estructura Básica

```yaml
# playbook.yml
---
- name: Configure web servers
  hosts: webservers
  become: yes                    # Usar sudo
  become_user: root              # Usuario sudo
  gather_facts: yes              # Recolectar info del sistema
  
  vars:
    app_port: 8080
    app_user: webapp
  
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
    
    - name: Start nginx service
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Copy config file
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
        owner: root
        group: root
        mode: '0644'
      notify: Restart nginx
  
  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted
```

### 🎮 Ejecutar Playbooks

```bash
# Ejecución básica
ansible-playbook playbook.yml
ansible-playbook -i inventory.ini playbook.yml

# Con variables extras
ansible-playbook playbook.yml -e "app_port=9090"
ansible-playbook playbook.yml -e "@vars.yml"

# Check mode (dry-run)
ansible-playbook playbook.yml --check

# Diff mode (ver cambios)
ansible-playbook playbook.yml --check --diff

# Limitar a hosts específicos
ansible-playbook playbook.yml --limit web1.example.com
ansible-playbook playbook.yml --limit webservers

# Desde un task específico
ansible-playbook playbook.yml --start-at-task="Install nginx"

# Tags
ansible-playbook playbook.yml --tags "config"
ansible-playbook playbook.yml --skip-tags "slow"

# Verbose
ansible-playbook playbook.yml -v     # -v, -vv, -vvv, -vvvv
```

### 🎯 Características Avanzadas

```yaml
# playbook-advanced.yml
---
- name: Advanced playbook features
  hosts: all
  gather_facts: yes
  
  vars:
    packages:
      - nginx
      - git
      - curl
  
  tasks:
    # Condicionales
    - name: Install packages on Ubuntu
      apt:
        name: "{{ packages }}"
        state: present
      when: ansible_distribution == "Ubuntu"
    
    - name: Install packages on CentOS
      yum:
        name: "{{ packages }}"
        state: present
      when: ansible_distribution == "CentOS"
    
    # Loops
    - name: Create multiple users
      user:
        name: "{{ item }}"
        state: present
      loop:
        - alice
        - bob
        - charlie
    
    # Loop con diccionarios
    - name: Add users with details
      user:
        name: "{{ item.name }}"
        uid: "{{ item.uid }}"
        state: present
      loop:
        - { name: 'alice', uid: 1001 }
        - { name: 'bob', uid: 1002 }
    
    # Registro de resultados
    - name: Check if service exists
      command: systemctl status nginx
      register: nginx_status
      ignore_errors: yes
    
    - name: Show nginx status
      debug:
        var: nginx_status
    
    # Condicional con registro
    - name: Start nginx if not running
      service:
        name: nginx
        state: started
      when: nginx_status.rc != 0
    
    # Block (agrupación de tasks)
    - name: Configure application
      block:
        - name: Install dependencies
          apt:
            name: python3-pip
            state: present
        
        - name: Install python packages
          pip:
            name: flask
            state: present
      
      rescue:
        - name: Handle errors
          debug:
            msg: "Installation failed, rolling back"
      
      always:
        - name: Always cleanup
          file:
            path: /tmp/install
            state: absent
    
    # Tags
    - name: Configure firewall
      ufw:
        rule: allow
        port: 80
      tags:
        - security
        - firewall
```

---

## 4. Roles

### 📁 Estructura de un Rol

```
roles/
└── nginx/
    ├── README.md
    ├── defaults/
    │   └── main.yml        # Variables por defecto
    ├── files/
    │   └── index.html      # Archivos estáticos
    ├── handlers/
    │   └── main.yml        # Handlers
    ├── meta/
    │   └── main.yml        # Metadata y dependencias
    ├── tasks/
    │   └── main.yml        # Tasks principales
    ├── templates/
    │   └── nginx.conf.j2   # Templates Jinja2
    ├── tests/
    │   ├── inventory
    │   └── test.yml
    └── vars/
        └── main.yml        # Variables del rol
```

### 📝 Ejemplo de Rol

**tasks/main.yml:**
```yaml
---
# roles/nginx/tasks/main.yml
- name: Install nginx
  apt:
    name: nginx
    state: present
    update_cache: yes
  tags: install

- name: Copy nginx config
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
  notify: Restart nginx
  tags: config

- name: Ensure nginx is running
  service:
    name: nginx
    state: started
    enabled: yes
  tags: service
```

**handlers/main.yml:**
```yaml
---
# roles/nginx/handlers/main.yml
- name: Restart nginx
  service:
    name: nginx
    state: restarted

- name: Reload nginx
  service:
    name: nginx
    state: reloaded
```

**defaults/main.yml:**
```yaml
---
# roles/nginx/defaults/main.yml
nginx_port: 80
nginx_user: www-data
nginx_worker_processes: auto
nginx_worker_connections: 1024
```

**templates/nginx.conf.j2:**
```nginx
user {{ nginx_user }};
worker_processes {{ nginx_worker_processes }};

events {
    worker_connections {{ nginx_worker_connections }};
}

http {
    server {
        listen {{ nginx_port }};
        server_name {{ ansible_hostname }};
        
        location / {
            root /var/www/html;
            index index.html;
        }
    }
}
```

### 🎮 Usar Roles

```yaml
# playbook-with-roles.yml
---
- name: Configure web servers
  hosts: webservers
  become: yes
  
  roles:
    - common
    - nginx
    - { role: deploy_app, app_version: '1.2.3' }
  
  # O con tasks antes/después
  pre_tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
  
  roles:
    - nginx
  
  post_tasks:
    - name: Verify nginx
      uri:
        url: http://localhost
        return_content: yes
```

```bash
# Crear estructura de rol
ansible-galaxy init nginx
ansible-galaxy init roles/myapp

# Instalar roles de Ansible Galaxy
ansible-galaxy install geerlingguy.nginx
ansible-galaxy install -r requirements.yml

# requirements.yml
# - name: geerlingguy.nginx
#   version: 3.1.4
# - src: https://github.com/user/role.git
#   name: custom-role
```

---

## 5. Variables

### 📊 Precedencia de Variables (menor a mayor)

1. role defaults
2. inventory file/script group vars
3. inventory group_vars/all
4. playbook group_vars/all
5. inventory group_vars/*
6. playbook group_vars/*
7. inventory file/script host vars
8. inventory host_vars/*
9. playbook host_vars/*
10. host facts
11. play vars
12. play vars_prompt
13. play vars_files
14. role vars
15. block vars
16. task vars
17. extra vars (-e)

### 📝 Definir Variables

```yaml
# En playbook
---
- name: Example
  hosts: all
  vars:
    app_name: myapp
    app_version: "1.0"
  vars_files:
    - vars/main.yml
    - vars/secrets.yml
  
  tasks:
    - name: Show variable
      debug:
        msg: "{{ app_name }} version {{ app_version }}"
```

```yaml
# group_vars/webservers.yml
---
http_port: 80
https_port: 443
server_name: www.example.com
```

```yaml
# host_vars/web1.example.com.yml
---
server_id: 1
backup_server: yes
```

### 🎯 Usar Variables

```yaml
# Variables simples
- name: Install {{ package_name }}
  apt:
    name: "{{ package_name }}"
    state: present

# Variables de diccionario
user:
  name: john
  uid: 1001
  shell: /bin/bash

- name: Create user
  user:
    name: "{{ user.name }}"
    uid: "{{ user['uid'] }}"
    shell: "{{ user.shell }}"

# Variables de lista
packages:
  - nginx
  - git
  - curl

- name: Install packages
  apt:
    name: "{{ item }}"
    state: present
  loop: "{{ packages }}"

# Facts (variables del sistema)
- debug:
    msg: "{{ ansible_hostname }}"
- debug:
    msg: "{{ ansible_default_ipv4.address }}"
- debug:
    msg: "{{ ansible_distribution }} {{ ansible_distribution_version }}"

# Variables registradas
- name: Get service status
  command: systemctl status nginx
  register: result
  
- debug:
    var: result.stdout_lines
```

---

## 6. Módulos Importantes

### 📦 Gestión de Paquetes

```yaml
# APT (Debian/Ubuntu)
- name: Install packages
  apt:
    name:
      - nginx
      - git
    state: present
    update_cache: yes

# YUM/DNF (CentOS/RHEL)
- name: Install packages
  yum:
    name: nginx
    state: latest

# PIP (Python)
- name: Install python packages
  pip:
    name: flask
    version: 2.0.1
    state: present
```

### 📁 Archivos y Directorios

```yaml
# Crear directorio
- name: Create directory
  file:
    path: /app/data
    state: directory
    owner: appuser
    group: appgroup
    mode: '0755'

# Crear archivo
- name: Create file
  file:
    path: /app/config.txt
    state: touch
    mode: '0644'

# Copiar archivo
- name: Copy file
  copy:
    src: files/config.yaml
    dest: /etc/app/config.yaml
    owner: root
    mode: '0644'

# Template (Jinja2)
- name: Deploy config template
  template:
    src: templates/app.conf.j2
    dest: /etc/app/app.conf
    backup: yes

# Línea en archivo
- name: Add line to file
  lineinfile:
    path: /etc/hosts
    line: "192.168.1.10 server1.local"
    state: present

# Bloque en archivo
- name: Add block to file
  blockinfile:
    path: /etc/nginx/nginx.conf
    block: |
      server {
          listen 8080;
      }
    marker: "# {mark} ANSIBLE MANAGED BLOCK"
```

### 👤 Usuarios y Grupos

```yaml
# Crear usuario
- name: Create user
  user:
    name: appuser
    uid: 1001
    group: appgroup
    shell: /bin/bash
    home: /home/appuser
    create_home: yes
    state: present

# Crear grupo
- name: Create group
  group:
    name: appgroup
    gid: 1001
    state: present
```

### 🔧 Servicios

```yaml
# Gestionar servicio
- name: Start nginx
  service:
    name: nginx
    state: started
    enabled: yes

# Systemd
- name: Reload systemd
  systemd:
    daemon_reload: yes

- name: Enable service
  systemd:
    name: myapp
    enabled: yes
    state: started
```

### 💻 Comandos y Scripts

```yaml
# Comando simple
- name: Run command
  command: /usr/bin/uptime
  register: uptime_result

# Shell (con pipes y redirects)
- name: Run shell command
  shell: echo "test" | grep test > /tmp/output.txt

# Script
- name: Run script
  script: scripts/deploy.sh
  args:
    creates: /tmp/deployed.flag
```

### 🌐 Git

```yaml
# Clonar repositorio
- name: Clone repository
  git:
    repo: https://github.com/user/repo.git
    dest: /app/repo
    version: main
    force: yes
```

### 🐳 Docker

```yaml
# Contenedor Docker
- name: Run nginx container
  docker_container:
    name: nginx
    image: nginx:latest
    state: started
    ports:
      - "80:80"
    volumes:
      - /host/data:/data
```

---

## 7. Troubleshooting

### 🔍 Debug y Testing

```yaml
# Debug
- name: Show variable
  debug:
    var: my_variable

- name: Show message
  debug:
    msg: "Value is {{ my_variable }}"

# Assert
- name: Verify condition
  assert:
    that:
      - ansible_distribution == "Ubuntu"
      - ansible_distribution_version >= "20.04"
    fail_msg: "Unsupported OS"

# Failed when
- name: Check status
  command: systemctl status nginx
  register: result
  failed_when: "'failed' in result.stdout"

# Changed when
- name: Check config
  command: cat /etc/config
  register: config
  changed_when: false
```

### 🐛 Comandos de Troubleshooting

```bash
# Syntax check
ansible-playbook playbook.yml --syntax-check

# Dry run
ansible-playbook playbook.yml --check

# Ver cambios
ansible-playbook playbook.yml --check --diff

# Modo verbose
ansible-playbook playbook.yml -vvv

# Step mode (confirmar cada task)
ansible-playbook playbook.yml --step

# Listar tasks
ansible-playbook playbook.yml --list-tasks
ansible-playbook playbook.yml --list-tags

# Probar conexión
ansible all -m ping -i inventory.ini
ansible all -m setup -i inventory.ini  # Gather facts
```

---

## 📝 Comandos Esenciales

```bash
# Ejecución
ansible-playbook playbook.yml
ansible-playbook -i inventory.ini playbook.yml
ansible-playbook playbook.yml --check --diff
ansible-playbook playbook.yml -e "var=value"
ansible-playbook playbook.yml --tags "tag1,tag2"
ansible-playbook playbook.yml --limit host1

# Ad-hoc
ansible all -m ping
ansible webservers -m command -a "uptime"
ansible all -m setup
ansible all -m shell -a "df -h"

# Inventario
ansible-inventory --list
ansible all --list-hosts

# Roles
ansible-galaxy init rolename
ansible-galaxy install username.rolename

# Vault (secrets)
ansible-vault create secrets.yml
ansible-vault edit secrets.yml
ansible-vault encrypt file.yml
ansible-vault decrypt file.yml
ansible-playbook playbook.yml --ask-vault-pass
```

---

## 🎓 Preguntas Típicas

1. **¿Qué es idempotencia?**
   - Ejecutar múltiples veces produce el mismo resultado

2. **¿Diferencia entre copy y template?**
   - copy: archivos estáticos
   - template: procesados con Jinja2

3. **¿Cuándo usar command vs shell?**
   - command: comandos simples, más seguro
   - shell: cuando necesitas pipes, redirects

4. **¿Qué hace un handler?**
   - Task que se ejecuta cuando es notificado
   - Se ejecuta al final del playbook
   - Útil para reiniciar servicios

---

## 🔗 Recursos

- [Ansible Documentation](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/)
- [Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)

---

**💡 Consejo:** Practica creando roles y playbooks. El test evaluará comprensión de estructura y ejecución.
