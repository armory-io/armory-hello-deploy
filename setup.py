#!/usr/bin/env python

from distutils.core import setup

setup(name='hello-deploy',
      version='1.0',
      description='Armory Hello Deploy Site',
      author='Isaac Mosquera',
      author_email='isaac@armory.io',
      packages=['armory.hellodeploy'],
      scripts=[
        'armory/scripts/start_server.py',
     ],
     install_requires=[
          'nose==1.3.7',
          'Flask==0.12'
     ],
     data_files=[
        ('/etc/init/',['armory/scripts/armory-hello-server.conf'])
    ]
)
