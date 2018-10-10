#!/usr/bin/env python
# coding: utf-8

"""Tools to deal with lists"""

import numpy as np


def pearson(lst1, lst2):
    """Calculates pearson coefficient of arrays

    :param lst1: first list
    :param lst2: second list
    :returns: Pearson coefficient of arrays

    """
    return np.corrcoef(lst1, lst2)[0][1]


def normalize_array(lst):
    """Normalizes list

    :param lst: Array of floats
    :returns: Normalized (in [0, 1]) input array

    """
    np_arr = np.array(lst)
    x_normalized = np_arr / np_arr.max(axis=0)
    return list(x_normalized)


def is_in_all(value, lists):
    """Checks if item is in all lists

    :param value: Value to check
    :param lists: List of lists
    :returns: True iff value is in all inner lists

    """
    for l in lists:
        if value not in l:
            return False

    return True


def find_commons(lists):
    """Finds common values

    :param lists: List of lists
    :returns: List of values that are in common between inner lists

    """
    others = lists[1:]
    return [
        val
        for val in lists[0]
        if is_in_all(val, others)
    ]
