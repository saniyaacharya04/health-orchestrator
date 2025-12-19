#!/usr/bin/env bash
set -e

echo "=== [E2E] Starting Health Orchestrator ==="

# Start service in background
make run > /tmp/health_orchestrator.log 2>&1 &
APP_PID=$!

echo "Service PID: $APP_PID"

# Ensure cleanup on exit
cleanup() {
  echo "=== [E2E] Stopping service ==="
  kill $APP_PID 2>/dev/null || true
}
trap cleanup EXIT

# Wait for service to be ready
echo "=== [E2E] Waiting for service ==="
for i in {1..10}; do
  if curl -s http://localhost:8000/health >/dev/null; then
    echo "Service is up"
    break
  fi
  sleep 1
done

# Health check
echo "=== [E2E] Testing /health ==="
HEALTH_RESPONSE=$(curl -s http://localhost:8000/health)
echo "Response: $HEALTH_RESPONSE"

if [[ "$HEALTH_RESPONSE" != *"ok"* ]]; then
  echo "Health check failed"
  exit 1
fi

# Orchestration check
echo "=== [E2E] Testing /orchestrate ==="
ORCH_RESPONSE=$(curl -s -X POST http://localhost:8000/orchestrate)
echo "Response: $ORCH_RESPONSE"

if [[ "$ORCH_RESPONSE" != *"action_taken"* ]]; then
  echo "Orchestration failed"
  exit 1
fi

echo "=== E2E TEST PASSED ==="
