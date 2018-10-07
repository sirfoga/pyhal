# !/usr/bin/python3
# coding: utf-8


""" Typical operations on strings made easy """

from difflib import SequenceMatcher

from pyparsing import Literal, Word, nums, Combine, Optional, delimitedList, \
    alphas, oneOf, Suppress


def how_similar_are(str1, str2):
    """

    Args:
      str1: str
    First string
      str2: str
    Second string

    Returns:
      float in [0, 1]
      Similarity of a VS b

    """

    return SequenceMatcher(None, str1, str2).ratio()


def get_max_similar(string, lst):
    """

    Args:
      string: str
    String to find
      lst: of str
    Strings available

    Returns:
      float, int)
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

    Args:
      strings: of str
    Words

    Returns:
      float
      Average length of word on list

    """

    if not strings:
        return 0

    return sum(len(word) for word in strings) / len(strings)


def just_alphanum(string):
    """

    Args:
      string: str
    String

    Returns:
      str
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
    """

    Args:
      text: 

    Returns:

    """
    esc_key = Literal('\x1b')
    integer = Word(nums)
    escape_seq = Combine(
        esc_key + '[' + Optional(delimitedList(integer, ';')) +
        oneOf(list(alphas)))
    return Suppress(escape_seq).transformString(text)


def is_string_well_formatted(string):
    """

    Args:
      string: string
    String to parse

    Returns:
      bool
      True iff string is good formatted

    """

    # False iff there are at least \n, \r, \t,"  "
    is_bad_formatted = ":" in string or \
                       "\\'" in string or \
                       "\n" in string or \
                       "\r" in string or \
                       "\t" in string or \
                       "\\n" in string or \
                       "\\r" in string or \
                       "\\t" in string or \
                       "  " in string
    return not is_bad_formatted


def html_stripper(string):
    """

    Args:
      string: string
    String to parse

    Returns:
      string
      Given string with raw HTML elements removed

    """

    out = string
    while not is_string_well_formatted(
            out):  # while there are some improvements to do
        out = out.replace(":", "") \
            .replace("\\'", "\'") \
            .replace("\\n", "") \
            .replace("\\r", "") \
            .replace("\\t", "") \
            .replace("\n", "") \
            .replace("\r", "") \
            .replace("\t", "") \
            .replace("  ", " ") \
            .strip()

    return str(out)
