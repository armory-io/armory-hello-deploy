#!/usr/bin/env python
import os
from distutils.core import setup

build_number = os.environ.get("BUILD_NUMBER", "0")
setup(name='hello-deploy',
    version='0.%s' % build_number,
    description='Armory Hello Deploy Site',
    author='Isaac Mosquera',
    author_email='isaac@armory.io',
    data_files=[
        ('/etc/init/',['etc/armory-hello-server.conf']),
        ('/etc/default/armory-hello-deploy',['etc/armory-hello-server.properties'])
    ]
)
