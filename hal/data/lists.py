#!/usr/bin/env python
# coding: utf-8

""" Tools to deal with lists """

import numpy as np


def pearson(lst1, lst2):
    """ Pearson coefficient of arrays"""

    return np.corrcoef(lst1, lst2)[0][1]


def normalize_array(arr):
    """
    :param arr: [] of float
        Array of floats
    :return: [] of float
        Normalized (in [0, 1]) input array
    """

    np_arr = np.array(arr)
    x_normalized = np_arr / np_arr.max(axis=0)
    return list(x_normalized)


def is_in_all(value, lst):
    """
    :param value: anything
        Value to check
    :param lst: [] of []
        List of lists
    :return: bool
        True iff value is in all inner lists
    """

    for l in lst:
        if value not in l:
            return False

    return True


def find_commons(lst):
    """
    :param lst: [] of []
        List of lists
    :return: []
        List of values that are in common between inner lists
    """

    others = lst[1:]
    return [
        val
        for val in lst[0]
        if is_in_all(val, others)
    ]
