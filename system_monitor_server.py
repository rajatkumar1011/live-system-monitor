import psutil
import datetime
from flask import Flask, jsonify, render_template

# Initialize the Flask application
# The second argument tells Flask where to look for the HTML file.
app = Flask(__name__, template_folder='.')

def get_performance_metrics():
    """
    Retrieves the current CPU and memory usage percentages.
    """
    # Get CPU usage percentage over a short interval
    cpu_usage = psutil.cpu_percent(interval=0.5)

    # Get virtual memory information (RAM)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    return cpu_usage, memory_usage

@app.route('/')
def index():
    """
    Serves the main HTML page.
    """
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    """
    API endpoint to get the latest system stats.
    """
    cpu, memory = get_performance_metrics()
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    
    # Return the data as a JSON object
    return jsonify({
        "cpu_percent": cpu,
        "memory_percent": memory,
        "timestamp": timestamp
    })

if __name__ == "__main__":
    # This part is mostly for testing on your own computer.
    # Render will use the 'gunicorn' command you provide instead.
    app.run(host="0.0.0.0", port=5000)

