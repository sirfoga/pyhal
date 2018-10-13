# -*- coding: utf-8 -*-


"""Tests hal.times.utils implementation"""

import datetime

from hal.tests.utils import BatteryTests
from hal.times.utils import Timing


class TestTiming:
    """Tests Timing class"""

    @staticmethod
    def test_parse_hh_mm_ss():
        """Tests hal.times.utils.Timing.parse_hh_mm_ss method"""

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

    @staticmethod
    def test_get_seconds():
        """Tests hal.times.utils.Timing.get_seconds method"""

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

    @staticmethod
    def test_parse_hh_mm():
        """Tests hal.times.utils.Timing.parse_hh_mm method"""

        tests = {
            "12:12": datetime.time(hour=12, minute=12),
            "12": datetime.time(minute=12)
        }
        tests = {
            Timing(key).parse_hh_mm(): val
            for key, val in tests.items()
        }

        BatteryTests(tests).assert_all()
