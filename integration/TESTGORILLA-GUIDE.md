# 📝 Guía Específica para TestGorilla

## 🎯 ¿Qué es TestGorilla?

TestGorilla es una plataforma de evaluación pre-empleo que usa tests estandarizados para evaluar habilidades técnicas de candidatos.

## 📊 Formato del Test

### Tipos de Preguntas

1. **Selección Múltiple (40%)**
   - Una o varias respuestas correctas
   - Basadas en conocimiento conceptual
   - Tiempo: ~2 min por pregunta

2. **Escenarios Prácticos (30%)**
   - Situaciones reales de trabajo
   - Troubleshooting y resolución de problemas
   - Tiempo: ~3 min por escenario

3. **Análisis de Código/Config (20%)**
   - Identificar errores
   - Interpretar configuraciones
   - Tiempo: ~3 min por pregunta

4. **Evaluación Cognitiva (10%)**
   - Razonamiento lógico
   - Resolución de problemas
   - Tiempo: ~1 min por pregunta

### ⏱️ Tiempo y Estructura

- **Duración total:** 45-60 minutos
- **Número de preguntas:** 20-30
- **Sin pausas:** Debes completar en una sesión
- **No se puede retroceder:** Marca si dudas y avanza

## 🎓 Qué Evalúa para Cloud Integration Engineer

### Alta Prioridad (60%)

1. **Linux Administration**
   - Comandos de red (ip, iptables, netstat)
   - Gestión de servicios (systemd)
   - Troubleshooting
   - Bash scripting básico

2. **Kubernetes**
   - Pods, Deployments, Services
   - Debugging (logs, describe, events)
   - ConfigMaps y Secrets
   - Health checks (probes)

3. **Docker**
   - Dockerfile
   - Comandos básicos
   - Volúmenes y networks
   - Troubleshooting

4. **Networking**
   - VLANs
   - Routing
   - IPTables
   - Diagnóstico (ping, traceroute, tcpdump)

### Media Prioridad (30%)

5. **Ansible**
   - Playbooks básicos
   - Roles y estructura
   - Variables
   - Idempotencia

6. **Terraform**
   - Workflow (init, plan, apply)
   - State management
   - Resources básicos

7. **Git**
   - Rebase y merge
   - Cherry-pick
   - Resolución de conflictos

### Baja Prioridad (10%)

8. **OpenStack**
   - Componentes principales
   - Comandos básicos

9. **Monitoreo**
   - Grafana, Kibana conceptos
   - Uso básico

## 🎯 Estrategia para el Test

### Antes del Test

**1 semana antes:**
- [ ] Repasa README de cada carpeta
- [ ] Practica comandos en terminal
- [ ] Crea VMs/contenedores de prueba
- [ ] Haz ejercicios de la carpeta 10

**1 día antes:**
- [ ] Repasa CHEATSHEET.md
- [ ] Duerme bien
- [ ] Prepara ambiente tranquilo

**Antes de empezar:**
- [ ] Cierra distracciones
- [ ] Ten papel y lápiz
- [ ] Usa audífonos si ayuda
- [ ] Verifica internet estable

### Durante el Test

**Gestión de tiempo:**
```
0-10 min:  Preguntas 1-7   (fáciles/conocidas)
10-25 min: Preguntas 8-15  (medias)
25-40 min: Preguntas 16-22 (difíciles)
40-45 min: Revisar marcadas
```

**Estrategias:**

1. **Lee toda la pregunta**
   - No asumas por las primeras palabras
   - Busca palabras clave

2. **Elimina opciones incorrectas**
   - Descarta las obviamente falsas
   - Reduce a 2-3 opciones

3. **No te atasques**
   - Si dudas, marca y continúa
   - Vuelve al final si hay tiempo

4. **Busca patrones**
   - Opciones muy específicas suelen ser correctas
   - "Depende" o "todas" son frecuentes en respuestas correctas

5. **Confía en tu intuición**
   - Si algo "suena mal", probablemente lo es
   - Tu primera respuesta suele ser correcta

## 📚 Preguntas Frecuentes por Tema

### Linux

**P: ¿Cómo verificas qué proceso usa un puerto?**
```bash
ss -tulpn | grep :8080
lsof -i :8080
netstat -tulpn | grep 8080
```

**P: ¿Cómo configuras una IP estática en Ubuntu 20.04?**
```
Editar /etc/netplan/*.yaml y ejecutar netplan apply
```

**P: ¿Diferencia entre systemctl stop y systemctl kill?**
```
stop: SIGTERM graceful
kill: SIGKILL forzado
```

### Kubernetes

**P: Pod en CrashLoopBackOff, ¿qué revisas primero?**
```bash
kubectl logs pod-name --previous
kubectl describe pod pod-name
```

**P: ¿Diferencia entre liveness y readiness probe?**
```
liveness: reinicia si falla
readiness: quita de service si falla
```

**P: ¿Cómo ves los logs de un pod?**
```bash
kubectl logs pod-name
kubectl logs pod-name -c container-name (multi-container)
```

