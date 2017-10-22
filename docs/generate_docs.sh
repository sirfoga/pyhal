# !/usr/bin/env bash
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
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


doxygen doxygen/Doxyfile  # doxygen docs

epydoc --config epydoc/Epydoc_html  # epydoc docs
epydoc --config epydoc/Epydoc_latex
epydoc --config epydoc/Epydoc_pdf

cd sphinx  # sphunx docs
make html
make latex
cd _build/latex && make  # compile latex
cd _build/html && make  # compile html
