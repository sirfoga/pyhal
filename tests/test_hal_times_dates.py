# -*- coding: utf-8 -*-


"""Tests hal.times.dates implementation"""

import datetime

from hal.times.dates import Weekday


class TestWeekday:
    """Tests Weekday class"""

    @staticmethod
    def test_get_next():
        """Tests hal.times.dates.Weekday.get_next method"""

        day = Weekday.MONDAY
        next_day = Weekday.get_next(day)
        today = datetime.datetime.today()
        delta = next_day - today

        assert delta.days < 7

    @staticmethod
    def test_get_last():
        """Tests hal.times.dates.Weekday.get_last method"""

        day = Weekday.MONDAY
        last_day = Weekday.get_last(day)
        today = datetime.datetime.today()
        delta = today - last_day

        assert delta.days < 7


class TestDay:
    """Tests Day class"""

    @staticmethod
    def test_get_just_date():
        """Tests hal.times.dates.Day.get_just_date method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_is_in_this_week():
        """Tests hal.times.dates.Day.is_in_this_week method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_is_date_in_between():
        """Tests hal.times.dates.Day.is_date_in_between method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_get_next_weekday():
        """Tests hal.times.dates.Day.get_next_weekday method"""

        pass  # todo auto generated method stub

    @staticmethod
    def test_get_last_weekday():
        """Tests hal.times.dates.Day.get_last_weekday method"""

        pass  # todo auto generated method stub
