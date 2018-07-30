# !/usr/bin/python3
# coding: utf_8

""" Setups library and install dependencies """


from setuptools import setup, find_packages


DESCRIPTION = \
    "HAL\n\n\
    A multipurpose library homemade from scratch to perform great stuff in a pythonic way\n\
    \n\
    Install\n\n\
    - $ pip3 install . --upgrade --force-reinstall, from the source\n\
    - $ pip3 install pyhal, via pip\n\
    \n\
    Questions and issues\n\n\
    The Github issue tracker is only for bug reports and feature requests."


setup(
    name="PyHal",
    version="10.0.3",
    author="sirfoga",
    author_email="sirfoga@protonmail.com",
    description="A multipurpose library to perform great stuff in the most "
                "easy, short and pythonic way.",
    long_description=DESCRIPTION,
    keywords="library scratch maths",
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
        "pycrypto",
        "pymongo",
        "requests",
        "scipy",
        "send2trash",
        "sklearn",
        "statsmodels",
        "stem",
        "unidiff"
    ],
    test_suite="tests"
)
