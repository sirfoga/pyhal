# -*- coding: utf-8 -*-

"""Typical operations on dicts made easy"""

import numpy as np

from hal.strings.utils import how_similar_are


def how_similar_dicts(d1, d2):
    """Calculates similarity

    :param d1: Dictionary
    :param d2: Dictionary
    :returns: measure of how much similar values of dictionaries are

    """
    values = []
    for k in d1:  # iterate keys
        if k in d2 and d1[k] and d2[k]:  # make sure values are comparable
            values.append(
                how_similar_are(str(d1[k]), str(d2[k]))
            )
    return np.mean(values)  # average


def get_inner_keys(d):
    """Gets 2nd-level dictionary keys

    :param d: dict
    :returns: inner keys

    """

    keys = []

    for key in d.keys():
        inner_keys = d[key].keys()
        keys += [
            key + " " + inner_key  # concatenate
            for inner_key in inner_keys
        ]

    return keys


def get_inner_data(d):
    """Gets 2nd-level data into 1st-level dictionary

    :param d: dict
    :returns: with 2nd-level data

    """

    out = {}

    for key in d.keys():
        inner_keys = d[key].keys()
        for inner_key in inner_keys:
            new_key = key + " " + inner_key  # concatenate
            out[new_key] = d[key][inner_key]

    return out
