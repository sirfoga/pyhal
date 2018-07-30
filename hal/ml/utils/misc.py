#!/usr/bin/env python
# coding: utf-8

""" Various tools and utilities to deal with database and machine learning. """

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
