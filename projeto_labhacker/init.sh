#!/bin/sh

# wait for Postgres to start
postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="", host="db")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
echo "Delete migrations"
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
echo "Create makemigrations"
python3 manage.py makemigrations
echo "Create migrate"
python3 manage.py migrate
echo "Run server"
python3 manage.py runserver 0.0.0.0:8000