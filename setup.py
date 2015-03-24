#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from setuptools import find_packages
from distutils.core import setup


# Variables ===================================================================
changelog = open('CHANGES.rst').read()
long_description = "\n\n".join([
    open('README.rst').read(),
    changelog
])


# Functions & classes =========================================================
def allSame(s):
    return not filter(lambda x: x != s[0], s)


def hasDigit(s):
    return any(map(lambda x: x.isdigit(), s))


def getVersion(data):
    data = data.splitlines()
    return filter(
        lambda (x, y):
            len(x) == len(y) and allSame(y) and hasDigit(x) and "." in x,
        zip(data, data[1:])
    )[0][0]


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
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Text Processing",
    ],
    license='MIT',

    packages=find_packages('src'),
    package_dir={'': 'src'},
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
