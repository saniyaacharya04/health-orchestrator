from health_orchestrator.core.logging import get_logger

logger = get_logger(__name__)


def execute_action(action: str):
    if action == "RESTART":
        logger.warning("Executing RESTART action")
    elif action == "NO_ACTION":
        logger.info("No action executed")
    else:
        logger.error(f"Unknown action received: {action}")
