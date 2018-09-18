#!/usr/bin/env python
# coding: utf-8


""" Common tools involving maths """


def get_nice_percentage(num, den):
    """
    :param num: float
        Numerator of fraction
    :param den: float
        Denominator of fraction
    :return: str
        Ratio as percentage
    """

    if den == 0:
        den = float('inf')

    raw = num / den * 100.0
    return '{:.4}'.format(raw)
