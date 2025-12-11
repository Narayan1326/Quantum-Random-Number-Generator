# Quantum RNG Architecture

This document captures the high-level architecture for the Quantum Random Number Generator project.

## Components

1. **Django Backend**  
   - Exposes `/api/random` endpoint powered by Qiskit.  
   - Applies von Neumann or SHA-256 extractors before responding.  
   - Includes `/health` endpoint for uptime checks.  
   - Provides throttling, CORS support, and pytest coverage.

2. **Flask Frontend**  
   - Collects user inputs (bits + mode) and calls backend API.  
   - Visualizes bit distribution with HTML/CSS.  
   - Simple and lightweight interface.

3. **Railway Deployment**  
   - Backend served by Gunicorn + Django.  
   - Frontend served as a Flask application.  
   - `railway.yml` defines both services and their configurations.

## Data Flow

```
[User] -> [Flask Frontend] -> [Requests to Django API]
        -> [Django REST API] -> [Qiskit Engine]
        -> [Extractor] -> [Response JSON]
```

## Security

- Secrets stored as environment variables.  
- Rate limiting via DRF throttles.  
- Optional IBMQ hardware gated by token presence.
