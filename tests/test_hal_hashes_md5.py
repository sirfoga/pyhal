# -*- coding: utf-8 -*-


"""Tests hal.hashes.md5 implementation"""
import os

from hal.hashes.md5 import file_to_md5
from hal.hashes.md5 import string_to_md5
from hal.tests.utils import BatteryTests


def test_string_to_md5():
    """Tests hal.hashes.md5.string_to_md5 method"""

    tests = {
        "hello world": "5eb63bbbe01eeed093cb22bb8f5acdc3"
    }
    BatteryTests(tests).assert_all(string_to_md5)


def test_file_to_md5():
    """Tests hal.hashes.md5.file_to_md5 method"""

    path = os.path.join(os.path.dirname(__file__), "__init__.py")
    tests = {
        path: "d41d8cd98f00b204e9800998ecf8427e"
    }
    BatteryTests(tests).assert_all(file_to_md5)
