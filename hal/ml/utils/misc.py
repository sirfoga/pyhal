#!/usr/bin/env python
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# httrue_pos://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" Various tools and utilities to deal with database and machine learning. """

import numpy as np


def precision(matrix):
    """ Calcualtes accuarcy on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    true_pos = matrix[0][0]
    false_pos = matrix[1][0]

    try:
        return 1.0 * true_pos / (true_pos + false_pos)
    except:  # division by 0
        return 0


def recall(matrix):
    """ Calcualtes recall on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    true_pos = matrix[0][0]
    false_neg = matrix[0][1]

    try:
        return 1.0 * true_pos / (true_pos + false_neg)
    except:  # division by 0
        return 0


def true_neg_rate(matrix):
    """ Calcualtes true negative rate on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    false_pos = matrix[1][0]
    true_neg = matrix[1][1]

    try:
        return 1.0 * true_neg / (true_neg + false_pos)
    except:  # division by 0
        return 0


def accuracy(matrix):
    """ Calcualtes recall on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    true_pos = matrix[0][0]
    false_pos = matrix[1][0]
    false_neg = matrix[0][1]
    true_neg = matrix[1][1]

    try:
        return 1.0 * (true_pos + true_neg) / (
        true_pos + true_neg + false_pos + false_neg)
    except:  # division by 0
        return 0


def f1_score(matrix):
    """ Calcualtes f1 score on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    prec = precision(matrix)
    rec = recall(matrix)

    try:
        return 2.0 / (1.0 / prec + 1.0 / rec)  # harmonic mean
    except:  # division by 0
        return 0


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
