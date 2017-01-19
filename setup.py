#!/usr/bin/env python
import os
from distutils.core import setup

build_number=os.environ.get("BUILD_NUMBER", "0")
setup(name='hello-deploy',
    version='0.%s' % build_number,
    description='Armory Hello Deploy Site',
    author='Isaac Mosquera',
    author_email='isaac@armory.io',
    install_requires=[
        'Flask==0.12',
    ],
    packages=[
        'armory',
        'armory.hellodeploy',
        'armory.hellodeploy.static',
        'armory.hellodeploy.templates'
    ],
    scripts=['armory/scripts/hello_deploy_start.py'],
    package_data={'': ['*.*']},
    include_package_data=True,
    data_files=[
        ('/etc/init/',['etc/armory-hello-deploy.conf']),
        ('/etc/default/',[
            'etc/default/armory-hello-deploy',
            'etc/server-env'
        ])
    ]
)
