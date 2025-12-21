# 🚀 CI/CD y GitOps - Guía Práctica

## 🎯 ¿Qué es CI/CD?

**CI (Continuous Integration)**: Integrar código frecuentemente con tests automáticos  
**CD (Continuous Delivery)**: Deploy automático a ambientes (staging, producción)

---

## 🔄 GitLab CI - Lo más usado en empresas

### Archivo: `.gitlab-ci.yml`

```yaml
# Stages del pipeline
stages:
  - test
  - build
  - deploy

# Variables globales
variables:
  DOCKER_REGISTRY: "registry.example.com"
  APP_NAME: "myapp"

# Job: Tests
test:
  stage: test
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - pytest tests/
    - flake8 .
  coverage: '/TOTAL.*\s+(\d+%)$/'
  only:
    - merge_requests
    - main

# Job: Build Docker Image
build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $DOCKER_REGISTRY
    - docker build -t $DOCKER_REGISTRY/$APP_NAME:$CI_COMMIT_SHA .
    - docker build -t $DOCKER_REGISTRY/$APP_NAME:latest .
    - docker push $DOCKER_REGISTRY/$APP_NAME:$CI_COMMIT_SHA
    - docker push $DOCKER_REGISTRY/$APP_NAME:latest
  only:
    - main

# Job: Deploy to Staging
deploy_staging:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context staging
    - kubectl set image deployment/$APP_NAME $APP_NAME=$DOCKER_REGISTRY/$APP_NAME:$CI_COMMIT_SHA
    - kubectl rollout status deployment/$APP_NAME
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - main

# Job: Deploy to Production (manual)
deploy_production:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context production
    - kubectl set image deployment/$APP_NAME $APP_NAME=$DOCKER_REGISTRY/$APP_NAME:$CI_COMMIT_SHA
    - kubectl rollout status deployment/$APP_NAME
  environment:
    name: production
    url: https://example.com
  when: manual  # Requiere aprobación manual
  only:
    - main
```

---

### GitLab CI - Ejemplos Avanzados

#### Pipeline con Tests, Security Scan, y Deploy

```yaml
stages:
  - test
  - security
  - build
  - deploy

# Tests unitarios
unit_tests:
  stage: test
  image: node:18-alpine
  script:
    - npm ci
    - npm run test:unit
  coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

# Tests de integración
integration_tests:
  stage: test
  image: node:18-alpine
  services:
    - postgres:14
    - redis:7
  variables:
    DATABASE_URL: "postgresql://test:test@postgres:5432/testdb"
    REDIS_URL: "redis://redis:6379"
  script:
    - npm ci
    - npm run test:integration

# Lint
lint:
  stage: test
  image: node:18-alpine
  script:
    - npm ci
    - npm run lint
    - npm run format:check

# Security scan con Trivy
security_scan:
  stage: security
  image: aquasec/trivy:latest
  script:
    - trivy image --severity HIGH,CRITICAL $DOCKER_REGISTRY/$APP_NAME:latest
  allow_failure: true

# SAST (Static Application Security Testing)
sast:
  stage: security
  image: returntocorp/semgrep
  script:
    - semgrep --config=auto --json --output=sast-report.json .
  artifacts:
    reports:
      sast: sast-report.json

# Build multi-arch
build_multiarch:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $DOCKER_REGISTRY
    - docker buildx create --use
  script:
    - docker buildx build \
        --platform linux/amd64,linux/arm64 \
        --tag $DOCKER_REGISTRY/$APP_NAME:$CI_COMMIT_SHA \
        --tag $DOCKER_REGISTRY/$APP_NAME:latest \
        --push .
  only:
    - main

# Deploy con Helm
deploy_helm:
  stage: deploy
  image: alpine/helm:latest
  script:
    - helm upgrade --install $APP_NAME ./helm-chart \
        --set image.tag=$CI_COMMIT_SHA \
        --set ingress.host=staging.example.com \
        --namespace staging \
        --create-namespace \
        --wait
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - main
```

---

## 🔧 GitHub Actions

