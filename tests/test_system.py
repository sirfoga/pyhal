# !/usr/bin/python
# coding: utf_8


"""Tests files handling methods """

import os
import random
import shutil

from hal.files.models.system import fix_raw_path, remove_year, \
    remove_brackets, extract_name_max_chars, BAD_CHARS, prettify, ls_recurse, \
    is_file, get_parent_folder_name, list_content, FileSystem, \
    RUSSIAN_CHARS
from hal.tests.utils import random_name, BatteryTests


class TestPaths:
    """Tests hal.files.models.FileSystem path handlers """

    def test_fix_raw_path(self):
        """Asserts iff FileSystem.fix_raw_path correctly handles raw paths"""

        tests = {
            "//a/b/c": "/a/b/c",  # double separators
            os.getenv("HOME"): os.getenv("HOME") + "/",
            "/a/b/c.txt": "/a/b/c.txt"  # files
        }
        BatteryTests(tests).assert_all(fix_raw_path)

    def test_remove_year(self):
        """Asserts iff FileSystem.remove_year correctly removes years from
            paths
        """

        tests = {
            "Today is 1980": "Today is ",
            # year in start, middle, end position of sentence
            "Today 1980 is ": "Today  is ",
            "1980 Today is ": " Today is ",
            "19803": "3",  # composition of year
            "20012002": ""
        }
        BatteryTests(tests).assert_all(remove_year)

    def test_remove_brackets(self):
        """Asserts iff FileSystem.remove_bracket correctly removes brackets
            from paths"""

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
        BatteryTests(tests).assert_all(remove_brackets)

    def test_extract_name_max_chars(self):
        """Asserts iff FileSystem.extract_name_max_chars correctly extracts
            name from paths"""

        tests = {
            "012345678a": "012345678a",  # length
            "012345678b ": "012345678b",
            "012345678c  ": "012345678c",
            " 012345678d": "012345678d",
            "  012345678e": "012345678e",
            " 0 12345678e": "0",
            "012345678912345678f": "0123456789"  # remove
        }
        BatteryTests(tests).assert_all(extract_name_max_chars, max_chars=10)

    def test_prettify(self):
        """Asserts iff FileSystem.prettify correctly prettifies bad strings"""

        bad_string = "".join(BAD_CHARS)
        tests = {
            bad_string: "",
            bad_string + bad_string: "",
            "a " + BAD_CHARS[0] + " ": "a",
            bad_string + "a good string" + bad_string: "a_good_string"
        }

        BatteryTests(tests).assert_all(prettify, blank="_")

    def test_is_file(self):
        """Asserts files are files, and folders are not"""

        tests = {
            os.getenv("HOME"): False,
            __file__: True
        }

        BatteryTests(tests).assert_all(is_file)

    def test_is_archive_mac(self):
        """Asserts files are archive from a Mac"""

        tests = {
            "macosx": True,
            __file__: False
        }
        tests = {
            FileSystem(key).is_archive_mac(): val
            for key, val in tests.items()
        }

        BatteryTests(tests).assert_all()

    def test_is_russian(self):
        """Asserts files contain russian chars"""

        tests = {
            "".join([random.choice(RUSSIAN_CHARS)] * 15 + ["fjdhf"]): True,
            "".join([random.choice(RUSSIAN_CHARS)] * 2 + ["fjdhf"]): False,
            __file__: False
        }
        tests = {
            FileSystem(key).is_russian(): val
            for key, val in tests.items()
        }

        BatteryTests(tests).assert_all()

    def test_get_parent_folder(self):
        """Asserts parent folder guessing"""

        tests = {
            "/a/b/c": "b",
            "/a/b/c/": "b",
            "/a/b/c//": "b"
        }

        BatteryTests(tests).assert_all(get_parent_folder_name)


class TestLs:
    """Tests hal.files.models.FileSystem folders/files functions """

    def prepare_temp_files(self):
        """Creates temp file for testing"""

        # create folder structure, at the end it will be like
        # working_folder/
        #             file1
        #             file2
        #             hidden_file
        #             inner_folder/
        #                         file11
        #                         file12
        self.working_folder = random_name()
        self.inner_folder = os.path.join(
            self.working_folder,
            random_name()
        )
        self.file12 = os.path.join(
            self.inner_folder,
            random_name()
        )
        self.file11 = os.path.join(
            self.inner_folder,
            random_name()
        )
        self.hidden_file = os.path.join(
            self.working_folder,
            "." + random_name()  # hidden requires dot before
        )
        self.file2 = os.path.join(
            self.working_folder,
            random_name()
        )
        self.file1 = os.path.join(
            self.working_folder,
            random_name()
        )

        self._create_temp_files()

    def _create_temp_files(self):
        """Creates files/folders structure for tests"""

        os.makedirs(self.working_folder)  # create folders
        os.makedirs(self.inner_folder)
        for file in [self.file1, self.file2, self.hidden_file, self.file11,
                     self.file12]:
            open(file, "a").close()  # create files

    def purge_temp_files(self):
        """Removes all temp files"""

        shutil.rmtree(self.working_folder)  # remove main folder

    def test_ls_dir(self):
        """Asserts iff FileSystem.ls_dir correctly list only folders"""

        self.prepare_temp_files()
        tests = {
            self.working_folder: {self.file1, self.file2, self.inner_folder},
            self.inner_folder: {self.file11, self.file12}
        }

        BatteryTests(tests).assert_all(list_content, recurse=False)
        self.purge_temp_files()

    def test_ls_recurse(self):
        """Asserts iff FileSystem.ls_recurse correctly list recursively"""

        self.prepare_temp_files()
        tests = {
            self.working_folder: {self.file1, self.file2, self.inner_folder,
                                  self.file11, self.file12}
        }

        BatteryTests(tests).assert_all(list_content, recurse=True)
        self.purge_temp_files()

    def test_ls_hidden(self):
        """Asserts iff FileSystem.ls correctly list hidden files"""

        self.prepare_temp_files()
        tests = {
            self.working_folder: {self.file1, self.file2, self.inner_folder,
                                  self.file11, self.file12, self.hidden_file}
        }

        BatteryTests(tests).assert_all(ls_recurse, include_hidden=True)
        self.purge_temp_files()
