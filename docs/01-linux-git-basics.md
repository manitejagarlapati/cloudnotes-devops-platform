# Phase 1 — Linux & Git Basics

## 1. Introduction

Before building a DevOps project, we need to understand the environment in which applications are developed, managed and deployed.

The first technologies used in this project were:

- Linux
- Bash
- Git
- GitHub
- SSH

---

# 2. Why Linux?

Most cloud servers and DevOps environments are based on Linux.

As a DevOps engineer, we need to be comfortable with:

- Files and directories
- Permissions
- Processes
- Users
- Shell commands
- Environment variables
- Networking
- Services

---

Ah, yes — you mean **what exactly should you put inside your existing `01-linux-git-basics.md` file**, not create another introduction file.

For `docs/01-linux-git-basics.md`, let's make it a **proper beginner-friendly chapter based on what you actually did**.

Use this structure:

````markdown
# Chapter 1 — Linux, Users, SSH and Git Basics

## 1.1 Introduction

Before building the CloudNotes application, we need to understand the environment in which a DevOps engineer works.

In this phase, we learned the basic Linux commands, Linux users, SSH, Git and GitHub.

The goal was not to memorize commands, but to understand what each command does and why it is useful in real-world DevOps work.

---

# 1.2 What is Linux?

Linux is an operating system widely used for servers, cloud infrastructure and DevOps environments.

Many applications deployed on AWS run on Linux servers.

As a DevOps engineer, we need to be comfortable working with Linux from the command line.

---

# 1.3 Linux Terminal

The terminal allows us to interact with Linux by entering commands.

For example:

```bash
pwd
````

shows our current directory.

```bash
ls
```

lists files and directories.

```bash
cd directory_name
```

moves into another directory.

---

# 1.4 Important Linux Commands

| Command  | Purpose                            |
| -------- | ---------------------------------- |
| `pwd`    | Shows the current directory        |
| `ls`     | Lists files and directories        |
| `ls -la` | Lists files including hidden files |
| `cd`     | Changes directory                  |
| `mkdir`  | Creates a directory                |
| `touch`  | Creates a file                     |
| `cat`    | Displays file contents             |
| `whoami` | Shows the current user             |
| `id`     | Shows user and group information   |
| `ps`     | Shows running processes            |
| `clear`  | Clears the terminal                |

---

# 1.5 Understanding `pwd`

The command:

```bash
pwd
```

means:

**Print Working Directory**

Example:

```text
/home/maniteja/cloudnotes-devops-platform
```

This tells us exactly where we currently are.

This became important while building our project because running a command from the wrong directory can result in errors such as:

```text
No such file or directory
```

---

# 1.6 Understanding `whoami`

The command:

```bash
whoami
```

shows the user currently executing commands.

For example:

```text
root
```

means the terminal is currently operating as the root user.

Later, we switched to the normal user:

```bash
su - maniteja
```

After switching:

```bash
whoami
```

returned:

```text
maniteja
```

---

# 1.7 Root vs Normal User

Linux has different levels of permissions.

The `root` user has administrative privileges and can perform almost any operation on the system.

A normal user has more restricted permissions.

For example:

```text
root
 ↓
Administrative access

maniteja
 ↓
Normal user access
```

In real-world environments, applications should not unnecessarily run as root.

Using a normal user reduces the risk of accidentally modifying or deleting important system files.

---

# 1.8 Understanding `/home`

Linux stores normal users' home directories inside `/home`.

For example:

```text
/home/maniteja
```

is the home directory of the `maniteja` user.

Our project is located at:

```text
/home/maniteja/cloudnotes-devops-platform
```

---

# 1.9 Understanding SSH

SSH stands for:

**Secure Shell**

SSH allows us to securely communicate with another computer over a network.

The basic idea is:

```text
Your Computer
      |
      | SSH
      ↓
Remote Linux Server
```

In DevOps, SSH is commonly used to connect to cloud servers such as AWS EC2 instances.

---

# 1.10 SSH Keys

SSH can use a public/private key pair for authentication.

```text
Private Key
     ↓
Kept secret

Public Key
     ↓
Can be placed on the remote server
```

The private key should never be shared.

The server uses the public key to verify that the connecting user possesses the corresponding private key.

---

# 1.11 SSH and GitHub

One important lesson from this project was that SSH does not necessarily mean opening a terminal on another machine.

SSH can also be used for authentication.

For example, Git can communicate with GitHub using an SSH connection.

Conceptually:

```text
Local Computer
      |
      | SSH authentication
      ↓
GitHub
      |
      ↓
