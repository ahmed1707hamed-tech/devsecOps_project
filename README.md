# 🛡️ DevSecOps CI/CD Pipeline

A complete **DevSecOps project** implementing an automated software delivery lifecycle from source code to secure Kubernetes deployment and monitoring.

The project integrates **CI/CD, security scanning, Docker, Kubernetes, Helm, Argo CD, Prometheus, Grafana, Terraform, and Ansible**.

---

## 🏗️ Architecture

![DevSecOps Architecture](docs/images/devsecops-architecture.png)

### Architecture Flow

```text
Developer
    │
    ▼
  GitHub
    │
    ▼
GitHub Actions
    │
    ├── Pytest
    ├── Gitleaks
    ├── pip-audit
    ├── Docker Build
    └── Trivy
          │
          ▼
      Docker Hub
          │
          ▼
        Argo CD
          │
          ▼
     Kubernetes
       │      │
       ▼      ▼
    Backend PostgreSQL
       │
       ▼
   Prometheus
       │
       ▼
     Grafana

🚀 Project Overview

This project demonstrates a production-style DevSecOps workflow where security is integrated throughout the software development and deployment lifecycle.

The pipeline automatically:

Runs application tests.
Scans the repository for exposed secrets.
Scans Python dependencies for vulnerabilities.
Builds a Docker image.
Scans the Docker image using Trivy.
Pushes the validated image to Docker Hub.
Uses Argo CD for GitOps-based deployment.
Deploys the application to Kubernetes.
Monitors the cluster and application using Prometheus and Grafana.



| Security Stage      | Tool      | Purpose                                 |
| ------------------- | --------- | --------------------------------------- |
| Automated Testing   | Pytest    | Validate application functionality      |
| Secret Scanning     | Gitleaks  | Detect exposed secrets                  |
| Dependency Scanning | pip-audit | Detect vulnerable Python packages       |
| Container Scanning  | Trivy     | Detect vulnerabilities in Docker images |





⚙️ GitHub Actions

The CI/CD workflow is implemented using GitHub Actions.

Pipeline Stages
Code Push
    │
    ▼
Checkout
    │
    ▼
Pytest
    │
    ├──────────────┐
    ▼              ▼
Gitleaks       pip-audit
    │              │
    └──────┬───────┘
           ▼
      Docker Build
           │
           ▼
       Trivy Scan
           │
           ▼
       Docker Hub
Workflow
Checkout source code
Setup Python 3.12
Install dependencies
Run Pytest
Run Gitleaks
Run pip-audit
Build Docker image
Scan Docker image with Trivy
Login to Docker Hub
Push Docker image
🐳 Docker

The backend application is containerized using Docker.

Docker Build
     │
     ▼
Trivy Security Scan
     │
     ▼
Docker Hub
     │
     ▼
Kubernetes
Docker Image
ahmed7amed9/devsecops-backend:latest

The Docker image is automatically built and published through GitHub Actions after passing the required security and testing stages.

☸️ Kubernetes

The application is deployed on Kubernetes.

Kubernetes Components
Deployment
Pods
Services
ConfigMaps
Secrets
Namespace
Helm
Resource Requests and Limits
Application Namespace
devsecops
Running Services
devsecops-backend
devsecops-postgres
Backend Deployment

The backend is configured with multiple replicas for improved availability.

Backend Replicas: 3
Backend Service
Type: NodePort
Port: 8000
NodePort: 30080
⎈ Helm

Helm is used to package and manage the Kubernetes application.

Helm Structure
helm/
└── devsecops/
    ├── Chart.yaml
    ├── values.yaml
    └── templates/
        ├── backend-deployment.yaml
        ├── backend-service.yaml
        ├── postgres-deployment.yaml
        ├── postgres-service.yaml
        └── namespace.yaml
Helm Configuration

The application configuration is controlled through values.yaml.

Example:

backend:
  replicaCount: 3

  image:
    repository: ahmed7amed9/devsecops-backend
    tag: latest

  service:
    type: NodePort
    port: 8000
    targetPort: 8000
    nodePort: 30080
🔁 GitOps with Argo CD

Argo CD is used to implement GitOps-based Continuous Delivery.

Argo CD continuously monitors the GitHub repository and synchronizes the Kubernetes cluster with the desired state stored in Git.

Argo CD Application
Application: devsecops
Namespace: argocd
Source: GitHub
Path: helm/devsecops
Target Revision: main
Destination: Kubernetes Cluster
Current Status
Sync Status: Synced
Health Status: Healthy

This provides automated and reliable Kubernetes deployments whenever the desired state changes in Git.

📊 Monitoring & Observability

The Kubernetes environment is monitored using:

Prometheus
Grafana
Kubernetes Metrics
Node Exporter
kube-state-metrics
Monitoring Architecture
Kubernetes
     │
     ├── Nodes
     ├── Pods
     ├── Deployments
     └── Services
          │
          ▼
      Prometheus
          │
          ▼
       Grafana
🔎 Prometheus

Prometheus collects metrics from the Kubernetes cluster and application workloads.

It monitors:

Kubernetes Nodes
Pods
Deployments
CPU Usage
Memory Usage
Application Metrics
Kubernetes Components

📈 Grafana

Grafana is used to visualize the collected Prometheus metrics.

Dashboards provide visibility into:

CPU Usage
Memory Usage
Pod Status
Node Metrics
Request Rate
Kubernetes Resources
Application Performance
📡 Application Metrics

The backend exposes a Prometheus metrics endpoint:

/metrics

Metrics flow:

Backend
   │
   ├── /metrics
   │
   ▼
Prometheus
   │
   ▼
Grafana

This allows application-level monitoring in addition to infrastructure monitoring.

🗄️ PostgreSQL

PostgreSQL is used as the application's database.

Database: taskdb
User: postgres
Port: 5432
Service: devsecops-postgres

The PostgreSQL service is exposed internally through a Kubernetes ClusterIP service and is accessible by the backend inside the cluster.

🏗️ Infrastructure as Code

Terraform is used for infrastructure provisioning.

Terraform
    │
    ├── VPC
    ├── Subnets
    ├── Internet Gateway
    ├── Route Tables
    ├── Security Groups
    └── EC2

Terraform allows infrastructure to be defined and managed as code, providing reproducible infrastructure deployments.

⚙️ Configuration Management

Ansible is used for automated server configuration and environment preparation.

Typical tasks include:

Installing Docker
Installing Kubernetes
Configuring servers
Creating users
Configuring firewall rules
Installing required tools
Preparing deployment environments
🧰 Technologies
Category	Technologies
Source Control	Git, GitHub
CI/CD	GitHub Actions
Security	Gitleaks, Trivy, pip-audit
Testing	Pytest
Containerization	Docker
Registry	Docker Hub
Orchestration	Kubernetes
Package Management	Helm
GitOps	Argo CD
Monitoring	Prometheus
Visualization	Grafana
Infrastructure as Code	Terraform
Configuration Management	Ansible
Backend	FastAPI
Database	PostgreSQL
📂 Project Structure
devsecops-project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── backend/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
│
├── helm/
│   └── devsecops/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── backend-deployment.yaml
│           ├── backend-service.yaml
│           ├── postgres-deployment.yaml
│           ├── postgres-service.yaml
│           └── namespace.yaml
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── ansible/
│   ├── inventory/
│   ├── playbooks/
│   └── roles/
│
├── monitoring/
│   ├── prometheus/
│   └── grafana/
│
├── docs/
│   └── images/
│       ├── devsecops-architecture.png
│       ├── github-actions-pipeline.png
│       ├── argocd.png
│       ├── prometheus-targets.png
│       └── grafana-dashboard.png
│
├── docker-compose.yml
└── README.md
🔄 Complete DevSecOps Flow
                       ┌──────────────┐
                       │   Developer  │
                       └──────┬───────┘
                              │
                           Git Push
                              │
                              ▼
                       ┌──────────────┐
                       │    GitHub    │
                       └──────┬───────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  GitHub Actions  │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
           Pytest         Gitleaks      pip-audit
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                       Docker Build
                             │
                             ▼
                        Trivy Scan
                             │
                             ▼
                        Docker Hub
                             │
                             ▼
                         Argo CD
                             │
                             ▼
                       Kubernetes
                        │       │
                        ▼       ▼
                     Backend PostgreSQL
                        │
                        ▼
                    Prometheus
                        │
                        ▼
                      Grafana
🛡️ Security Lifecycle

Security is implemented throughout the software delivery lifecycle.

Source Code
     │
     ▼
Secret Scan
     │
     ▼
Dependency Scan
     │
     ▼
Automated Tests
     │
     ▼
Docker Build
     │
     ▼
Trivy Image Scan
     │
     ▼
Secure Docker Image
     │
     ▼
Docker Hub
     │
     ▼
Kubernetes
🎯 Key Features
✅ Automated CI/CD Pipeline
✅ Automated Testing
✅ Secret Detection
✅ Dependency Vulnerability Scanning
✅ Docker Image Security Scanning
✅ Containerized Backend
✅ Kubernetes Deployment
✅ Three Backend Replicas
✅ Helm-based Deployment
✅ GitOps with Argo CD
✅ Infrastructure as Code with Terraform
✅ Configuration Management with Ansible
✅ Prometheus Monitoring
✅ Grafana Dashboards
✅ Application Metrics
✅ Automated Docker Image Publishing
✅ PostgreSQL Database
✅ Kubernetes Resource Management
📸 Project Screenshots
GitHub Actions

Argo CD

Prometheus

Grafana

Architecture

👨‍💻 Author

Ahmed Mohammed Hamed

Cloud & DevOps Engineer

GitHub: ahmed1707hamed-tech

⭐ Project Highlights

This project demonstrates a complete DevSecOps workflow combining:

CI/CD + Security + Docker + Kubernetes + Helm + GitOps + Monitoring + Terraform + Ansible

The workflow starts from a developer pushing code to GitHub and continues through automated testing, security validation, Docker image publishing, GitOps deployment with Argo CD, Kubernetes orchestration, and real-time monitoring using Prometheus and Grafana.







