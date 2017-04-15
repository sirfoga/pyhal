#!/usr/bin/env python
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" Functions to deal with matrices. """

import numpy as np


def precision(matrix):
    """ Calcualtes accuarcy on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    tp = matrix[0][0]
    fp = matrix[1][0]

    try:
        return 1.0 * tp / (tp + fp)
    except Exception:  # division by 0
        return 0


def recall(matrix):
    """ Calcualtes recall on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    tp = matrix[0][0]
    fn = matrix[0][1]

    try:
        return 1.0 * tp / (tp + fn)
    except Exception:  # division by 0
        return 0


def tn_rate(matrix):
    """ Calcualtes true negative rate on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    fp = matrix[1][0]
    tn = matrix[1][1]

    try:
        return 1.0 * tn / (tn + fp)
    except Exception:  # division by 0
        return 0


def accuracy(matrix):
    """ Calcualtes recall on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    tp = matrix[0][0]
    fp = matrix[1][0]
    fn = matrix[0][1]
    tn = matrix[1][1]

    try:
        return 1.0 * (tp + tn) / (tp + tn + fp + fn)
    except Exception:  # division by 0
        return 0


def f1_score(matrix):
    """ Calcualtes f1 score on database

        :param matrix: 2x2 matrix that looks like
        True Positive  - False Negative
             |         -       |
        False Positive - True Negative
    """

    p = precision(matrix)
    r = recall(matrix)

    try:
        return 2.0 / (1.0 / p + 1.0 / r)  # harmonic mean
    except Exception:  # division by 0
        return 0


def get_column_of_matrix(column_index, matrix):
    """
    :param column_index: int >= 0
        Column index to take
    :param matrix: [] of []
        Matrix
    :return: []
        Column of array at position given
    """

    try:
        np_matrix = np.array(matrix)
        np_column = np_matrix[:, column_index]
        return list(np_column)
    except:
        return []


def get_subset_of_matrix(headers_to_sample, all_headers, data):
    """
    :param headers_to_sample: [] of str
        List of columns to get
    :param all_headers: [] of str
        List of all headers in matrix
    :param data: [] of []
        Matrix of float values
    :return: [] of []
        Correlation matrix of selected columns
    """

    header_to_column = {}  # create index of headers
    for header in all_headers:
        header_to_column[header] = all_headers.index(header)

    matrix_subset = []
    for header in headers_to_sample:
        header_ind = header_to_column[header]  # index of header
        header_column = get_column_of_matrix(header_ind, data)

        for i in range(len(header_column)):
            header_column[i] = float(header_column[i])  # get float

        matrix_subset.append(header_column)

    return matrix_subset
