from flask import Flask, jsonify
from flask_cors import CORS
import psutil
from datetime import datetime
import pytz

app = Flask(__name__)
CORS(app)

def get_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    
    # Get the current time and convert it to IST
    ist = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.now(ist)
    timestamp = now_ist.strftime('%H:%M:%S') # e.g., 16:07:15

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

