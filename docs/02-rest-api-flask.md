Great. Let's move to **Chapter 2 — REST API & Flask** and document what you actually built.

## Step 1 — Create/open Chapter 2

In VS Code, open:

```text
docs/02-rest-api-flask.md
```

Paste this:

````markdown
# Chapter 2 — REST APIs and Flask

## 2.1 Introduction

After setting up Linux, Git, GitHub and SSH, the next step was to build the backend of the CloudNotes application.

For this phase, we used Python and Flask to create a REST API.

The goal was to understand how applications communicate with a backend using HTTP.

---

## 2.2 What is a Backend?

A backend is the part of an application responsible for processing requests, applying business logic and working with data.

A simplified architecture is:

Client
   ↓
Backend API
   ↓
Database

For CloudNotes:

Client
   ↓
Flask API
   ↓
Notes data

---

## 2.3 What is Flask?

Flask is a lightweight Python web framework.

It allows us to create web applications and APIs using Python.

For example:

```python
from flask import Flask

app = Flask(__name__)
````

This creates a Flask application.

---

## 2.4 What is an API?

API stands for:

Application Programming Interface.

An API provides a way for one application to communicate with another application.

For example:

Client
↓
GET /notes
↓
Flask
↓
Notes data
↓
JSON response

The client does not need to know how the backend internally stores the data.

---

## 2.5 What is REST?

REST is an architectural style commonly used for building web APIs.

REST APIs use HTTP methods to represent operations on resources.

Our resource is:

`notes`

We use different HTTP methods to work with notes.

| Method | Purpose     |
| ------ | ----------- |
| GET    | Read data   |
| POST   | Create data |
| PUT    | Update data |
| DELETE | Delete data |

---

## 2.6 What is an Endpoint?

An endpoint is a specific URL through which an API provides functionality.

Examples from CloudNotes:

```text
GET /notes
POST /notes
GET /notes/1
PUT /notes/1
DELETE /notes/1
```

Here:

```text
/notes
```

represents the notes resource.

And:

```text
/notes/1
```

represents note number 1.

---

## 2.7 GET

GET is used to retrieve information.

Example:

```bash
curl http://localhost:5000/notes
```

The request means:

"Give me the notes."

The server returns a response, usually in JSON format.

---

## 2.8 POST

POST is used to create new data.

Example:

```bash
curl -X POST http://localhost:5000/notes \
-H "Content-Type: application/json" \
-d '{"title":"AWS","content":"Learn EC2"}'
```

The request contains data that the server should store.

Conceptually:

Client
↓
POST /notes
↓
JSON data
↓
Flask
↓
Create note

---

## 2.9 PUT

PUT is used to update an existing resource.

Example:

```bash
curl -X PUT http://localhost:5000/notes/1 \
-H "Content-Type: application/json" \
-d '{"title":"AWS EC2","content":"Learn EC2 deployment"}'
```

The `/1` identifies the note being updated.

---

## 2.10 DELETE

DELETE is used to remove a resource.

Example:

```bash
curl -X DELETE http://localhost:5000/notes/1
```

The server identifies note 1 and removes it.

---

## 2.11 HTTP Request

An HTTP request contains information sent from the client to the server.

Conceptually:

Client
↓
HTTP Request
↓
Flask

A request can contain:

* HTTP method
* URL
* Headers
* Body

For example:

```text
POST /notes
Content-Type: application/json

