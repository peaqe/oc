PYTHON=python3
PIP=pip3

all: lint

lint:
	flake8 oc setup.py

init:
	$(PIP) install pip --upgrade
	$(PIP) install pipenv --upgrade
	pipenv install --dev

publish: lint
	$(PYTHON) setup.py sdist bdist_wheel
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
	rm -rf build dist .egg oc.egg-info

test-publish: lint
	$(PYTHON) setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	rm -rf build dist .egg oc.egg-info

clean:
	find . -name *.py[oc] -or -name *~ | xargs rm -f
	rm -rf build dist .egg *.egg-info
	$(PYTHON) setup.py clean

.PHONY: clean test-publish publish init lint
