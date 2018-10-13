# !/usr/bin/python
# coding: utf_8


"""Tests string implementation"""
import datetime

from hal.tests.utils import BatteryTests
from hal.times.utils import Timing


class TestUtils:
    """Tests timing utils"""

    def test_timing_parse_hh_mm_ss(self):
        """Asserts parsing string"""

        tests = {
            "12:12:12": datetime.time(hour=12, minute=12, second=12),
            "12:12": datetime.time(minute=12, second=12),
            "12": datetime.time(second=12)
        }
        tests = {
            Timing(key).parse_hh_mm_ss(): val
            for key, val in tests.items()
        }
        BatteryTests(tests).assert_all()

    def test_timing_parse_hh_mm(self):
        """Asserts parsing string"""

        tests = {
            "12:12": datetime.time(hour=12, minute=12),
            "12": datetime.time(minute=12)
        }
        tests = {
            Timing(key).parse_hh_mm(): val
            for key, val in tests.items()
        }
        BatteryTests(tests).assert_all()

    def test_timing_get_seconds(self):
        """Asserts getting seconds"""

        tests = {
            "20:12:12": 20 * 60 * 60 + 12 * 60 + 12,
            "12:12": 12 * 60 + 12,
            "12": 12
        }
        tests = {
            Timing(key).get_seconds(): val
            for key, val in tests.items()
        }
        BatteryTests(tests).assert_all()
