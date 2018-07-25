#!/usr/bin/env bash
# coding: utf_8

# Generates docs in correct git branch
# Commits changes in that branch
# Returns to main branch

OUTPUT_FOLDER="doxygen/html/"
DOCS_FOLDER="docs/"
DOCS_BRANCH="gh-pages"
BUILD_FOLDER="build/"
BUILD_COMMAND="doxygen Doxyfile"
COMMIT_MSG=$(git log -1 --pretty=%B)  # last commit message
COMMIT_MSg="${COMMIT_MSG} (generated docs)"  # add docs notice

echo "> always remember to commit any changes before checking out branches"
echo "> cleaning..."
rm -rf ${OUTPUT_FOLDER}  # clean
rm -rf ${BUILD_FOLDER}

echo "> generating..."
# todo eval ${BUILD_COMMAND}  # make docs
# todo mv ${OUTPUT_FOLDER}* ${BUILD_FOLDER}  # move to build folder

echo "> moving to docs branch"
# todo git checkout ${DOCS_BRANCH}  # change branch (to publish docs)
# todo mv ${BUILD_FOLDER}* ../  # move to root

rm -rf ${BUILD_FOLDER}  # clean

echo "> committing changes"
# todo git add --all
# todo git commit -m "${COMMIT_MSG} (generated docs)"

echo "> exiting..."
git checkout master