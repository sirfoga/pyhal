# !/usr/bin/python
# coding: utf_8


""" Tests files handling methods """

import os
import shutil
from functools import partial
from unittest import TestCase, main

from hal.files.models.system import fix_raw_path, ls_dir, remove_year, \
    remove_brackets, ls_recurse, extract_name_max_chars, BAD_CHARS, prettify
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


class TestLs(TestCase):
    """ Tests hal.files.models.FileSystem folders/files functions """

    def prepare_temp_files(self):
        """
        :return: void
            Creates temp file for testing
        """

        super().__init__()

        # create folder structure, at the end it will be like
        # working_folder/
        #             file1
        #             file2
        #             hidden_file
        #             inner_folder/
        #                         file11
        #                         file12
        self.working_folder = utils.random_name()
        self.file1 = os.path.join(
            self.working_folder,
            utils.random_name()
        )
        self.file2 = os.path.join(
            self.working_folder,
            utils.random_name()
        )
        self.hidden_file = os.path.join(
            self.working_folder,
            "." + utils.random_name()  # hidden requires dot before
        )
        self.inner_folder = os.path.join(
            self.working_folder,
            utils.random_name()
        )
        self.file11 = os.path.join(
            self.inner_folder,
            utils.random_name()
        )
        self.file12 = os.path.join(
            self.inner_folder,
            utils.random_name()
        )
        self._create_temp_files()

    def _create_temp_files(self):
        """
        :return: void
            Creates files/folders structure for tests
        """

        os.makedirs(self.working_folder)  # create folders
        os.makedirs(self.inner_folder)
        for file in [self.file1, self.file2, self.hidden_file, self.file11,
                     self.file12]:
            open(file, "a").close()  # create files

    def purge_temp_files(self):
        """
        :return: void
            Removes all temp files
        """

        shutil.rmtree(self.working_folder)  # remove main folder

    def test_ls_dir(self):
        """
        :return: bool
            True iff FileSystem.ls_dir correctly list only folders
        """

        self.prepare_temp_files()
        tests = {
            self.working_folder: [self.file1, self.file2, self.inner_folder],
            self.inner_folder: [self.file11, self.file12]
        }

        try:
            utils.battery_test(
                self.assertCountEqual, tests, ls_dir
            )
        except Exception as exception:
            raise exception
        finally:
            self.purge_temp_files()

    def test_ls_recurse(self):
        """
        :return: bool
            True iff FileSystem.ls_recurse correctly list recursively
        """

        self.prepare_temp_files()
        tests = {
            self.working_folder: [self.file1, self.file2, self.inner_folder,
                                  self.file11, self.file12]
        }

        try:
            utils.battery_test(
                self.assertCountEqual, tests, ls_recurse
            )
        except Exception as exception:
            raise exception
        finally:
            self.purge_temp_files()

    def test_ls_hidden(self):
        """
        :return: bool
            True iff FileSystem.ls correctly list hidden files
        """

        self.prepare_temp_files()
        tests = {
            self.working_folder: [self.file1, self.file2, self.inner_folder,
                                  self.file11, self.file12, self.hidden_file]
        }

        try:
            utils.battery_test(
                self.assertCountEqual, tests, ls_recurse,
                {"include_hidden": True}
            )
        except Exception as exception:
            raise exception
        finally:
            self.purge_temp_files()


if __name__ == '__main__':
    main()
