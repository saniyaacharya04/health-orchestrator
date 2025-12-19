from health_orchestrator.core.logging import get_logger

logger = get_logger(__name__)


def detect_failure(metrics, cpu_threshold, memory_threshold, error_threshold):
    failure = (
        metrics["cpu"] > cpu_threshold
        or metrics["memory"] > memory_threshold
        or metrics["error_rate"] > error_threshold
    )

    logger.info(
        f"Failure detection evaluated",
    )

    if failure:
        logger.warning(f"Failure detected with metrics={metrics}")
    else:
        logger.info("System operating within thresholds")

    return failure
