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


def get_just_date(date):
    """
    :param date: datetime
        Date with possible hours
    :return: date
        Just day, month and year (setting hours to 00:00:00)
    """

    return datetime.datetime(
        date.year,
        date.month,
        date.day
    )


def get_next_weekday(weekday, including_today=False):
    """
    :param weekday: Weekday
        Weekday to get
    :param including_today: bool
        If today is sunday and requesting next sunday, I shall return today
    :return: datetime
        Date of next monday, tuesday ...
    """

    now = datetime.datetime.now()
    if now.weekday() == weekday.value and including_today:
        delta = datetime.timedelta(days=0)
    elif now.weekday() == weekday.value and not including_today:
        delta = datetime.timedelta(days=7)
    else:
        delta = datetime.timedelta(
            (7 + weekday.value - now.weekday()) % 7
        )  # time delta to next instance
    return get_just_date(now + delta)


def get_last_weekday(weekday, including_today=False):
    """
    :param weekday: Weekday
        Weekday to get
    :param including_today: bool
        If today is sunday and requesting next sunday, I shall return today
    :return: datetime
        Date of next monday, tuesday ...
    """

    now = datetime.datetime.now()
    if now.weekday() == weekday.value and including_today:
        delta = datetime.timedelta(days=0)
    elif now.weekday() == weekday.value and not including_today:
        delta = - datetime.timedelta(days=7)
    else:
        delta = datetime.timedelta(
            - now.weekday() + weekday.value
        )  # time D to last sunday
    return get_just_date(now + delta)


def is_date_in_between(date, start, end):
    """
    :param date: datetime
        Date to check
    :param start: datetime
        Date cannot be before this date
    :param end: datetime
        Date cannot be after this date
    :return: bool
        True iff date is in between dates
    """

    return get_just_date(start) <= get_just_date(date) < get_just_date(end)


def is_in_this_week(date):
    """
    :param date: datetime
        Date
    :return: bool
        True iff date is in this week (from sunday to sunday)
    """

    return is_date_in_between(
        get_just_date(date),
        get_last_weekday(Weekday.SUNDAY, including_today=True),
        get_next_weekday(Weekday.SUNDAY)
    )