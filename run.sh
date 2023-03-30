#!/bin/sh


python ./titan/manage.py makemigrations
python ./titan/manage.py migrate --no-input

gunicorn titan.wsgi:application --bind 0.0.0.0:8000 &

unlink /etc/nginx/sites-enabled/default

nginx -g 'daemon off;'