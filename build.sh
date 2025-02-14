#!/usr/bin/env bash

set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Crear directorio para archivos media si no existe
mkdir -p mediafiles