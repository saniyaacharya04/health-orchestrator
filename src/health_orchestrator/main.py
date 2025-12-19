from flask import Flask, jsonify
from health_orchestrator.core.logging import get_logger
from health_orchestrator.monitors.health_monitor import generate_metrics
from health_orchestrator.monitors.failure_detector import detect_failure
from health_orchestrator.healing.decision_engine import predict_action
from health_orchestrator.orchestrator.actions import execute_action

logger = get_logger(__name__)

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    logger.info("Health check requested")
    return jsonify({"status": "ok"}), 200


@app.route("/orchestrate", methods=["POST"])
def orchestrate():
    logger.info("Orchestration triggered")

    metrics = generate_metrics()
    failure = detect_failure(metrics, cpu_threshold=80, memory_threshold=80, error_threshold=5)

    action = predict_action(metrics)
    execute_action(action)

    response = {
        "metrics": metrics,
        "failure_detected": failure,
        "action_taken": action,
    }

    logger.info(f"Orchestration completed with response={response}")
    return jsonify(response), 200


def main():
    logger.info("Starting Health Orchestrator service")
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
