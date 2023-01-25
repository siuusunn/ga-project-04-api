#!/bin/bash

echo "dropping database red-packet-clicker"
dropdb red-packet-clicker

echo "creating database red-packet-clicker"
createdb red-packet-clicker

python3 manage.py makemigrations

python3 manage.py migrate

echo "inserting items"
python3 manage.py loaddata items/seeds.json

echo "inserting users"
python3 manage.py loaddata jwt_auth/seeds.json

echo "inserting comments"
python3 manage.py loaddata comments/seeds.json

echo "inserting pockets"
python3 manage.py loaddata pockets/seeds.json