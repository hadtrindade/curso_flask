clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf *egg-info
	rm -rf *tox/
	rm -rf docs/_build
	pip install -e .['dev'] --upgrade --no-cache


install:
	pip install -e .['dev']

init_db:
	FLASK_APP=chico_delivery/app.py flask create-db
	FLASK_APP=chico_delivery/app.py flask db upgrade

test:
	pytest tests/ -v --cov=chico_delivery



