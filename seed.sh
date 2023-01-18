#!/bin/bash

echo "dropping database red-packet-clicker"
dropdb red-packet-clicker

echo "creating database red-packet-clicker"
createdb red-packet-clicker

python manage.py makemigrations

python manage.py migrate

echo "inserting users"
python3 manage.py loaddata jwt_auth/seeds.json

echo "inserting items"
python3 manage.py loaddata items/seeds.json