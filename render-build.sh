#!/usr/bin/env bash
set -euo pipefail

echo "Running backend build steps"
cd backend

python manage.py migrate --noinput
python manage.py collectstatic --noinput

cd ..

echo "Installing Flask frontend dependencies"
cd frontend
pip install -r requirements.txt