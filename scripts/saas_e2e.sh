#!/usr/bin/env bash
set -e

make run > /tmp/saas.log 2>&1 &
PID=$!
sleep 2

ORG=$(curl -s -X POST http://localhost:8000/api/dev/bootstrap)
KEY=$(echo $ORG | python -c "import sys,json;print(json.load(sys.stdin)['api_key'])")

RESP=$(curl -s -X POST http://localhost:8000/api/v1/metrics \
  -H "X-API-Key: $KEY" \
  -d '{"cpu":95}')

echo "$RESP" | grep "Upgrade Required"

kill $PID
echo "SAAS E2E PASSED"
