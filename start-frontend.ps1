# PowerShell script to start the Flask frontend
# Frontend: Flask on port 5173

Write-Host "Starting Flask frontend..." -ForegroundColor Cyan

cd frontend
$env:FLASK_APP="app.py"
$env:BACKEND_URL="http://localhost:8000"
flask run --host=0.0.0.0 --port=5173