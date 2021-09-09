# Django-auth

This repository implements django authentication with Auth0 single login and TypingDNA Verify's 2FA.

## Requirements

1. Python3 and Git installed on your machine
2. Auth0 Account
3. TypingDNA's Account

## To follow through:

- Clone the repository:

``` bash
$git clone https://github.com/auth0-blog/ga-django-python.git
```

- Install all the packages using:

```bash
$pip install -r requirements.txt
```

- Once done with installations, create and make migrations by running:

```bash
$python3 manage.py makemigrations
$python3 manage.py migrate
```

- to create a superuser(admin), Run:

```bash
$python3 manage.py createsuperuser
```

. To start the server, run:

```bash
$python3 manage.py runserver to start the server
```

Your browser should open automatically and show the application UI. If it doesn't start automatically, please open it manually and point it to http://localhost:8000


