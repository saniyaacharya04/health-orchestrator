#!/usr/bin/env bash
set -e

echo "=== SAAS E2E TEST START ==="

make run > /tmp/saas.log 2>&1 &
PID=$!

cleanup() {
  kill $PID 2>/dev/null || true
}
trap cleanup EXIT

sleep 2

echo "Bootstrapping organization..."

ORG_JSON=$(curl -s -X POST http://localhost:8000/api/dev/bootstrap \
  -H "Content-Type: application/json" \
  -d '{"org_name":"e2e-org"}')

echo "Bootstrap response: $ORG_JSON"

export ORG_JSON

API_KEY=$(python -c "
import json, os
print(json.loads(os.environ['ORG_JSON'])['api_key'])
")

echo "Using API key: $API_KEY"
echo "Testing freemium enforcement..."

RESP=$(curl -s -X POST http://localhost:8000/api/v1/metrics \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $API_KEY" \
  -d '{"cpu":95}')

echo "Metrics response: $RESP"

if echo "$RESP" | grep -q "Upgrade Required"; then
  echo "Freemium enforcement WORKING"
else
  echo "ERROR: Freemium enforcement FAILED"
  exit 1
fi

echo "=== SAAS E2E PASSED ==="
