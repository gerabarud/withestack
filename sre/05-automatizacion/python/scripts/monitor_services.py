#!/usr/bin/env python3
"""
monitor_services.py - Monitor de servicios con alertas
Monitorea servicios, APIs y recursos del sistema
"""

import os
import sys
import time
import psutil
import requests
import smtplib
import logging
from email.mime.text import MIMEText
from datetime import datetime
from typing import List, Dict, Tuple

# Configuración
CONFIG = {
    'cpu_threshold': 80,
    'memory_threshold': 85,
    'disk_threshold': 85,
    'alert_email': 'admin@example.com',
    'smtp_server': 'localhost',
    'check_interval': 60,  # segundos
}

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('/var/log/monitor_services.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class SystemMonitor:
    """Monitor de recursos del sistema"""
    
    def __init__(self):
        self.alerts = []
    
    def check_cpu(self) -> Tuple[bool, float]:
        """Verificar uso de CPU"""
        cpu_percent = psutil.cpu_percent(interval=1)
        
        if cpu_percent > CONFIG['cpu_threshold']:
            msg = f"CPU usage alto: {cpu_percent}%"
            logger.warning(msg)
            self.alerts.append(msg)
            return False, cpu_percent
        
        logger.info(f"CPU usage: {cpu_percent}%")
        return True, cpu_percent
    
    def check_memory(self) -> Tuple[bool, float]:
        """Verificar uso de memoria"""
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        
        if memory_percent > CONFIG['memory_threshold']:
            msg = f"Memoria alta: {memory_percent}%"
            logger.warning(msg)
            self.alerts.append(msg)
            return False, memory_percent
        
        logger.info(f"Memoria: {memory_percent}%")
        return True, memory_percent
    
    def check_disk(self) -> Tuple[bool, List[Dict]]:
        """Verificar uso de disco"""
        issues = []
        disk_info = []
        
        for partition in psutil.disk_partitions():
            if 'loop' in partition.device or 'snap' in partition.mountpoint:
                continue
            
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info.append({
                    'mountpoint': partition.mountpoint,
                    'percent': usage.percent,
                    'free': usage.free / (1024**3),  # GB
                })
                
                if usage.percent > CONFIG['disk_threshold']:
                    msg = f"Disco lleno en {partition.mountpoint}: {usage.percent}%"
                    logger.warning(msg)
                    self.alerts.append(msg)
                    issues.append(msg)
                else:
                    logger.info(f"Disco {partition.mountpoint}: {usage.percent}%")
            
            except PermissionError:
                continue
        
        return len(issues) == 0, disk_info
    
    def check_load_average(self) -> Tuple[bool, float]:
        """Verificar load average"""
        load_avg = os.getloadavg()[0]  # 1-minute load
        cpu_count = psutil.cpu_count()
        threshold = cpu_count * 2
        
        if load_avg > threshold:
            msg = f"Load average alto: {load_avg:.2f} (CPUs: {cpu_count})"
            logger.warning(msg)
            self.alerts.append(msg)
            return False, load_avg
        
        logger.info(f"Load average: {load_avg:.2f}")
        return True, load_avg
    
    def get_top_processes_by_cpu(self, limit=5) -> List[Dict]:
        """Obtener procesos con mayor uso de CPU"""
        processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # Ordenar por CPU
        processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
        return processes[:limit]
    
    def get_top_processes_by_memory(self, limit=5) -> List[Dict]:
        """Obtener procesos con mayor uso de memoria"""
        processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # Ordenar por memoria
        processes.sort(key=lambda x: x['memory_percent'], reverse=True)
        return processes[:limit]


class ServiceMonitor:
    """Monitor de servicios"""
    
    def __init__(self):
        self.alerts = []
    
    def check_service(self, service_name: str) -> bool:
        """Verificar si un servicio systemd está running"""
        try:
            # Usando systemctl
            result = os.system(f'systemctl is-active --quiet {service_name}')
            
            if result == 0:
                logger.info(f"Servicio {service_name}: running")
                return True
            else:
                msg = f"Servicio {service_name}: NOT running"
                logger.error(msg)
                self.alerts.append(msg)
                return False
        
        except Exception as e:
            logger.error(f"Error verificando {service_name}: {e}")
            return False
    
    def check_port(self, port: int) -> bool:
        """Verificar si un puerto está escuchando"""
        for conn in psutil.net_connections():
            if conn.laddr.port == port and conn.status == 'LISTEN':
                logger.info(f"Puerto {port}: listening")
                return True
        
        msg = f"Puerto {port}: NOT listening"
        logger.error(msg)
        self.alerts.append(msg)
        return False
    
    def check_http_endpoint(self, url: str, timeout: int = 5) -> Tuple[bool, int]:
        """Verificar endpoint HTTP"""
        try:
            response = requests.get(url, timeout=timeout)
            status_code = response.status_code
            
            if 200 <= status_code < 300:
                logger.info(f"Endpoint {url}: OK (status {status_code})")
                return True, status_code
            else:
                msg = f"Endpoint {url}: status {status_code}"
                logger.warning(msg)
                self.alerts.append(msg)
                return False, status_code
        
        except requests.exceptions.Timeout:
            msg = f"Endpoint {url}: timeout"
            logger.error(msg)
            self.alerts.append(msg)
            return False, 0
        
        except requests.exceptions.RequestException as e:
            msg = f"Endpoint {url}: error - {str(e)}"
            logger.error(msg)
            self.alerts.append(msg)
            return False, 0


class AlertManager:
    """Gestor de alertas"""
    
    @staticmethod
    def send_email(subject: str, body: str):
        """Enviar email de alerta"""
        try:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = 'monitor@system'
            msg['To'] = CONFIG['alert_email']
            
            with smtplib.SMTP(CONFIG['smtp_server']) as server:
                server.send_message(msg)
            
            logger.info(f"Email enviado a {CONFIG['alert_email']}")
        
        except Exception as e:
            logger.error(f"Error enviando email: {e}")
    
    @staticmethod
    def send_alerts(alerts: List[str]):
        """Enviar todas las alertas acumuladas"""
        if not alerts:
            logger.info("No hay alertas que enviar")
            return
        
        hostname = os.uname().nodename
        subject = f"Alertas de Sistema - {hostname}"
        body = f"Alertas detectadas en {hostname}:\n\n"
        body += "\n".join(f"- {alert}" for alert in alerts)
        body += f"\n\nFecha: {datetime.now()}"
        
        logger.warning(f"Enviando {len(alerts)} alertas")
        AlertManager.send_email(subject, body)


def generate_report(system_monitor: SystemMonitor) -> str:
    """Generar reporte del sistema"""
    report = []
    report.append("=" * 50)
    report.append(f"System Monitor Report - {datetime.now()}")
    report.append("=" * 50)
    
    # System info
    report.append(f"\nHostname: {os.uname().nodename}")
    report.append(f"Uptime: {time.time() - psutil.boot_time():.0f} seconds")
    
    # CPU
    _, cpu = system_monitor.check_cpu()
    report.append(f"CPU Usage: {cpu:.1f}%")
    
    # Memory
    _, mem = system_monitor.check_memory()
    report.append(f"Memory Usage: {mem:.1f}%")
    
    # Disk
    _, disks = system_monitor.check_disk()
    report.append("\nDisk Usage:")
    for disk in disks:
        report.append(f"  {disk['mountpoint']}: {disk['percent']:.1f}% (Free: {disk['free']:.1f} GB)")
    
    # Load
    _, load = system_monitor.check_load_average()
    report.append(f"\nLoad Average: {load:.2f}")
    
    # Top processes
    report.append("\nTop 5 Processes by CPU:")
    for proc in system_monitor.get_top_processes_by_cpu():
        report.append(f"  {proc['name']} (PID {proc['pid']}): {proc['cpu_percent']:.1f}%")
    
    report.append("\nTop 5 Processes by Memory:")
    for proc in system_monitor.get_top_processes_by_memory():
        report.append(f"  {proc['name']} (PID {proc['pid']}): {proc['memory_percent']:.1f}%")
    
    report.append("=" * 50)
    
    return "\n".join(report)


def main():
    """Main function"""
    logger.info("Iniciando monitor de servicios")
    
    # Inicializar monitores
    system_monitor = SystemMonitor()
    service_monitor = ServiceMonitor()
    
    # Verificar sistema
    system_monitor.check_cpu()
    system_monitor.check_memory()
    system_monitor.check_disk()
    system_monitor.check_load_average()
    
    # Verificar servicios críticos
    services = ['docker', 'nginx', 'sshd']
    for service in services:
        service_monitor.check_service(service)
    
    # Verificar puertos
    ports = [22, 80, 443]
    for port in ports:
        service_monitor.check_port(port)
    
    # Verificar endpoints HTTP
    endpoints = [
        'http://localhost/health',
        'http://localhost:8080/api/health',
    ]
    for endpoint in endpoints:
        service_monitor.check_http_endpoint(endpoint)
    
    # Generar reporte
    report = generate_report(system_monitor)
    print(report)
    
    # Consolidar alertas
    all_alerts = system_monitor.alerts + service_monitor.alerts
    
    # Enviar alertas si hay
    if all_alerts:
        AlertManager.send_alerts(all_alerts)
        sys.exit(1)
    else:
        logger.info("Monitor completado sin problemas")
        sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Monitor detenido por usuario")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Error inesperado: {e}", exc_info=True)
        sys.exit(1)
