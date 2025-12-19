.PHONY: run test lint

run:
\tpython -m health_orchestrator.main

test:
\tpytest -v

lint:
\tpython -m compileall src
