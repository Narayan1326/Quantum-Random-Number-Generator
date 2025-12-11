#!/bin/bash
# Bash script to start the development servers
# Backend: Django/Gunicorn on port 8000
# Frontend: Flask on port 5173

echo "Starting QNRG Development Servers..."
echo ""

# Start backend with Gunicorn
echo "Starting Django backend with Gunicorn on http://localhost:8000..."
cd backend
export PYTHONPATH=..
gunicorn config.wsgi:application --bind 0.0.0.0:8000 &
BACKEND_PID=$!
cd ..

# Wait a bit for backend to start
sleep 3

# Start Flask frontend
echo "Starting Flask frontend on http://localhost:5173..."
cd frontend
export BACKEND_URL=http://localhost:8000
python run.py &
FRONTEND_PID=$!
cd ..

echo ""
echo "✓ Backend: http://localhost:8000 (PID: $BACKEND_PID)"
echo "✓ Frontend: http://localhost:5173 (PID: $FRONTEND_PID)"
echo ""
echo "Servers are running. Press Ctrl+C to stop..."

# Wait for interrupt
trap "echo ''; echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT

# Keep script running
wait