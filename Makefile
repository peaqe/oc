PYTHON=python3

all: lint

lint:
	flake8 oc.py setup.py

publish: lint
	$(PYTHON) setup.py sdist bdist_wheel
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
	rm -rf build dist .egg oc.egg-info

test-publish: lint
	$(PYTHON) setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	rm -rf build dist .egg oc.egg-info

clean:
	rm -rf *~  build dist .egg *.egg-info
	$(PYTHON) setup.py clean

.PHONY: clean test-publish publish lint
