# -*- coding: utf-8 -*-

"""Typical operations on dicts made easy"""

import numpy as np

from hal.strings.utils import how_similar_are


def how_similar_dicts(dict1, dict2):
    """Calculates similarity

    :param dict1: Dictionary
    :param dict2: Dictionary
    :returns: measure of how much similar values of dictionaries are
    """
    values = []
    for k in dict1:  # iterate keys
        if k in dict2 and dict1[k] and dict2[k]:
            values.append(
                how_similar_are(str(dict1[k]), str(dict2[k]))
            )
    return np.mean(values)  # average


def get_inner_keys(dictionary):
    """Gets 2nd-level dictionary keys

    :param dictionary: dict
    :returns: inner keys
    """

    keys = []

    for key in dictionary.keys():
        inner_keys = dictionary[key].keys()
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
