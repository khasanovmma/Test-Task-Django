# Test-Task-Django

**Table of contents:**
- [Installation](#markdown-header-install)
- [Run](#markdown-header-run)
- [Run using Docker](#markdown-header-run-using-docker)


First of all, clone this repository in the folder and open it in cmd

```
git clone https://github.com/khasanovmma/Test-Task-Django.git
```

## Install

Use the package manager pip to install foobar

```
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy env.example and paste in the root project directory and configure it

```
.env.local
```

.env configuration

```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=*
STRIPE_PUBLISHABLE_KEY=
STRIPE_SECRET_KEY=
```

## Run

Default Run the web service
```
python manage.py runserver
```

Run with a specific host and port
```
python manage.py runserver 0.0.0.0:8080
```

## Run using Docker
```
docker-compose up --build 
```