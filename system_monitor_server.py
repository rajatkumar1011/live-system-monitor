import psutil
import datetime
from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='.')

def get_performance_metrics():
    cpu_usage = psutil.cpu_percent(interval=0.5)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    return cpu_usage, memory_usage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    cpu, memory = get_performance_metrics()
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    return jsonify({
        "cpu_percent": cpu,
        "memory_percent": memory,
        "timestamp": timestamp
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

