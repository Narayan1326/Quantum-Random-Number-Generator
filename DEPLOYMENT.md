# Deployment Guide

This document explains how to deploy the Quantum Random Number Generator (QRNG) application to Railway.

## Prerequisites

1. A GitHub account
2. A Railway account (railway.app)
3. Git installed on your local machine

## Deployment Steps

### Deploy to Railway.app

#### 1. Push to GitHub

First, make sure your project is pushed to a GitHub repository:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/qrng.git
git push -u origin main
```

#### 2. Deploy to Railway

1. Go to [Railway Dashboard](https://railway.app/)
2. Create a new project
3. Connect your GitHub repository
4. Railway will automatically detect the `railway.yml` configuration file
5. Deploy both services (backend and frontend)
6. Add environment variables in the Railway dashboard:
   - For backend:
     - `DJANGO_SECRET_KEY`: Your secret key (keep this secure)
   - For frontend:
     - No additional variables needed (BACKEND_URL is automatically configured)

Alternatively, you can use the Railway CLI:

1. Install the Railway CLI: `npm install -g @railway/cli`
2. Login: `railway login`
3. Initialize: `railway init`
4. Deploy: `railway up`

### Manual Deployment Scripts

You can also use the provided deployment scripts:

#### For Linux/Mac:
```bash
chmod +x start-dev.sh
./start-dev.sh
```

#### For Windows:
```powershell
.\start-dev.ps1
```

## Environment Variables

### Backend (.env file in backend directory)
```env
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,anotherdomain.com
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
API_THROTTLE_ANON=30/min
API_THROTTLE_USER=120/min
API_THROTTLE_QRNG=60/min
IBMQ_TOKEN=  # Optional: For IBM Quantum hardware
IBMQ_BACKEND=ibmq_qasm_simulator
```

### Frontend
```env
BACKEND_URL=https://your-backend-url.com
PORT=10000
```

## Troubleshooting

1. **Backend connection issues**:
   - Ensure `ALLOWED_HOSTS` includes your frontend domain
   - Check CORS settings in `backend/config/settings.py`
   - Verify `BACKEND_URL` is correctly set in frontend environment

2. **Module not found errors**:
   - Ensure `PYTHONPATH` is set correctly
   - Check that all dependencies are installed

3. **Deployment fails**:
   - Check build logs in Railway dashboard
   - Ensure all environment variables are set
   - Verify requirements.txt files are up to date
   - Try specifying Python version 3.11 in runtime.txt

4. **Railpack build errors**:
   - Railway uses Railpack to build Python applications
   - If you encounter "Error creating build plan with Railpack":
     - Ensure you have a `runtime.txt` file specifying Python version (e.g., `python-3.11`)
     - Check that all dependencies in `requirements.txt` are compatible with Python 3.11
     - Some packages like qiskit may have specific build requirements
     - Consider using Docker-based deployment if Railpack continues to fail

5. **Qiskit dependency issues**:
   - Qiskit is a complex package with native dependencies
   - If build fails due to qiskit, try:
     - Using Python 3.11 (more compatible)
     - Checking Railway build logs for specific error messages
     - Considering a Docker deployment approach

## Scaling Considerations

For production use:
1. Upgrade from free tier to paid plans for better performance
2. Add a custom domain
3. Enable automatic deploys from GitHub
4. Set up monitoring and alerts
5. Consider using a managed database instead of SQLite