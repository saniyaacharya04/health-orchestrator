.PHONY: run test lint clean e2e

run:
	python -m health_orchestrator.main

test:
	pytest -q

e2e:
	bash scripts/saas_e2e.sh

lint:
	python -m compileall src

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -rf .pytest_cache
