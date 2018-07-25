# !/usr/bin/python3
# coding: utf-8


""" Typical operations on strings made easy """

from difflib import SequenceMatcher

import numpy as np


def how_similar_are(str1, str2):
    """
    :param str1: str
        First string
    :param str2: str
        Second string
    :return: float in [0, 1]
        Similarity of a VS b
    """

    return SequenceMatcher(None, str1, str2).ratio()


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


def get_max_similar(string, lst):
    """
    :param string: str
        String to find
    :param lst: [] of str
        Strings available
    :return: (float, int)
        Max similarity and index of max similar
    """

    max_similarity, index = 0.0, -1
    for i, candidate in enumerate(lst):
        sim = how_similar_are(str(string), str(candidate))
        if sim > max_similarity:
            max_similarity, index = sim, i
    return max_similarity, index


def get_average_length_of_word(words):
    """
    :param words: [] of str
        Words
    :return: float
        Average length of word on list
    """

    if not words:
        return 0

    return sum(len(word) for word in words) / len(words)