Git Repository
```

This allows commands such as:

```bash
git push
```

to authenticate securely.

---

# 1.12 What is Git?

Git is a distributed version control system.

It tracks changes made to files in a project.

Without version control, developers might create files such as:

```text
project-final
project-final-v2
project-final-new
project-final-new-final
```

Git solves this problem by maintaining a history of changes.

---

# 1.13 Git Repository

A Git repository is a project whose files and history are tracked by Git.

We created a repository for:

```text
cloudnotes-devops-platform
```

We can check whether a directory is a Git repository using:

```bash
git status
```

---

# 1.14 Git Working Area

Git can be understood using three main stages:

```text
Working Directory
       ↓
Staging Area
       ↓
Repository
```

### Working Directory

Files we are currently editing.

### Staging Area

Files selected for the next commit.

### Repository

The permanent Git history containing commits.

---

# 1.15 `git status`

The command:

```bash
git status
```

shows the current state of the repository.

For example:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

This means there are no uncommitted changes.

---

# 1.16 `git add`

When we modify a file, Git detects the change.

We can stage the changes using:

```bash
git add .
```

The `.` means the changes in the current directory are included.

---

# 1.17 `git commit`

A commit creates a saved version in Git history.

Example:

```bash
git commit -m "Initialize CloudNotes DevOps project"
```

The message describes what was changed.

A good commit message helps developers understand the project's history.

---

# 1.18 `git log`

We can view previous commits using:

```bash
git log --oneline
```

Example:

```text
66bf54d Initialize CloudNotes DevOps project
```

This gives us a short version of the project's history.

---

# 1.19 GitHub

Git and GitHub are not the same thing.

### Git

Version control software running on our computer.

### GitHub

A platform that hosts Git repositories remotely.

The relationship is:

```text
Local Computer
      |
      | Git
      ↓
Local Repository
      |
      | git push
      ↓
GitHub
```

---

# 1.20 `git push`

The command:

```bash
git push
```

uploads local commits to the remote GitHub repository.

During our project, we pushed the CloudNotes project to GitHub.

After pushing, Git reported:

```text
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

This confirmed that our local repository and GitHub repository were synchronized.

---

# 1.21 Our Git Workflow

The workflow we used is:

```text
Write / Modify Code
       ↓
git status
       ↓
git add .
       ↓
git commit
       ↓
git push
       ↓
GitHub
```

This workflow will become extremely important later when we introduce CI/CD.

---

# 1.22 Problems We Encountered

Learning by building means that errors are expected.

### Problem 1 — Running as root

At one point:

```bash
whoami
```

returned:

```text
root
```

We switched to the normal user:

```bash
su - maniteja
```

Then verified:

```bash
whoami
```

which returned:

```text
maniteja
```

### Lesson

Always understand which Linux user is executing your commands.

---

### Problem 2 — GitHub SSH confusion

We initially tested SSH against GitHub and received:

```text
Hi ...! You've successfully authenticated,
but GitHub does not provide shell access.
```

This was not an error.

It means GitHub accepted the SSH authentication, but GitHub does not provide an interactive Linux shell through that SSH connection.

### Lesson

SSH can be used for authentication without providing shell access.

---

### Problem 3 — Wrong directory

We encountered:

```text
No such file or directory
```

because commands were being executed from an incorrect path.

We used:

```bash
pwd
```

to identify the current directory.

### Lesson

Before running commands, understand where you are.

---

# 1.23 Real-World DevOps Application

The concepts learned in this chapter connect directly to professional DevOps work.

For example:

```text
Developer
    ↓
Git
    ↓
GitHub
    ↓
CI/CD
    ↓
AWS
    ↓
Linux Server
    ↓
Application
```

A DevOps engineer may:

* Work inside Linux servers
* Use SSH to connect to servers
* Manage users and permissions
* Use Git for version control
* Push code to GitHub
* Trigger CI/CD pipelines
* Deploy applications to AWS

---

# 1.24 What I Learned

At the end of this phase, I understand:

* What Linux is
* How to navigate Linux
* Linux users
* Root vs normal users
* `pwd`
* `ls`
* `cd`
* `whoami`
* `id`
* SSH
* SSH keys
* Git
* Git repositories
* Git staging
* Git commits
* Git history
* GitHub
* `git push`

More importantly, I understand how these technologies fit into a DevOps workflow.

---

# 1.25 Next Chapter

In the next chapter, we will build the backend of CloudNotes using Flask.

We will learn:

* What a backend is
* What an API is
* What REST means
* HTTP methods
* GET
* POST
* PUT
* DELETE
* Endpoints
* Requests
* Responses
* JSON
* HTTP status codes
* API testing with curl

The project will then evolve from a simple Python application into a real backend service.

```

