# Health Orchestrator

**Production-Style SaaS for Automated System Health Monitoring & Self-Healing**

Health Orchestrator is a **SaaS-ready backend system** that monitors system metrics, detects failures, enforces freemium feature access, and orchestrates automated recovery actions.
It is designed to demonstrate **end-to-end ownership**, **backend architecture**, and **real SaaS engineering practices**.

This is **not a demo project** — it is structured the way real infrastructure SaaS products are built.

---

## Core Capabilities

### 1. System Monitoring

* CPU, memory, error-rate metric ingestion
* Structured JSON logging
* Deterministic, testable metric generation

### 2. Failure Detection

* Threshold-based failure detection engine
* Configurable limits per metric
* Clean separation between monitoring and decision logic

### 3. Healing Decision Engine

* Rule-based fallback (always available)
* ML-ready decision path (premium-gated)
* Safe default behavior when models are unavailable

### 4. Orchestration Layer

* Action execution abstraction
* Supports restart / no-action flows
* Extendable for real infrastructure hooks

---

## SaaS Architecture (Key Differentiator)

### Organization & Auth

* Organization bootstrap endpoint
* API-key based authentication
* Multi-tenant aware design

### Freemium Enforcement

* **Free Plan**

  * Metrics ingestion
  * Health checks
* **Premium Plan (Locked / Placeholder)**

  * Auto-orchestration
  * ML-based healing
  * Integrations
  * Audit logs

Requests to locked features return:

```json
{
  "error": "Upgrade Required",
  "feature": "auto_orchestration",
  "current_plan": "free"
}
```

### Usage Tracking

* Per-organization usage counters
* Ready for billing integration

### Billing (Stripe-Ready Stubs)

* `/billing/upgrade` endpoint
* Stripe webhook handler placeholder
* Clean separation between billing logic and core system

---

## API Overview

### Health Check

```http
GET /health
```

### Organization Bootstrap (Dev)

```http
POST /api/dev/bootstrap
```

Returns:

* `org_id`
* `api_key`
* `plan`

### Metric Ingestion (SaaS)

```http
POST /api/v1/metrics
X-API-Key: <api_key>
```

### Billing

```http
POST /billing/upgrade
POST /billing/webhook
```

---

## End-to-End Testing

### Unit Tests

```bash
pytest -q
```

### SaaS E2E Test

```bash
bash scripts/saas_e2e.sh
```

E2E validates:

* Org bootstrap
* API key auth
* Freemium enforcement
* Correct HTTP status codes
* Full service lifecycle

---

## Local Development

### Environment Setup

```bash
conda create -n health-orchestrator python=3.10
conda activate health-orchestrator
pip install -r requirements.txt
```

### Run Service

```bash
make run
```

Service runs at:

```
http://localhost:8000
```

---

## CI/CD

GitHub Actions pipeline:

* Dependency install
* Unit tests
* SaaS E2E validation

Located at:

```
.github/workflows/ci.yml
```

---

## Infrastructure Readiness

Included but optional:

* Dockerfile
* docker-compose
* Helm charts
* Kubernetes manifests

This allows:

* Local dev
* Containerized deployment
* Kubernetes deployment

---

## Project Structure (High Level)

```
src/health_orchestrator/
├── api/            # HTTP routes
├── billing/        # Billing stubs
├── core/           # Logging, config, errors
├── healing/        # Decision engine
├── monitors/       # Metrics + failure detection
├── orchestrator/   # Action execution
├── saas/           # Auth, plans, usage, RBAC
└── main.py         # Application entrypoint
```

---

## Why This Project Stands Out

This project demonstrates:

* Real SaaS thinking (freemium, billing, auth)
* Clean backend architecture
* Production-style logging
* CI + E2E discipline
* Infrastructure awareness
* End-to-end ownership

It is intentionally built the way **early-stage startups and platform teams** design backend systems.

---

## Roadmap (Optional Future Work)

* Replace in-memory stores with Postgres
* Async workers for orchestration
* Real ML model integration
* Stripe checkout integration
* Rate limiting per API key
* Web dashboard

---

## License

MIT License