### Archivo: `.github/workflows/ci.yml`

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # Tests
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov flake8
      
      - name: Run tests
        run: |
          pytest --cov=. --cov-report=xml
      
      - name: Lint
        run: flake8 .
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml

  # Build Docker Image
  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.event_name == 'push'
    permissions:
      contents: read
      packages: write
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Log in to Container Registry
        uses: docker/login-action@v2
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v4
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=sha,prefix={{branch}}-
            type=semver,pattern={{version}}
      
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}

  # Deploy to staging
  deploy_staging:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment:
      name: staging
      url: https://staging.example.com
    
    steps:
      - name: Deploy to Kubernetes
        uses: azure/k8s-deploy@v4
        with:
          namespace: staging
          manifests: |
            k8s/deployment.yaml
            k8s/service.yaml
          images: |
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
```

---

## 🎯 Jenkins Pipeline

### Jenkinsfile (Declarative)

```groovy
pipeline {
    agent any
    
    environment {
        DOCKER_REGISTRY = 'registry.example.com'
        APP_NAME = 'myapp'
        DOCKER_CREDENTIALS = credentials('docker-registry-creds')
        KUBECONFIG = credentials('kubeconfig')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    pip install -r requirements.txt
                    pytest tests/ --junitxml=test-results.xml
                    flake8 . --output-file=flake8-report.txt
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REGISTRY}", 'docker-registry-creds') {
                        def app = docker.build("${APP_NAME}:${BUILD_NUMBER}")
                        app.push()
                        app.push('latest')
                    }
                }
            }
        }
        
        stage('Security Scan') {
            steps {
                sh "trivy image ${DOCKER_REGISTRY}/${APP_NAME}:${BUILD_NUMBER}"
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    kubectl --kubeconfig=$KUBECONFIG set image \
                        deployment/${APP_NAME} \
                        ${APP_NAME}=${DOCKER_REGISTRY}/${APP_NAME}:${BUILD_NUMBER} \
                        -n staging
                    
                    kubectl --kubeconfig=$KUBECONFIG rollout status \
                        deployment/${APP_NAME} \
                        -n staging
                '''
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy to production?', ok: 'Deploy'
                
                sh '''
                    kubectl --kubeconfig=$KUBECONFIG set image \
                        deployment/${APP_NAME} \
                        ${APP_NAME}=${DOCKER_REGISTRY}/${APP_NAME}:${BUILD_NUMBER} \
                        -n production
                    
                    kubectl --kubeconfig=$KUBECONFIG rollout status \
                        deployment/${APP_NAME} \
                        -n production
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            slackSend(
                color: 'good',
                message: "Deployment successful: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
            )
        }
        failure {
            slackSend(
                color: 'danger',
                message: "Deployment failed: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
            )
        }
    }
}
```

---

## 🔐 Best Practices CI/CD

### 1. Secrets Management

```yaml
# GitLab CI - usando variables protegidas
deploy:
  script:
    - echo $DB_PASSWORD | docker login --username $DB_USER --password-stdin
  only:
    - main

# GitHub Actions - usando secrets
- name: Login
  env:
    PASSWORD: ${{ secrets.DB_PASSWORD }}
  run: echo "$PASSWORD" | docker login --username user --password-stdin
```

### 2. Caching Dependencies

```yaml
# GitLab CI
test:
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
      - .pip-cache/
  before_script:
    - pip install --cache-dir .pip-cache -r requirements.txt

# GitHub Actions
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

### 3. Matrix Testing

```yaml
# GitLab CI
test:
  parallel:
    matrix:
      - PYTHON_VERSION: ['3.9', '3.10', '3.11']
        NODE_VERSION: ['16', '18', '20']
  image: python:${PYTHON_VERSION}
  script:
    - pytest

# GitHub Actions
test:
  strategy:
    matrix:
      python-version: [3.9, '3.10', 3.11]
      os: [ubuntu-latest, macos-latest, windows-latest]
  runs-on: ${{ matrix.os }}
  steps:
    - uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
```

---

## 🎯 GitOps con ArgoCD

### Application Manifest

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  
  source:
    repoURL: https://github.com/company/myapp
    targetRevision: main
    path: k8s/overlays/production
    helm:
      values: |
        image:
          tag: v1.2.3
        replicas: 3
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
  
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  
  syncPolicy:
    automated:
      prune: true      # Eliminar recursos que no están en Git
      selfHeal: true   # Auto-corregir drift
    syncOptions:
      - CreateNamespace=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

