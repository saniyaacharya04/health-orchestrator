def handle_webhook(payload: dict) -> dict:
    event_type = payload.get("type")

    if event_type == "checkout.session.completed":
        return {"status": "plan_upgraded"}

    return {"status": "ignored"}
