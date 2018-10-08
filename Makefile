.PHONY: docs
init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

pip-init:
    pip3 install . --upgrade --force-reinstall

fast-init:
    PACKAGE="hal"
    LOCAL_FOLDER="${PWD}/${PACKAGE}/*"
    PYTHON_VERSION="python3.6"
    DIST_FOLDER="/usr/local/lib/${PYTHON_VERSION}/dist-packages/${PACKAGE}"

    cd ..
    rm -rf ${DIST_FOLDER}  # clean
    mkdir ${DIST_FOLDER}
    cp -r ${LOCAL_FOLDER} ${DIST_FOLDER}  # copy recursively
    echo "Installed to ${DIST_FOLDER}"

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
	pip3 install 'twine>=1.5.0'
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg requests.egg-info

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"