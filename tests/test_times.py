# !/usr/bin/python
# coding: utf_8


"""Tests times implementation"""

import datetime
from time import time

from hal.tests.utils import BatteryTests
from hal.times.profile import get_time_eta
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


class TestProfile:
    """Tests profiling module"""

    def test_get_time_eta(self):
        """Asserts time ETA calculations"""

        time_slack = 10
        start_time = time() - time_slack
        to_do = 10

        tests = {
            (10, to_do, start_time): {
                "tot": to_do,
                "%": 100.0,
                "h": 0,
                "m": 0,
                "s": 0
            },
            (0, to_do, start_time): {
                "tot": to_do,
                "%": 0.0,
                "h": 0,
                "m": 0,
                "s": 0
            }
        }

        for key, val in tests.items():
            attempt = get_time_eta(key[0], key[1], key[2])
            val["done"] = key[0]

            assert attempt == val
