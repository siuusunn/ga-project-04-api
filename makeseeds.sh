#!/bin/bash

echo "creating items/seeds.json"
python manage.py dumpdata items --output items/seeds.json --indent=2;

echo "creating jwt_auth/seeds.json"
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;