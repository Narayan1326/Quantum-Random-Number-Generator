# PowerShell script to start the QRNG project
# Backend: Django on port 8000
# Frontend: Flask on port 5173

Write-Host "Starting Quantum Random Number Generator (QRNG) Project..." -ForegroundColor Cyan
Write-Host ""

# Function to check if a port is in use
function Test-Port {
    param([int]$Port)
    $process = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
    return $process -ne $null
}

# Check if ports are already in use
if (Test-Port 8000) {
    Write-Host "Warning: Port 8000 (Backend) is already in use!" -ForegroundColor Yellow
}

if (Test-Port 5173) {
    Write-Host "Warning: Port 5173 (Frontend) is already in use!" -ForegroundColor Yellow
}

# Start backend in background
Write-Host "Starting Django backend on http://localhost:8000..." -ForegroundColor Yellow
$backendJob = Start-Job -ScriptBlock {
    cd "$using:PSScriptRoot\backend"
    $env:PYTHONPATH = ".."
    $env:DEBUG = "True"
    python manage.py runserver
}

# Wait a bit for backend to start
Start-Sleep -Seconds 3

# Start Flask frontend
Write-Host "Starting Flask frontend on http://localhost:5173..." -ForegroundColor Yellow
$frontendJob = Start-Job -ScriptBlock {
    cd "$using:PSScriptRoot\frontend"
    $env:BACKEND_URL = "http://localhost:8000"
    python app.py
}

Write-Host ""
Write-Host "✓ Backend: http://localhost:8000" -ForegroundColor Green
Write-Host "✓ Frontend: http://localhost:5173" -ForegroundColor Green
Write-Host ""
Write-Host "Both servers are running in the background." -ForegroundColor Cyan
Write-Host "Press any key to stop all servers..." -ForegroundColor Cyan

# Wait for user input
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Stop the jobs
Write-Host "Stopping servers..." -ForegroundColor Yellow
Stop-Job $backendJob
Stop-Job $frontendJob
Remove-Job $backendJob
Remove-Job $frontendJob

Write-Host "Servers stopped." -ForegroundColor Green