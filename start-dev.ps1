# PowerShell script to start the development servers
# Backend: Django/Gunicorn on port 8000
# Frontend: Flask on port 5173

Write-Host "Starting QNRG Development Servers..." -ForegroundColor Cyan
Write-Host ""

# Start backend with Gunicorn
Write-Host "Starting Django backend with Gunicorn on http://localhost:8000..." -ForegroundColor Yellow
cd backend
$env:PYTHONPATH=".."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "gunicorn config.wsgi:application --bind 0.0.0.0:8000" -WindowStyle Minimized
cd ..

# Wait a bit for backend to start
Start-Sleep -Seconds 3

# Start Flask frontend
Write-Host "Starting Flask frontend on http://localhost:5173..." -ForegroundColor Yellow
cd frontend
$env:BACKEND_URL="http://localhost:8000"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python run.py" -WindowStyle Minimized
cd ..

Write-Host ""
Write-Host "✓ Backend: http://localhost:8000" -ForegroundColor Green
Write-Host "✓ Frontend: http://localhost:5173" -ForegroundColor Green
Write-Host ""
Write-Host "Servers are running. Press any key to stop..." -ForegroundColor Cyan
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Kill the processes (optional cleanup)
Write-Host "Stopping servers..." -ForegroundColor Yellow
Get-Process | Where-Object {$_.MainWindowTitle -like "*powershell*"} | Where-Object {$_.Path -like "*powershell*"} | Stop-Process -Force -ErrorAction SilentlyContinue