# !/usr/bin/python3
# coding: utf-8

# Copyright 2016-2018 Stefano Fogarollo
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


""" Datetime utils """

import datetime
from enum import Enum


class Weekday(Enum):
    """ Representing weekday by using ints (datetime standard) """

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def get_next_weekday(weekday):
    """
    :param weekday: Weekday
        Weekday to get
    :return: datetime
        Date of next monday, tuesday ...
    """

    now = datetime.datetime.now()
    if now.weekday() == weekday:
        return now + datetime.timedelta(days=7)

    t = datetime.timedelta(
        (7 + weekday.value - now.weekday()) % 7
    )  # time delta to next instance
    return now + t
