import os
import signal
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Storage for IPs and data (mock database for simplicity)
# For production, use a real database like SQLite or PostgreSQL.
ips = []
data = []

# Banner function
def banner():
    print("\n       ██   ██  ██████  ██    ██ ███    ██ ██████ ")
    print("       ██   ██ ██    ██ ██    ██ ████   ██ ██   ██ ")
    print("       ███████ ██    ██ ██    ██ ██ ██  ██ ██   ██ ")
    print("       ██   ██ ██    ██ ██    ██ ██  ██ ██ ██   ██ ")
    print("       ██   ██  ██████   ██████  ██   ████ ██████  \n")
    print("       Hound Ver 0.2 - Now Powered by Python & Flask")
    print("       Hosted on Render.com\n")

# Signal handling to gracefully stop the server
def signal_handler(sig, frame):
    print("\n[!] Stopping the server...")
    os._exit(0)

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')  # Ensure you create an `index.html` file in a `templates` folder

@app.route('/log_ip', methods=['POST'])
def log_ip():
    ip = request.remote_addr
    if ip not in ips:
        ips.append(ip)
    return jsonify({"message": "IP logged successfully", "ip": ip})

@app.route('/get_ips', methods=['GET'])
def get_ips():
    return jsonify(ips)

@app.route('/log_data', methods=['POST'])
def log_data():
    incoming_data = request.json
    data.append(incoming_data)
    return jsonify({"message": "Data logged successfully", "data": incoming_data})

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data)

# Start the server
if __name__ == '__main__':
    banner()
    signal.signal(signal.SIGINT, signal_handler)
    print("[+] Starting Flask server on port 8080...")
    app.run(host="0.0.0.0", port=8080)
