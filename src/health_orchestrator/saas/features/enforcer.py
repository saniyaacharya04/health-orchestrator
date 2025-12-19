from health_orchestrator.saas.features.gates import is_feature_enabled

def enforce_feature(plan: str, feature: str):
    if not is_feature_enabled(plan, feature):
        return False, {
            "error": "Upgrade Required",
            "feature": feature,
            "current_plan": plan
        }
    return True, None
