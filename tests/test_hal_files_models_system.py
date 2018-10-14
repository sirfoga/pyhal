# -*- coding: utf-8 -*-


"""Tests hal.files.models.system implementation"""

import random
import shutil

from hal.files.models.system import FileSystem
from hal.files.models.system import extract_name_max_chars
from hal.files.models.system import fix_raw_path, BAD_CHARS, RUSSIAN_CHARS
from hal.files.models.system import get_parent_folder_name
from hal.files.models.system import is_file
from hal.files.models.system import list_content
from hal.files.models.system import ls_recurse
from hal.files.models.system import prettify
from hal.files.models.system import remove_brackets
from hal.files.models.system import remove_year
from hal.tests.utils import BatteryTests, random_name


def test_fix_raw_path():
    """Tests hal.files.models.os.fix_raw_path method"""

    tests = {
        "//a/b/c": "/a/b/c",  # double separators
        os.getenv("HOME"): os.getenv("HOME") + "/",
        "/a/b/c.txt": "/a/b/c.txt"  # files
    }

    BatteryTests(tests).assert_all(fix_raw_path)


def test_remove_year():
    """Tests hal.files.models.os.remove_year method"""

    tests = {
        "Today is 1980": "Today is ",
        # year in start, middle, end position of sentence
        "Today 1980 is ": "Today  is ",
        "1980 Today is ": " Today is ",
        "19803": "3",  # composition of year
        "20012002": ""
    }

    BatteryTests(tests).assert_all(remove_year)


def test_remove_brackets():
    """Tests hal.files.models.os.remove_brackets method"""

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


def test_extract_name_max_chars():
    """Tests hal.files.models.os.extract_name_max_chars method"""

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


def test_prettify():
    """Tests hal.files.models.os.prettify method"""

    bad_string = "".join(BAD_CHARS)
    tests = {
        bad_string: "",
        bad_string + bad_string: "",
        "a " + BAD_CHARS[0] + " ": "a",
        bad_string + "a good string" + bad_string: "a_good_string"
    }

    BatteryTests(tests).assert_all(prettify, blank="_")


def test_is_file():
    """Tests hal.files.models.os.is_file method"""

    tests = {
        os.getenv("HOME"): False,
        __file__: True
    }

    BatteryTests(tests).assert_all(is_file)


def test_is_folder():
    """Tests hal.files.models.os.is_folder method"""

    pass  # todo auto generated method stub


def test_get_parent_folder_name():
    """Tests hal.files.models.os.get_parent_folder_name method"""

    tests = {
        "/a/b/c": "b",
        "/a/b/c/": "b",
        "/a/b/c//": "b"
    }

    BatteryTests(tests).assert_all(get_parent_folder_name)


def test_get_folder_name():
    """Tests hal.files.models.os.get_folder_name method"""

    pass  # todo auto generated method stub


class TestLs:
    """Tests hal.files.models.os.ls* methods"""

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
        """Tests hal.files.models.os.ls_dir method"""

        self.prepare_temp_files()
        tests = {
            self.working_folder: {self.file1, self.file2, self.inner_folder},
            self.inner_folder: {self.file11, self.file12}
        }

        for key, val in tests.items():
            assert set(list_content(key, False)) == val

        self.purge_temp_files()

    def test_ls_recurse(self):
        """Tests hal.files.models.os.ls_recurse method"""

        self.prepare_temp_files()
        tests = {
            self.working_folder: {self.file1, self.file2, self.inner_folder,
                                  self.file11, self.file12}
        }

        for key, val in tests.items():
            assert set(list_content(key, True)) == val

        self.purge_temp_files()

    def test_list_hidden_content(self):
        """Tests hal.files.models.os.list_content method (hidden=True)"""

        self.prepare_temp_files()
        tests = {
            self.working_folder: {self.file1, self.file2, self.inner_folder,
                                  self.file11, self.file12, self.hidden_file}
        }

        for key, val in tests.items():
            assert set(ls_recurse(key, include_hidden=True)) == val

        self.purge_temp_files()

    def test_list_content(self):
        """Tests hal.files.models.os.list_content method"""

        pass  # todo auto generated method stub


class TestFileSystem:
    """Tests FileSystem class"""

    @staticmethod
    def test_is_hidden():
        """Tests hal.files.models.os.Fileos.is_hidden method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_is_archive_mac():
        """Tests hal.files.models.os.Fileos.is_archive_mac method"""

        tests = {
            "macosx": True,
            __file__: False
        }
        tests = {
            FileSystem(key).is_archive_mac(): val
            for key, val in tests.items()
        }

        BatteryTests(tests).assert_all()

    @staticmethod
    def test_is_russian():
        """Tests hal.files.models.os.Fileos.is_russian method"""

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

    @staticmethod
    def test_trash():
        """Tests hal.files.models.os.Fileos.trash method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_rename():
        """Tests hal.files.models.os.Fileos.rename method"""

        pass  # todo auto generated method stub
