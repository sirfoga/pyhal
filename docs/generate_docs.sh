#!/usr/bin/env bash

doxygen doxygen/Doxyfile  # doxygen docs

epydoc --config epydoc/Epydoc_html  # epydoc docs
epydoc --config epydoc/Epydoc_latex
epydoc --config epydoc/Epydoc_pdf

cd sphinx  # sphunx docs
make html
make latex
cd _build/latex && make  # compile latex docs
