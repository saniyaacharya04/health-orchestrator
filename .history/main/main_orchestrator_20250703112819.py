from flask import Flask, jsonify
import threading
import time
from prometheus_client import start_http_server, Gauge, CollectorRegistry, REGISTRY

from health_monitor.health_monitor import collect_metrics
from failure_detection.failure_detection import detect_failures, fetch_metrics
from healing_decision_engine.healing_decision_engine import recommend_healing_action
from orchestration.orchestration import execute_action

app = Flask(__name__)
orchestrator_status = {"running": False, "last_run": None}

# Create a custom registry (to avoid duplicates on re-import)
registry = CollectorRegistry()

# Prometheus metrics (using default REGISTRY here only once)
failure_count_gauge = Gauge("failure_count", "Number of failures detected", registry=REGISTRY)
healing_actions_total = Gauge("healing_actions_total", "Number of healing actions taken", registry=REGISTRY)
service_health = Gauge("service_health", "Health of the microservice", ["service_id"], registry=REGISTRY)

def orchestrate_loop():
    orchestrator_status["running"] = True
    while True:
        try:
            metrics = fetch_metrics()
            failures = detect_failures(metrics)
            actions = recommend_healing_action(failures)

            failure_count_gauge.set(len(failures))
            healing_actions_total.set(len(actions))

            for service_id, action in actions.items():
                health_value = 0 if action != "NO_ACTION" else 1
                service_health.labels(service_id=service_id).set(health_value)
                execute_action(action, f"my_microservice_{service_id}")

            orchestrator_status["last_run"] = time.strftime("%Y-%m-%d %H:%M:%S")

        except Exception as e:
            print(f"[ERROR] in orchestrate_loop: {e}")
            orchestrator_status["last_run"] = f"Error: {e}"

        time.sleep(10)

@app.route("/")
def status():
    return jsonify({
        "message": "Health Orchestrator is running!",
        "orchestrator_status": orchestrator_status
    })

if __name__ == "__main__":
    print("🚀 Starting Prometheus metrics server on port 9000...")
    start_http_server(9000)

    print("🚀 Starting health orchestrator thread...")
    orchestrator_thread = threading.Thread(target=orchestrate_loop, daemon=True)
    orchestrator_thread.start()

    print("🚀 Starting Flask app on port 8000...")
    app.run(host="0.0.0.0", port=8000)
