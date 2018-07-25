#!/usr/bin/env bash
# coding: utf_8

# Pushes changes in docs branch
# Returns to main branch

chmod +x make.sh

echo "> always remember to commit any changes before checking out branches"
echo "> generating..."
./make.sh

echo "> moving to docs branch"
git checkout gh-pages  # change branch (to publish docs)
git push origin gh-pages

echo "> exiting..."
git checkout master