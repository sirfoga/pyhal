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

    @staticmethod
    def get_next(weekday, including_today=False):
        """Gets next day of week

        :param weekday: day of week
        :param including_today: If today is sunday and requesting next sunday
        :return: Date of next monday, tuesday ..
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
        return Day(now + delta).get_just_date()

    @staticmethod
    def get_last(weekday, including_today=False):
        """Gets last day of week

        :param weekday: day of week
        :param including_today: If today is sunday and requesting last sunday
        :return: Date of last monday, tuesday ..
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
        return Day(now + delta).get_just_date()


class Day:
    def __init__(self, date_time, week_end=Weekday.SUNDAY):
        """
        :param date_time: Date
        :param week_end: Day when weekend ends
        """

        self.date_time = date_time
        self.week_end = week_end

    def get_just_date(self):
        """Parses just date from date-time

        :return: Just day, month and year (setting hours to 00:00:00)
        """
        return datetime.datetime(
            self.date_time.year,
            self.date_time.month,
            self.date_time.day
        )

    def is_in_this_week(self):
        """Checks if date is in this week (from sunday to sunday)

        :return: True iff date is in this week (from sunday to sunday)
        """
        return self.is_date_in_between(
            Weekday.get_last(self.week_end, including_today=True),
            Weekday.get_next(self.week_end)
        )

    def is_date_in_between(self, start, end):
        """Checks if date is in between dates

        :param start: Date cannot be before this date
        :param end: Date cannot be after this date
        :return: True iff date is in between dates
        """

        start = Day(start).get_just_date()
        now = self.get_just_date()
        end = Day(end).get_just_date()

        return start <= now <= end

    def get_next_weekday(self, including_today=False):
        """Gets next week day

        :param including_today: If today is sunday and requesting next sunday
        :return: Date of next monday, tuesday ..
        """
        weekday = self.date_time.weekday()
        return Weekday.get_next(weekday, including_today=including_today)

    def get_last_weekday(self, including_today=False):
        """Gets last week day

        :param including_today: If today is sunday and requesting next sunday
        :return: Date of last monday, tuesday ..
        """
        weekday = self.date_time.weekday()
        return Weekday.get_last(weekday, including_today=including_today)
