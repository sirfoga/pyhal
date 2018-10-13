# !/usr/bin/python
# coding: utf_8


"""Tests string implementation"""

from hal.tests.utils import BatteryTests
from hal.wrappers import errors


class TestErrorWrappers:
    """Tests wrappers"""

    def test_true_false_returns(self):
        """Asserts True/False wrapper"""

        @errors.true_false_returns
        def f(x):
            return 1.0 / x

        tests = {
            0: False,
            1: True,
            2: True,
            -1.2: True
        }
        BatteryTests(tests).assert_all(f)

    def test_none_returns(self):
        """Asserts None wrapper"""

        @errors.none_returns
        def f(x):
            return 1.0 / x

        tests = {
            0: None,
            1: 1,
            2: 1 / 2,
            -1.2: 1 / -1.2
        }
        BatteryTests(tests).assert_all(f)
