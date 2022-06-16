#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations app
python manage.py migrate app
gunicorn -c gunicorn.conf.py project.wsgi:application
exec "$@"