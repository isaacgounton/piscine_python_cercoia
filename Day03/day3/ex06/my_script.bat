#!/usr/bin/env bash

pip install virtualenv
virtualenv -p python django_venv
source django_venv/bin/activate
pip install -r requirement.txt

django-admin startproject Django
cd Django
python manage.py startapp helloworld