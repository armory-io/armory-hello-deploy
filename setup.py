#!/usr/bin/env python

from distutils.core import setup

setup(name='hello-deploy',
    version='1.0',
    description='Armory Hello Deploy Site',
    author='Isaac Mosquera',
    author_email='isaac@armory.io',
    data_files=[
        ('/etc/init/',['etc/armory-hello-server.conf']),
    ]
)
