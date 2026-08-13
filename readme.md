# The Project We'll Build

## CloudNotes - Production DevOps Platform

A simple Notes application that users can:

- Register/Login
- Create Notes
- Upload Images
- Store data in a database

The application itself is simple. The focus is on the infrastructure.

It will eventually include:

```
User
    │
Internet
    │
Nginx (Reverse Proxy)
    │
Flask API
    │
PostgreSQL (AWS RDS)
    │
Amazon S3 (Image Storage)

-------------------------

GitHub
    │
Webhook
    │
Jenkins
    │
Docker Build
    │
Amazon ECR
    │
EC2
    │
Docker Compose
    │
CloudWatch
    │
SNS Alerts

-------------------------

Terraform

creates

IAM
VPC
EC2
RDS
S3
Security Groups

-------------------------

Ansible

installs

Docker
Jenkins
Nginx

-------------------------

Kubernetes

Deploy Application


```

This is close to what many companies use.

---

# MASTER ROADMAP

There are **12 modules**. Each builds on the previous one.

---

# MODULE 0 — Foundations (2–3 days)

### Goal

Understand the environment you'll work in.

### Learn

- What is DevOps?
- SDLC (Software Development Life Cycle)
- CI vs CD
- Agile basics
- Client → Server → Database flow
- HTTP & HTTPS
- DNS
- Linux overview
- Virtualization vs Containers
- Cloud basics
- What AWS provides

### Mini Task

Draw your own architecture diagram.

---

# MODULE 1 — Linux (3–4 days)

This is the most important module because almost everything in DevOps runs on Linux.

### Learn

- File system
- Navigation
- Permissions
- Users & groups
- sudo
- SSH
- SCP
- Vim
- Nano
- Networking commands
- Process management
- Services (`systemctl`)
- Cron jobs
- Environment variables
- Package managers
- Logs

### Mini Project

Configure a Linux server from scratch.

---

# MODULE 2 — Git & GitHub (2–3 days)

### Learn

- init
- clone
- add
- commit
- push
- pull
- branch
- merge
- pull requests
- resolving conflicts
- `.gitignore`

### Mini Project

Host your Notes project on GitHub.

---

# MODULE 3 — Python & Flask (2–3 days)

You don't need to become a Python expert.

Learn enough to deploy an application.

### Learn

- Flask basics
- REST API
- Routes
- Environment variables
- Requirements file

### Mini Project

Build the Notes API.

---

# MODULE 4 — Docker (4 days)

One of the most important DevOps skills.

### Learn

- Images
- Containers
- Dockerfile
- Layers
- Build
- Run
- Volumes
- Networks
- Docker Compose
- Multi-stage builds

### Mini Project

Run the Notes application in Docker.

---

# MODULE 5 — AWS Core (7–8 days)

This is the heart of the roadmap.

### IAM

- Users
- Groups
- Policies
- Roles
- MFA

---

### EC2

- Launch instances
- SSH
- Security Groups
- Elastic IP
- User Data

---

### VPC

- Public Subnet
- Private Subnet
- Route Table
- Internet Gateway
- NAT Gateway

---

### S3

- Buckets
- Objects
- Versioning
- Lifecycle
- Static Hosting

---

### RDS

- PostgreSQL
- Security
- Backups
- Multi-AZ (concept)

---

### CloudWatch

- Metrics
- Logs
- Alarms
- Dashboards

---

### ECR

Store Docker images.

---

### SNS

Email alerts.

---

### Mini Project

Deploy Notes application to EC2.

---

# MODULE 6 — CI/CD (5 days)

This is what many internship interviews focus on.

### Jenkins

- Installation
- Pipeline
- Jenkinsfile
- Credentials
- Agents
- Plugins

### GitHub Webhooks

Automatically trigger builds.

### Pipeline

```
Push

↓

GitHub

↓

Jenkins

↓

Build

↓

Test

↓

Docker Build

↓

Push to ECR

↓

Deploy to EC2

```

### Mini Project

Automatic deployment.

---

# MODULE 7 — Nginx (2 days)

### Learn

- Reverse Proxy
- Load balancing (concept)
- SSL
- HTTPS
- Domain configuration

Mini Project

Access your application through Nginx.

---

# MODULE 8 — Monitoring (2 days)

### CloudWatch

- Logs
- Metrics
- Dashboards
- Alarms

### Linux

- CPU
- Memory
- Disk

Mini Project

Receive an email when CPU exceeds a threshold.

---

# MODULE 9 — Terraform (4 days)

Infrastructure as Code.

### Learn

- Providers
- Variables
- Outputs
- Modules (basic)
- State
- Plan
- Apply
- Destroy

### Mini Project

Provision:

- VPC
- EC2
- S3
- IAM
- RDS

using Terraform.

---

# MODULE 10 — Ansible (3 days)

Automation.

### Learn

- Inventory
- Playbooks
- Roles (basic)
- Variables
- SSH

### Mini Project

Install Docker and Nginx automatically on EC2.

---

# MODULE 11 — Kubernetes (5–6 days)

Companies increasingly expect at least basic Kubernetes knowledge.

### Learn

- Pods
- ReplicaSets
- Deployments
- Services
- ConfigMaps
- Secrets
- Ingress
- Rolling Updates

### Mini Project

Deploy Notes application on Kubernetes.

---

# FINAL PROJECT

You'll end up with a repository like this:

```
cloudnotes-devops/

├── app/
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── terraform/
├── ansible/
├── kubernetes/
├── nginx/
├── monitoring/
├── scripts/
├── docs/
└── README.md

```

This structure is similar to what you'll find in many real engineering teams.

---

# Skills You'll Gain

| SkillPractical outcome |                                         |
| ---------------------- | --------------------------------------- |
| Linux                  | Manage servers confidently              |
| Git                    | Collaborate and track changes           |
| Python/Flask           | Understand and deploy applications      |
| Docker                 | Package applications consistently       |
| AWS                    | Deploy and manage cloud infrastructure  |
| Jenkins                | Automate builds and deployments         |
| Nginx                  | Route traffic and enable HTTPS          |
| CloudWatch             | Monitor systems and troubleshoot        |
| Terraform              | Provision infrastructure as code        |
| Ansible                | Automate server configuration           |
| Kubernetes             | Run containerized applications at scale |

---

# How We'll Work Together

I don't want this to be just another tutorial. We'll treat it like you're joining a company on your first day.

For **every module**, we'll follow the same structure:

1. **Concepts** – Why the technology exists and what problem it solves.
2. **Hands-on** – Build and configure it from scratch.
3. **Production Usage** – How companies use it in real environments.
4. **Interview Questions** – The questions you're likely to face and how to answer them.
5. **Best Practices** – What experienced engineers do differently.
6. **Mini Challenge** – A task to complete on your own.
7. **Project Integration** – Add the new skill to our main DevOps project.
