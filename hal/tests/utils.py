# !/usr/bin/python
# coding: utf_8


"""Tools to ease testing process """

import uuid


def battery_test(assert_type, tests, func, args=None):
    """Performs battery tests on objects

    :param assert_type: assert type
    :param tests: key, value what should be the result
    :param func: function to assert
    :param args: params in function (Default value = None)
    :returns: True iff all tests pass

    """
    if args is None:
        args = {}

    for test, good_result in tests.items():
        assert_type(func(test, *args), good_result)


def random_name():
    """Computes random name

    :returns: Pseudo-random name
    """
    return str(uuid.uuid4())
