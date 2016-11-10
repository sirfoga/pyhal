# !/usr/bin/python
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
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

import sys
import functools


def main(function):
    """
    :param function: callback function
        function to wrap
    :return: callback function return type
        wraps callback function
    """

    @functools.wraps(function)
    def _main(*args, **kwargs):
        """
        :param args: *
            args for callback function
        :param kwargs: **
            kwargs for callback function
        :return: callback function return type
            handle exception of callback function
        """

        try:
            function(*args, **kwargs)
        except KeyboardInterrupt:
            print("\r[!] User stopped program...\n%s")
        except Exception:
            print("\r[!] Unhandled exception occured...\n%s" % sys.exc_info()[1])
    return _main
