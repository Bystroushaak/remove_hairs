#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from setuptools import setup, find_packages

from docs import getVersion


# Variables ===================================================================
changelog = open('CHANGES.rst').read()
long_description = "\n\n".join([
    open('README.rst').read(),
    changelog
])


# Actual setup definition =====================================================
setup(
    name='remove_hairs',
    version=getVersion(changelog),
    description='Function form removing characters from both sides of string.',
    long_description=long_description,
    url='https://github.com/Bystroushaak/remove_hairs',

    author='Bystroushaak',
    author_email='bystrousak@kitakitsune.org',

    classifiers=[
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: MIT License",
    ],
    license='MIT',

    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=True,

    test_suite='py.test',
    tests_require=["pytest"],
    extras_require={
        "test": [
            "pytest"
        ],
        "docs": [
            "sphinx",
            "sphinxcontrib-napoleon",
        ]
    },
)
