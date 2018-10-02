# !/usr/bin/python3
# coding: utf-8


""" Typical operations on dicts made easy """

import numpy as np

from hal.strings.utils import how_similar_are


def how_similar_dicts(d1, d2):
    """
    :param d1: {}
        Dictionary
    :param d2: {}
        Dictionary
    :return: float in [0 - 1]
        A measure of how much similar values of dictionaries are
    """

    values = []
    for k in d1:  # iterate keys
        if k in d2 and d1[k] and d2[k]:  # make sure values are comparable
            values.append(
                how_similar_are(str(d1[k]), str(d2[k]))
            )
    return np.mean(values)  # average
