# Quantum Random Number Generator (QRNG)

A full-stack web application that generates truly random numbers using quantum computing principles via Qiskit. Features a Flask frontend with real-time statistics visualization and a Django REST API backend.

## Features

- **Quantum Random Number Generation**: Powered by Qiskit Hadamard circuits
- **Multiple Extraction Methods**: Von Neumann extractor or SHA-256 hash-based extraction
- **Real-time Statistics**: Dynamic visualization of bit distribution, entropy, and bias
- **Auto-refresh**: Optionally generate new random numbers automatically
- **Backend Health Monitoring**: Real-time status indicator
- **Modern UI**: Built with Flask and HTML/CSS

## Tech Stack

- **Backend**: Django 5.0+ with Django REST Framework
- **Frontend**: Flask with HTML/CSS
- **Quantum Computing**: Qiskit and Qiskit-Aer
- **Visualization**: Chart.js
- **Styling**: Bootstrap 5

## Prerequisites

- Python 3.12+ 
- Node.js 18+ and npm
- Qiskit dependencies (installed via requirements.txt)

## Quick Start

### Option 1: Using Startup Script (Recommended)

**Windows (PowerShell):**
```powershell
# Start both backend and frontend
.\start-project.ps1
```

### Option 2: Manual Setup

#### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
# From project root with PYTHONPATH set
cd ..
$env:PYTHONPATH="."
python backend/manage.py migrate
```

4. Start the Django server:
```bash
# Windows PowerShell
cd backend
$env:PYTHONPATH=".."
$env:DEBUG="True"
python manage.py runserver

# Linux/Mac
cd backend
export PYTHONPATH=..
export DEBUG=True
python manage.py runserver
```

Backend will run on `http://localhost:8000`

#### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Start the Flask server:
```bash
# Windows PowerShell
cd frontend
$env:BACKEND_URL="http://localhost:8000"
python app.py

# Linux/Mac
cd frontend
export BACKEND_URL=http://localhost:8000
python app.py
```

Frontend will run on `http://localhost:5173`

## API Endpoints

- `GET /health/` - Health check endpoint
- `GET /api/random/` - Generate random bits
  - Query parameters:
    - `bits` (default: 256) - Number of bits to generate (1-4096)
    - `mode` (default: simulator) - `simulator` or `ibmq`
    - `extractor` (default: von_neumann) - `von_neumann` or `hash`

Example:
```
GET /api/random/?bits=512&mode=simulator&extractor=hash
```

## Environment Variables

### Backend

Create a `.env` file in the `backend` directory (or use `env.example` as a template):

```env
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173
API_THROTTLE_ANON=30/min
API_THROTTLE_USER=120/min
API_THROTTLE_QRNG=60/min
IBMQ_TOKEN=  # Optional: For IBM Quantum hardware
IBMQ_BACKEND=ibmq_qasm_simulator
```

### Frontend

For production deployments, set the BACKEND_URL environment variable:
```env
BACKEND_URL=http://your-backend-url:8000
```

## Project Structure

```
QNRG/
├── backend/              # Django backend
│   ├── config/          # Django settings
│   ├── qrng/            # QRNG app
│   │   ├── extractor.py # Entropy extractors
│   │   ├── qiskit_engine.py # Quantum engine
│   │   └── views.py     # API views
│   └── manage.py
├── frontend/            # Flask frontend
│   ├── templates/       # HTML templates
│   ├── app.py           # Flask application
│   └── requirements.txt # Frontend dependencies
└── start-project.ps1    # Windows startup script
```

## Railway.app Deployment

The application is configured for deployment on Railway.app:

1. Backend served by Gunicorn + Django
2. Frontend served as a Flask application
3. `railway.yml` defines both services and their configurations

To deploy to Railway:
1. Push your code to a GitHub repository
2. Connect Railway to your repository
3. Railway will automatically detect the `railway.yml` configuration
4. Deploy both services
5. Set the `DJANGO_SECRET_KEY` environment variable in the Railway dashboard for the backend service

## Development Features

- **Dynamic Auto-refresh**: Enable auto-refresh with customizable interval
- **Health Monitoring**: Real-time backend connection status
- **Error Handling**: Comprehensive error messages and timeout handling
- **Copy & Download**: Export random data as text files
- **Responsive Design**: Works on desktop and mobile devices

## Troubleshooting

1. **Backend connection issues**: 
   - Ensure backend is running on port 8000
   - Check CORS settings in `backend/config/settings.py`
   - Verify `DEBUG=True` is set

2. **Module not found errors**:
   - Set `PYTHONPATH=.` before running Django commands
   - Ensure all dependencies are installed

3. **Frontend connection issues**:
   - Check `frontend/app.py` BACKEND_URL configuration
   - Verify backend is accessible at the configured URL

4. **Virtual environment conflicts**:
   - If you encounter import errors, temporarily rename the `.venv` directory
   - The project can run using the system Python environment
   - This is a known issue with the project's virtual environment setup

## License

This project is open source and available for educational and research purposes.