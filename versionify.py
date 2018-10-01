# !/usr/bin/python3
# coding: utf-8

""" Updates version in file with last commit """

import os

from hal.cvs.gits import Repository

REPO_LOCATION = os.getcwd()
OUTPUT_FILE = os.path.join(
    REPO_LOCATION,
    "VERSION"
)


def get_new_version(version):
    return version


def read_lines(path):
    """
    :param path: str
        Path of file
    :return: [] of str
        Lines in file
    """

    with open(path, "r") as inp:
        return inp.readlines()


def get_old_version():
    lines = read_lines(OUTPUT_FILE)
    raw = lines[0].strip()
    return raw


def update_version(new_version):
    """
    :param new_version: str
        Version to write as first line
    :return: void
        Writes file with new version
    """

    lines = read_lines(OUTPUT_FILE)
    lines[0] = new_version
    with open(OUTPUT_FILE, "w") as out:
        out.writelines(lines)


def main():
    print("Parsing", REPO_LOCATION)

    repo = Repository(REPO_LOCATION)
    new_version = repo.get_pretty_version(0.001)
    old_version = get_old_version()

    print("Old version:", old_version)
    print("New version:", new_version)

    new_line = get_new_version(new_version) + "\n"
    update_version(new_line)
    print("Written to", OUTPUT_FILE)


if __name__ == '__main__':
    main()
