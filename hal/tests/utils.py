# !/usr/bin/python
# coding: utf_8


""" Tools to ease testing process """

import uuid


def battery_test(assert_type, tests, func, args=None):
    """
    :param assert_type: function
        Type of assert
    :param tests: dict
        key= params in function, value= what should be the result
    :param func: function
        Function to apply
    :param args: *
        Extra args for function to call
    :return: bool
        True iff all tests pass
    """

    if args is None:
        args = {}

    for test, good_result in tests.items():
        assert_type(func(test, *args), good_result)


def random_name():
    """
    :return: str
        Pseudo-random name
    """

    return str(uuid.uuid4())
