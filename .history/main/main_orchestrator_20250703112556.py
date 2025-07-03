from flask import Flask, jsonify
import threading
import time
from prometheus_client import start_http_server, Gauge, REGISTRY

# --------------------------------------
# 🛡 Unregister metrics if already registered
# --------------------------------------
def unregister_if_exists(metric_name):
    try:
        collector = REGISTRY._names_to_collectors.get(metric_name)
        if collector:
            REGISTRY.unregister(collector)
    except Exception as e:
        print(f"Warning: Couldn't unregister {metric_name}: {e}")

for metric in ["failure_count", "healing_actions_total", "service_health"]:
    unregister_if_exists(metric)

# --------------------------------------
# 📦 Internal module imports
# --------------------------------------
from health_monitor.health_monitor import collect_metrics
from failure_detection.failure_detection import detect_failures, fetch_metrics
from healing_decision_engine.healing_decision_engine import recommend_healing_action
from orchestration.orchestration import execute_action

# --------------------------------------
# 🚀 Flask App + Status
# --------------------------------------
app = Flask(__name__)
orchestrator_status = {"running": False, "last_run": None}

# --------------------------------------
# 📊 Prometheus Metrics
# --------------------------------------
failure_count_gauge = Gauge("failure_count", "Number of failures detected")
healing_actions_total = Gauge("healing_actions_total", "Number of healing actions taken")
service_health = Gauge("service_health", "Health of the microservice", ["service_id"])

# --------------------------------------
# 🔁 Orchestration Loop
# --------------------------------------
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
                health = 0 if action != "NO_ACTION" else 1
                service_health.labels(service_id=service_id).set(health)
                execute_action(action, f"my_microservice_{service_id}")

            orchestrator_status["last_run"] = time.strftime("%Y-%m-%d %H:%M:%S")

        except Exception as e:
            print(f"[ERROR] in orchestrate_loop: {e}")
            orchestrator_status["last_run"] = f"Error: {e}"

        time.sleep(10)

# --------------------------------------
# 🌐 Flask Endpoint
# --------------------------------------
@app.route("/")
def status():
    return jsonify({
        "message": "Health Orchestrator is running!",
        "orchestrator_status": orchestrator_status
    })

# --------------------------------------
# 🧠 Entry Point
# --------------------------------------
if __name__ == "__main__":
    # Start Prometheus metrics server
    start_http_server(9000)

    # Start background thread for orchestrator
    orchestrator_thread = threading.Thread(target=orchestrate_loop, daemon=True)
    orchestrator_thread.start()

    # Start Flask app
    app.run(host="0.0.0.0", port=8000)
