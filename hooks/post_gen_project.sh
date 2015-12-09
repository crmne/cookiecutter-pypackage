#!/usr/bin/env bash

# fail on error
set -e

git init
git add .
pre-commit install
git commit -a -m "Initial Cookiecutter Commit."
git checkout -b "{{ cookiecutter.first_feature_branch_name }}"
echo "Project {{ cookiecutter.project_slug }} initialized successfully."
