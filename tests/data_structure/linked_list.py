# !/usr/bin/python
# coding: utf_8


""" Tests linked list implementation """

from functools import partial
from unittest import TestCase

from hal.files.models.system import fix_raw_path, remove_year, \
    remove_brackets, extract_name_max_chars, BAD_CHARS, prettify
from hal.tests import utils


class TestPaths(TestCase):
    """ Tests hal.files.models.FileSystem path handlers """

    def test_fix_raw_path(self):
        """
        :return: bool
            True iff FileSystem.fix_raw_path correctly handles raw paths
        """

        tests = {
            "//a/b/c": "/a/b/c",  # double separators
            "/a/b/c.txt": "/a/b/c.txt"  # files
        }
        utils.battery_test(
            self.assertEqual, tests, fix_raw_path
        )

    def test_remove_year(self):
        """
        :return: bool
            True iff FileSystem.remove_year correctly removes years from paths
        """

        tests = {
            "Today is 1980": "Today is ",
            # year in start, middle, end position of sentence
            "Today 1980 is ": "Today  is ",
            "1980 Today is ": " Today is ",
            "19803": "3",  # composition of year
            "20012002": ""
        }
        utils.battery_test(
            self.assertEqual, tests, remove_year
        )

    def test_remove_brackets(self):
        """
        :return: bool
            True iff FileSystem.remove_bracket correctly removes brackets
            from paths
        """

        tests = {
            "(": "",  # void
            "((": "",
            "()": "",
            "([)([{}": "",
            "a(": "a",  # mixed with words
            "(a]": "",
            "}{a{b": "ab",
            "a(b[c{d}])": "a"  # with words in between
        }
        utils.battery_test(self.assertEqual, tests, remove_brackets)

    def test_extract_name_max_chars(self):
        """
        :return: bool
            True iff FileSystem.extract_name_max_chars correctly extracts
            name from paths
        """

        tests = {
            "012345678a": "012345678a",  # length
            "012345678b ": "012345678b",
            "012345678c  ": "012345678c",
            " 012345678d": "012345678d",
            "  012345678e": "012345678e",
            "012345678912345678f": "0123456789"  # remove
        }
        utils.battery_test(
            self.assertEqual,
            tests,
            partial(extract_name_max_chars, max_chars=10)
        )

    def test_prettify(self):
        """
        :return: bool
            True iff FileSystem.prettify correctly prettifies bad strings
        """

        bad_string = "".join(BAD_CHARS)
        tests = {
            bad_string: "",
            bad_string + bad_string: "",
            bad_string + "a good string" + bad_string: "a_good_string"
        }
        utils.battery_test(self.assertEqual, tests,
                           partial(prettify, blank="_"))
