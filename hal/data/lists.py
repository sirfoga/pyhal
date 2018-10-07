#!/usr/bin/env python
# coding: utf-8

""" Tools to deal with lists """

import numpy as np


def pearson(lst1, lst2):
    """Pearson coefficient of arrays

    Args:
      lst1: 
      lst2: 

    Returns:

    """

    return np.corrcoef(lst1, lst2)[0][1]


def normalize_array(arr):
    """

    Args:
      arr: of float
    Array of floats

    Returns:
      of float
      Normalized (in [0, 1]) input array

    """

    np_arr = np.array(arr)
    x_normalized = np_arr / np_arr.max(axis=0)
    return list(x_normalized)


def is_in_all(value, lst):
    """

    Args:
      value: anything
    Value to check
      lst: of []
    List of lists

    Returns:
      bool
      True iff value is in all inner lists

    """

    for l in lst:
        if value not in l:
            return False

    return True


def find_commons(lst):
    """

    Args:
      lst: of []
    List of lists

    Returns:
      List of values that are in common between inner lists

    """

    others = lst[1:]
    return [
        val
        for val in lst[0]
        if is_in_all(val, others)
    ]
