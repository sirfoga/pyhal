# !/usr/bin/python3
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" Typical (and useful) function wrappers """

import functools
import sys

import colorama


def handle_exceptions(function):
    """
    :param function: callback function
        function to wrap
    :return: callback function return type
        wraps callback function
    """

    @functools.wraps(function)
    def _handle_exceptions(*args, **kwargs):
        """
        :param args: *
            args for callback function
        :param kwargs: **
            kwargs for callback function
        :return: callback function return type
            handle exception of callback function
        """

        function_name = function.__name__
        exception_string = \
            "name: " + function_name + "\n" + \
            "*args: " + str(args) + "\n" + \
            "**kwargs: " + str(kwargs)

        colorama.init()  # start color mode

        try:
            return function(*args, **kwargs)
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
