# -*- coding: utf-8 -*-


"""Tests hal.strings.models implementation"""

from hal.strings.models import String
from hal.tests.utils import BatteryTests


class TestString:
    """Tests String class"""

    @staticmethod
    def test_remove_escapes():
        """Tests hal.strings.models.String.remove_escapes method"""

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

    @staticmethod
    def test_remove_non_ansi():
        """Tests hal.strings.models.String.remove_non_ansi method"""

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

    @staticmethod
    def test_is_well_formatted():
        """Tests hal.strings.models.String.is_well_formatted method"""

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

    @staticmethod
    def test_strip_bad_html():
        """Tests hal.strings.models.String.strip_bad_html method"""

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

    @staticmethod
    def test_remove_all():
        """Tests hal.strings.models.String.remove_all method"""

        pass  # todo auto generated method stub
