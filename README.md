# Health Orchestrator [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Health Orchestrator is a Kubernetes-deployable Python application designed to monitor and manage health metrics of services, with automated healing and alerting mechanisms. It includes a Helm chart for easy deployment and management on any Kubernetes cluster.

---

## Features

- Monitor service health using custom metrics.
- Automatic healing based on health thresholds.
- Exposes Prometheus-compatible metrics for monitoring.
- Configurable via Helm values for flexible deployments.
- Includes readiness and liveness probes for Kubernetes.

---

## Project Structure

```

health-orchestrator/
├── app/                        # Main application code
├── docker/                     # Dockerfiles and docker-compose
├── helm-health-orchestrator/   # Helm chart for deployment
├── monitors/                   # Health monitoring and failure detection
├── healing/                    # Healing and decision engine modules
├── orchestrator/               # Actions and orchestration logic
├── deployment/                 # Kubernetes deployment/service templates
└── README.md

````

---

## Helm Chart Usage

The Helm chart simplifies deployment on Kubernetes.  

### Install the Chart

```bash
# Switch to your Kubernetes context (optional)
kubectl config use-context docker-desktop

# Install Helm chart
helm install health-orchestrator ./helm-health-orchestrator
````

### Verify Deployment

```bash
kubectl get pods
kubectl get svc health-orchestrator-helm-health-orchestrator
```

### Access the Application

```bash
export NODE_PORT=$(kubectl get svc health-orchestrator-helm-health-orchestrator -o jsonpath="{.spec.ports[0].nodePort}")
export NODE_IP=$(kubectl get nodes -o jsonpath="{.items[0].status.addresses[0].address}")
echo http://$NODE_IP:$NODE_PORT
```

---

## Configuration

Edit the `helm-health-orchestrator/values.yaml` to customize:

```yaml
replicaCount: 1

image:
  repository: health-orchestrator
  tag: latest
  pullPolicy: IfNotPresent

service:
  type: NodePort
  ports:
    api: 5000
    metrics: 8000
    nodePortAPI: 30001
    nodePortMetrics: 30002

readinessProbe:
  path: /metrics
  port: metrics
  initialDelaySeconds: 5
  periodSeconds: 10

livenessProbe:
  path: /metrics
  port: metrics
  initialDelaySeconds: 15
  periodSeconds: 20

serviceAccount:
  create: true
  name: ""

ingress:
  enabled: false

httpRoute:
  enabled: false

autoscaling:
  enabled: false
  minReplicas: 1
  maxReplicas: 3
  targetCPUUtilizationPercentage: 80
```

---

## Metrics

Exposes Prometheus metrics at:

```
/metrics
```

Example metrics:

```
python_gc_objects_collected_total
python_gc_collections_total
process_cpu_seconds_total
process_resident_memory_bytes
...
```

---

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make changes and commit.
4. Push your branch and open a Pull Request.

---

## License

MIT License © 2025 Saniya Acharya
