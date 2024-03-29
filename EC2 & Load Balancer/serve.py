from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def trigger_stress():
    # Start a new process to run stress_cpu.py
    subprocess.Popen(["python", "stress_cpu.py"])
    return "CPU stress process started", 200

@app.route('/', methods=['GET'])
def get_private_ip():
    # Get the private IP address
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
