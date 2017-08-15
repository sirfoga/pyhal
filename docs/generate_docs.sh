#!/usr/bin/env bash

doxygen doxygen/Doxyfile  # doxygen docs

epydoc --config epydoc/Epydoc_dvi  # epydoc docs
epydoc --config epydoc/Epydoc_html
epydoc --config epydoc/Epydoc_latex
epydoc --config epydoc/Epydoc_pdf
epydoc --config epydoc/Epydoc_ps
