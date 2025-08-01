# fastapi-jwt-postgres
FastAPI JWT Authentication with PostgreSQL and RBAC
# FastAPI JWT Authentication with RBAC

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)


## Features

- 🔐 JWT Authentication with access tokens
- 👥 Role-Based Access Control (Admin/User)
- 🔒 Password hashing using bcrypt
- 🗄️ PostgreSQL database with SQLModel ORM
- 📦 CRUD operations for projects with permission control
- ⚡ FastAPI for high performance API endpoints

## Prerequisites

- Python 3.7+
- PostgreSQL 12+
- pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fastapi-jwt-rbac.git
cd fastapi-jwt-rbac

##Install dependencies:

pip install fastapi sqlmodel passlib python-jose[cryptography] psycopg2-binary python-dotenv uvicorn

DATABASE_URL = "postgresql://postgres:yourpassword@localhost/fastapi_jwt"

## API Endpoints

### Authentication

| Endpoint | Method | Description | Access |
|----------|--------|-------------|--------|
| `/signup` | POST | Register new user | Public |
| `/login` | POST | Get JWT token | Public |

### Projects

| Endpoint | Method | Description | Access |
|----------|--------|-------------|--------|
| `/projects` | GET | List all projects | User+Admin |
| `/projects` | POST | Create new project | Admin only |
| `/projects/{id}` | PUT | Update project | Admin only |
| `/projects/{id}` | DELETE | Delete project | Admin only |

## Database Schema

Tables:
- `user` - Stores user credentials and roles
- `project` - Stores project information
