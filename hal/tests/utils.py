# !/usr/bin/python
# coding: utf_8


""" Tools to ease testing process """

import uuid


def battery_test(assert_type, tests, func, args=None):
    """

    Args:
      assert_type: function
    Type of assert
      tests: dict
    key= params in function, value= what should be the result
      func: function
    Function to apply
      args: Extra args for function to call (Default value = None)

    Returns:
      bool
      True iff all tests pass

    """

    if args is None:
        args = {}

    for test, good_result in tests.items():
        assert_type(func(test, *args), good_result)


def random_name():
    """:return: str
        Pseudo-random name

    Args:

    Returns:

    """

    return str(uuid.uuid4())