---

## 🔄 Pipeline Patterns Comunes

### 1. Blue-Green Deployment

```yaml
# Paso 1: Deploy nueva versión (green)
deploy_green:
  script:
    - kubectl apply -f deployment-green.yaml
    - kubectl wait --for=condition=available deployment/myapp-green

# Paso 2: Smoke tests
smoke_tests:
  script:
    - curl http://myapp-green-service/health
    - ./run-smoke-tests.sh

# Paso 3: Switch traffic
switch_traffic:
  script:
    - kubectl patch service myapp -p '{"spec":{"selector":{"version":"green"}}}'

# Paso 4: Cleanup old version
cleanup:
  script:
    - kubectl delete deployment myapp-blue
```

### 2. Canary Deployment

```yaml
# Paso 1: Deploy canary (10% traffic)
deploy_canary:
  script:
    - kubectl apply -f deployment-canary.yaml
    - kubectl set image deployment/myapp-canary myapp=$IMAGE:$TAG
    - kubectl patch virtualservice myapp -p '{"spec":{"http":[{"route":[{"destination":{"host":"myapp-stable"},"weight":90},{"destination":{"host":"myapp-canary"},"weight":10}]}]}}'

# Paso 2: Monitor metrics
monitor:
  script:
    - ./check-error-rate.sh  # Si error rate OK, continuar
    - ./check-latency.sh

# Paso 3: Increase to 50%
increase_traffic:
  script:
    - kubectl patch virtualservice myapp -p '{"spec":{"http":[{"route":[{"destination":{"host":"myapp-stable"},"weight":50},{"destination":{"host":"myapp-canary"},"weight":50}]}]}}'

# Paso 4: Promote to 100%
promote:
  script:
    - kubectl set image deployment/myapp-stable myapp=$IMAGE:$TAG
    - kubectl delete deployment myapp-canary
```

---

## 📊 Monitoring de Pipelines

### Métricas Clave

```promql
# Pipeline success rate
sum(rate(ci_pipeline_status{status="success"}[1h])) 
/ 
sum(rate(ci_pipeline_status[1h])) * 100

# Pipeline duration
histogram_quantile(0.95, 
  rate(ci_pipeline_duration_seconds_bucket[1h])
)

# Deployment frequency
sum(increase(deployments_total[1d]))

# Lead time (commit to production)
histogram_quantile(0.95, 
  rate(deployment_lead_time_seconds_bucket[1d])
)

# MTTR (Mean Time To Recovery)
avg(incident_resolution_seconds)

# Change failure rate
sum(rate(deployment_status{status="failed"}[7d])) 
/ 
sum(rate(deployment_status[7d])) * 100
```

---

## ✅ Checklist CI/CD

**Pipeline debe incluir:**
- [ ] Tests automáticos (unit, integration)
- [ ] Linting/code quality checks
- [ ] Security scanning (SAST, container scan)
- [ ] Build de artefactos (Docker images)
- [ ] Deploy automático a staging
- [ ] Deploy manual/aprobado a production
- [ ] Rollback automático si falla
- [ ] Notificaciones (Slack, email)
- [ ] Metrics y logging

**Best Practices:**
- [ ] Secrets en variables de entorno/vault, nunca en código
- [ ] Usar caching para dependencias
- [ ] Pipelines rápidos (<10 min ideal)
- [ ] Tests en paralelo cuando sea posible
- [ ] Immutable artifacts (tag de Docker no cambia)
- [ ] Semantic versioning
- [ ] Rollback fácil y rápido
- [ ] Documentar proceso de deploy

---

## 🎓 Conceptos Clave TestGorilla

**P: ¿Qué es CI?**  
R: Integrar código frecuentemente con tests automáticos para detectar bugs temprano

**P: ¿Diferencia entre Continuous Delivery y Continuous Deployment?**  
R: Delivery = listo para producción (manual), Deployment = automático a producción

**P: ¿Qué es GitOps?**  
R: Usar Git como source of truth para infraestructura. Todo cambio via Git.

**P: ¿Qué es un pipeline stage?**  
R: Fase del pipeline (test, build, deploy). Si una falla, se detiene.

**P: ¿Cuándo usar deployment manual vs automático?**  
R: Manual para producción (control), automático para staging/dev (velocidad)
