#!/bin/sh

python3 manage.py loaddata apps/products/fixtures/initial_data.json

python3 manage.py runserver 0.0.0.0:8000