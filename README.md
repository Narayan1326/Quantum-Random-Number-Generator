# 🔮 Quantum Random Number Generator (QRNG)

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org)
[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com)
[![Flask](https://img.shields.io/badge/Flask-3.0-black.svg)](https://flask.palletsprojects.com)
[![Qiskit](https://img.shields.io/badge/Qiskit-Quantum-purple.svg)](https://qiskit.org)
[![Chart.js](https://img.shields.io/badge/Chart.js-Visualization-red.svg)](https://www.chartjs.org)

A powerful full-stack application that generates **true quantum-based random numbers** using Qiskit Hadamard circuits, providing real-time visualizations, entropy extraction, and a modern dual-framework architecture using **Django (Backend)** and **Flask (Frontend)**.

---

## 🚀 Features

### 🎯 Core Functionality
- ⚛️ **Quantum Random Number Generation** using Qiskit  
- 🧮 **Multiple Entropy Extractors** — Von Neumann or SHA-256  
- 📊 **Real-time Statistics** — Bit distribution, entropy & bias  
- 🔁 **Auto-refresh Mode** — Continuous random number stream  
- ❤️ **Backend Health Indicator** — Live connection monitoring  
- 🖥️ **Modern UI** built with Flask + HTML/CSS  

---

## 🧩 Tech Stack

### 🖥️ Backend
- **Django 5.0+**  
- **Django REST Framework**  
- **Qiskit** for quantum circuit execution  
- **Gunicorn** for production (Railway deployment)

### 🎨 Frontend
- **Flask**  
- **Chart.js**  
- **Bootstrap 5** for styling  

### ⚙️ Other Tools
- **Python 3.12+**  
- **Qiskit-Aer** (simulated quantum backend)

---

## 🏗️ Project Structure

```
QRNG/
├── backend/               # Django backend
│   ├── config/            # Settings & config
│   ├── qrng/              # Core QRNG logic
│   │   ├── extractor.py   # Entropy extractors
│   │   ├── qiskit_engine.py # Quantum engine
│   │   └── views.py       # REST API views
│   └── manage.py
├── frontend/              # Flask frontend
│   ├── templates/         # HTML templates
│   ├── app.py             # Flask server
│   └── requirements.txt
└── start-project.ps1      # Auto-start script (Windows)
```

---

## ⚙️ Getting Started

### 📋 Prerequisites

- Python 3.12+
- Node.js 18+
- Qiskit dependencies

---


## 🛠️ Installation & Setup

### ▶️ Option 1: Auto Startup (Recommended)

**Windows PowerShell**

```
.\start-project.ps1
```

### ▶️ Option 2: Manual Setup
- 🖥️ Backend Setup (Django)**

1. Navigate to backend:

```
cd backend
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run migrations:

```
cd ..
$env:PYTHONPATH="."
python backend/manage.py migrate
```

4. Start server:

```
cd backend
$env:PYTHONPATH=".."
python manage.py runserver
```

➤ Backend runs on http://localhost:8000

### 🌐 Frontend Setup (Flask)

1. Navigate to frontend:

```
cd frontend
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Start frontend:

```
python app.py
```

➤ Frontend runs on http://localhost:5173

---


## 🔌 API Endpoints

###📥 Random Number Generation

```
GET /api/random/?bits=512&mode=simulator&extractor=hash
```

**Endpoints**

- ```GET /health/``` — Health status
- ```GET /api/random/``` — Generate quantum random bits
  - ```bits``` → Default: 256
  - ```mode``` → simulator / ibmq
  - ```extractor``` → von_neumann / hash

---


## 🔧 Environment Variables

### 🔹 Backend ```.env```

```
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173
IBMQ_TOKEN=
IBMQ_BACKEND=ibmq_qasm_simulator
```

### 🔹 Frontend

```
BACKEND_URL=http://your-backend-url:8000
```


## 🚀 Deployment (Railway.app)

- Django served using Gunicorn
- Flask served as a standalone app
- Fully configured using railway.yml

**Steps:**

1. Push to GitHub
2. Connect Railway
3. Railway auto-detects config
4. Deploy both frontend & backend
5. Set environment variables

---


## 💡 Development Features

- ⏱ Auto-refresh interval
- 🧪 Error & timeout handling
- 📁 Export random bits as text files
- 📱 Responsive mobile-friendly UI
- 🧭 Real-time QRNG system health

---

## 🛠 Troubleshooting

###❗ Backend Issues

- Check port ```8000```
- Validate CORS in Django settings

### ❗ Frontend Issues

- ```BACKEND_URL``` mismatch
- Missing Python packages

### ❗ Virtual Environment Problems

- Rename ```.venv``` temporarily
- Use system Python environment

---

📜 License

This project is open-source and intended for research & educational use.
