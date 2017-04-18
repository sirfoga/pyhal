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


from setuptools import setup, find_packages


DESCRIPTION = \
    "HAL\n\n\
    Handy Algorithmic Library: a multipurpose library homemade from scratch to perform great stuff in a pythonic way.\n\
    \n\
    Examples\n\n\
    You can take a look at my other repository: there are lots of implementations from various HAL modules.\n\
    \n\
    Install\n\n\
    - $ python3 setup.py install from the source\n\
    - $ pip3 install pyhal via pip\n\
    \n\
    Questions and issues\n\n\
    The github issue tracker is only for bug reports and feature requests." \
    "Anything else, such as questions for help in using the library, should be posted in StackOverflow.\n\
    \n\
    License: Apache License Version 2.0, January 2004"


setup(
    name="PyHal",
    version="4.4.4",
    author="sirfoga",
    author_email="sirfoga@protonmail.com",
    description="Hal is a from-scratch home-made multipurpose library to perform most of stuff in python.",
    long_description=DESCRIPTION,
    license="Apache License, Version 2.0",
    keywords="library scratch maths",
    url="https://github.com/sirfoga/hal",
    packages=find_packages(exclude=["tests"]),
    install_requires=[  # TODO: uncomment packages (but travis will fail)
        "bs4",
        "mutagen",
        "numpy",
        "pycrypto",
        "scipy",
        "sklearn",
        "requests",
        "lxml",
        "send2trash"
    ],
    test_suite="tests"
)
