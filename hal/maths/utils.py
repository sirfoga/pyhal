# !/usr/bin/python3
# coding: utf-8

""" Tools realtive to maths """


def get_percentage_relative_to(val, other):
    """
    # Arguments
      val: 
      other: 

    # Returns:
    """
    val = float(val)
    other = float(other)
    ratio = val / other - 1

    return ratio * 100.0
