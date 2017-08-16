# !/usr/bin/python
# coding: utf_8

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


""" Tools to ease testing process """

import uuid


def battery_test(assert_type, tests, function, args=None):
    """
    :param assert_type: function
        Type of assert
    :param tests: dict
        key= params in function, value= what should be the result
    :param function: function
        Function to apply
    :param args: *
        Extra args for function to call
    :return: bool
        True iff all tests pass
    """

    if args is None:
        args = {}

    for test, good_result in tests.items():
        assert_type(function(test, *args), good_result)


def random_name():
    """
    :return: str
        Pseudo-random name
    """

    return str(uuid.uuid4())
