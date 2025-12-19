def upgrade_plan(org_id: str) -> dict:
    return {
        "status": "locked",
        "message": "Upgrade requires payment",
        "next_step": "stripe_checkout"
    }
