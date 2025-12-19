from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest

status_counter = Counter('orchestrator_status', 'Tracks orchestrator health')

def create_routes(app):
    @app.route('/')
    def home():
        status_counter.inc()
        return jsonify({"status": "Health Orchestrator running"})

    @app.route('/metrics')
    def metrics():
        return generate_latest(), 200
