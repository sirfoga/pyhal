# !/bin/bash
# coding: utf_8

LOCAL_FOLDER="${PWD}/hal/*"
PYTHON_VERSION="python3.6"
DIST_FOLDER="/usr/local/lib/${PYTHON_VERSION}/dist-packages/hal"

rm -rf ${DIST_FOLDER}  # clean
mkdir ${DIST_FOLDER}
cp -r ${LOCAL_FOLDER} ${DIST_FOLDER}  # copy recursively
echo "Installed to ${DIST_FOLDER}"