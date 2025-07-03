# main_orchestrator.py

from flask import Flask, jsonify
import threading
import time

from health_monitor.health_monitor import collect_metrics
from failure_detection.failure_detection import detect_failures, fetch_metrics
from healing_decision_engine.healing_decision_engine import recommend_healing_action
from orchestration.orchestration import execute_action


app = Flask(__name__)
orchestrator_status = {"running": False, "last_run": None}

def orchestrate_loop():
    orchestrator_status["running"] = True
    while True:
        metrics = fetch_metrics()
        failures = detect_failures(metrics)
        actions = recommend_healing_action(failures)

        for service_id, action in actions.items():
            execute_action(action, f"my_microservice_{service_id}")

        orchestrator_status["last_run"] = time.strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(10)  # Run every 10 seconds

@app.route("/")
def status():
    return jsonify({
        "message": "Health Orchestrator is running!",
        "orchestrator_status": orchestrator_status
    })

if __name__ == "__main__":
    # Start orchestrator in background
    orchestrator_thread = threading.Thread(target=orchestrate_loop, daemon=True)
    orchestrator_thread.start()

    # Start Flask app
    app.run(host="0.0.0.0", port=8000)
