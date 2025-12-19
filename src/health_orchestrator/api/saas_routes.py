from flask import request, jsonify
from health_orchestrator.saas.auth.api_keys import validate_api_key
from health_orchestrator.saas.usage.tracker import record_usage
from health_orchestrator.saas.features.enforcer import enforce_feature
from health_orchestrator.saas.orgs.models import Organization
from health_orchestrator.healing.decision_engine import predict_action
from health_orchestrator.orchestrator.actions import execute_action

_ORGS = {}

def register_saas_routes(app):

    @app.route("/api/v1/metrics", methods=["POST"])
    def ingest_metrics():
        api_key = request.headers.get("X-API-Key")
        org_id = validate_api_key(api_key)

        if not org_id:
            return jsonify({"error": "Invalid API key"}), 401

        org = _ORGS.get(org_id)
        if not org:
            return jsonify({"error": "Organization not found"}), 404

        allowed, error = enforce_feature(org.plan, "auto_orchestration")
        if not allowed:
            return jsonify(error), 403

        metrics = request.json or {}
        record_usage(org_id, "metrics_ingest")

        action = predict_action(metrics)
        execute_action(action)

        return jsonify({
            "status": "processed",
            "action": action
        }), 200

    # internal helper
    def _register_org(org: Organization):
        _ORGS[org.id] = org

    app._register_org = _register_org
