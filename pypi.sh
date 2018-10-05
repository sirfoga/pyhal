# !/bin/bash
# coding: utf_8

INSTALL_FOLDER=${PWD}
TWINE_FOLDER="${HOME}/bin/twine/twine/"

rm -rf build dist *.egg-info  # clean
python3 setup.py sdist bdist_wheel  # build

cd ${TWINE_FOLDER}
python3 __main__.py upload ${INSTALL_FOLDER}/dist/*  # upload
