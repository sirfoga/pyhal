# !/bin/bash
# coding: utf_8

PACKAGE="hal"
LOCAL_FOLDER="${PWD}/${PACKAGE}/*"
PYTHON_VERSION="python3.6"
DIST_FOLDER="/usr/local/lib/${PYTHON_VERSION}/dist-packages/${PACKAGE}"

rm -rf ${DIST_FOLDER}  # clean
mkdir ${DIST_FOLDER}
cp -r ${LOCAL_FOLDER} ${DIST_FOLDER}  # copy recursively
echo "Installed to ${DIST_FOLDER}"