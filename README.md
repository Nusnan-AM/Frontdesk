# Frontdesk Project

Frontdesk is a Django-based application designed to streamline the management of tasks and operations. This project uses Django 5.1.5, REST Framework, and MySQL as the database backend.

---

## Table of Contents

- [Project Features](#project-features)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [Database Configuration](#database-configuration)
- [Installed Apps](#installed-apps)
- [API and Middleware](#api-and-middleware)
- [Static Files](#static-files)
- [Authentication and Security](#authentication-and-security)

---

## Project Features

- Admin panel for managing users and operations.
- RESTful APIs with Django REST Framework.
- Cross-Origin Resource Sharing (CORS) enabled.
- Configurable database and environment settings using `.env`.
- Customizable authentication and login redirects.

---

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Frontdesk
2. **Create a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3. **Set up the .env file (see Environment Variables).**:
   ```bash
    SECRET_KEY=your-secret-key
    DEBUG=True
    DB_NAME=your-database-name
    DB_USER=your-database-username
    DB_PASSWORD=your-database-password
    DB_HOST=your-database-host
    DB_PORT=your-database-port

4. **Running the Project**:
   ```bash
   python manage.py runserver
