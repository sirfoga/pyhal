# -*- coding: utf-8 -*-

"""Wrappers to function that handle errors"""

import functools


def true_false_returns(func):
    """Executes function, if error returns False, else True

    :param func: function to call
    :returns: True iff ok, else False

    """

    @functools.wraps(func)
    def _execute(*args, **kwargs):
        """Executes function, if error returns False, else True

        :param args: args of function
        :param kwargs: extra args of function
        :param *args: 
        :param **kwargs: 
        :returns: True iff ok, else False
        """

        try:
            func(*args, **kwargs)
            return True
        except:
            return False

    return _execute


def none_returns(func):
    """Executes function, if error returns None else value of function

    :param func: function to call
    :returns: None else value of function

    """

    @functools.wraps(func)
    def _execute(*args, **kwargs):
        """Executes function, if error returns None else value of function

        :param args: args of function
        :param kwargs: extra args of function
        :param *args: 
        :param **kwargs: 
        :returns: None else value of function
        """

        try:
            return func(*args, **kwargs)
        except:
            return None

    return _execute
