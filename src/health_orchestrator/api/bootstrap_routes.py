from flask import jsonify, request
from health_orchestrator.saas.orgs.models import Organization
from health_orchestrator.saas.auth.api_keys import generate_api_key
from health_orchestrator.saas.features.plans import FREE

def register_bootstrap_routes(app):

    @app.route("/api/dev/bootstrap", methods=["POST"])
    def bootstrap_org():
        payload = request.json or {}
        name = payload.get("org_name", "demo-org")

        org = Organization.create(name, plan=FREE)
        api_key = generate_api_key(org.id)

        app._register_org(org)

        return jsonify({
            "org_id": org.id,
            "org_name": org.name,
            "plan": org.plan,
            "api_key": api_key
        }), 201