{
    "title": "AWS",
    "content": "Learn EC2"
}
```

---

## 2.12 HTTP Response

The server sends a response back to the client.

A response can contain:

* Status code
* Headers
* Response body

Example:

```text
HTTP/1.1 200 OK
Content-Type: application/json
```

followed by JSON data.

---

## 2.13 JSON

JSON stands for:

JavaScript Object Notation.

It is commonly used to exchange data between applications.

Example:

```json
{
    "id": 1,
    "title": "AWS",
    "content": "Learn EC2"
}
```

JSON is useful because it is simple for both humans and applications to understand.

---

## 2.14 HTTP Status Codes

HTTP status codes tell the client what happened.

Important codes:

| Code | Meaning            |
| ---- | ------------------ |
| 200  | Request successful |
| 201  | Resource created   |
| 400  | Bad request        |
| 404  | Resource not found |
| 405  | Method not allowed |
| 500  | Server error       |

During this project, we specifically encountered:

```text
405 Method Not Allowed
```

This became an important debugging lesson.

---

## 2.15 404 Not Found

A 404 means the requested resource or endpoint could not be found.

For example:

```text
GET /notes/99
```

when note 99 does not exist.

The API can return:

```json
{
    "error": "Note not found"
}
```

---

## 2.16 405 Method Not Allowed

A 405 is different from a 404.

A 404 means:

"The requested resource was not found."

A 405 means:

"The endpoint exists, but that HTTP method is not allowed."

For example:

```text
DELETE /notes/1
```

could produce:

```text
405 Method Not Allowed
```

if the running Flask application does not have DELETE registered for that endpoint.

This was one of the real problems encountered while building CloudNotes.

---

## 2.17 Testing the API

We used `curl` to communicate with the API from the terminal.

For example:

```bash
curl http://localhost:5000/notes
```

This allowed us to test the API without needing a frontend application.

The development workflow became:

Client command
↓
HTTP request
↓
Flask
↓
Response
↓
Terminal

---

## 2.18 CRUD

CRUD represents four basic operations:

Create
Read
Update
Delete

For CloudNotes:

```text
Create → POST
Read   → GET
Update → PUT
Delete → DELETE
```

This is one of the fundamental patterns used when building applications that manage data.

---

## 2.19 Temporary RAM Storage

Initially, the application stored notes in a Python list.

Conceptually:

```python
notes = []
```

This means the data exists only in the application's memory.

The architecture was:

```text
Client
   ↓
Flask
   ↓
Python list
   ↓
RAM
```

This works for learning and testing, but it is not suitable for persistent production data.

---

## 2.20 The RAM Data Problem

We discovered an important limitation.

When the Flask application stops and starts again, the Python list is recreated.

Therefore:

```text
Application running
       ↓
notes stored in RAM
       ↓
Application stopped
       ↓
RAM cleared
       ↓
Notes disappear
```

This created the requirement for a real database.

---

## 2.21 Why We Need PostgreSQL

Instead of:

Flask → RAM

we need:

Flask → PostgreSQL

PostgreSQL will provide persistent storage.

The new architecture will become:

Client
↓
Flask REST API
↓
PostgreSQL
↓
Persistent data

This is the reason PostgreSQL is the next phase of the project.

---

## 2.22 Problems Encountered

### Problem: Python command not found

The system did not recognize:

```bash
python
```

but provided:

```bash
python3
```

This taught us that Linux environments can have different command configurations.

---

### Problem: Flask server stopped

When the Flask process was stopped using:

```text
Ctrl+C
```

the API became unavailable.

Requests then failed to connect to:

```text
localhost:5000
```

This helped us understand that the development server must be running while testing the API.

---

### Problem: 405 Method Not Allowed

We encountered a situation where the DELETE endpoint returned:

```text
405 Method Not Allowed
```

We inspected the registered methods using the HTTP OPTIONS request.

This demonstrated an important debugging principle:

Don't assume the code and running application are identical.

Always inspect what the running application is actually serving.

---

## 2.23 Real-World Application

REST APIs are used throughout modern software systems.

For example:

Mobile App
↓
REST API
↓
Backend
↓
Database

or:

Frontend
↓
API Gateway / Load Balancer
↓
Backend
↓
Database

In a production DevOps environment, our Flask application will eventually run on AWS infrastructure.

---

## 2.24 What I Learned

At the end of this phase, I understand:

* Backend
* Flask
* API
* REST
* HTTP
* HTTP methods
* GET
* POST
* PUT
* DELETE
* Endpoints
* Requests
* Responses
* JSON
* Status codes
* CRUD
* curl
* RAM storage
* Why persistent databases are required

Most importantly, I learned how a client communicates with a backend application.

---

## 2.25 Next Chapter

The next phase is:

**PostgreSQL**

We will replace the temporary Python list with a real database.

The architecture will change from:

Flask
↓
RAM

to:

Flask
↓
PostgreSQL

This will allow our application to persist data even when the application is restarted.

````

### Then save it.

After saving, run:

```bash
git status
````

Then:

```bash
git add docs/02-rest-api-flask.md
git commit -m "docs: add REST API and Flask chapter"
git push
```

Once that is pushed, **we move immediately to PostgreSQL** — no more spending time on the DELETE issue.
