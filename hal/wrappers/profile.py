# -*- coding: utf-8 -*-

"""Wrappers to profile functions"""

import functools

from hal.profile.models import Timer
from hal.streams.logger import log_message


def log_time(func):
    """Executes function and logs time

    :param func: function to call
    :return: function result
    """

    @functools.wraps(func)
    def _execute(*args, **kwargs):
        """Executes function and logs time

        :param args: args of function
        :param kwargs: extra args of function
        :param *args: args
        :param **kwargs: extra args
        :return: function result
        """

        func_name = func.func_name
        timer = Timer()
        log_message(func_name, "has started")

        result = func(*args, **kwargs)

        seconds = "{:.3f}".format(timer.elapsed_time())
        log_message(func_name, "has finished. Execution time:", seconds, "s")

        return result

    return _execute
