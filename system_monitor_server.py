from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import psutil
from datetime import datetime
import pytz

app = Flask(__name__)
CORS(app)

# This new route tells the server to show your index.html file
# when a user visits the main homepage.
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

def get_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    
    ist = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.now(ist)
    timestamp = now_ist.strftime('%H:%M:%S')

    return {
        "cpu_percent": cpu_percent,
        "memory_percent": memory_info.percent,
        "timestamp": timestamp
    }

@app.route('/api/stats')
def stats():
    return jsonify(get_stats())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

