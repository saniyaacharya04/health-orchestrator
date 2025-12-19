def is_feature_enabled(plan: str, feature: str) -> bool:
    free_features = {
        "basic_orchestration",
        "manual_trigger",
    }

    premium_features = {
        "ml_decision_engine",
        "auto_orchestration",
        "integrations",
        "audit_logs",
    }

    if plan == "free":
        return feature in free_features

    if plan == "premium":
        return feature in free_features.union(premium_features)

    return False
