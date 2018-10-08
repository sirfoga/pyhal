#!/usr/bin/env python

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


LITTLE_DESCRIPTION = "Your swiss knife to perform fast and easy pythonic stuff"
DESCRIPTION = \
    "HAL\n" + LITTLE_DESCRIPTION + "\n\
    Install\n\
    - $ pip install . --upgrade --force-reinstall, from the source\n\
    - $ pip install PyHal, via pip\n\
    Questions and issues\n\
    The Github issue tracker is only for bug reports and feature requests."
VERSION = open("VERSION").readlines()[0]
VERSION_NUMBER = VERSION.split(" ")[0]


setup(
    name="PyHal",
    version=VERSION_NUMBER,
    author="sirfoga",
    author_email="sirfoga@protonmail.com",
    description=LITTLE_DESCRIPTION,
    long_description=DESCRIPTION,
    keywords="hal library general-purpose",
    url="https://github.com/sirfoga/pyhal",
    packages=find_packages(exclude=["tests"]),
    test_suite="tests"
)
