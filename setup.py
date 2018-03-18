#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(name='archub',
    version='0.0.1',
    install_requires=[
        'requests',
        'pygithub',
    ],
    author='Don Grote',
    author_email='dgrote@refirmlabs.com',
    scripts=[
        'scripts/archub',
        'scripts/ah',
    ],
    packages=find_packages(exclude=['tests']))
