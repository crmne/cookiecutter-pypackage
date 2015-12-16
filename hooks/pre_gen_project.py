#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def verify_executable_installed(executable, instmsg):
    from distutils.spawn import find_executable

    if not find_executable(executable):
        print("ERROR: {0}: command not found!".format(executable))
        print("Installation: " + instmsg)

        # exits with status 1 to indicate failure
        sys.exit(1)


def verify_python_module_name():
    import re

    MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

    module_name = '{{ cookiecutter.project_slug }}'

    if not re.match(MODULE_REGEX, module_name):
        print('ERROR: %s is not a valid Python module name!' % module_name)

        # exits with status 1 to indicate failure
        sys.exit(1)


def verify_feature_branch_name():
    import subprocess

    branch_name = '{{ cookiecutter.first_feature_branch_name }}'

    process_name = ['git', 'check-ref-format', '--branch', branch_name]
    process = subprocess.Popen(process_name)
    exit_status = process.wait()

    if exit_status != 0:
        print('ERROR: %s is not a valid feature branch name!' % branch_name)

        # exits with status != 0 to indicate failure
        sys.exit(exit_status)


if __name__ == '__main__':
    verify_executable_installed("pre-commit", "pip install pre-commit")
    verify_executable_installed("wercker", "see http://wercker.com/downloads")
    verify_python_module_name()
    verify_feature_branch_name()
