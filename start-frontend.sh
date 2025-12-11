#!/bin/bash
# Bash script to start the Flask frontend
# Frontend: Flask on port 5173

echo "Starting Flask frontend..."
cd frontend
export FLASK_APP=app.py
export BACKEND_URL=http://localhost:8000
flask run --host=0.0.0.0 --port=5173