#!/usr/bin/env python
# coding: utf-8


""" Models to version stuff """


class Level:
    """ Level of version number """

    def __init__(self, name, max_inner, start=0):
        """
        :param name: str
            Name of level (debug reasons only)
        :param max_inner: int
            Max number of this level. If you set to 0 this level will
            increase never
        :param start: int
            Start at this number
        """

        self.name = name
        self.max_inner = max_inner
        self.current = start

    def can_increase(self, amount):
        """
        :param amount: int
            Increase number by this amount
        :return: bool
            True iff can actually increase by this amount
        """

        return self.current + amount <= self.max_inner

    def increase(self, amount=1):
        """
        :param amount: int
            Increase number by this amount
        :return: bool
            True iff increase was successful
        """

        if self.can_increase(amount):
            self.current += amount
            return True

        return False

    def to_max(self):
        """
        :return: void
            Maximize this number
        """

        self.current = self.max_inner

    def zero(self):
        """
        :return: void
            Zeroes this number
        """

        self.current = 0


class Subsystem:
    """ List of levels of version system """

    def __init__(self, levels):
        """
        :param levels: [] of Level
            Levels in order of importance (from left to right)
        """

        


class VersionNumber:
    """ Version """
