#!/usr/bin/env python

from __future__ import absolute_import
from setuptools import setup, find_packages

from dung.util.plugin import entrypoints_for_plugins
import dung.command

setup(name='dung',
    version='1.0',
    description='''dung beetle simulation''',
    author='Daniel Holz',
    author_email='dgholz@gmail.com',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'simplejson',
        'argparse',
        'pyzmq',
    ],
    entry_points={
        'console_scripts': [
            "dung = dung.cli:main",
        ],
        'dung.command': entrypoints_for_plugins(dung.command),
    },
    tests_require=['nose>=1.0'],
    test_suite='nose.collector',
)
