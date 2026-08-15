 `03-postgres.md`**. 

That file is documentation for the **PostgreSQL part of CloudNotes**. It is **not another Python/code file**.

Since we already got PostgreSQL connected successfully, the purpose of `03-postgres.md` is to document what we did.

You can put this in it:

# 03 — PostgreSQL Setup

## 1. What is PostgreSQL?

PostgreSQL is the database used by CloudNotes to permanently store application data.

Our Flask application communicates with PostgreSQL using the `psycopg` Python library.

```text
Flask Application
       |
       | psycopg
       ↓
PostgreSQL
       |
       ↓
cloudnotes database
```

## 2. Database Details

```text
Database: cloudnotes
User: cloudnotes_user
Host: localhost
Port: 5432
```

> Do not put the database password in documentation or GitHub.

## 3. Create Database

We created the PostgreSQL database:

```sql
CREATE DATABASE cloudnotes;
```

## 4. Create Database User

We created a dedicated PostgreSQL user for the application:

```sql
CREATE USER cloudnotes_user WITH PASSWORD 'YOUR_PASSWORD';
```

The application uses this user to connect to the database.

## 5. Notes Table

CloudNotes stores notes inside the `notes` table.

Example structure:

```sql
CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);
```

The table contains:

| Column    | Purpose                 |
| --------- | ----------------------- |
| `id`      | Unique ID for each note |
| `title`   | Note title              |
| `content` | Note content            |

## 6. Flask → PostgreSQL Connection

Our Flask application uses `psycopg`:

```python
import psycopg
```

The database configuration is:

```python
DB_CONFIG = {
    "dbname": "cloudnotes",
    "user": "cloudnotes_user",
    "password": "YOUR_PASSWORD",
    "host": "localhost",
    "port": 5432
}
```

The connection function is:

```python
def get_db_connection():
    return psycopg.connect(**DB_CONFIG)
```

## 7. Connection Test

We tested the PostgreSQL connection from Flask.

The terminal showed:

```text
PostgreSQL connection successful!
```

This confirms:

```text
Flask
  ↓
psycopg
  ↓
PostgreSQL
```

is working correctly.

## 8. Current Status

```text
✅ PostgreSQL installed
✅ cloudnotes database created
✅ Application user created
✅ notes table created
✅ Flask connected to PostgreSQL
✅ GET /notes tested successfully
```

### Important

For now, **don't worry about CRUD, Docker, or AWS in this file**.

