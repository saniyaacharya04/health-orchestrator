from flask import Flask, jsonify
from health_orchestrator.core.logging import get_logger
from health_orchestrator.monitors.health_monitor import generate_metrics
from health_orchestrator.monitors.failure_detector import detect_failure
from health_orchestrator.healing.decision_engine import predict_action
from health_orchestrator.orchestrator.actions import execute_action

from health_orchestrator.api.saas_routes import register_saas_routes
from health_orchestrator.api.bootstrap_routes import register_bootstrap_routes
from health_orchestrator.api.billing_routes import register_billing_routes

logger = get_logger(__name__)
app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/orchestrate", methods=["POST"])
def orchestrate():
    metrics = generate_metrics()
    failure = detect_failure(metrics, 80, 80, 5)
    action = predict_action(metrics)
    execute_action(action)

    return jsonify({
        "metrics": metrics,
        "failure_detected": failure,
        "action_taken": action
    }), 200

# SaaS + Billing wiring (THIS WAS MISSING)
register_bootstrap_routes(app)
register_saas_routes(app)
register_billing_routes(app)

def main():
    logger.info("Starting Health Orchestrator SaaS")
    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
