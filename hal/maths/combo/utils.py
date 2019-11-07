#!/usr/bin/env python
# coding: utf-8


def recursive_set(lst, length):
    """Returns the set of all possible sets with such items

    :param lst: list
    :param length: length of inner sets
    :return: set of all sets
    """

    if length <= 1:
        return [[x] for x in lst]  # just 1 occurrence of all possible items

    smaller_set = recursive_set(lst, length - 1)
    return [
        [item, *prev]
        for item in lst
        for prev in smaller_set
    ]


def get_superset(iterable, length):
    """Returns the set of all possible sets with such items

    :param iterable: iterable
    :param length: length of inner sets
    :return: set of all sets
    """

    lst = list(set(iterable))
    return recursive_set(lst, length)
