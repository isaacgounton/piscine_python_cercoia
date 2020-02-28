#!/usr/bin/env bash

#en quittant virtualenv doit etre active

pip install virtualenv
virtualenv -p python django_venv
source django_venv/bin/activate
pip install -r requirement.txt