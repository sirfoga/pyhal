# !/usr/bin/python3
# coding: utf-8


""" Typical operations on strings made easy """

from difflib import SequenceMatcher

from pyparsing import Literal, Word, nums, Combine, Optional, delimitedList, \
    alphas, oneOf, Suppress


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


def get_average_length_of_string(strings):
    """
    :param strings: [] of str
        Words
    :return: float
        Average length of word on list
    """

    if not strings:
        return 0

    return sum(len(word) for word in strings) / len(strings)


def just_alphanum(string):
    """
    :param string: str
        String
    :return: str
        All numbers and letters in string
    """

    chars = []

    i = 0
    while i < len(string):
        char = string[i]
        if char == "\\":
            i += 1
        else:
            chars.append(char)

        i += 1

    return "".join(chars)


def non_ansi_string(text):
    esc_key = Literal('\x1b')
    integer = Word(nums)
    escape_seq = Combine(
        esc_key + '[' + Optional(delimitedList(integer, ';')) +
        oneOf(list(alphas)))
    return Suppress(escape_seq).transformString(text)
