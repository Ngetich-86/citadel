# Django Project Setup Guide

This guide will walk you through setting up a Django development environment and creating a new project.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for version control)

## Setting Up the Development Environment

### 1. Create a Virtual Environment

```bash
# Navigate to your project directory
cd Backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Django

```bash
# Make sure pip is up to date
python -m pip install --upgrade pip

# Install Django
pip install django

# (Optional) Create requirements.txt
pip freeze > requirements.txt
```

### 3. Create a New Django Project

```bash
# Create a new Django project
django-admin startproject config .

# Create a new app
python manage.py startapp server
```

### 4. Initial Project Setup

1. Add your app to `config/settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Add your app here
]
```

2. Run initial migrations:
```bash
python manage.py migrate
```

3. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```

4. Start the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see your Django project running!

## Project Structure

```
Backend/
├── venv/                  # Virtual environment
├── config/               # Project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                 # Your app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── requirements.txt
```

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/) (for API development)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/) (for debugging)

## other Commands

```bash
# Run migrations
python manage.py migrate

# Create new migrations
python manage.py makemigrations

# Start development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test
```

## Working with PostgreSQL

### 1. Install PostgreSQL Dependencies

First, make sure you have PostgreSQL installed on your system. Then, install the required Python packages:

```bash
# Activate your virtual environment if not already activated
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install psycopg2 (PostgreSQL adapter for Python)
pip install psycopg2-binary

# Install django-environ for environment variables
pip install django-environ

# Update requirements.txt
pip freeze > requirements.txt
```

### 2. Configure Database Settings

Update your `config/settings.py` file to use PostgreSQL:

```python
import environ

# Initialize environ
env = environ.Env()
environ.Env.read_env()

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='5432'),
    }
}
```

### 3. Create .env File

Create a `.env` file in your project root (same level as manage.py) with your database credentials:

```plaintext
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

### 4. Create Database

1. Open PostgreSQL command prompt or pgAdmin
2. Create a new database:
```sql
CREATE DATABASE your_database_name;
```

### 5. Run Migrations

After setting up the database, run migrations:

```bash
python manage.py migrate
```

### Common PostgreSQL Commands

```bash
# Connect to PostgreSQL
psql -U your_username

# List all databases
\l

# Connect to a specific database
\c database_name

# List all tables
\dt

# Exit PostgreSQL
\q
```

### Troubleshooting PostgreSQL

1. Make sure PostgreSQL service is running
2. Verify database credentials in .env file
3. Check if psycopg2 is installed correctly
4. Ensure database exists and is accessible
5. Check PostgreSQL logs for specific errors
