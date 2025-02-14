#!/usr/bin/env bash

set -o errexit
pip install -r requirements.txt

# Crear y dar permisos a los directorios
mkdir -p mediafiles
mkdir -p staticfiles
chmod -R 755 mediafiles
chmod -R 755 staticfiles

python manage.py collectstatic --no-input
python manage.py migrate