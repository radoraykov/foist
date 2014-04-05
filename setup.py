#!/usr/bin/env python

import os
import sys

import foist

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


packages = [
    'foist',
]

requires = [
    'flask-restful'
]

with open('README.md') as f:
    readme = f.read()

setup(
    name='requests',
    version=foist.__version__,
    description='Web redacting tool',
    long_description=readme,
    author='',
    author_email='',
    url='https://github.com/obshtestvo/foist',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'foist': 'foist'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ),
)