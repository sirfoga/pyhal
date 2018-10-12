#!/usr/bin/env python

import os

from setuptools import setup, find_packages


def get_version_details(path):
    """Parses version file

    :param path: path to version file
    :return: version details
    """

    with open(path, "r") as reader:
        lines = reader.readlines()
        data = {
            line.split(" = ")[0].replace("__", ""):
                line.split(" = ")[1].strip().replace("'", "")
            for line in lines
        }
        return data


# folders
HERE = os.path.abspath(os.path.dirname(__file__))
SRC_FOLDER = os.path.join(HERE, "hal")

# version
VERSION_FILE = os.path.join(SRC_FOLDER, "__version__.py")
VERSION = get_version_details(VERSION_FILE)

# descriptions
LITTLE_DESCRIPTION = VERSION["description"]
DESCRIPTION = \
    "HAL\n" + LITTLE_DESCRIPTION + "\n\
    Install\n\
    - $ make install, with pipenv\n\
    - $ make pip-install, with pip\n\
    - $ pip install PyHal, via pip\n\
    Questions and issues\n\
    The Github issue tracker is only for bug reports and feature requests."


setup(
    name=VERSION["title"],
    version=VERSION["version"],
    author=VERSION["author"],
    author_email=VERSION["author_email"],
    description=LITTLE_DESCRIPTION,
    long_description=DESCRIPTION,
    keywords="hal library general-purpose",
    url=VERSION["url"],
    packages=find_packages(exclude=["tests"])
)
