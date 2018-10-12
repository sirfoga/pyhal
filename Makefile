init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

pip-install:
	pip3 install . --upgrade --force-reinstall
	version=$(pip3 show pyhal | grep "Version" | awk '{split($0, a, " "); print a[2]}')
	@echo "\033[95m\nInstalled version $version\033[0m"

fast-install:
	rm -rf /usr/local/lib/python3.6/dist-packages/hal
	mkdir /usr/local/lib/python3.6/dist-packages/hal
	cp -r hal/ /usr/local/lib/python3.6/dist-packages/
	@echo "\033[95m\nInstalled to /usr/local/lib/python3.6/dist-packages/hal\033[0m"

test:
	# This runs all of the tests, on both Python 2 and Python 3.
	detox

ci:
	pipenv run py.test -n 8 --boxed --junitxml=report.xml

flake8:
	pipenv run flake8 --ignore=E501,F401,E128,E402,E731,F821 requests

coverage:
	pipenv run py.test --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=requests tests

publish:
	rm -fr build dist *egg *.egg-info
	pip3 install 'twine>=1.5.0'
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist *egg *.egg-info
	@echo "\033[95m\nPublished at https://pypi.org/project/PyHal/\033[0m"

docs:
	cd docs && make html
	@echo "\033[95m\nBuild successful! View the docs homepage at docs/_build/html/index.html.\033[0m"