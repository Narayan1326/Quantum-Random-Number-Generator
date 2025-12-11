import os
from app import app

if __name__ == '__main__':
    # Get port from environment variable or default to 5173
    port = int(os.environ.get('PORT', 5173))
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=port, debug=False)