.PHONY: clean docs
VERSION := $(shell pip3 show PyHal | grep "Version" | awk '{split($$0, a, " ");print a[2]}')
HERE := $(shell pwd)

clean:
	rm -fr build dist *egg *.egg-info

show-installed-version:
	@echo "\033[95m\nInstalled PyHal v$(VERSION)\033[0m"

install:
	pipenv install
	$(MAKE) show-installed-version

pip-install:
	pip3 install -r requirements.txt . --upgrade --force-reinstall
	$(MAKE) show-installed-version

fast-install:
	sudo rm -rf /usr/local/lib/python3.6/dist-packages/hal
	sudo mkdir /usr/local/lib/python3.6/dist-packages/hal
	sudo cp -r hal/ /usr/local/lib/python3.6/dist-packages/
	@echo "\033[95m\nInstalled to /usr/local/lib/python3.6/dist-packages/hal\033[0m"
	$(MAKE) show-installed-version

test:
	rm -rf htmlcov/
	python3 -m pytest --cov=./ --cov-report=html
	@echo "\033[95m\nTest report htmlcov/index.html\033[0m"

flake8:
	pipenv run flake8 --ignore=E501,F401,E128,E402,E731,F821,E722 hal

pylint:
	pylint3 -j 8 hal/* || pylint-exit $?

coverage:
	pipenv run py.test --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=requests tests

publish:
	$(MAKE) clean
	pip3 install 'twine>=1.5.0'
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	$(MAKE) clean
	@echo "\033[95m\nPublished at https://pypi.org/project/PyHal/\033[0m"

docs:
	cd docs && $(MAKE) html
	@echo "\033[95m\nBuild successful! View the docs homepage at $(HERE)/docs/_build/html/index.html.\033[0m"
	xdg-open "$(HERE)/docs/_build/html/index.html"


bug-report:
	python3 hal/help.py
