# 🏗️ Terraform - Infrastructure as Code

## 📚 Índice
1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [Sintaxis HCL](#sintaxis-hcl)
3. [Providers y Recursos](#providers-y-recursos)
4. [Variables y Outputs](#variables-y-outputs)
5. [State Management](#state-management)
6. [Módulos](#módulos)
7. [Troubleshooting](#troubleshooting)

---

## 1. Conceptos Fundamentales

### 🎯 ¿Qué es Terraform?

Terraform es una herramienta de Infrastructure as Code (IaC) que permite:
- Definir infraestructura en código
- Provisionar recursos en múltiples providers
- Gestionar el ciclo de vida de la infraestructura
- Trabajar con estado compartido

**Componentes clave:**
- **Provider**: Plugin para interactuar con APIs (AWS, Azure, GCP, etc.)
- **Resource**: Componente de infraestructura (VM, red, disco)
- **Data Source**: Información de recursos existentes
- **Module**: Conjunto reutilizable de recursos
- **State**: Registro del estado actual de la infraestructura

### 🔄 Workflow Terraform

```bash
# 1. Inicializar (descargar providers)
terraform init

# 2. Planear (ver cambios)
terraform plan

# 3. Aplicar (ejecutar cambios)
terraform apply

# 4. Destruir (eliminar recursos)
terraform destroy
```

---

## 2. Sintaxis HCL

### 📝 Estructura Básica

```hcl
# main.tf

# Provider configuration
terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Resource
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  tags = {
    Name = "WebServer"
    Env  = "Production"
  }
}

# Data source
data "aws_ami" "ubuntu" {
  most_recent = true
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
  
  owners = ["099720109477"]
}

# Output
output "instance_ip" {
  value = aws_instance.web.public_ip
}
```

### 🔤 Tipos de Bloques

```hcl
# Terraform block - configuración global
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}

# Variable block
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

# Local values
locals {
  common_tags = {
    Project = "MyApp"
    Env     = var.environment
  }
}

# Module block
module "vpc" {
  source = "./modules/vpc"
  
  cidr_block = "10.0.0.0/16"
  tags       = local.common_tags
}
```

---

## 3. Providers y Recursos

### ☁️ AWS Provider Example

```hcl
# providers.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region     = var.aws_region
  access_key = var.aws_access_key  # Mejor usar AWS CLI config
  secret_key = var.aws_secret_key  # o variables de entorno
}

# Multiple providers (multi-region)
provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

# Use specific provider
resource "aws_instance" "west_server" {
  provider = aws.west
  
  ami           = "ami-123456"
  instance_type = "t2.micro"
}
```

### 🖥️ Recursos Comunes

```hcl
# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "main-vpc"
  }
}

# Subnet
resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
  
  map_public_ip_on_launch = true
  
  tags = {
    Name = "public-subnet"
  }
}

# Security Group
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group for web servers"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    description = "HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    description = "HTTPS from anywhere"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "web-sg"
  }
}

# EC2 Instance
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  subnet_id     = aws_subnet.public.id
  
  vpc_security_group_ids = [aws_security_group.web.id]
  
  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y nginx
              systemctl start nginx
              EOF
  
  tags = {
    Name = "web-server"
  }
}

# EBS Volume
resource "aws_ebs_volume" "data" {
  availability_zone = aws_instance.web.availability_zone
  size              = 20
  
  tags = {
    Name = "data-volume"
  }
}

resource "aws_volume_attachment" "data_attach" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.data.id
  instance_id = aws_instance.web.id
}
```

### 🔗 Referencias entre Recursos

```hcl
# Implicit dependency (reference)
resource "aws_instance" "web" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public.id  # Referencia
}

# Explicit dependency
resource "aws_instance" "app" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
  
  depends_on = [
    aws_security_group.web,
    aws_subnet.public
  ]
}
```

---

## 4. Variables y Outputs

### 📊 Variables

```hcl
# variables.tf
variable "environment" {
  description = "Environment name"
  type        = string
  default     = "development"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
  
  validation {
    condition     = contains(["t2.micro", "t2.small", "t2.medium"], var.instance_type)
    error_message = "Instance type must be t2.micro, t2.small, or t2.medium."
  }
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

variable "tags" {
  description = "Resource tags"
  type        = map(string)
  default = {
    Project = "MyApp"
    Managed = "Terraform"
  }
}

variable "server_config" {
  description = "Server configuration"
  type = object({
    instance_type = string
    disk_size     = number
    enable_backup = bool
  })
  default = {
    instance_type = "t2.micro"
    disk_size     = 20
    enable_backup = true
  }
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}
```

**Formas de asignar variables:**

```bash
# 1. Archivo terraform.tfvars
# terraform.tfvars
environment = "production"
instance_type = "t2.small"

# 2. Archivo .tfvars específico
terraform apply -var-file="prod.tfvars"

# 3. Línea de comandos
terraform apply -var="instance_type=t2.small"

# 4. Variables de entorno
export TF_VAR_instance_type="t2.small"
terraform apply

# 5. Interactivo (si no está definida)
terraform apply
# > var.instance_type
#   Enter a value:
```

### 📤 Outputs

```hcl
# outputs.tf
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.web.id
}

output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.web.public_ip
}

output "instance_private_ip" {
  description = "Private IP of the EC2 instance"
  value       = aws_instance.web.private_ip
  sensitive   = false
}

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

# Output from module
output "vpc_cidr" {
  value = module.vpc.vpc_cidr_block
}
```

```bash
# Ver outputs
terraform output
terraform output instance_public_ip
terraform output -json
```

---

## 5. State Management

### 💾 Terraform State

El state file (`terraform.tfstate`) almacena el estado actual de la infraestructura.

```bash
# Ver state
terraform show
terraform state list
terraform state show aws_instance.web

# Manipular state
terraform state mv aws_instance.old aws_instance.new
terraform state rm aws_instance.web
terraform state pull > backup.tfstate
terraform state push backup.tfstate

# Refresh state
terraform refresh
terraform apply -refresh-only
```

### 🗄️ Remote State

```hcl
# Backend S3 (AWS)
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

# Backend Azure
terraform {
  backend "azurerm" {
    resource_group_name  = "terraform-rg"
    storage_account_name = "tfstate"
    container_name       = "tfstate"
    key                  = "prod.terraform.tfstate"
  }
}

# Backend GCS (Google Cloud)
terraform {
  backend "gcs" {
    bucket = "my-terraform-state"
    prefix = "prod"
  }
}
```

```bash
# Inicializar backend
terraform init

# Migrar backend
terraform init -migrate-state

# Reconfigurar backend
terraform init -reconfigure
```

### 🔒 State Locking

```hcl
# DynamoDB table para locking (AWS)
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  
  attribute {
    name = "LockID"
    type = "S"
  }
}
```

---

## 6. Módulos

### 📦 Crear Módulo

```
modules/
└── vpc/
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    └── README.md
```

**modules/vpc/main.tf:**
```hcl
resource "aws_vpc" "main" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support   = var.enable_dns_support
  
  tags = merge(
    var.tags,
    {
      Name = var.vpc_name
    }
  )
}

resource "aws_subnet" "public" {
  count = length(var.public_subnet_cidrs)
  
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.public_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]
  
  map_public_ip_on_launch = true
  
  tags = merge(
    var.tags,
    {
      Name = "${var.vpc_name}-public-${count.index + 1}"
    }
  )
}
```

**modules/vpc/variables.tf:**
```hcl
variable "vpc_name" {
  description = "Name of the VPC"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for VPC"
  type        = string
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
}

variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
}

variable "enable_dns_hostnames" {
  description = "Enable DNS hostnames"
  type        = bool
  default     = true
}

variable "enable_dns_support" {
  description = "Enable DNS support"
  type        = bool
  default     = true
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}
```

**modules/vpc/outputs.tf:**
```hcl
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "vpc_cidr_block" {
  description = "CIDR block of the VPC"
  value       = aws_vpc.main.cidr_block
}

output "public_subnet_ids" {
  description = "IDs of public subnets"
  value       = aws_subnet.public[*].id
}
```

### 🎮 Usar Módulo

```hcl
# main.tf
module "vpc" {
  source = "./modules/vpc"
  
  vpc_name             = "production-vpc"
  cidr_block           = "10.0.0.0/16"
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24"]
  availability_zones   = ["us-east-1a", "us-east-1b"]
  
  tags = {
    Environment = "production"
    Project     = "myapp"
  }
}

# Usar outputs del módulo
resource "aws_instance" "web" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
  subnet_id     = module.vpc.public_subnet_ids[0]
}

output "vpc_id" {
  value = module.vpc.vpc_id
}
```

---

## 7. Troubleshooting

### 🔍 Comandos de Debugging

```bash
# Validar sintaxis
terraform validate

# Formatear código
terraform fmt
terraform fmt -recursive

# Ver plan detallado
terraform plan -out=tfplan
terraform show tfplan

# Aplicar con log
TF_LOG=DEBUG terraform apply
TF_LOG=TRACE terraform apply
TF_LOG_PATH=terraform.log terraform apply

# Graph (dependencias)
terraform graph | dot -Tpng > graph.png

# Console interactivo
terraform console
> aws_instance.web.public_ip
> var.instance_type
```

### 🐛 Problemas Comunes

**1. State lock:**
```bash
# Forzar unlock (usar con cuidado)
terraform force-unlock <LOCK_ID>
```

**2. State drift:**
```bash
# Refresh state
terraform refresh
terraform apply -refresh-only

# Comparar
terraform plan
```

**3. Import recursos existentes:**
```bash
# Importar recurso
terraform import aws_instance.web i-1234567890abcdef0

# Generar configuración (Terraform 1.5+)
terraform plan -generate-config-out=generated.tf
```

**4. Destruir recurso específico:**
```bash
terraform destroy -target=aws_instance.web
```

---

## 📝 Comandos Esenciales

```bash
# Inicialización
terraform init
terraform init -upgrade

# Planificación
terraform plan
terraform plan -out=tfplan
terraform plan -destroy

# Aplicación
terraform apply
terraform apply -auto-approve
terraform apply tfplan

# Destrucción
terraform destroy
terraform destroy -auto-approve
terraform destroy -target=resource

# State
terraform state list
terraform state show resource
terraform state rm resource
terraform state mv source dest

# Outputs
terraform output
terraform output name

# Formato y validación
terraform fmt
terraform validate

# Workspace
terraform workspace list
terraform workspace new dev
terraform workspace select prod
```

---

## 🎓 Preguntas Típicas

1. **¿Qué es el state de Terraform?**
   - Archivo que mapea configuración con recursos reales
   - Almacena metadata y estado actual

2. **¿Diferencia entre plan y apply?**
   - plan: muestra cambios sin aplicar
   - apply: ejecuta los cambios

3. **¿Para qué sirven los módulos?**
   - Reutilizar configuración
   - Organizar código
   - Abstracción y encapsulación

4. **¿Cómo manejar secretos?**
   - Variables sensibles
   - Vault/secrets managers
   - Backends cifrados

5. **¿Qué es un provider?**
   - Plugin que interactúa con APIs
   - Define recursos disponibles

---

## 🔗 Recursos

- [Terraform Documentation](https://www.terraform.io/docs/)
- [Terraform Registry](https://registry.terraform.io/)
- [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

---

**💡 Consejo:** Practica creando infraestructura simple. El test evaluará comprensión de workflow y troubleshooting.
