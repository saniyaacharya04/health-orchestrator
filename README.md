# Health Orchestrator

Health Orchestrator is a **production-grade backend platform** that simulates **automated system health monitoring and self-healing orchestration**, inspired by real-world **SRE and Platform Engineering systems** used in cloud-native environments.

The system continuously evaluates service metrics, detects failures, decides recovery actions using **rule-based and ML-assisted logic**, and executes orchestration actions with **structured logging, automated testing, and deployment readiness**.

This project demonstrates **end-to-end engineering ownership**, not a tutorial or toy application.

---

## Problem Statement

Modern distributed systems require:

* Continuous health monitoring
* Fast and reliable failure detection
* Automated recovery decisions
* Observability and traceability
* Safe degradation when ML components fail

Manual intervention is slow, error-prone, and does not scale.

Health Orchestrator addresses this problem by providing a **self-healing control plane** that mimics how real production systems detect issues and respond automatically.

---

## Key Features

### Core Features (Fully Implemented)

* System metrics generation (CPU, memory, error rate)
* Failure detection using configurable thresholds
* Healing decision engine:

  * Rule-based fallback logic
  * Optional ML-assisted inference with safe degradation
* Orchestration action execution
* REST API service
* Structured JSON logging
* Unit testing and end-to-end validation
* Docker, Kubernetes, and Helm readiness

### Intentional Design Choices

* No ML model artifacts committed to Git
* System remains functional when ML components are unavailable
* Clear separation of concerns between monitoring, decision-making, and execution

---

## Architecture Overview

```
                ┌────────────────────┐
                │   REST API Layer   │
                │  (/health, /orch) │
                └─────────┬──────────┘
                          │
          ┌───────────────┴───────────────┐
          │        Monitoring Layer        │
          │  Health Monitor + Failure Det. │
          └───────────────┬───────────────┘
                          │
          ┌───────────────┴───────────────┐
          │      Decision Engine           │
          │  Rule-based + ML-assisted      │
          └───────────────┬───────────────┘
                          │
          ┌───────────────┴───────────────┐
          │     Orchestration Actions      │
          │   Restart / No-Action Logic   │
          └───────────────────────────────┘
```

Each layer is independently testable and replaceable, closely mirroring real internal platform systems.

---

## Project Structure

```
health-orchestrator/
├── src/health_orchestrator/
│   ├── api/            # HTTP routes
│   ├── core/           # logging, config, errors
│   ├── monitors/       # metrics and failure detection
│   ├── healing/        # decision engine (rules + ML)
│   ├── orchestrator/   # action execution
│   └── main.py         # application entrypoint
├── tests/              # unit tests
├── scripts/            # end-to-end validation
├── docker/             # containerization
├── helm/               # Kubernetes Helm chart
├── deployment/         # raw Kubernetes manifests
├── Makefile
└── requirements.txt
```

---

## API Endpoints

### Health Check

```
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

### Orchestration Trigger

```
POST /orchestrate
```

Response:

```json
{
  "metrics": {
    "cpu": 43,
    "memory": 14,
    "error_rate": 5
  },
  "failure_detected": false,
  "action_taken": "NO_ACTION"
}
```

---

## Observability

* Centralized structured JSON logging
* Log levels: INFO, WARNING, ERROR
* Logs compatible with ELK, Loki, and CloudWatch pipelines
* No print statements in business logic

Example log:

```json
{
  "timestamp": "2025-12-19T09:53:45.668386",
  "level": "INFO",
  "logger": "health_orchestrator.healing.decision_engine",
  "message": "No action required"
}
```

---

## Testing Strategy

### Unit Tests

```bash
pytest -q
```

### End-to-End Test

```bash
bash scripts/e2e.sh
```

The end-to-end test performs the following:

* Starts the service
* Waits for readiness
* Calls `/health`
* Calls `/orchestrate`
* Fails immediately if any step breaks

This mirrors CI-level validation used in real production teams.

---

## Running Locally

### Environment Setup

```bash
conda create -n health-orchestrator python=3.10 -y
conda activate health-orchestrator
pip install -r requirements.txt
```

### Run the Service

```bash
make run
```

The service runs at:

```
http://localhost:8000
```

---

## Failure Modes and Handling

| Failure Scenario             | Handling Strategy               |
| ---------------------------- | ------------------------------- |
| Missing ML model             | Rule-based fallback             |
| ML inference error           | Safe NO_ACTION                  |
| High CPU or memory           | Trigger RESTART                 |
| Unknown orchestration action | Logged without crashing         |
| API misuse                   | Controlled response             |
| Service crash                | Container or Kubernetes restart |

---

## Scaling and Production Considerations

* Replace Flask development server with Gunicorn
* Integrate real metrics sources (Prometheus, OpenTelemetry)
* Externalize thresholds using environment configuration
* Persist orchestration actions for auditability
* Enable Horizontal Pod Autoscaling via Kubernetes
* Integrate with real orchestration backends

---

## Skills Demonstrated

* Backend system design
* SRE and platform engineering concepts
* ML system degradation handling
* Structured logging and observability
* Test-driven refactoring
* Docker and Kubernetes readiness
* CI-style end-to-end validation

---

## License

MIT License

---

## Final Note

This project is intentionally structured to resemble a **real internal platform service**, not a tutorial.
It is suitable for **resume shortlisting, system design interviews, and GitHub code reviews**.

---

