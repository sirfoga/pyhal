# -*- coding: utf-8 -*-

"""Typical operations on strings made easy"""

from difflib import SequenceMatcher


def how_similar_are(str1, str2):
    """Computes similarity between strings

    :param str1: First string
    :param str2: Second string
    :return: Similarity of a VS b
    """
    return SequenceMatcher(None, str1, str2).ratio()


def get_max_similar(string, lst):
    """Finds most similar string in list

    :param string: String to find
    :param lst: Strings available
    :return: Max similarity and index of max similar
    """
    max_similarity, index = 0.0, -1
    for i, candidate in enumerate(lst):
        sim = how_similar_are(str(string), str(candidate))
        if sim > max_similarity:
            max_similarity, index = sim, i
    return max_similarity, index


def get_average_length_of_string(strings):
    """Computes average length of words

    :param strings: list of words
    :return: Average length of word on list
    """
    if not strings:
        return 0

    return sum(len(word) for word in strings) / len(strings)


def convert2sentence_case(string, splitter='. '):
    def prettify_sentence(s):
        return s.strip()

    def convert(s):
        return s[0].upper() + s[1:]

    def join_separate(s, joiner='. '):
        return joiner.join(s)

    sentences = string.split(splitter)
    sentences = map(prettify_sentence, sentences)  # prettify
    sentences = map(convert, sentences)  # convert
    out = join_separate(sentences)  # combine
    return out
