# !/bin/bash
# coding: utf_8

# Uploads to pypi the dist files

python3 setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
rm -rf build dist *.egg-info