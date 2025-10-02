#!/bin/sh
python manage.py migrate --noinput
python scripts/seed.py
exec gunicorn app.wsgi:application -b 0.0.0.0:8080
