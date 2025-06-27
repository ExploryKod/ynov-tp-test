.PHONY: install test test-verbose coverage coverage-report clean lint all

install:
	pip install -r requirements.txt

test:
	pytest

test-verbose:
	pytest -v -s

coverage:
	pytest --cov=src/bibliotheque --cov-report=html --cov-report=term-missing

coverage-report:
	pytest --cov=src/bibliotheque --cov-report=html
	@echo "Rapport généré dans htmlcov/index.html"

clean:
	rm -rf htmlcov/ .coverage .pytest_cache/ __pycache__/
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyc" -delete

lint:
	python -m py_compile src/bibliotheque/*.py
	python -m py_compile tests/*.py

all: clean install test coverage
