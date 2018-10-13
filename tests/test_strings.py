# -*- coding: utf-8 -*-


"""Tests string implementation"""

from hal.strings.models import String
from hal.tests.utils import BatteryTests


class TestString:
    """Tests linked list"""

    def test_remove_escapes(self):
        """Asserts removal of anything except letters and numbers"""

        tests = {
            "a": "a",
            "a\\a1": "a1",
            "a\\?A2": "aA2"
        }
        tests = {
            String(key).remove_escapes(): val
            for key, val in tests.items()
        }

        BatteryTests(tests).assert_all()

    def test_remove_non_ansi(self):
        """Asserts removal of non ANSI chars"""

        tests = {
            "a": "a",
            "a\x1b[30m": "a",
            "a\x1b[31m": "a"
        }
        tests = {
            String(key).remove_non_ansi(): val
            for key, val in tests.items()
        }

        BatteryTests(tests).assert_all()

    def test_is_well_formatted(self):
        """Asserts is well formatted"""

        tests = {
            "a": True,
            "a\n": False,
            "a\\t": False
        }
        tests = {
            String(key).is_well_formatted(): val
            for key, val in tests.items()
        }

        BatteryTests(tests).assert_all()

    def test_strip_bad_html(self):
        """Asserts bad HTML stripper"""

        tests = {
            "a": True,
            "a\n": "a",
            "a\\t": "a"
        }
        tests = {
            String(key).strip_bad_html(): val
            for key, val in tests.items()
        }

        BatteryTests(tests).assert_all()
