#!/usr/bin/env bash
# coding: utf_8

# Copyright 2016-2018 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


OUTPUT_FOLDER="epydoc/html/"
DOCS_FOLDER="docs/"
LOCAL_DOCS_FOLDER="$HOME/Coding/Python/docs/pyhal"
BUILD_FOLDER="build/"
COMMIT_MSG=$(git log -1 --pretty=%B)  # last commit message

echo "\n\n<<<<    CLEANING    >>>>\n\n"
rm -rf ${OUTPUT_FOLDER}  # clean
rm -rf ${BUILD_FOLDER}
rm -rf ${LOCAL_DOCS_FOLDER}
mkdir ${BUILD_FOLDER}  # prepare build folder

echo "\n\n<<<<    GENERATING DOCS    >>>>\n\n"
epydoc --config epydoc/Epydoc_html  # make docs
cp ${OUTPUT_FOLDER}* ${LOCAL_DOCS_FOLDER}  # copy docs
mv ${OUTPUT_FOLDER}* ${BUILD_FOLDER}  # move to build folder

echo "\n\n<<<<    MOVING TO GH-PAGES    >>>>\n\n"
git checkout gh-pages  # change branch (to publish docs)
mv ${BUILD_FOLDER}* ../

rm -rf ${BUILD_FOLDER}  # clean

echo "\n\n<<<<    COMMITTING    >>>>\n\n"
git add --all
git commit -m "${COMMIT_MSG} (generated docs)"

echo "\n\n<<<<    GETTING BACK TO MASTER    >>>>\n\n"
git checkout master