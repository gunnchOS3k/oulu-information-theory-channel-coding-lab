install:
	pip install -r requirements.txt

test:
	PYTHONPATH=src pytest -q

e2e:
	PYTHONPATH=src python3 scripts/run_all_experiments.py
	PYTHONPATH=src python3 scripts/generate_figures.py
	@echo PASS e2e
