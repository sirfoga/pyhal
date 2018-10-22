# -*- coding: utf-8 -*-


"""Tests hal.times.profile implementation"""

from time import time

from hal.times.profile import get_time_eta


def test_get_time_eta():
    """Tests hal.times.profile.get_time_eta method"""

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
