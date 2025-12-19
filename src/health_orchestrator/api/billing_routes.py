from flask import request, jsonify
from health_orchestrator.billing.service import upgrade_plan
from health_orchestrator.billing.webhook import handle_webhook
from health_orchestrator.core.logging import get_logger

logger = get_logger(__name__)

def register_billing_routes(app):

    @app.route("/billing/upgrade", methods=["POST"])
    def billing_upgrade():
        payload = request.json or {}
        org_id = payload.get("org_id")

        if not org_id:
            return jsonify({"error": "org_id required"}), 400

        logger.info(f"Billing upgrade requested for org={org_id}")
        return jsonify(upgrade_plan(org_id)), 402

    @app.route("/billing/webhook", methods=["POST"])
    def billing_webhook():
        payload = request.json or {}
        logger.info("Stripe webhook received")
        return jsonify(handle_webhook(payload)), 200
