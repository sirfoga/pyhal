#!/usr/bin/env python
# coding: utf-8

""" Tools to deal with lists """

import numpy as np


def pearson(lst1, lst2):
    """
    Calculates pearson coefficient of arrays

    # Arguments
      lst1: first list
      lst2: second list

    # Returns
        value: Pearson coefficient of arrays
    """
    return np.corrcoef(lst1, lst2)[0][1]


def normalize_array(lst):
    """
    Normalizes list

    # Arguments
      lst:  Array of floats

    # Returns
        list: Normalized (in [0, 1]) input array
    """
    np_arr = np.array(lst)
    x_normalized = np_arr / np_arr.max(axis=0)
    return list(x_normalized)


def is_in_all(value, lists):
    """
    Checks if item is in all lists

    # Arguments
      value: Value to check
      lists: List of lists

    # Returns
        bool: True iff value is in all inner lists
    """
    for l in lists:
        if value not in l:
            return False

    return True


def find_commons(lists):
    """
    Finds common values

    # Arguments
      lists:  List of lists

    # Returns
        list: List of values that are in common between inner lists
    """
    others = lists[1:]
    return [
        val
        for val in lists[0]
        if is_in_all(val, others)
    ]
