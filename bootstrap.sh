#!/usr/bin/env bash

apt-get update
apt-get install -y git
apt-get install -y python-pip
apt-get install -y nginx
apt-get install -y postgresql
apt-get install -y curl

pip install gunicorn
pip install django
pip install django-tastypie
pip install psycopg2

sudo service nginx stop
sudo nginx -c /vagrant/django_gunicorn_nginx.conf
sudo service nginx start
sudo python /vagrant/src/manage.py runserver 127.0.0.1:8000
# sudo python /vagrant/src/manage.py run_gunicorn 127.0.0.1:8000