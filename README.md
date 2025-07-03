
# Container and Microservices Health Orchestrator

This project monitors containerized microservices using Prometheus-style metrics, detects failures, makes healing decisions using a machine learning model, and triggers healing actions automatically.

## Features

- Health metrics collection (CPU, memory, error rate)
- Failure detection logic
- ML-based healing decision engine
- Automated orchestration actions (e.g., restart)
- Prometheus `/metrics` endpoint
- Flask-based API with live status
- Deployable via Docker and Kubernetes

---

## Project Structure

```
health-orchestrator/
│
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── app.py                         # Main Flask + Orchestration runner
│
├── health_monitor/
│   └── health_monitor.py         # Simulated health metrics generator
│
├── failure_detection/
│   └── failure_detection.py      # Detects failures based on metrics
│
├── healing_decision_engine/
│   ├── healing_decision_engine.py # Predicts healing actions
│   └── model.pkl                  # Pre-trained ML model
│
├── orchestration/
│   └── orchestration.py          # Executes healing actions
└── requirements.txt
```

---

## Docker Build

Make sure Minikube uses the local Docker daemon:

```bash
eval $(minikube docker-env)
docker build -t health-orchestrator:latest .
```

---

## Kubernetes Deployment

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Check pod status:

```bash
kubectl get pods -w
```

Check service and open in browser:

```bash
minikube service health-orchestrator-service
```

---

## Endpoints

* `GET /` — Orchestrator status
* `GET /metrics` — Prometheus-compatible metrics

---

## Model (ML)

* `healing_decision_engine/model.pkl`: Pre-trained model to decide between `"RESTART"` or `"NO_ACTION"` based on:

  * CPU usage
  * Memory usage
  * Error rate

---

## Local Development (Optional)

Run orchestrator:

```bash
python app.py
```

Run simulated health monitor:

```bash
python health_monitor/health_monitor.py
```

---

## Dependencies

```bash
pip install -r requirements.txt
```

Common dependencies include:

* Flask
* prometheus_client
* joblib
* numpy

---

## Observability

Use Prometheus to scrape `/metrics` for alerts and dashboards.

---

## Future Improvements

* Add authentication to APIs
* Replace mock data with real metrics collectors (e.g., Node Exporter)
* Support container auto-scaling
* Grafana integration

---


---
