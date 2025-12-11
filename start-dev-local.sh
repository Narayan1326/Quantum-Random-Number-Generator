#!/bin/bash
# Bash script to start the development servers
# Backend: Django on port 8000
# Frontend: Flask on port 5173

echo "Starting QNRG Development Servers..."
echo ""

# Set environment variables for backend
export PYTHONPATH=.
export DEBUG=True
export CORS_ALLOW_ALL=True

# Start backend in background
echo "Starting Django backend on http://localhost:8000..."
cd backend
PYTHONPATH=.. DEBUG=True python manage.py runserver &
BACKEND_PID=$!
cd ..

# Wait a bit for backend to start
sleep 3

# Note: Flask frontend needs to be started manually in a separate terminal
# To start Flask frontend:
# cd frontend
# export BACKEND_URL=http://localhost:8000
# python app.py

echo ""
echo "✓ Backend: http://localhost:8000 (PID: $BACKEND_PID)"
echo "ℹ Frontend: Start Flask manually in a separate terminal"
echo ""
echo "Both servers are running. Press Ctrl+C to stop..."

# Wait for interrupt
trap "echo ''; echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT

# Keep script running
wait