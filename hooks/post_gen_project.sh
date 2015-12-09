#!/usr/bin/env bash

# fail on error
set -e

echo "Setting up local git repository..."
git init
git add .
pre-commit install
git commit -a -m "Initial Cookiecutter Commit."
git checkout -b "{{ cookiecutter.first_feature_branch_name }}"
echo "Setting up virtualenv..."
virtualenv --system-site-packages env
echo "Project {{ cookiecutter.project_slug }} initialized successfully."
