#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def verify_python_module_name():
    import re

    MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

    module_name = '{{ cookiecutter.module_name }}'

    if not re.match(MODULE_REGEX, module_name):
        print('ERROR: %s is not a valid Python module name!' % module_name)

        # exits with status 1 to indicate failure
        sys.exit(1)


def verify_feature_branch_name():
    import subprocess

    branch_name = '{{ cookiecutter.first_feature_branch_name }}'

    process = subprocess.Popen(['git', 'check-ref-format', branch_name])
    exit_status = process.wait()

    if exit_status != 0:
        print('ERROR: %s is not a valid feature branch name!' % branch_name)

        # exits with status != 0 to indicate failure
        sys.exit(exit_status)


if __name__ == '__main__':
    verify_python_module_name()
    verify_feature_branch_name()
