# !/usr/bin/python3
# coding: utf-8


""" Useful function wrappers """

import functools
import sys

import colorama


def handle_exceptions(func):
    """
    :param func: callback function
        function to wrap
    :return: callback function return type
        wraps callback function
    """

    @functools.wraps(func)
    def _handle_exceptions(*args, **kwargs):
        """
        :param args: *
            args for callback function
        :param kwargs: **
            kwargs for callback function
        :return: callback function return type
            handle exception of callback function
        """

        function_name = func.__name__
        exception_string = \
            "name: " + function_name + "\n" + \
            "*args: " + str(args) + "\n" + \
            "**kwargs: " + str(kwargs)

        colorama.init()  # start color mode

        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print(
                colorama.Fore.RED + colorama.Style.BRIGHT + "\r[!] User "
                                                            "stopped program"
                                                            " in function" +
                colorama.Style.RESET_ALL)
            print(exception_string)
        except:
            print(
                colorama.Fore.RED + colorama.Style.BRIGHT + "\r[!] Unhandled "
                                                            "exception "
                                                            "occurred...\n%s" %
                sys.exc_info()[1] + colorama.Style.RESET_ALL)
            print(exception_string)

    return _handle_exceptions
