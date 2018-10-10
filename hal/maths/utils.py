# -*- coding: utf-8 -*-
""" Tools realtive to maths """


def get_percentage_relative_to(val, other):
    """
    :param val:
    :param other:
    """
    val = float(val)
    other = float(other)
    ratio = val / other - 1

    return ratio * 100.0


def divide(numerator, denominator):
    """
    Handles errors of division
    :param numerator: Numerator
    :param denominator: Denominator
    :returns: division value
    """

    try:
        return float(numerator) / float(denominator)
    except:
        return float("nan")
