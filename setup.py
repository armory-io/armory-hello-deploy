#!/usr/bin/env python
import os
from setuptools import setup, find_packages

build_number=os.environ.get("BUILD_NUMBER", "0")
print(find_packages())
setup(name='hello-deploy',
    version='0.%s.0' % build_number,
    description='Armory Hello Deploy Site',
    author='Isaac Mosquera',
    author_email='isaac@armory.io',
    install_requires=[
        'Flask==0.12'
    ],
    packages= find_packages(),
    # [
    #     'armory',
    #     'armory.hellodeploy',
    #     'armory.hellodeploy.static',
    #     'armory.hellodeploy.templates'
    # ],
    scripts=['armory/scripts/hello_deploy_start.py'],
    include_package_data=True,

    # hopefully fpm can do this one day (add separate files)
    # data_files=[
        # ('/etc/init/',['/home/armory/etc/armory-hello-deploy.conf']),
        # ('/etc/default/',[
        #     '/home/armory/etc/default/armory-hello-deploy',
        #     '/home/armory/etc/server-env'
        # ])
    # ]
)
