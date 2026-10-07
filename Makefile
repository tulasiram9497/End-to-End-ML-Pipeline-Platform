PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PYTHON_VENV := $(VENV)/bin/python

.PHONY: install lint format test typecheck clean run-api

install:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

lint:
	$(PYTHON_VENV) -m ruff check src tests
	$(PYTHON_VENV) -m black --check src tests

format:
	$(PYTHON_VENV) -m black src tests
	$(PYTHON_VENV) -m ruff check --fix src tests

test:
	$(PYTHON_VENV) -m pytest -q

typecheck:
	$(PYTHON_VENV) -m mypy src

clean:
	rm -rf $(VENV) .pytest_cache .mypy_cache .ruff_cache

run-api:
	$(PYTHON_VENV) -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
