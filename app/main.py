from flask import Flask, jsonify
import threading
from prometheus_client import start_http_server, generate_latest
from monitors.health_monitor import generate_metrics
from monitors.failure_detector import detect_failure
from healing.decision_engine import predict_action
from orchestrator.actions import execute_action
import time

app = Flask(__name__)

CPU_THRESHOLD = 90
MEMORY_THRESHOLD = 90
ERROR_THRESHOLD = 5
MODEL_PATH = "healing/model.pkl"

def orchestrator_loop():
    while True:
        metrics = generate_metrics()
        if detect_failure(metrics, CPU_THRESHOLD, MEMORY_THRESHOLD, ERROR_THRESHOLD):
            action = predict_action(metrics, MODEL_PATH)
            execute_action(action)
        time.sleep(5)  # Run every 5 seconds

@app.route("/")
def home():
    return jsonify({"status": "orchestrator running"})

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    # Start Prometheus metrics server in a thread
    threading.Thread(target=lambda: start_http_server(8000), daemon=True).start()
    # Start orchestrator loop in a thread
    threading.Thread(target=orchestrator_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
