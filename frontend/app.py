from flask import Flask, render_template, request, jsonify, send_from_directory
import requests
import os
from flask_compress import Compress

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600  # Cache static files for 1 hour
Compress(app)  # Enable gzip compression

# Configuration
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:8000')

@app.route('/')
def index():
    return render_template('index.html')

# Serve favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/api/generate', methods=['GET'])
def generate_random():
    # Get parameters from query string
    bits = request.args.get('bits', 256, type=int)
    mode = request.args.get('mode', 'simulator')
    extractor = request.args.get('extractor', 'von_neumann')
    
    # Validate parameters
    if bits < 8 or bits > 4096:
        return jsonify({'error': 'Bits must be between 8 and 4096'}), 400
    
    if mode not in ['simulator']:
        return jsonify({'error': 'Mode must be simulator'}), 400
        
    if extractor not in ['von_neumann', 'hash']:
        return jsonify({'error': 'Extractor must be von_neumann or hash'}), 400
    
    # Call Django backend API
    try:
        response = requests.get(f'{BACKEND_URL}/api/random/', params={
            'bits': bits,
            'mode': mode,
            'extractor': extractor
        }, timeout=60)
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': f'Backend API error: {response.status_code}'}), response.status_code
            
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Backend request timed out. Please try again.'}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Unable to connect to backend service. Please check if the service is running.'}), 502
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500

@app.route('/api/health')
def health_check():
    try:
        response = requests.get(f'{BACKEND_URL}/health/', timeout=5)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'status': 'error', 'message': 'Backend unhealthy'}), 500
    except requests.exceptions.ConnectionError:
        return jsonify({'status': 'error', 'message': 'Backend unreachable - connection failed'}), 502
    except requests.exceptions.Timeout:
        return jsonify({'status': 'error', 'message': 'Backend unreachable - timeout'}), 504
    except requests.exceptions.RequestException:
        return jsonify({'status': 'error', 'message': 'Backend unreachable - general error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5173, debug=True)
    
