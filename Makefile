.PHONY: run test lint

run:
	python -m health_orchestrator.main

test:
	pytest -v

lint:
	python -m compileall src
