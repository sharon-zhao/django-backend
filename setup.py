uploadParameters"""Sets up the package"""

#!/usr/bin/env python
 # -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py
import os
import io
import json
from setuptools import setup, find_packages

# with open('README.md') as f:
#     README = f.read()
#
# with open('LICENSE.md') as f:
#     LICENSE = f.read()
with io.open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding="utf-8") as f:
    readme = f.read()

with io.open(os.path.join(os.path.dirname(__file__), 'package.json'), encoding="utf-8") as f:
    package = json.loads(f.read())

setup(
    name='django-envoy-api',
    version='0.1.0',
    description='GA SEI Boston Django Authentication Template',
    long_description=README,
    author='<author>',
    author_email='<email>',
    # url='https://git.generalassemb.ly/ga-wdi-boston/django-envoy-api',
    url=package['homepage'],
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs')),
    packages=['s3direct'],
    include_package_data=True,
    install_requires=['django>=1.8'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
