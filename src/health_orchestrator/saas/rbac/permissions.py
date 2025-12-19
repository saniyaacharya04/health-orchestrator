def can_execute_action(role: str) -> bool:
    return role in {"admin", "member"}
