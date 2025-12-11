# Deployment Guide

This document explains how to deploy the Quantum Random Number Generator (QRNG) application to Render.

## Prerequisites

1. A GitHub account
2. A Render account (free tier available at render.com)
3. Git installed on your local machine

## Deployment Steps

### 1. Push to GitHub

First, make sure your project is pushed to a GitHub repository:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/qrng.git
git push -u origin main
```

### 2. Deploy to Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New+" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - Name: `qrng-backend`
   - Environment: `Python 3`
   - Build command: `cd backend && pip install -r requirements.txt`
   - Start command: `cd backend && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`
   - Plan type: Free

5. Add environment variables:
   - `DJANGO_SECRET_KEY`: Your secret key (keep this secure)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your Render URL (e.g., `qrng-backend.onrender.com`)
   - `PYTHONPATH`: `..`

6. Click "Create Web Service"

7. Deploy the frontend:
   - Click "New+" and select "Web Service" again
   - Name: `qrng-frontend`
   - Environment: `Python 3`
   - Build command: `cd frontend && pip install -r requirements.txt`
   - Start command: `cd frontend && export BACKEND_URL=https://YOUR_BACKEND_URL && python run.py`
   - Plan type: Free

8. Add environment variables for frontend:
   - `PORT`: `10000` (or any port you prefer)
   - `BACKEND_URL`: The URL of your deployed backend service

### 3. Alternative: Using render.yaml

If you have the `render.yaml` file in your repository, Render will automatically detect and configure both services.

### 4. Manual Deployment Scripts

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
   - Check build logs in Render dashboard
   - Ensure all environment variables are set
   - Verify requirements.txt files are up to date

## Scaling Considerations

For production use:
1. Upgrade from free tier to paid plans for better performance
2. Add a custom domain
3. Enable automatic deploys from GitHub
4. Set up monitoring and alerts
5. Consider using a managed database instead of SQLite