# Configuration & Secrets — CloudNotes Learning Notes

## 1. Why Configuration Matters

An application needs configuration values to know how to connect to external services.

CloudNotes currently needs PostgreSQL configuration such as:

```text
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD
```

These values can change depending on the environment.

```text
Development
     ↓
localhost PostgreSQL

Production
     ↓
AWS RDS PostgreSQL
```

The application code should not need to be rewritten just because the environment changes.

---

## 2. Configuration vs Application Code

Application code contains the logic of the application.

Example:

```text
Flask routes
Database queries
Authentication logic
Business logic
```

Configuration contains environment-specific values.

Example:

```text
Database host
Database port
Database name
External service URLs
```

These should be separated.

```text
Application Code
       +
Configuration
       +
Secrets
       =
Running Application
```

---

## 3. Why Secrets Should Not Be Hardcoded

A bad approach is:

```python
conn = psycopg.connect(
    host="localhost",
    dbname="cloudnotes",
    user="cloudnotes_user",
    password="mypassword123"
)
```

The password is now part of the source code.

If the code is pushed to GitHub, the secret could be exposed.

Therefore:

> Passwords, API keys, tokens, and other sensitive credentials should not be hardcoded into source code.

---

## 4. Environment Variables

Environment variables allow configuration to exist outside the application source code.

Example:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=cloudnotes
DB_USER=cloudnotes_user
DB_PASSWORD=********
```

Python can read an environment variable using:

```python
import os

db_host = os.getenv("DB_HOST")
db_password = os.getenv("DB_PASSWORD")
```

The architecture becomes:

```text
Operating System
       ↓
Environment Variables
       ↓
Flask Application
       ↓
psycopg
       ↓
PostgreSQL
```

---

## 5. `.env` Files

During local development, environment variables are often stored in a `.env` file.

Example:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=cloudnotes
DB_USER=cloudnotes_user
DB_PASSWORD=your_password
```

The `.env` file should not be committed to Git.

Add it to `.gitignore`:

```text
.env
```

This prevents Git from tracking the local secrets file.

---

## 6. `.gitignore`

`.gitignore` tells Git which files should not be tracked.

For example:

```text
.env
__pycache__/
*.pyc
```

This is useful for preventing local configuration and generated files from entering the repository.

Important:

> `.gitignore` is not a secret-management system. It only prevents Git from tracking files.

---

## 7. Development vs Production

CloudNotes will eventually run in different environments.

### Development

```text
Flask
  ↓
localhost
  ↓
PostgreSQL
```

### Production

```text
EC2
  ↓
RDS PostgreSQL
```

The application should obtain the database configuration from its environment instead of hardcoding environment-specific values.

For example:

```text
Development:

DB_HOST=localhost
```

Production could use an RDS endpoint:

```text
DB_HOST=<RDS endpoint>
```

The application logic can remain the same.

---

## 8. Secrets in Production

For production systems, important secrets should be stored using an appropriate secret-management mechanism rather than casually placing passwords on servers.

Later in the CloudNotes project we will learn AWS options such as:

```text
AWS Secrets Manager
AWS Systems Manager Parameter Store
```

These will be covered when we reach the AWS section of the roadmap.

---

## 9. What Should Be Stored in Git?

### Safe to store

```text
Application source code
Documentation
requirements.txt
Dockerfile
Jenkinsfile
Terraform configuration
Kubernetes manifests
.gitignore
```

### Should generally NOT be stored directly

```text
Database passwords
API keys
Private tokens
Access keys
Production credentials
.env files containing secrets
```

---

## 10. DevOps Principle

A key principle learned from this phase is:

> **Separate application code from environment-specific configuration and secrets.**

This makes applications easier to:

* Deploy
* Test
* Move between environments
* Secure
* Automate

It is especially important for CI/CD and cloud deployments.

---

## 11. CloudNotes Architecture

The configuration flow will eventually look like:

```text
                    GitHub
                       |
                       | Application Code
                       v
                  CloudNotes
                       |
             +---------+---------+
             |                   |
            Code          Configuration
             |                   |
             |              Environment
             |                   |
             +---------+---------+
                       |
                       v
                     Flask
                       |
                     psycopg
                       |
                       v
                  PostgreSQL
```

In production:

```text
EC2
 |
 | Configuration
 |
 v
Flask
 |
 | Database credentials
 v
RDS PostgreSQL
```

---

## 12. Security Principle

The principle of least privilege learned earlier also applies to secrets.

Applications should receive only the credentials and permissions they need.

For example:

```text
CloudNotes
    ↓
Application database credentials
    ↓
Required database permissions
```

The application should not receive unnecessary
