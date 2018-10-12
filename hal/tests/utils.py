# !/usr/bin/python
# coding: utf_8


"""Tools to ease testing process """

import uuid


class BatteryTests:
    """Performs assertions on tests"""

    def __init__(self, dictionary):
        """
        :param dictionary: tests
        """
        self.tests = dictionary

    def assert_all(self, func=None, *args, **kwargs):
        """Asserts tests

        :param func: function to assert
        :param args: params in function
        :param kwargs: extra params
        :return: True iff all tests pass
        """

        if args is None:
            args = {}

        tests = self.tests.items()
        if func is not None:
            tests = [
                (func(key, *args, **kwargs), val)
                for key, val in tests
            ]

        for test, good_result in tests:
            assert test == good_result


def random_name():
    """Computes random name

    :return: Pseudo-random name
    """
    return str(uuid.uuid4())