### Docker

**P: ¿Diferencia entre CMD y ENTRYPOINT?**
```
ENTRYPOINT: ejecutable fijo
CMD: argumentos por defecto
```

**P: ¿Cómo optimizas tamaño de imagen?**
```
- Multi-stage build
- Usar alpine
- Limpiar cache en mismo RUN
```

**P: ¿Diferencia entre volume y bind mount?**
```
volume: gestionado por Docker
bind mount: path del host
```

### Networking

**P: ¿Qué es una VLAN?**
```
Red lógica sobre red física, usa tag 802.1Q
```

**P: ¿Cómo habilitas IP forwarding?**
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```

**P: ¿Diferencia entre SNAT y DNAT?**
```
SNAT: modifica IP origen (NAT salida)
DNAT: modifica IP destino (port forward)
```

### Ansible

**P: ¿Qué es idempotencia?**
```
Ejecutar múltiples veces produce mismo resultado
```

**P: ¿Diferencia entre copy y template?**
```
copy: archivos estáticos
template: procesados con Jinja2
```

**P: ¿Para qué sirve un handler?**
```
Task que se ejecuta cuando es notificado
Se ejecuta al final del playbook
```

### Terraform

**P: ¿Qué hace terraform plan?**
```
Muestra cambios sin aplicar
```

**P: ¿Qué es el state?**
```
Archivo que mapea configuración con recursos reales
```

**P: ¿Diferencia entre variables y locals?**
```
variables: input del usuario
locals: valores calculados/intermedios
```

### Git

**P: ¿Diferencia entre merge y rebase?**
```
merge: conserva historial, crea merge commit
rebase: reescribe historial, queda lineal
```

**P: ¿Cuándo usar cherry-pick?**
```
Para aplicar commits específicos a otra rama
Útil para hotfixes
```

**P: ¿Diferencia entre reset y revert?**
```
reset: reescribe historial (privado)
revert: crea commit nuevo (público)
```

## ⚠️ Errores Comunes a Evitar

1. **Asumir sin leer**
   - Lee toda la pregunta antes de responder

2. **Sobre-pensar**
   - Las respuestas suelen ser directas

3. **Cambiar respuestas**
   - Solo si estás seguro del error

4. **Quedarse atascado**
   - Marca y avanza

5. **No gestionar tiempo**
   - Revisa el reloj cada 10 preguntas

## 🎯 Simulación de Preguntas

### Pregunta 1 (Fácil)
**¿Cuál comando muestra los pods en Kubernetes?**

A) `kubectl list pods`  
B) `kubectl get pods` ✓  
C) `kubectl show pods`  
D) `kubectl ps`

**Explicación:** El comando básico es `kubectl get <resource>`

---

### Pregunta 2 (Media)
**Un contenedor está en estado "CrashLoopBackOff". ¿Cuál es la MEJOR forma de diagnosticar?**

A) Reiniciar el contenedor  
B) Ver los logs del contenedor anterior ✓  
C) Eliminar y recrear el pod  
D) Verificar la imagen

**Explicación:** `kubectl logs pod --previous` muestra logs del crash

---

### Pregunta 3 (Difícil)
**Necesitas que un pod espere a que MySQL esté listo antes de iniciar. ¿Qué usas?**

A) Liveness probe  
B) Readiness probe  
C) Init container ✓  
D) postStart hook

**Explicación:** Init containers se ejecutan antes y deben completarse exitosamente

---

### Pregunta 4 (Escenario)
**Un servicio web no responde. Los pods están "Running" pero las peticiones fallan. ¿Qué revisas?**

A) Logs de los pods  
B) Readiness probe ✓  
C) Recursos del cluster  
D) Imagen del contenedor

**Explicación:** Si readiness probe falla, el pod no recibe tráfico del Service

---

## 📊 Scoring y Resultados

**Rangos típicos:**
- 85-100%: Excelente
- 70-84%: Bueno
- 60-69%: Aceptable
- <60%: Insuficiente

**Whitestack probablemente busca:** >70%

## 🎁 Recursos de Último Minuto

**Lee antes del test:**
1. [CHEATSHEET.md](./CHEATSHEET.md)
2. Sección "Comandos Esenciales" de cada guía
3. "Preguntas Típicas" de cada guía

**Practica 30 min antes:**
```bash
# Kubernetes
kubectl get pods
kubectl describe pod
kubectl logs pod

# Docker
docker ps
docker logs container
docker exec -it container sh

# Linux
systemctl status nginx
journalctl -u nginx
ss -tulpn
```

## 💡 Último Consejo

**Confía en tu preparación.** Has estudiado el material necesario. Durante el test:

1. Mantén la calma
2. Lee cuidadosamente
3. Gestiona tu tiempo
4. Confía en tu conocimiento

**¡Mucha suerte! 🍀**

---

**Creado para:** Cloud Integration Engineer @ Whitestack  
**Fecha:** Diciembre 2025  
**Última actualización:** Antes de tu test
