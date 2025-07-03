from flask import Flask, jsonify
import threading
import time
from prometheus_client import start_http_server, Gauge, REGISTRY

# Unregister any previous registrations (useful in reload/dev mode)
for collector in list(REGISTRY._names_to_collectors):
    if collector in ["failure_count", "healing_actions_total", "service_health"]:
        REGISTRY.unregister(REGISTRY._names_to_collectors[collector])

from health_monitor.health_monitor import collect_metrics
from failure_detection.failure_detection import detect_failures, fetch_metrics
from healing_decision_engine.healing_decision_engine import recommend_healing_action
from orchestration.orchestration import execute_action

# Initialize Flask app
app = Flask(__name__)
orchestrator_status = {"running": False, "last_run": None}

# Initialize Prometheus metrics
failure_count_gauge = Gauge("failure_count", "Number of failures detected")
healing_actions_total = Gauge("healing_actions_total", "Number of healing actions taken")
service_health = Gauge("service_health", "Health of the microservice", ["service_id"])
