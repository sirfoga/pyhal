# -*- coding: utf-8 -*-

"""Datetime utils """

import datetime
from enum import Enum


class Weekday(Enum):
    """Representing weekday by using ints (datetime standard)"""

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def get_just_date(date):
    """Parses just date from date-time

    :param date: Date with possible hours
    :returns: Just day, month and year (setting hours to 00:00:00)

    """
    return datetime.datetime(
        date.year,
        date.month,
        date.day
    )


def get_next_weekday(weekday, including_today=False):
    """Gets next week day

    :param weekday: Weekday to get
    :param including_today: If today is sunday and requesting next sunday (Default value = False)
    :returns: Date of next monday, tuesday ...

    """
    now = datetime.datetime.now()
    if now.weekday() == weekday.value and including_today:
        delta = datetime.timedelta(days=0)
    elif now.weekday() == weekday.value and not including_today:
        delta = datetime.timedelta(days=7)
    else:
        delta = datetime.timedelta(
            (7 + weekday.value - now.weekday()) % 7
        )  # times delta to next instance
    return get_just_date(now + delta)


def get_last_weekday(weekday, including_today=False):
    """Gets last week day

    :param weekday: weekday to get
    :param including_today: If today is sunday and requesting next sunday (Default value = False)
    :returns: Date of last monday, tuesday ...

    """
    now = datetime.datetime.now()
    if now.weekday() == weekday.value and including_today:
        delta = datetime.timedelta(days=0)
    elif now.weekday() == weekday.value and not including_today:
        delta = - datetime.timedelta(days=7)
    else:
        if now.weekday() > weekday.value:
            delta = - datetime.timedelta(
                now.weekday() - weekday.value
            )  # times delta
        else:
            delta = - datetime.timedelta(
                now.weekday() + (7 - weekday.value)
            )  # times delta
    return get_just_date(now + delta)


def is_date_in_between(date, start, end):
    """Checks if date is in between dates

    :param date: Date to check
    :param start: Date cannot be before this date
    :param end: Date cannot be after this date
    :returns: True iff date is in between dates

    """
    return get_just_date(start) <= get_just_date(date) < get_just_date(end)


def is_in_this_week(date):
    """Checks if date is in this week (from sunday to sunday)

    :param date: Date
    :returns: True iff date is in this week (from sunday to sunday)

    """
    return is_date_in_between(
        get_just_date(date),
        get_last_weekday(Weekday.SUNDAY, including_today=True),
        get_next_weekday(Weekday.SUNDAY)
    )
