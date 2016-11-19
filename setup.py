# !/usr/bin/python3
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os

from setuptools import setup, find_packages


def read(fname):
    """
    :param fname: string
        Path to file to read
    :return: string
        Content of file specified
    """

    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="PyHal",
    version="4.3",
    author="sirfoga",
    author_email="sirfoga@protonmail.com",
    description="Hal is a from-scratch home-made multipurpose library to perform most of stuff in python.",
    long_description=read("README.md"),
    license="Apache License, Version 2.0",
    keywords="library scratch maths",
    url="https://github.com/sirfoga/hal",
    packages=find_packages(exclude=["tests"]),
    install_requires=[  # TODO: uncomment packages (but travis will fail)
        "bs4",
        # "matplotlib",
        # "mutagen",
        "numpy",
        "pycrypto",
        # "scipy",
        # "sklearn",
        "requests",
        "lxml",
        "send2trash"
    ],
    test_suite="tests"
)
