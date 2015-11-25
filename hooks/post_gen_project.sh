#!/usr/bin/env sh

git init
git add .
pre-commit install
git commit -a -m "Initial Cookiecutter Commit."
