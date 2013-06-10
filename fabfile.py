__author__ = 'jond'

from fabric.api import *
from fabtools.vagrant import vagrant

@task
def nginx_start():
    sudo('nginx -c /vagrant/django_gunicorn_nginx.conf')
    sudo('service nginx start')

@task
def nginx_stop():
    sudo('service nginx stop')

@task
def nginx_reload():
    nginx_stop()
    nginx_start()

@task
def djangoserver_start():
    with cd('/vagrant/src/'):
        sudo('python manage.py runserver 127.0.0.1:8000')

@task
def gunicorn_start():
    with cd('/vagrant/src/'):
        sudo('python manage.py run_gunicorn 127.0.0.1:8000')

@task
def dev_start():
    """
    Starts the vagrant vm in development mode
    """
    nginx_reload()
    djangoserver_start()

@task
def pro_start():
    """
    Starts the vagrant vm in production mode
    """
    nginx_reload()
    gunicorn_start()
