# !/usr/bin/python
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


import unittest
from functools import partial

from hal.files import models


class TestFileSystem(unittest.TestCase):
    """ test hal.files.models module """

    @staticmethod
    def battery_test(assert_type, tests, f):
        """
        :param assert_type: function
            Type of assert
        :param tests: dict
            key= params in function, value= what should be the result
        :param f: function
            Function to apply
        :return: bool
            True iff all tests pass
        """

        for test, good_result in tests.items():
            assert_type(f(test), good_result)

    def test_fix_raw_path(self):
        tests = {
            "//a/b/c": "/a/b/c",  # double separators
            "/a/b/c.txt": "/a/b/c.txt"  # files
        }

        self.battery_test(self.assertEqual, tests,
                          models.FileSystem.fix_raw_path)

    def test_remove_year(self):
        tests = {
            "Today is 1980": "Today is ",
            # year in start, middle, end position of sentence
            "Today 1980 is ": "Today  is ",
            "1980 Today is ": " Today is ",
            "19803": "3",  # composition of year
            "20012002": ""
        }

        self.battery_test(self.assertEqual, tests,
                          models.FileSystem.remove_year)

    def test_remove_brackets(self):
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

        self.battery_test(self.assertEqual, tests,
                          models.FileSystem.remove_brackets)

    def test_extract_name_max_chars(self):
        tests = {
            "012345678a": "012345678a",  # length
            "012345678b ": "012345678b",
            "012345678c  ": "012345678c",
            " 012345678d": "012345678d",
            "  012345678e": "012345678e",
            "012345678912345678f": "0123456789"  # remove
        }

        self.battery_test(self.assertEqual, tests,
                          partial(models.FileSystem.extract_name_max_chars,
                                  max_chars=10))

    def test_prettify(self):
        bad_string = "".join(models.BAD_CHARS)

        tests = {
            bad_string: "",
            bad_string + bad_string: "",
            bad_string + "a good string" + bad_string: "a_good_string"
        }
        self.battery_test(self.assertEqual, tests,
                          partial(models.FileSystem.prettify, r="_"))

    def test_ls_dir(self):
        return True  # TODO: maybe create some folder first

    def test_ls_recurse(self):
        return True  # TODO: maybe create some folder first

    def test_ls(self):
        return True  # TODO: maybe create some folder first


if __name__ == '__main__':
    unittest.main()
