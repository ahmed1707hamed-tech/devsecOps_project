<div align="center">

# 🍔 DevSecOps Pipeline Project
### Cloud-Native Monitoring & Observability Stack on AWS

<p align="center">

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-K3s-326CE5?style=for-the-badge&logo=kubernetes)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform)
![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana)
![AWS](https://img.shields.io/badge/AWS-Free%20Tier-FF9900?style=for-the-badge&logo=amazonaws)

</p>

Production-ready, cloud-native monitoring stack providing end-to-end observability, automated infrastructure provisioning, and localized telemetry configuration for a food delivery application framework.

</div>

---

# 📑 Table of Contents

- Overview
- Architecture
- Tech Stack
- Project Structure
- Cloud Engineering Workflow
- Infrastructure Provisioning
- Configuration Management
- Kubernetes & Telemetry Deployment
- Monitoring & Observability
- Visual Dashboards & Verification
- User Request & Metric Flow
- Deployment Guide
- Features
- Future Improvements
- Author

---

# 🚀 Overview

This project implements an automated, scalable infrastructure and localized monitoring framework for a food delivery platform. 

The entire cloud architecture is provisioned on **AWS EC2** hosting a lightweight **K3s Kubernetes Cluster**. The system relies on Terraform for infrastructure as code, Ansible for automated system configuration, and a dedicated, production-grade telemetry pipeline built using Prometheus and Grafana to track runtime environments dynamically.

---

# 🏗 Architecture

<p align="center">
  <img src="docs/images/architecture.png" alt="Architecture Diagram" width="100%">
</p>

---

# ⚡ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Infrastructure** | Terraform |
| **Configuration** | Ansible |
| **Orchestration** | K3s Kubernetes |
| **Containers** | Docker |
| **Ingress Control** | NGINX Ingress |
| **Telemetry & Collection** | Prometheus |
| **Visualization** | Grafana |
| **Cloud Provider** | AWS (EC2, VPC, Security Groups) |

---

# 📁 Project Structure

```text
devsecops-project
│
├── terraform/          # AWS Core Infrastructure Configuration
├── ansible/            # Cluster Configuration & Tooling Playbooks
├── k8s/                # Localized Core Kubernetes Manifests
├── monitoring/         # Prometheus & Grafana Configuration Files
└── docs/
    └── images/         # Documentation & Dashboard Screenshots

````

Cloud Engineering Workflow

Terraform Infrastructure Provisioning
                 │
                 ▼
Ansible Cluster Node Configuration
                 │
                 ▼
K3s Kubernetes Cluster Deployment
                 │
                 ▼
Target Application Framework Initialization
                 │
                 ▼
Prometheus & Grafana Localized Stack Launch
                 │
                 ▼
Active Metrics Scraping & Dashboard Visualization



Infrastructure Provisioning
Cloud infrastructure automation is fully handled via Terraform, deploying isolated network environments on AWS:

VPC & Subnets: Custom public and private network spaces.

Gateways & Routing: Internet Gateways linked with active Route Tables.

Firewalls: Dynamic Security Groups controlling strict network traffic flow.

Compute: High-performance EC2 instances optimized for cluster workloads.

⚙ Configuration Management
Ansible automation playbooks remotely handle systemic environment setups:

Installing and updating localized Docker dependencies.

Provisioning, configuring, and initializing the K3s cluster.

Setting up administrative tools, package requirements, and system utilities.

Preparing the runtime orchestration environment for internal telemetry agents.

☸ Kubernetes & Telemetry Deployment
The application platform and monitoring layers run inside the managed K3s cluster ecosystem:

Dynamic Storage: Automated Persistent Volumes for configuration storage.

Self-Healing: Declarative deployment objects ensuring high uptime.

Traffic Management: Dedicated NGINX Ingress configuration to manage routing paths securely.

📊 Monitoring & Observability
A dedicated, isolated telemetry pipeline explicitly focused on cluster diagnostics without external dependencies:

Prometheus: Actively pulls platform and infrastructure performance metrics.

Grafana: Provides custom metrics visualization through unified web dashboards.

Tracked Performance Metrics
System-wide CPU and Memory consumption.

Node health parameters and physical disk usage profiles.

Request delivery distributions and cluster network traffic.

🖼️ Visual Dashboards & Verification
Prometheus Targets & Alerts
Verify active endpoints scraping status and configured cluster threshold limits:

Grafana Analytics Dashboard
Real-time status insights visualization for hosted services:

🌐 User Request & Metric Flow


User / Administrator
        │
     Browser
        │
  NGINX Ingress
        │
┌───────┴─────────────────────────────────┐
│           K3s Cluster Runtime           │
│                                         │
│   Grafana Dashboard <── Prometheus      │
│                            │ (Scrapes)  │
│                            ▼            │
│                 Food Delivery Platform  │
└─────────────────────────────────────────┘

⚙ Deployment
1. Provision AWS Resources
cd terraform/
terraform init
terraform apply -auto-approve

2. Configure Node Environments
Bash
cd ../ansible/
ansible-playbook -i inventory.ini site.yml
3. Deploy Kubernetes & Telemetry Components
Bash
kubectl apply -f k8s/
kubectl apply -f monitoring/
4. Verify System Deployment
Bash
kubectl get pods -A
kubectl get svc -n monitoring
✨ Features
Automated Infrastructure as Code (Terraform).

Dynamic Multi-Node System Provisioning (Ansible).

Lightweight Cluster Orchestration via K3s.

Dedicated, Localized Monitoring Engine (Prometheus).

Customized Telemetry Visualization Dashboards (Grafana).

Granular NGINX Ingress Resource Routing.

Persistent Cluster Storage Architectures.

📚 Future Improvements
Automated HTTPS Integration using TLS Certificates.

Horizontal Pod Autoscaler (HPA) for load adaptation.

High-Availability External Load Balancers.

Production Secret management integrations.

Centralized cluster alerting notification engines.

👨‍💻 Author
Ahmed Hamed

Cloud Engineer

GitHub: github.com/ahmed1707hamed-tech

LinkedIn: linkedin.com/in/ahmed-hamed-340570364

⭐ If you found this project useful, don't forget to give it a Star!


