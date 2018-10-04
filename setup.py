# !/usr/bin/python3
# coding: utf_8

""" Setups library and install dependencies """


from setuptools import setup, find_packages

LITTLE_DESCRIPTION = "A multipurpose library homemade from scratch to perform " \
                     "great stuff in a pythonic way "
DESCRIPTION = \
    "HAL\n" + LITTLE_DESCRIPTION + "\n\
    Install\n\
    - $ pip3 install . --upgrade --force-reinstall, from the source\n\
    - $ pip3 install PyHal, via pip\n\
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
    keywords="library scratch awesome",
    url="https://github.com/sirfoga/pyhal",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "aiohttp",
        "aiosocks",
        "bs4",
        "colorama",
        "Crypto",
        "GitPython",
        "httplib2",
        "lxml",
        "matplotlib",
        "mutagen",
        "numpy",
        "oauth2client",
        "psutil",
        "pymongo",
        "requests",
        "scipy",
        "send2trash",
        "sklearn",
        "statsmodels",
        "stem",
        "unidiff", 'pyparsing'
    ],
    test_suite="tests"
)
