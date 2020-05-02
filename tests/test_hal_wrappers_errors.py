# -*- coding: utf-8 -*-


"""Tests hal.wrappers.errors implementation"""

from hal.tests.utils import BatteryTests
from hal.wrappers.errors import none_returns
from hal.wrappers.errors import true_false_returns


def test_true_false_returns():
    """Tests hal.wrappers.errors.true_false_returns method"""

    @true_false_returns
    def f(x):
        return 1.0 / x

    tests = {
        0: False,
        1: True,
        2: True,
        -1.2: True
    }
    BatteryTests(tests).assert_all(f)


def test_none_returns():
    """Tests hal.wrappers.errors.none_returns method"""

    @none_returns
    def f(x):
        return 1.0 / x

    tests = {
        0: None,
        1: 1,
        2: 1 / 2,
        -1.2: 1 / -1.2
    }
    BatteryTests(tests).assert_all(f)
