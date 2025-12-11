# PowerShell script to start the development servers
# Backend: Django on port 8000
# Frontend: Flask on port 5173

Write-Host "Starting QNRG Development Servers..." -ForegroundColor Cyan
Write-Host ""

# Start backend in background
Write-Host "Starting Django backend on http://localhost:8000..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\backend'; `$env:PYTHONPATH='..'; `$env:DEBUG='True'; `$env:CORS_ALLOW_ALL='True'; python manage.py runserver" -WindowStyle Minimized

# Wait a bit for backend to start
Start-Sleep -Seconds 3

# Note: Flask frontend needs to be started manually in a separate terminal
# To start Flask frontend:
# cd frontend
# $env:BACKEND_URL="http://localhost:8000"
# python app.py

Write-Host ""
Write-Host "✓ Backend: http://localhost:8000" -ForegroundColor Green
Write-Host "ℹ Frontend: Start Flask manually in a separate terminal" -ForegroundColor Cyan
Write-Host ""
Write-Host "Both servers are running. Press any key to stop all servers..." -ForegroundColor Cyan
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Kill the processes (optional cleanup)
Write-Host "Stopping servers..." -ForegroundColor Yellow
Get-Process | Where-Object {$_.MainWindowTitle -like "*powershell*"} | Where-Object {$_.Path -like "*powershell*"} | Stop-Process -Force -ErrorAction SilentlyContinue