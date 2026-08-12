<div align="center">

# 🛡️ DevSecOps Project

### End-to-End DevSecOps CI/CD Pipeline with Kubernetes, GitOps & Monitoring

<p align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Argo CD](https://img.shields.io/badge/Argo_CD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)

<br>

**A complete DevSecOps project demonstrating automated testing, security scanning, containerization, Kubernetes deployment, GitOps and monitoring.**

</div>

---

# 📑 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Project Screenshots](#-project-screenshots)
- [Technology Stack](#-technology-stack)
- [DevSecOps Workflow](#-devsecops-workflow)
- [DevSecOps Security Pipeline](#-devsecops-security-pipeline)
- [GitHub Actions CI/CD](#-github-actions-cicd)
- [Docker](#-docker)
- [Kubernetes](#-kubernetes)
- [Helm](#-helm)
- [GitOps with Argo CD](#-gitops-with-argo-cd)
- [Monitoring & Observability](#-monitoring--observability)
- [Infrastructure as Code](#-infrastructure-as-code)
- [Configuration Management](#-configuration-management)
- [Project Structure](#-project-structure)
- [Deployment Flow](#-complete-deployment-flow)
- [Key Features](#-key-features)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

# 🚀 Overview

This project demonstrates a complete **DevSecOps lifecycle** for a containerized FastAPI application with PostgreSQL.

The project integrates security directly into the CI/CD pipeline using **Gitleaks, pip-audit and Trivy**, then builds and publishes Docker images to Docker Hub.

The application is deployed on **Kubernetes** using **Helm**, while **Argo CD** provides GitOps-based Continuous Delivery.

The Kubernetes environment is monitored using **Prometheus and Grafana**.

The project demonstrates the complete flow from:

**Code → Testing → Security → Docker → Registry → GitOps → Kubernetes → Monitoring**

---

# 🏗️ Architecture

<p align="center">

<img src="docs/images/architecture-diagram.png" width="100%">

</p>

### High-Level Architecture

```text
Developer
    │
    ▼
GitHub Repository
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
        │       │
        ▼       ▼
     Backend PostgreSQL
        │
        ▼
   Prometheus
        │
        ▼
      Grafana
