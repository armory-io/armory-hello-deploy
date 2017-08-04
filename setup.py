#!/usr/bin/env python
import os
from setuptools import setup, find_packages

build_number = os.environ.get("BUILD_NUMBER", "0")
print(find_packages())
setup(name='hello-deploy',
    version='0.%s.0' % build_number,
    description='Armory Hello Deploy Site',
    author='Isaac Mosquera',
    author_email='isaac@armory.io',
    install_requires=[
        'Flask==0.12',
        'apscheduler'
    ],
    packages= find_packages(),
    scripts=['armory/scripts/hello_deploy_start.py',
            'armory/scripts/inject_canary_errors.py'
    ],
    include_package_data=True
)
